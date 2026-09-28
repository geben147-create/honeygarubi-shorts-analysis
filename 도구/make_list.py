"""분석 대상 20개 목록(data/videos.json): 허니가루비 일본 관련 상위 20개(h01~h20)."""
import json

rk = json.load(open('data/ranking.json', encoding='utf-8'))
vids = []
for r in rk['picked']:
    vids.append({'key': f"h{r['rank']:02d}", 'group': 'honey', 'rank': r['rank'], 'id': r['id'], 'title': r['title'],
                 'channel': rk['channel'], 'subs': 181000, 'sector': r['category'], 'date': r['date'], 'dur': r['dur'],
                 'views': r['views'], 'likes': r.get('likes'), 'comments': r.get('comments'), 'score': r['score'], 'age_days': r['age_days']})
json.dump(vids, open('data/videos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(vids), 'videos')
