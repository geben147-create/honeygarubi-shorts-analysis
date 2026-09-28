# 쇼츠 컷별 분석 JSON 작성 지침 (허니가루비 — 일본 관련 10개 + 육아·자녀 고충 10개)

역할: 세계 최고 수준의 숏폼 스토리 에디터·연출가·사운드 디자이너. 쇼츠 1개를 **컷 단위로 완전 분해**해 `videos/<키>/analysis.json` 1개를 쓴다.
이 채널(허니가루비, 실사가 아닌 2등신 캐릭터 애니메이션 사연 쇼츠)은 **스토리텔링 구조**가 핵심이다. 사용자가 특히 궁금한 것에 초점을 맞춘다:

1. **소재·어그로(훅)** — 무엇을 소재로 골랐고, 제목·첫 프레임·첫 3초가 어떻게 손가락을 멈추게 하나
2. **앵글** — 클로즈업·인서트(스마트폰 화면·메신저 캡처 등)·배경 컷을 어떻게 섞나
3. **빠른 컷(빡빡빡)** — 컷 길이·자막 타이핑 속도·리듬이 무엇에 맞춰 잘리나
4. **소리** — 내레이션(TTS/성우) 톤, 배경음악, 효과음(뾰로롱·쿵·반짝 등)을 어떻게 쓰나
5. **편집 퀄·효과** — 전환(스모크 와이프 등)·자막 애니메이션·색보정 등 이 채널만의 시그니처
6. **캐릭터 클로즈업 vs 텍스트/배경만** — 얼굴(캐릭터)이 나오는 컷과 스크린샷·배경·텍스트 카드만 나오는 컷의 비율과 역할
7. **스토리 구조** — 훅(제목 암시) → 상황 설명 → 전개 → 반전/오해 → 해소/교훈 의 기승전결이 어떻게 짜였는지 (이 채널은 실화 사연 내레이션형이라 스토리 비트가 특히 중요)

## 1. 먼저 볼 것 (작업 폴더 = 이 파일의 두 단계 위 `work2/`, 모든 경로는 work2 기준)
- `data/videos.json` — 내 키(h01~h10 = 육아·자녀 카테고리, h11~h20 = 일본 관련 카테고리)의 제목·조회수·댓글·카테고리(`sector` 필드에 `japan`|`parenting`)
- `videos/<키>/cuts.json` — 컷 번호(idx)·시작·끝·길이·밝기·움직임. **컷 번호와 시간은 이 파일 그대로**(합치거나 나누지 말 것). `active_box`(상단 고정 타이틀 바를 뺀 실제 변화 영역)가 있으면 그 정보를 참고
- `videos/<키>/sheets/sheet_XX.jpg` — 콘택트시트(1장 = 4컷, 행 = 컷 1개: 시작|중간|끝). **Read 도구로 전부 본다**
- `videos/<키>/timeline_XX.jpg` — 1초 간격 전체 흐름(1장 = 20초). 컷 검출이 못 잡은 자막 교체·미세 전환 확인용. **전부 본다**
- `videos/<키>/hook_0-3s.jpg`(처음 3초, 0.2초 간격), `ending_last3s.jpg`(마지막 3초), `src.jpg`(썸네일)
- 확대가 필요하면 `shots/sNNN_a.jpg|_m.jpg|_z.jpg`(360×640)
- `audio.json` — LUFS·온셋(타격점) 수·초당 온셋·컷-온셋 일치율(`cut_onset_sync_pct`) vs 우연 기준(`chance_sync_pct`)·고역비(`hf_ratio_4k`)·컷별 값(`per_shot`). `spectrogram.png`
- `whisper.json` — 내레이션 받아쓰기(한국어). 이 채널은 대사가 거의 항상 있으므로 스토리 비트 작성에 적극 활용
- `ocr_palette.json` — 컷별 화면 글자(위치·크기)·대표색. 상단 고정 타이틀 바(제목 요약)도 매 컷 잡히니 구분해서 볼 것
- `faces.json` — OpenCV 실사 얼굴 검출 참고값. **이 채널은 2D 애니메이션 캐릭터라 검출률이 낮게 나오는 게 정상**(대부분 0.0~0.2) — 캐릭터 얼굴 등장 여부는 반드시 눈으로 판단하고 note 에 "애니메이션 캐릭터라 자동 검출값은 참고만" 명시
- `comments.json` — 인기 댓글 60개 + 설명란(작성자 이름 없음)

## 2. JSON 구조 (키는 영어, 값은 한국어. prompt 만 영어) — 이전 채널 분석과 같은 스키마를 그대로 쓴다
최상위 필수 키:
```
key, group("honey"), rank, id, fmt, sector("japan"|"parenting" — data/videos.json 값 그대로), logline, why[], formula[],
hook{title_hook, first_frame, first_1s, first_3s, text_hook, aggro_types[], promise_payoff, retention_devices[], ending_loop, score, score_note},
topic{material, novelty, trend_hook, series},
visual{people{face_pct, hands_pct, object_only_pct, face_role, note}, angles[{name, shots[], pct, why}], sizes{ECU,CU,MS,WS}, look, signature_shots[]},
pacing{summary, cuts_real, avg_shot_s, median_shot_s, cpm, fastest_run, slowest, speed_ramps, rhythm_note, curve[{t0,t1,cps,note}]},
sound{summary, layers{asmr,bgm,voice,sfx}, asmr[{t,n,type,how}], sfx[{t,n,type,role}], bgm{guess,role,level}, voice{present,type,timing}, mix, sound_first},
edit_fx{summary, transitions[{type,count,shots[]}], effects[{name,shots[],how}], grade, quality_diff[]},
captions{summary, styles[{name,spec,use}], density, note},
beats[{name,t0,t1,e,desc}],
comments_insight{themes[{theme,share,example_paraphrase}], what_triggers_comments, uploader_pin},
shots[], tech[], adapt{keep[], change[], idea_ai_shorts, idea_live_action},
kit{shoot_list[], edit_recipe[], sfx_search[]}
```
- `visual.people.*`: 이 채널에서는 "얼굴"=캐릭터 클로즈업, "손"=캐릭터 상반신/전신(손짓 포함), "물체만"=스크린샷·텍스트 카드·배경만 나오는 컷으로 재해석해서 채운다. `face_role` 에 이 재해석을 명시할 것
- `visual.angles.name`: 이 채널에 맞는 앵글 표현 예 — "캐릭터 클로즈업", "캐릭터 상반신", "스마트폰/메신저 화면 인서트", "배경·풍경 컷", "텍스트 카드", "상단 고정 타이틀 바"(항상 떠 있음, 별도 표기)
- `hook.score`: 1~10 정수. `beats[].e`: -1~+1
- `edit_fx.transitions`: 이 채널의 시그니처인 흰 연기(스모크) 와이프, 컷인 확대, 자막 타이핑 등을 반드시 포함
- `sound.sfx`/`sound.asmr`: 이 채널은 ASMR이 아니라 **효과음·배경음악·내레이션 톤**이 핵심이므로, `sound.asmr` 배열은 "효과음·강조 사운드" 타임라인으로 채우고(이름은 스키마 호환을 위해 유지), `sound.voice`에 내레이션 성우 톤·타이핑 속도를 상세히
- `beats`: 이 채널 서사 구조에 맞춰 명명 — 예: 훅(제목 암시) → 상황 설정 → 전개 1 → 전개 2(반전 요소) → 절정/오해 → 해소 → 교훈/엔딩 멘트. 6~10개
- `comments_insight`: 댓글 60개 기준 반응 분류(공감/자기 경험담/캐릭터 귀여움/육아 공감/일본 문화 정보성 등)
- `tech` 10개 이상(컷 번호 포함), `kit.edit_recipe` 6~10단계, `kit.sfx_search` 영어 검색어 8~15개

### 컷 객체(shots[] 원소) — 전부 필수, cuts.json 컷 수와 같은 개수, n = 1..N 순서
```
{"n":1, "cut_type":"hard", "subj":"object", "sz":"ECU", "ang":"탑다운", "cam":"고정", "speed":"1x",
 "act":"...", "asmr":"...", "sfx":"", "cap":"", "fx":"...", "role":"hook", "why":"...", "shoot":"...", "prompt":"..."}
```
- `cut_type`: hard | jump(같은 구도에서 자막·표정만 바뀜) | match | whip | dissolve(스모크 와이프 포함) | flash | false(검출 오류)
- `subj`: face(캐릭터 클로즈업) | face_hands(캐릭터 상반신 이상) | hands(손짓·소품과 캐릭터 일부) | object(배경·소품만) | person(사용 안 함 — 실사 아님) | text(스크린샷·텍스트 카드·타이틀 바만) | mixed
- `sz`: ECU | CU | MCU | MS | WS | EWS | insert
- `ang`: 위 목록에서 이 채널에 맞는 표현 사용(정면 | 측면 | 클로즈업 | 부감 | 화면 인서트 | 텍스트 카드 등 — 최소 하나는 `정면|측면|탑다운|하이앵글|로우앵글|매크로|POV|부감` 표준 단어 포함)
- `cam`: 고정 | 푸시인 | 풀아웃 | 팬 | 편집 줌(펀치인) | 크래시 줌 — 이 채널은 정지 일러스트에 편집으로 줌/흔들림을 주는 경우가 많음, 있는 그대로 적을 것
- `speed`: 대부분 1x. 타이핑 애니메이션 속도가 다르면 note
- `act`: 화면 내용 1~2문장(그림 속 행동 + 자막 대사 요지)
- `asmr`: 이 컷의 강조 사운드(효과음·BGM 변화) — 없으면 "BGM만"
- `sfx`: 편집 효과음 이름 — 없으면 ""
- `cap`: 화면 자막의 **의도 요약**(원문 대사 복사 금지, 1~3단어 조각까지만)
- `fx`: 전환 + 컷 안 효과(스모크 와이프, 흔들림, 타이핑 애니메이션, 강조색 텍스트, 스티커 등)
- `role`: hook | setup | build | tension | reveal | payoff | reaction | rehook | cta | loop | broll
- `why`: 이 컷이 여기 있는 이유(스토리 진행·시청 유지 관점)
- `shoot`: 재현 제작 팁(일러스트 장면 구성·자막 타이밍·성우 톤 등 구체적으로, 한국어)
- `prompt`: AI 이미지/영상 재현용 **영어** 1~2문장(2D 캐릭터 일러스트 스타일 명시, 실존 인물·상표명 금지)

## 3. 품질 기준
- `why` 5~7개: 구체적 숫자(조회수·컷 수·초·일치율)와 컷 번호 포함
- `formula` 8~12단계
- 훅 분석은 hook_0-3s.jpg 를 0.2초 단위로 읽고 시각을 적을 것. 상단 고정 타이틀 바 문구도 훅 분석에 포함(제목과 다르면 그 차이도 적기)
- 소리 분석은 audio.json 수치 인용. 이 채널은 내레이션 대사 중심이라 컷-온셋 일치율이 낮게 나올 수 있음 — 그 경우 "대사·자막 타이밍 편집"으로 해석
- 얼굴(캐릭터) 비율은 눈으로 직접 세어 채우고, faces.json 참고값과 다르면 note 에 "애니메이션이라 자동 검출과 다름" 명시
- 모르는 것은 "추정"/"확인 불가". 지어내지 말 것

## 4. 저작권 (엄격 — 결과는 공개 저장소에 올라감)
- 원본 자막·내레이션 대사·댓글 문장을 **옮겨 적지 말고 의도만 요약**(1~3단어 조각까지만)
- 댓글은 의역. 작성자 이름·아이디 금지
- 제목은 data/videos.json 에 이미 있으니 통째로 반복하지 말 것
- 캐릭터 외형은 이 채널 고유 디자인이므로 `prompt` 에는 "a chibi-style 2D animated character with pink hair"처럼 일반화해서 쓰고, 채널명·캐릭터 고유명(가루비 등)은 쓰지 않는다

## 5. 검증 (반드시 실행, 통과할 때까지 고치기)
`PYTHONUTF8=1 python tools/validate.py <키>` — 마지막 줄이 `OK` 가 될 때까지 고친다.
다른 영상 폴더·다른 파일은 수정 금지. 최종 답변(반환값)은 요약 JSON만.
