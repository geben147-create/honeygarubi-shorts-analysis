# -*- coding: utf-8 -*-
"""h18 analysis_head.json + shots_part1.json 생성"""
import json, os

d = os.path.join('videos', 'h18')

head = {
    "key": "h18",
    "group": "honey",
    "rank": 18,
    "id": "tbmehEfKnZQ",
    "fmt": "shorts",
    "sector": "japan",
    "logline": "일본인 아빠를 둔 딸이 자기 성씨를 100번 자랑하다 아빠 성씨를 듣고 '베꼈다'고 오해해 노발대발하는 21초 실화 육아 사연 애니메이션",
    "why": [
        "조회수 82.3만은 구독자 18.1만의 약 4.5배(823,225÷181,000)로, 유튜브 메타 제목('일본 딸래미가 아빠 이름 듣고 놀란 이유')과 화면 상단 고정 타이틀 바 문구('딸이 아빠 이름을 싫어했던 이유')가 서로 다른 결로 궁금증을 이중 자극한다.",
        "idx1(0.00~1.97s, 1.97초 홀드)의 완전 정적 타이틀 카드 뒤 idx2(1.97~2.17s, 0.20초, 13컷 중 가장 짧은 컷)의 화이트 스모크 와이프로 전환해 시선을 붙잡는다.",
        "cut_onset_sync_pct 25.0%는 chance_sync_pct 44.8%보다 오히려 19.8%p 낮아, 음악 비트가 아니라 대사·리액션 타이밍에 전적으로 종속된 편집임을 수치로 보여준다.",
        "idx8(10.21~12.08s, 1.87초)의 이름표 리빌 컷은 hf_ratio_4k 0.235로 13컷 평균(0.087)의 약 2.7배에 달해, 반짝이는 파티클 SFX가 정확히 이 컷에 배치됐음을 확인해준다.",
        "idx9~10(12.08~16.05s, 두 컷)은 peak_db가 각각 -13.2dB로 13컷 중 공동 최고치를 기록, 딸 캐릭터의 놀람→분노 리액션이 오디오상으로도 가장 크게 터지는 구간임을 뒷받침한다.",
        "캐릭터 얼굴 단독 리액션 클로즈업은 13컷 중 idx7·8·9·10(4컷, 약 31%)이고, 캐릭터 없이 텍스트 카드·전환만 나오는 컷은 idx1·2(2컷, 약 15%)뿐이라 실화 인용형보다 리액션 중심 편집에 가깝다.",
        "faces.json 자동 얼굴 검출은 idx4에서만 face_frac 0.2(11.5%)로 잡히고 나머지 12컷은 전부 0.0이지만, 눈으로 센 캐릭터 등장 비율(얼굴+상반신 합산 약 85%)과는 무관하다(2D 애니메이션 특성상 note 처리)."
    ],
    "formula": [
        "유튜브 메타 제목엔 '놀란'이라는 감정 단어를 넣어 클릭 유도",
        "영상 내 상단 고정 타이틀 바엔 '싫어했던 이유'로 더 단정적인 문구를 써 재프레이밍",
        "0~2.17초 정적 타이틀/썸네일 카드 홀드 + 0.20초 스모크 와이프로 도입",
        "딸 캐릭터 단독 컷으로 '내 성씨가 좋다'는 자기 자랑성 대사 시작",
        "부녀가 함께 있는 배경 컷으로 전환하며 '일본인 아빠 사연' 서브타이틀 삽입",
        "반복 대사(x100 강조 말풍선)로 코믹한 리듬을 만들며 다음 사건을 예열",
        "아빠의 반문(놀람 표정)으로 시점을 전환",
        "이름표를 파티클 애니메이션으로 리빌해 아빠 캐릭터 이름·나이를 공개",
        "딸의 오해(성씨를 아빠가 베꼈다는 착각)로 반전을 도입, 클로즈업 리액션 2연타로 감정을 고조",
        "아빠의 정정 시도 대사로 갈등을 지속",
        "일본어+한국어 병기 말풍선으로 다시 한번 반박하며 정보 밀도를 최고조로",
        "해결 없이 '성을 바꾸자'는 엉뚱한 제안 펀치라인으로 다음 화 예고 없이 단발 완결"
    ],
    "hook": {
        "title_hook": "유튜브 메타 제목은 '~놀란 이유'로 감정을 부각하고, 실제 화면 상단 고정 타이틀 바는 '~싫어했던 이유'라는 더 단정적인 문구를 써 서로 다른 결로 이중 후킹한다.",
        "first_frame": "상단 고정 타이틀 바('가루비' 로고 + '딸이 아빠 이름을 싫어했던 이유')와 하단 흰 배경의 설명 카드(문구+채널 아이콘+날짜 표기)가 겹쳐 보이는 완전 정적 화면.",
        "first_1s": "0~1.0초 사이 카드가 전혀 움직이지 않고 유지되며(idx1), 시청자가 제목 문구를 읽을 시간을 확보한다.",
        "first_3s": "1.97초 지점에서 화이트 스모크 와이프(idx2, 0.20초)가 시작되고, 2.17~2.60초에 어두운 서재풍 실내 배경과 딸 캐릭터가 드러나며 자기 성씨를 좋아한다는 자막이 등장한다(hook_0-3s.jpg 0.2초 단위 확인).",
        "text_hook": "상단 고정 타이틀 바 문구가 영상 내내 유지되며 '이유' 부분만 노란색으로 강조돼 궁금증의 핵심 단어에 시선이 머물게 한다.",
        "aggro_types": [
            "메타 제목/화면 내 타이틀 이중 프레이밍",
            "결과 은닉형 궁금증(제목에 '이유'만 제시, 답 미공개)",
            "국제(한일) 가정 설정으로 신선함 부여",
            "반전형 오해 구조(딸이 상황을 거꾸로 이해)"
        ],
        "promise_payoff": "제목이 약속한 '이유'는 딸이 자신의 성씨를 자랑하다 아빠의 성씨를 듣고 '베꼈다'고 오해해 화를 내는 것으로 21초 안에 즉시 회수되며, 다음 화 예고 없이 완결된다.",
        "retention_devices": [
            "초반 정적 홀드+스모크 전환으로 시선 재집중",
            "반복 대사(x100)로 코믹 리듬 형성",
            "이름표 파티클 리빌 이펙트로 정보 공개 강조",
            "클로즈업 리액션 2연타(idx9~10)로 감정 고조",
            "일본어+한국어 병기 말풍선으로 이국적 신선함과 정보량 동시 제공"
        ],
        "ending_loop": "명시적 다음 화 예고는 없음 — '아빠 성을 바꾸자'는 엉뚱한 제안 후 마무리 내레이션으로 종료되며, 댓글 다수가 성씨 상속 논리를 유머러스하게 정정하는 반응으로 이어진다.",
        "score": 8,
        "score_note": "구독자 18.1만 대비 조회수 82.3만(약 4.5배), 좋아요 1.16만·댓글 215로 참여율이 우수하다. 21초라는 짧은 러닝타임 안에 오해→반전→펀치라인이 명확해 완결성이 높다."
    },
    "topic": {
        "material": "국제(한일) 가정에서 딸이 성씨 상속 개념을 오해해 아빠가 자기 성을 '베꼈다'고 화를 낸 실화 기반 육아 에피소드",
        "novelty": "성씨가 부계로 상속된다는 사실을 모르는 유아의 순수한 오해를 코미디로 승화하고, 아빠의 대사를 일본어+한국어 병기 말풍선으로 표현해 국제가정 디테일을 살렸다",
        "trend_hook": "국제결혼·다문화 가정 육아 콘텐츠에 대한 관심 + 유아의 엉뚱한 논리(성씨 상속 오해)라는 보편적 육아 공감 소재",
        "series": "이 영상 자체로 완결되는 단발성 에피소드로 보이며, 후속편 존재 여부는 확인 불가(댓글로 미루어 동일 캐릭터가 반복 등장하는 시리즈물로 추정)"
    },
    "visual": {
        "people": {
            "face_pct": 31,
            "hands_pct": 54,
            "object_only_pct": 15,
            "face_role": "이 채널에서 '얼굴'은 캐릭터 얼굴 단독 리액션 클로즈업(idx7·8·9·10, 반응·리빌 중심), '손'은 캐릭터 상반신 이상(제스처·투샷 포함, idx3·4·5·6·11·12·13), '물체만'은 캐릭터 없이 텍스트 카드·전환 효과만 나오는 컷(idx1·2)으로 재해석했다.",
            "note": "faces.json 자동 얼굴 검출값은 idx4를 제외하면 전부 0.0 수준으로 참고용일 뿐이며, 위 비율은 13개 컷을 직접 눈으로 세어 산출했다."
        },
        "angles": [
            {"name": "타이틀/썸네일 카드", "shots": [1], "pct": 8, "why": "도입부 정적 홀드로 제목을 읽게 하는 구간"},
            {"name": "전환 이펙트(스모크 와이프)", "shots": [2], "pct": 8, "why": "장면 진입 전 시선 재집중"},
            {"name": "캐릭터 단독 클로즈업(제스처)", "shots": [3, 6], "pct": 15, "why": "딸의 자기 자랑 대사를 전달하는 컷"},
            {"name": "부녀 배경 투샷(서재 배경)", "shots": [4, 5], "pct": 15, "why": "집에서 이름 쓰기 연습을 하는 상황 설명 컷"},
            {"name": "캐릭터 리액션 클로즈업", "shots": [7, 9, 10], "pct": 23, "why": "아빠의 반문과 딸의 놀람·분노를 전달하는 감정 컷"},
            {"name": "이름표 파티클 리빌", "shots": [8], "pct": 8, "why": "아빠 캐릭터의 이름·나이를 공개하는 정보 컷"},
            {"name": "부녀 투샷(감정 대립)", "shots": [11], "pct": 7, "why": "아빠가 정정을 시도하는 갈등 지속 컷"},
            {"name": "말풍선+이름표 투샷(JP/KR 병기)", "shots": [12], "pct": 8, "why": "일본어+한국어 병기 대사로 정보 밀도가 가장 높은 컷"},
            {"name": "부녀 후면 투샷(엔딩)", "shots": [13], "pct": 8, "why": "시점을 바꿔 여운을 남기는 엔딩 컷"}
        ],
        "sizes": {"ECU": 2, "CU": 2, "MCU": 0, "MS": 5, "WS": 2, "insert": 2},
        "look": "저채도 서재풍 실내(초록빛 책장·베이지 톤)에 고채도 파스텔 캐릭터(연분홍 헤어의 딸, 네이비 정장의 아빠)가 대비되고, 상단 고정 타이틀 바는 흰 배경에 검정+노랑 텍스트, 하단 대사 자막은 검정 반투명 바 위 흰 글씨로 통일돼 있다. 이름표 리빌 컷(idx8)과 병기 말풍선 컷(idx12)에서는 노란 강조색 텍스트가 추가된다.",
        "signature_shots": [
            "idx2 화이트 스모크 와이프 전환(0.20초, 전체 최단컷)",
            "idx8 이름표 파티클 리빌 이펙트",
            "idx9~10 클로즈업 리액션 2연타(놀람→노발대발)",
            "idx12 일본어+한국어 병기 말풍선과 캐릭터명 이름표 동시 노출",
            "idx13 부녀 후면 실루엣 투샷 엔딩"
        ]
    },
    "pacing": {
        "summary": "13개 컷, 총 21.42초. 평균 1.65초/컷(중앙값 1.67초)로 대사 전달에 맞춘 중간 속도 편집이며, 유일한 전환 컷 idx2(0.20초)만 예외적으로 짧다.",
        "cuts_real": 13,
        "avg_shot_s": 1.65,
        "median_shot_s": 1.67,
        "cpm": 36.4,
        "fastest_run": "idx2(1.97~2.17s, 0.20초) 하나만 극단적으로 짧은 스모크 전환 컷이며, 그 외에는 1.0~2.3초대의 완만한 리듬이 유지된다.",
        "slowest": "idx6(5.94~8.24s)과 idx9(12.08~14.38s)가 각각 2.30초로 공동 최장 컷이며, 반복 대사 리듬과 딸의 놀람 리액션 홀드 구간이다.",
        "speed_ramps": "도입부(0~2.17s)는 정적 홀드+스모크 전환 1회, 중반(5.94~10.21s)은 반복 대사+리액션으로 완만하게 늘어지다가, 반전 구간(10.21~16.05s)에서 3컷으로 압축, 후반(16.05~21.42s)은 다시 2초 안팎으로 늘어져 대사를 읽게 한다.",
        "rhythm_note": "cut_onset_sync_pct 25.0%가 chance_sync_pct 44.8%보다 19.8%p 낮아, 이 채널은 음악 비트를 오히려 피해 편집하며 전적으로 내레이션·자막 타이밍에 컷을 맞춘다(대사 중심 편집의 수치적 증거).",
        "curve": [
            {"t0": 0.0, "t1": 2.169, "cps": 0.92, "note": "타이틀 홀드+스모크 전환 1회"},
            {"t0": 2.169, "t1": 5.939, "cps": 0.8, "note": "딸의 자기 자랑 시작+부녀 배경 소개"},
            {"t0": 5.939, "t1": 10.21, "cps": 0.47, "note": "반복 대사+아빠 반문, 완만한 리듬"},
            {"t0": 10.21, "t1": 16.049, "cps": 0.51, "note": "이름표 리빌+반전 리액션 2연타"},
            {"t0": 16.049, "t1": 21.421, "cps": 0.56, "note": "대립+병기 말풍선+엔딩 펀치라인"}
        ]
    },
    "sound": {
        "summary": "배경음악(BPM 약 152 추정)이 내레이션 아래 낮게 깔리고, 효과음은 전환(idx2 스모크)·리빌(idx8 이름표)·감정 절정(idx9~10 리액션)에 집중 배치됐다. cut_onset_sync_pct 25.0%로 비트보다 대사·리액션 타이밍이 편집을 지배한다.",
        "layers": {"asmr": False, "bgm": True, "voice": True, "sfx": True},
        "asmr": [
            {"t": 1.97, "n": "화이트 스모크 전환 효과음", "type": "whoosh", "how": "idx1→idx2 전환 시작과 동시 재생, peak_db -22.3dB로 상대적으로 조용한 편"},
            {"t": 2.17, "n": "장면 리빌 스팅어", "type": "reveal_sting", "how": "스모크가 걷히며 서재 배경이 드러나는 idx3 진입과 동시"},
            {"t": 5.94, "n": "말풍선 팝업음", "type": "pop", "how": "idx6 강조 말풍선 등장과 동시, onsets_per_s 4.34로 13컷 중 최고"},
            {"t": 8.24, "n": "놀람 스팅어", "type": "surprise_sting", "how": "idx7 아빠 반문 리액션(느낌표 이펙트)과 동시"},
            {"t": 10.21, "n": "이름표 반짝임 SFX", "type": "sparkle", "how": "idx8 이름표 파티클 리빌과 매칭, hf_ratio_4k 0.235로 13컷 중 최고치"},
            {"t": 12.08, "n": "놀람 들숨음", "type": "gasp", "how": "idx9 딸의 놀람 리액션과 동시, peak_db -13.2dB로 공동 최고"},
            {"t": 14.38, "n": "분노 강조 스팅어", "type": "anger_sting", "how": "idx10 분노 상태 라벨 컷과 매칭, peak_db -13.2dB로 공동 최고"},
            {"t": 16.05, "n": "땀 흘림 폴리", "type": "sweat_foley", "how": "idx11 아빠의 진땀 표정 컷 강조"},
            {"t": 17.62, "n": "말풍선 팝업음(2)", "type": "pop", "how": "idx12 일본어+한국어 병기 말풍선 등장과 동시"},
            {"t": 19.82, "n": "엔딩 마무리 스팅어", "type": "outro_sting", "how": "idx13 펀치라인 컷 마무리"}
        ],
        "sfx": [
            {"t": 1.97, "n": "스모크 훅", "type": "transition", "role": "장면 전환 강조"},
            {"t": 8.24, "n": "느낌표 팝", "type": "ui", "role": "아빠 반문 리액션 강조"},
            {"t": 10.21, "n": "반짝 파티클음", "type": "sparkle", "role": "이름표 리빌 강조"},
            {"t": 12.08, "n": "놀람 들숨", "type": "gasp", "role": "딸 리액션 강조"},
            {"t": 14.38, "n": "분노 스팅어", "type": "anger", "role": "분노 리액션 강조"},
            {"t": 19.82, "n": "마무리 스팅어", "type": "outro", "role": "펀치라인 마무리"}
        ],
        "bgm": {
            "guess": "미디엄업템포 배경 트랙(BPM 약 152 추정)",
            "role": "내레이션 아래 낮게 깔리는 기본 트랙, 리액션 구간에서 텐션 소폭 상승",
            "level": "내레이션보다 낮게 믹스(I_LUFS -16.6 기준 보이스 우선)"
        },
        "voice": {
            "present": True,
            "type": "여성 내레이션(한국어 대사체, TTS 또는 성우 추정) + 캐릭터별 대사(딸·아빠 톤 구분)",
            "timing": "자막 등장과 거의 동시에 발화되며 문장 끝마다 짧은 pause를 두어 컷 전환과 맞춘다. idx12에서는 아빠 대사가 일본어+한국어로 동시 표기된다."
        },
        "mix": "I_LUFS -16.6, LRA 3.9 LU, TruePeak -1.5dBFS로 다이내믹레인지가 좁게 압축돼 내레이션 명료도를 우선한 믹스",
        "sound_first": "idx8 이름표 리빌 직전 반짝임음이 살짝 먼저 들어와 다음 정보(이름·나이 공개)를 예고하는 편집"
    },
    "edit_fx": {
        "summary": "13컷 중 하드컷 11회, 스모크 와이프 1회(idx2)로 구성되며, 이름표 파티클 리빌(idx8)과 일본어+한국어 병기 말풍선(idx12)이 이 영상만의 시그니처다.",
        "transitions": [
            {"type": "스모크 화이트 와이프", "count": 1, "shots": [2]},
            {"type": "하드컷", "count": 11, "shots": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}
        ],
        "effects": [
            {"name": "이름표 파티클 리빌", "shots": [8], "how": "연기·반짝임 파티클이 뭉쳐 이름과 나이 텍스트를 만드는 리빌 애니메이션"},
            {"name": "느낌표 팝업 이펙트", "shots": [7], "how": "아빠의 놀람 표정 위에 빨간 느낌표가 팝업"},
            {"name": "강조색 말풍선(주황 배경)", "shots": [6], "how": "반복 대사를 주황 배경 말풍선으로 강조"},
            {"name": "일본어+한국어 병기 말풍선", "shots": [12], "how": "아빠 대사를 상단 일본어, 하단 한국어로 동시 표기해 국제가정 설정을 시각화"},
            {"name": "캐릭터 이름표(하단 라벨)", "shots": [12], "how": "각 캐릭터 발치에 이름 라벨 표시"},
            {"name": "후면 실루엣 처리", "shots": [13], "how": "아빠를 검은 실루엣(뒷모습)으로 처리해 엔딩의 시점 전환을 표시"},
            {"name": "상태 라벨(감정 표기)", "shots": [10], "how": "괄호 안 상태 텍스트를 캐릭터 위에 직접 표기"}
        ],
        "grade": "채도 대비가 뚜렷한 파스텔 톤 컬러그레이딩으로, 실내 배경은 저채도 그린·베이지, 캐릭터는 고채도 핑크·네이비로 분리돼 인물이 항상 도드라진다.",
        "quality_diff": [
            "이름표를 파티클 애니메이션으로 리빌해 정보 전달을 게임화",
            "다국어(일본어+한국어) 병기 말풍선으로 단순 내레이션 이상의 디테일 제공",
            "후면 실루엣 컷(idx13)으로 마지막에 시점을 바꿔 여운을 남김"
        ]
    },
    "captions": {
        "summary": "상단 고정 타이틀 바(흰 배경, '이유' 부분만 노란 강조)가 21초 내내 유지되고, 하단에는 대사 자막이 검정 반투명 바 위에 매 컷마다 교체되며, idx4~9 구간에는 보조 서브타이틀(사연 소개용)이 추가로 표시된다.",
        "styles": [
            {"name": "상단 고정 타이틀 바", "spec": "흰 배경/검정+노랑 텍스트, 화면 상단 고정", "use": "영상 내내 유지, 제목 요약"},
            {"name": "하단 대사 자막", "spec": "검정 반투명 바, 흰 텍스트, 컷마다 교체", "use": "내레이션 대사 표시"},
            {"name": "서브 타이틀(사연 소개)", "spec": "작은 흰 텍스트, 화면 중앙 상단", "use": "idx4~9 구간, 가족 배경 맥락 제공"},
            {"name": "상태 라벨", "spec": "괄호 안 굵은 텍스트, 캐릭터 위", "use": "idx10, 감정 상태 강조"},
            {"name": "이름표 라벨", "spec": "캐릭터 발치 라벨(흰 배경/검정 텍스트)", "use": "idx8·12, 캐릭터명·나이 표기"},
            {"name": "일본어+한국어 병기 말풍선", "spec": "손글씨풍 말풍선, 상단 일본어/하단 한국어", "use": "idx12, 아빠 대사"}
        ],
        "density": "대사가 있는 13컷 중 11컷에 하단 자막이 존재해 자막 밀도가 매우 높으며(idx2 전환 컷만 예외), 서브타이틀·이름표까지 겹치는 idx8·12는 한 화면에 자막 레이어가 최대 3겹까지 쌓인다.",
        "note": "유튜브 메타 제목과 화면 내 고정 타이틀 바 문구가 서로 달라 궁금증 프레이밍이 이중으로 작동한다(hook 항목 참고). 서브 타이틀이 일본인 아빠 설정을 명시적으로 알려준다."
    },
    "beats": [
        {"name": "훅(타이틀 카드+스모크 전환)", "t0": 0.0, "t1": 2.169, "e": 0.1, "desc": "정적 타이틀/썸네일 카드 홀드 후 화이트 스모크로 전환해 궁금증을 예열한다"},
        {"name": "상황 설정1(딸의 자기 자랑 시작)", "t0": 2.169, "t1": 3.77, "e": 0.3, "desc": "딸 캐릭터가 자기 성씨가 참 좋다며 자랑을 시작한다"},
        {"name": "상황 설정2(가족 배경 소개)", "t0": 3.77, "t1": 5.939, "e": 0.2, "desc": "집에서 이름 쓰기 연습을 하는 부녀 배경 컷과 함께 일본인 아빠라는 서브타이틀이 등장한다"},
        {"name": "전개(반복 자랑)", "t0": 5.939, "t1": 8.242, "e": 0.4, "desc": "딸이 자기 성이 좋은 이유를 수십 가지쯤 반복해서 늘어놓는다"},
        {"name": "전환(아빠의 반문)", "t0": 8.242, "t1": 10.21, "e": 0.1, "desc": "아빠가 놀란 표정으로 자신의 성씨가 뭔지 되묻는다"},
        {"name": "reveal(이름표 공개)", "t0": 10.21, "t1": 12.079, "e": 0.2, "desc": "파티클 이펙트로 아빠 캐릭터의 이름과 나이가 공개된다"},
        {"name": "오해/반전(놀람→분노)", "t0": 12.079, "t1": 16.049, "e": -0.5, "desc": "딸이 놀라 자기 성씨를 아빠가 베꼈다며 노발대발한다"},
        {"name": "해소 시도(아빠의 반박)", "t0": 16.049, "t1": 19.82, "e": -0.2, "desc": "아빠가 오히려 네가 베낀 것이라고 정정하고, 일본어+한국어 병기 말풍선으로 다시 한번 억울함을 표현하지만 딸은 받아들이지 않는다"},
        {"name": "엔딩 펀치라인", "t0": 19.82, "t1": 21.421, "e": 0.7, "desc": "딸이 아빠 성을 바꾸는 게 어떠냐는 엉뚱한 제안을 하며 마무리 내레이션으로 끝난다"}
    ],
    "comments_insight": {
        "themes": [
            {"theme": "성씨 상속 논리 정정(유머)", "share": "약 45%", "example_paraphrase": "성씨는 아빠에게서 물려받은 것이므로 딸이 반대로 오해했다는 지적을 드립으로 표현"},
            {"theme": "캐릭터 귀여움/애정 표현", "share": "약 25%", "example_paraphrase": "딸 캐릭터의 반응이 귀엽다는 짧은 감탄"},
            {"theme": "본인 경험담 공유", "share": "약 15%", "example_paraphrase": "어릴 적 비슷하게 순진한 착각을 했던 개인 일화"},
            {"theme": "패러디·말장난 댓글", "share": "약 10%", "example_paraphrase": "성씨를 소재로 한 가상 대사나 말장난 패러디"},
            {"theme": "채널·캐릭터 정보성 반응", "share": "약 5%", "example_paraphrase": "채널 이름이 곧 캐릭터의 성씨라는 점을 새롭게 알았다는 반응"}
        ],
        "what_triggers_comments": "성씨가 부계로 상속된다는 상식을 거꾸로 이해한 유아의 순진한 오해가 '지적하고 싶은' 욕구를 자극해 댓글을 유도하며, 채널명 자체가 캐릭터의 성씨라는 설정을 새로 알게 된 반응도 참여를 이끈다.",
        "uploader_pin": "확인 불가(고정 댓글 정보 없음)"
    },
    "tech": [
        "idx2(1.97~2.17s, 0.20초)는 13컷 중 가장 짧아 전체 최단컷이며 motion_mean 14.01로 스모크 전환다운 급격한 움직임을 보인다.",
        "idx4(3.77~4.77s)는 sat_mean 67.2로 13컷 중 채도가 가장 높은 축에 속해 서재 배경 위 캐릭터가 도드라진다.",
        "idx6(5.94~8.24s, 2.30초)은 onsets_per_s 4.34로 13컷 중 가장 오디오 온셋이 조밀해 반복 대사 리듬과 일치한다.",
        "idx8(10.21~12.08s, 1.87초)은 hf_ratio_4k 0.235로 전체 평균(0.087) 대비 약 2.7배 높아 이름표 리빌 파티클 SFX의 수치적 증거다.",
        "idx9(12.08~14.38s)와 idx10(14.38~16.05s)은 peak_db가 각각 -13.2dB로 13컷 중 공동 최고치이며, 딸의 놀람→분노 리액션이 오디오상 가장 크게 터지는 구간이다.",
        "idx8~9 경계(cut_nearest_onset_s 0.344s)와 idx9~10 경계(0.24s)는 온셋과의 거리가 멀어, 비트가 아니라 대사·리액션 타이밍에 맞춘 컷임을 재확인한다.",
        "idx2~3 경계(cut_nearest_onset_s 0.033s)와 idx7~8 경계(0.04s)는 온셋과 가장 가까워, 전환·리빌 컷에는 SFX가 정확히 매칭됐음을 보여준다.",
        "cut_onset_sync_pct 25.0%가 chance_sync_pct 44.8%보다 19.8%p 낮아, 이 채널은 음악 비트를 오히려 피해 편집하는 것으로 해석된다(이전 분석과 달리 비트 회피형 편집의 특이 사례).",
        "faces.json 얼굴 검출은 idx4에서만 face_frac 0.2(11.5%)로 잡히며 나머지 12컷은 전부 0으로, 2D 캐릭터 특성상 자동 검출과 눈으로 센 등장 비율(얼굴+상반신 합산 약 85%)이 크게 괴리된다.",
        "idx11(16.05~17.62s)은 bright_mean 101.2로 13컷 중 가장 어두운 축에 속해 아빠의 진땀·당황 표정을 그늘진 톤으로 강조한다.",
        "bpm_est 152로 빠른 템포의 배경음악이 추정되나, 실제 컷 리듬(평균 1.65초)과의 상관관계는 낮다(cut_onset_sync_pct 참고).",
        "cuts.json 기준 cuts_f 배열은 경계 12개, shots 배열은 13개 컷으로 구성 — 스키마상 13개 그대로 유지, false 컷 없음."
    ],
    "adapt": {
        "keep": [
            "이름표 파티클 리빌 이펙트",
            "일본어+한국어 병기 말풍선 연출",
            "반복 대사(x100)로 만드는 코믹 리듬",
            "메타 제목/고정 타이틀 바 이중 프레이밍",
            "후면 실루엣 엔딩 컷"
        ],
        "change": [
            "실제 외국어 대사는 번역 오류 방지를 위해 원어민 감수 필요",
            "상태 라벨 텍스트는 폰트 크기를 약간 줄여 가독성 개선 검토",
            "엔딩 펀치라인 이후 짧은 다음 화 예고 컷을 1개 추가해 시리즈 락인 강화 검토"
        ],
        "idea_ai_shorts": "AI 이미지 생성으로 2등신 캐릭터의 놀람·분노·당황 표정 세트를 미리 만들어두고, 국제가정(다국어 자막) 설정을 템플릿화해 '아이가 오해하는 가족 상식' 시리즈를 양산할 수 있다",
        "idea_live_action": "실제 부녀가 출연해 이름 쓰기 연습 장면을 라이브액션으로 찍고, 이름표 리빌은 자막 애니메이션으로, 외국어 대사는 실제 자막 병기로 유지해 동일 구조를 재현할 수 있다"
    },
    "kit": {
        "shoot_list": [
            "세로 9:16, 720x1280 해상도 캔버스",
            "상단 고정 타이틀 바 레이어(흰 배경+검정/노랑 텍스트) 최상단 고정",
            "서재풍 실내 배경 일러스트(책장·조명·화분) 1장",
            "2등신 딸 캐릭터 정면/제스처/놀람/분노 표정 최소 5종 일러스트",
            "2등신 아빠 캐릭터 정면/반문/땀 표정 최소 4종 일러스트",
            "이름표 파티클 리빌 애니메이션 템플릿",
            "외국어+한국어 병기 말풍선 템플릿",
            "서브타이틀(가족 배경 설명)용 작은 텍스트 레이어",
            "화이트 스모크 와이프 전환 소스 1개"
        ],
        "edit_recipe": [
            "0~1.97초 타이틀/썸네일 카드 고정",
            "1.97~2.17초 스모크 와이프 전환 삽입",
            "2.17~5.94초 딸 자기소개+부녀 배경 소개, 서브타이틀 삽입",
            "5.94~8.24초 반복 대사 말풍선 삽입, 온셋 조밀 구간과 맞춰 자막 타이핑",
            "8.24~10.21초 아빠 반문 리액션 클로즈업",
            "10.21~12.08초 이름표 파티클 리빌 이펙트+SFX 매칭",
            "12.08~16.05초 딸 리액션 2연타(놀람→분노) 클로즈업, peak_db 최고 구간으로 믹스",
            "16.05~19.82초 부녀 대립 투샷+외국어/한국어 병기 말풍선",
            "19.82~21.42초 후면 실루엣 엔딩 컷+펀치라인 자막"
        ],
        "sfx_search": [
            "whoosh transition sound",
            "smoke wipe sound effect",
            "cute pop up sfx",
            "comic surprise gasp",
            "anger tantrum sting",
            "sparkle reveal chime",
            "cartoon exclamation pop",
            "name tag reveal whoosh",
            "sweat drop foley",
            "upbeat lofi background loop 150 bpm",
            "cartoon blush sfx",
            "outro comedic sting"
        ]
    }
}

with open(os.path.join(d, 'analysis_head.json'), 'w', encoding='utf-8') as f:
    json.dump(head, f, ensure_ascii=False, indent=1)

shots = [
{"n":1,"cut_type":"hard","subj":"text","sz":"insert","ang":"정면(타이틀 카드, 인물 없음)","cam":"고정","speed":"1x",
 "act":"상단 고정 타이틀 바 문구 아래, 흰 배경의 설명 카드(문구+채널 아이콘+2026.07. 날짜)가 겹쳐 보이는 완전 정적 화면. 1.97초 동안 아무 변화가 없다.",
 "asmr":"BGM만","sfx":"","cap":"제목 예열","fx":"강조색(노랑) 텍스트","role":"hook",
 "why":"시청자가 상단 고정 타이틀 문구와 카드 문구를 모두 읽을 시간을 벌어주는 정적 도입부",
 "shoot":"흰 카드+로고+날짜 텍스트를 1.5~2초간 완전히 고정, 배경음악만 낮게 유지",
 "prompt":"A flat vertical title card graphic, bold headline text over a plain background with a small logo icon, no characters visible, clean minimal layout"},

{"n":2,"cut_type":"dissolve","subj":"object","sz":"insert","ang":"정면(전환 이펙트, 인물 없음)","cam":"고정","speed":"1x",
 "act":"화면 전체가 흰 스모크(연기) 텍스처로 뒤덮이며 다음 장면으로 전환되는 0.20초짜리 극단적으로 짧은 컷.",
 "asmr":"화이트 스모크 전환 효과음","sfx":"whoosh","cap":"","fx":"화이트 스모크 와이프","role":"hook",
 "why":"13컷 중 가장 짧은 컷(0.20초)으로 급격한 밝기·움직임 변화를 만들어 다음 장면 진입을 강조",
 "shoot":"흰 연기 텍스처 오버레이를 0.2초 내로 빠르게 지나가게 하고 whoosh 효과음을 정확히 매칭",
 "prompt":"An abstract white smoke wipe transition texture filling the frame, soft swirling cloud shapes, no characters, simple flat animation style"},

{"n":3,"cut_type":"hard","subj":"face_hands","sz":"MS","ang":"정면 캐릭터 클로즈업","cam":"고정","speed":"1x",
 "act":"서재풍 실내 배경(책장·조명·화분) 앞에 딸 캐릭터 혼자 등장, 두 팔을 들어 올리며 자기 성씨가 좋다는 대사를 한다.",
 "asmr":"BGM만","sfx":"","cap":"성씨 자랑","fx":"제스처 애니메이션(양팔 들어올리기)","role":"setup",
 "why":"스모크 전환 직후 첫 등장 컷으로 이야기의 화자(딸)와 배경을 소개",
 "shoot":"캐릭터를 화면 중앙 하단에 배치, 팔을 들어올리는 제스처 애니메이션과 함께 대사 자막을 동시에 타이핑",
 "prompt":"A chibi-style 2D animated character with light pink hair in twin buns, wearing a school-style sailor outfit, raising both arms happily in a cozy study room with bookshelves"},

{"n":4,"cut_type":"hard","subj":"mixed","sz":"WS","ang":"정면 배경 투샷","cam":"고정","speed":"1x",
 "act":"딸이 바닥에 앉아 종이에 글씨를 쓰는 연습을 하고, 뒤쪽 책상에는 정장 차림 아빠 캐릭터가 앉아 있다. 서브타이틀로 가족 배경 설명이 추가된다.",
 "asmr":"BGM만","sfx":"","cap":"가족 소개","fx":"서브타이틀 텍스트","role":"setup",
 "why":"두 캐릭터를 한 프레임에 담아 부녀 관계와 상황(이름 쓰기 연습)을 설명",
 "shoot":"딸은 전경 바닥에, 아빠는 후경 책상에 배치해 원근감을 주고 서브타이틀을 화면 상단에 작게 삽입",
 "prompt":"A wide shot of a cozy study room, a chibi girl character sitting on the floor practicing handwriting, a chibi father character in a business suit sitting at a desk in the background"},

{"n":5,"cut_type":"jump","subj":"mixed","sz":"WS","ang":"정면 배경 투샷","cam":"고정","speed":"1x",
 "act":"이전 컷과 동일한 구도가 유지된 채 하단 자막만 다음 문장으로 교체된다(점프컷).",
 "asmr":"BGM만","sfx":"","cap":"연습 지속","fx":"자막 교체","role":"setup",
 "why":"동일 구도를 유지해 제작비를 아끼면서도 자막만 바꿔 내레이션을 이어가는 전형적 점프컷",
 "shoot":"동일 배경·포즈를 유지하고 자막 텍스트만 교체, 캐릭터는 미세한 idle 모션만 부여",
 "prompt":"The same wide shot of a cozy study room with a chibi girl practicing handwriting on the floor and a chibi father in a suit at a desk behind her, nearly identical framing"},

{"n":6,"cut_type":"hard","subj":"face_hands","sz":"MS","ang":"정면 캐릭터+말풍선","cam":"고정","speed":"1x",
 "act":"딸 캐릭터 위로 주황색 배경의 강조 말풍선이 뜨며, 자기 성씨가 좋은 이유를 수십 가지 되풀이해서 말하는 모습이 반복 자막으로 표현된다.",
 "asmr":"말풍선 팝업음","sfx":"pop","cap":"이유 나열","fx":"강조색 말풍선(주황)","role":"build",
 "why":"onsets_per_s 4.34로 13컷 중 오디오 온셋이 가장 조밀해 대사가 빠르게 반복되는 코믹 구간을 수치로 뒷받침",
 "shoot":"주황 말풍선을 화면 상단에 팝업시키고, 같은 문구를 리듬감 있게 여러 번 겹쳐 자막 처리",
 "prompt":"A chibi girl character with a big speech bubble above her head, excited expression, cute repeated exclamation text bubble in orange, cozy study room background"},

{"n":7,"cut_type":"hard","subj":"face","sz":"CU","ang":"정면 리액션 클로즈업","cam":"편집 줌(펀치인)","speed":"1x",
 "act":"아빠 캐릭터 얼굴 클로즈업으로 전환, 놀란 표정과 함께 빨간 느낌표 이펙트가 팝업되며 자신의 성씨가 뭔지 되묻는다.",
 "asmr":"놀람 스팅어","sfx":"surprise_sting","cap":"반문","fx":"느낌표 팝업","role":"build",
 "why":"딸의 반복 대사 뒤 아빠 시점으로 전환해 다음 사건(이름표 공개)을 예열",
 "shoot":"아빠 얼굴을 CU로 펀치인, 느낌표 이펙트를 눈 위쪽에 팝업시키고 놀람 SFX 매칭",
 "prompt":"A close-up of a chibi father character's face with a surprised expression, round glasses-free face, business suit collar visible, red exclamation mark effects popping above his head"},

{"n":8,"cut_type":"dissolve","subj":"face","sz":"CU","ang":"정면 리액션+이름표 리빌","cam":"고정","speed":"1x",
 "act":"이전 컷과 같은 프레이밍이 유지된 채, 연기·반짝임 파티클이 뭉치며 아빠 캐릭터의 이름과 나이가 적힌 이름표 텍스트가 서서히 드러난다.",
 "asmr":"이름표 반짝임 SFX","sfx":"sparkle","cap":"이름표 공개","fx":"이름표 파티클 리빌","role":"reveal",
 "why":"hf_ratio_4k 0.235로 13컷 평균(0.087) 대비 약 2.7배 높아 반짝임 SFX가 정확히 이 컷에 배치된 수치적 증거",
 "shoot":"파티클 리빌 애니메이션을 1초 내외로 재생하고, 이름표 텍스트가 완성되는 순간과 반짝임 SFX를 정확히 매칭",
 "prompt":"A close-up of a chibi father character's face, with sparkling particle effects gathering below him to reveal a name tag caption with text and an age number"},

{"n":9,"cut_type":"hard","subj":"face","sz":"ECU","ang":"정면 익스트림 클로즈업","cam":"크래시 줌","speed":"1x",
 "act":"딸 캐릭터의 얼굴이 화면 대부분을 채우는 익스트림 클로즈업으로 전환, 눈을 크게 뜨며 놀라는 리액션을 보인다.",
 "asmr":"놀람 들숨음","sfx":"gasp","cap":"놀람","fx":"눈 확대 이펙트","role":"reaction",
 "why":"peak_db -13.2dB로 13컷 중 공동 최고치를 기록해 오디오상으로도 가장 크게 터지는 리액션 컷",
 "shoot":"딸 얼굴을 화면 가득 채우는 크래시 줌, 눈 하이라이트를 크게 그려 놀람을 강조",
 "prompt":"An extreme close-up of a chibi girl character's face, eyes wide open in shock, blushing cheeks, simple flat cartoon shading"},

{"n":10,"cut_type":"jump","subj":"face","sz":"ECU","ang":"정면 익스트림 클로즈업","cam":"고정","speed":"1x",
 "act":"동일한 익스트림 클로즈업 구도가 이어지며 딸의 표정이 놀람에서 분노로 바뀌고, 화면 위에 감정 상태를 나타내는 괄호 텍스트가 표기된다.",
 "asmr":"분노 강조 스팅어","sfx":"anger","cap":"분노 표출","fx":"상태 라벨(감정 표기)","role":"tension",
 "why":"peak_db -13.2dB로 idx9와 공동 최고치를 이어가며 오해로 인한 분노가 절정에 달하는 구간",
 "shoot":"동일 프레이밍을 유지한 채 표정만 분노로 전환하고, 얼굴 위에 상태 라벨 텍스트를 굵게 삽입",
 "prompt":"An extreme close-up of a chibi girl character's face, furious expression with a pouting mouth and reddened cheeks, small angry mark effects around her head"},

{"n":11,"cut_type":"hard","subj":"mixed","sz":"MS","ang":"정면 투샷","cam":"고정","speed":"1x",
 "act":"아빠와 딸이 나란히 있는 투샷으로 전환, 진땀을 흘리는 당황한 표정의 아빠가 딸의 오해를 정정하려 한다.",
 "asmr":"땀 흘림 폴리","sfx":"","cap":"정정 시도","fx":"땀방울 이펙트","role":"tension",
 "why":"bright_mean 101.2로 13컷 중 가장 어두운 축에 속해 당황스러운 분위기를 그늘진 톤으로 강조",
 "shoot":"두 캐릭터를 화면 좌우로 배치하고 아빠 이마에 땀방울 이펙트를 추가",
 "prompt":"A medium shot of a chibi father character with a nervous sweating expression next to a small chibi girl character, both in a dim cozy study room"},

{"n":12,"cut_type":"hard","subj":"mixed","sz":"MS","ang":"정면 투샷+말풍선","cam":"고정","speed":"1x",
 "act":"두 캐릭터 발치에 각각 이름 라벨이 표시되고, 아빠가 손글씨풍 말풍선으로 외국어와 한국어를 함께 표기한 대사를 하며 억울함을 다시 한번 표현한다.",
 "asmr":"말풍선 팝업음(2)","sfx":"pop","cap":"재반박","fx":"외국어+한국어 병기 말풍선","role":"payoff",
 "why":"자막 레이어(이름표+말풍선+하단 자막)가 최대 3겹까지 쌓이는 이 영상에서 정보 밀도가 가장 높은 컷",
 "shoot":"말풍선을 손글씨 폰트로 상단에 외국어, 하단에 한국어 순으로 표기하고 이름 라벨을 캐릭터 발치에 고정",
 "prompt":"A medium two-shot of a chibi father and a chibi girl character, the father with a hand-drawn speech bubble containing two lines of text in different scripts, small name tag labels below each character"},

{"n":13,"cut_type":"hard","subj":"mixed","sz":"MS","ang":"정면(아빠는 뒷모습 실루엣)","cam":"고정","speed":"1x",
 "act":"아빠가 검은 실루엣으로 뒷모습만 보이는 채 딸을 마주보고, 딸이 말풍선으로 엉뚱한 제안을 하며 영상이 끝난다.",
 "asmr":"엔딩 마무리 스팅어","sfx":"outro","cap":"엉뚱한 제안","fx":"후면 실루엣 처리","role":"loop",
 "why":"마지막에 시점을 뒤바꿔(아빠 뒷모습) 여운을 남기며 다음 화 예고 없이 단발로 마무리",
 "shoot":"아빠를 검은 단색 실루엣으로 처리하고 딸만 컬러로 살려 대비를 준 뒤, 말풍선과 마무리 자막을 겹쳐 종료",
 "prompt":"A medium shot from behind a dark silhouetted chibi father character facing a small colorful chibi girl character who has a speech bubble, cozy study room background"}
]

assert len(shots) == 13
with open(os.path.join(d, 'shots_part1.json'), 'w', encoding='utf-8') as f:
    json.dump(shots, f, ensure_ascii=False, indent=1)

print('head + shots_part1 written, shots:', len(shots))
