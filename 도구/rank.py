"""허니가루비 쇼츠 중 ① 일본 관련 ② 육아·자녀 고충 두 카테고리만 걸러 최신순+조회수순 종합으로 각 10개씩 선정.
사용: python tools/rank.py"""
import json, re, datetime
import numpy as np

BASE_DATE = datetime.date(2026, 9, 28)
rows = json.load(open('meta/all_rows.json', encoding='utf-8'))
JP_PAT = re.compile(r'일본|日本|엔화|도쿄|오사카|교토|일본인|일본어|재일|일드|이자카야|스시|돈키호테|규동|편의점')
PARENT_PAT = re.compile(r'아들|딸|육아|아이(?!돌)|학교|유치원|어린이집|자녀|손녀')  # '아이돌'은 자녀 얘기가 아니라서 제외
CAT_NAME = {'japan': '🇯🇵 일본 관련', 'parenting': '👶 육아·자녀 고충'}


def cat(title):
    t = title or ''
    if JP_PAT.search(t):
        return 'japan'
    if PARENT_PAT.search(t):
        return 'parenting'
    return None


base = [r for r in rows if r.get('dur') and r['dur'] <= 400 and (r.get('date') or '') >= '20250101']
for r in base:
    r['category'] = cat(r['title'])
    d = datetime.date(int(r['date'][:4]), int(r['date'][4:6]), int(r['date'][6:]))
    r['age_days'] = max((BASE_DATE - d).days, 1)
pool = [r for r in base if r['category']]


def pct_rank(vals):
    a = np.array(vals, dtype=float)
    return a.argsort().argsort() / max(len(a) - 1, 1)


pv = pct_rank([np.log10(r['views'] + 1) for r in pool])
pr = pct_rank([-r['age_days'] for r in pool])
for i, r in enumerate(pool):
    r['score'] = round(100 * (0.5 * pv[i] + 0.5 * pr[i]), 1)  # 최신순 + 조회수순 동일 가중(카테고리 내부 기준)

picked = []
for c in ('japan', 'parenting'):
    cand = sorted([r for r in pool if r['category'] == c], key=lambda r: -r['score'])[:10]
    picked += cand
picked.sort(key=lambda r: (-{'japan': 0, 'parenting': 1}[r['category']], -r['score']))
for i, r in enumerate(picked, 1):
    r['rank'] = i

out = {'base_date': str(BASE_DATE), 'channel': '허니가루비',
       'filter': '카테고리 ① 제목에 일본 관련 키워드 ② 제목에 육아·자녀 관련 키워드(①에 안 걸리는 것만) — 그 외 주제 제외',
       'weights': '조회수(log) 50% + 최신성 50% (카테고리 안에서 백분위, 카테고리별 상위 10개씩)',
       'categories': {c: {'name': CAT_NAME[c], 'pool_count': sum(1 for r in pool if r['category'] == c)} for c in CAT_NAME},
       'pool_size': len(pool), 'picked': picked, 'pool': pool}
json.dump(out, open('data/ranking.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('일본', out['categories']['japan']['pool_count'], '· 육아', out['categories']['parenting']['pool_count'], '후보 중 각 상위 10개 선정')
for r in picked:
    print(f"{r['rank']:2d} {r['score']:5.1f} {CAT_NAME[r['category']]:<14} {r['date']} {r['views']:>9,} {r['id']} {r['title'][:44]}")
