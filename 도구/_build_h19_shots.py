# -*- coding: utf-8 -*-
import json, os

D = os.path.join('videos', 'h19')

shots = [
{"n":1,"cut_type":"hard","subj":"text","sz":"insert","ang":"정면(타이틀 카드, 인물 없음)","cam":"고정","speed":"1x",
 "act":"채널 로고와 제목 텍스트 아래 SNS 게시물 캡처 형태의 서브 카피 카드(과일 비유 문구, 채널명·업로드월 표기)가 완전히 정지된 채 2초 넘게 유지된다.",
 "asmr":"BGM만","sfx":"","cap":"소재 예고","fx":"강조색(초록) 둘째 줄 텍스트",
 "role":"hook","why":"motion_mean 1.67로 14컷 중 가장 낮아 완전 정지 홀드임이 수치로 확인되며, 시청자가 소재 문구를 읽을 시간을 확보한다.",
 "shoot":"제목 두 줄(검정/초록)+하단 작은 서브카피 카드 구성, 2초 이상 완전 정지 유지",
 "prompt":"A flat social-media-style title card graphic with bold Korean-style headline text over a plain background, no characters visible, clean minimal layout"},

{"n":2,"cut_type":"dissolve","subj":"object","sz":"insert","ang":"정면(전환 그래픽)","cam":"고정","speed":"1x",
 "act":"화면 전체가 흰 연기 형태로 뒤덮이는 화이트 스모크 와이프 전환이 0.2초간 빠르게 지나간다.",
 "asmr":"스모크 전환 훅음","sfx":"whoosh","cap":"","fx":"스모크 와이프",
 "role":"hook","why":"bright_mean 239.8로 전체 14컷 중 최고치를 기록해 도입부와 본편을 시각적으로 구분짓는 전환점이 된다.",
 "shoot":"흰색 연기/구름 텍스처 소스를 0.2초 내로 빠르게 확산시키는 방식으로 제작",
 "prompt":"A bright white smoke wipe transition effect filling the frame, soft cloud-like texture, high-key lighting, motion blur"},

{"n":3,"cut_type":"whip","subj":"face_hands","sz":"CU","ang":"정면 클로즈업","cam":"편집 줌(펀치인)","speed":"1x",
 "act":"스모크가 걷히며 병원 실내를 배경으로 chibi 간호사 캐릭터의 상반신이 드러나고, 근무지와 직업을 밝히는 내레이션이 흐른다.",
 "asmr":"캐릭터 리빌 스팅어","sfx":"reveal_sting","cap":"직업 소개","fx":"펀치인 줌+잔여 스모크 블러",
 "role":"setup","why":"sat_mean 50.8로 idx1~2 대비 급상승해 캐릭터 색상이 화면에 본격 등장했음을 보여주는 첫 컷이다.",
 "shoot":"밝은 배경 위 chibi 캐릭터를 살짝 확대하며 등장시키고, 잔여 스모크 블러를 1~2프레임 남겨 자연스러운 리빌 연출",
 "prompt":"A chibi-style 2D animated nurse character with pastel-colored hair and a small nurse cap, upper body close-up, soft cel-shaded lighting, pastel hospital interior background"},

{"n":4,"cut_type":"hard","subj":"hands","sz":"insert","ang":"매크로(손 클로즈업 인서트)","cam":"고정","speed":"1x",
 "act":"플랫한 웹툰풍 화풍으로 그려진 손이 환자 호출 버튼을 누르고, 말풍선 안에는 호출을 받는 인물의 작은 얼굴 아이콘이 뜬다.",
 "asmr":"호출 버튼 삐빅음(연속)","sfx":"beep","cap":"호출 상황","fx":"화풍 전환(플랫 일러스트)",
 "role":"setup","why":"onsets_per_s 4.09로 14컷 중 가장 높은 오디오 타격 밀도를 기록해 짧은 비프음이 몰린 구간임을 수치로 뒷받침한다.",
 "shoot":"간호사 chibi 화풍과 구분되는 평면적 아이콘 스타일로 손과 버튼만 클로즈업, 말풍선 아이콘은 작게 배치",
 "prompt":"A flat webtoon-style illustration of a hand pressing a hospital call button, a small speech bubble with a simple face icon nearby, clean vector look"},

{"n":5,"cut_type":"hard","subj":"face","sz":"CU","ang":"정면 클로즈업","cam":"고정","speed":"1x",
 "act":"chibi 간호사 캐릭터가 호출음을 듣고 놀라거나 의아해하는 표정으로 짧게 반응한다.",
 "asmr":"BGM만","sfx":"","cap":"당황 반응","fx":"눈 깜빡임 표정 애니메이션",
 "role":"reaction","why":"onsets_per_s 0.0으로 오디오 타격이 거의 없는 구간이며, 다음 컷과의 경계가 온셋과 0.832초 떨어져 순수 대사 중심 컷임을 보여준다.",
 "shoot":"눈썹을 살짝 올리고 입을 벌린 반응 표정, 배경은 단순화해 표정에 집중",
 "prompt":"A chibi-style 2D animated nurse character, close-up surprised or puzzled facial expression, plain simplified background, soft pastel shading"},

{"n":6,"cut_type":"hard","subj":"face_hands","sz":"MCU","ang":"정면 투샷","cam":"고정","speed":"1x",
 "act":"플랫 화풍의 환자 소년 캐릭터가 병실에 나타나고, 간호사의 손과 무릎 일부가 프레임 가장자리에 함께 보인다.",
 "asmr":"BGM만","sfx":"","cap":"환자 등장","fx":"미세 팬 이동(호흡감)",
 "role":"setup","why":"idx6(6.27~8.24s)은 두 캐릭터가 처음 한 프레임에 함께 잡히는 컷으로 이후 전개(부탁·편지)의 관계를 설정한다.",
 "shoot":"소년 캐릭터를 정면 중앙에, 간호사의 손/무릎을 화면 하단 가장자리에 걸치듯 배치",
 "prompt":"A flat webtoon-style illustration of a small boy patient character in hospital pajamas, a nurse's hand and knee partially visible at the frame edge, soft indoor lighting"},

{"n":7,"cut_type":"hard","subj":"face","sz":"CU","ang":"정면 클로즈업(말풍선 인서트)","cam":"고정","speed":"1x",
 "act":"환자 소년의 클로즈업 위로 원어(일본어) 말풍선이 뜨고, 하단에는 그 내용을 요약한 한국어 자막이 타이핑 애니메이션으로 채워진다.",
 "asmr":"말풍선 팝음","sfx":"pop","cap":"부탁 전달","fx":"원어+자막 이중 표기, 자막 타이핑 애니메이션",
 "role":"build","why":"idx7(8.24~10.78s, 2.54초)은 14컷 중 가장 길게 지속되며 sat_mean 66.6으로 채도도 높아, 말풍선 내용을 읽게 하는 정보 전달 구간이다.",
 "shoot":"말풍선은 원어 그대로 유지하고 하단 자막만 한 글자씩 타이핑되듯 채워, 이중언어 디테일을 강조",
 "prompt":"A flat webtoon-style illustration of a small boy patient character speaking, a speech bubble with foreign script text above his head, a translated caption bar below"},

{"n":8,"cut_type":"hard","subj":"hands","sz":"insert","ang":"매크로(편지 클로즈업)","cam":"고정","speed":"1x",
 "act":"소년의 손이 접힌 편지를 내밀고, 편지 겉면에 반짝임 이펙트가 스치듯 지나간다.",
 "asmr":"BGM만","sfx":"sparkle","cap":"편지 전달","fx":"반짝임 스파클 오버레이",
 "role":"build","why":"편지라는 사건의 핵심 오브젝트를 매크로 클로즈업으로 강조해 다음 컷의 확산 전개로 자연스럽게 넘어간다.",
 "shoot":"편지를 화면 중앙에 크게 배치하고 짧은 반짝임 파티클을 겹쳐 특별한 물건임을 시각화",
 "prompt":"A close-up of a folded paper letter being handed over, small sparkle particle effects around it, flat illustration style"},

{"n":9,"cut_type":"hard","subj":"face_hands","sz":"MS","ang":"정면 그룹샷","cam":"고정","speed":"1x",
 "act":"chibi 간호사 세 명이 한 화면에 모여 편지 소식을 듣고 놀라거나 흥미로워하는 반응을 보인다.",
 "asmr":"편지 반짝임 마법음","sfx":"sparkle","cap":"소식 확산","fx":"핑크톤 하이라이트",
 "role":"tension","why":"sat_mean 84.6으로 전체 14컷 중 최고 채도를 기록해 세 캐릭터가 모인 핑크톤 그룹 컷임을 뒷받침한다.",
 "shoot":"세 캐릭터를 나란히 배치하고 표정을 각각 다르게 연출(놀람/호기심/미소)해 반응의 다양성을 보여줌",
 "prompt":"Three chibi-style 2D animated nurse characters with pastel pink hair grouped together, varied surprised and curious expressions, soft pink-toned hospital background"},

{"n":10,"cut_type":"hard","subj":"face_hands","sz":"MCU","ang":"정면(팝인 등장)","cam":"고정(캐릭터 팝인)","speed":"1x",
 "act":"빈 배경에서 chibi 간호사 한 명이 등장해 그 편지가 자기 것이라 주장하는 대사를 한다.",
 "asmr":"BGM만","sfx":"","cap":"주장1","fx":"캐릭터 팝인",
 "role":"tension","why":"idx10 시작 프레임은 캐릭터가 아직 등장하지 않은 빈 배경이고 중간 프레임에서 팝인하는 구조로, 소동의 첫 번째 자기주장을 코믹하게 연출한다.",
 "shoot":"빈 배경 홀드 0.3초 후 캐릭터가 옆에서 등장하는 팝인 타이밍으로 편집",
 "prompt":"A chibi-style 2D animated nurse character with wavy hair popping into frame with a confident smile, plain hospital room background"},

{"n":11,"cut_type":"hard","subj":"face_hands","sz":"MCU","ang":"정면 투샷","cam":"고정","speed":"1x",
 "act":"또 다른 chibi 간호사가 옆에서 끼어들며 자기가 그 편지의 주인이라고 반박하듯 주장한다.",
 "asmr":"캐릭터 등장 스팅어","sfx":"character_sting","cap":"주장2","fx":"컷 끝부분 모션 블러(다음 컷 예고)",
 "role":"tension","why":"faces.json 얼굴 검출값이 0.8(80%)로 14컷 중 유일하게 튀는 컷 — 두 캐릭터가 나란히 정면을 보는 구도의 결과로, 정면 대결 구도를 수치로도 뒷받침한다.",
 "shoot":"두 캐릭터를 좌우로 배치하고 표정 대비(자신만만 vs 당황)를 크게 주어 코믹함을 강조",
 "prompt":"Two chibi-style 2D animated nurse characters standing side by side, one confident and one flustered expression, plain hospital interior background"},

{"n":12,"cut_type":"whip","subj":"face_hands","sz":"MS","ang":"로우앵글 전신(팝인 리빌)","cam":"크래시 줌","speed":"1x",
 "act":"세 번째 chibi 간호사가 모션 블러와 함께 화면 앞으로 튀어나오며 자기가 제일 귀엽다고 주장하는 포즈를 취한다.",
 "asmr":"휩 전환 강조음","sfx":"whip_whoosh","cap":"주장3","fx":"모션 블러 휩 팝인",
 "role":"tension","why":"hf_ratio_4k 0.233으로 14컷 중 최고치를 기록해 휩 전환 강조음이 실제로 삽입됐음을 수치로 뒷받침한다.",
 "shoot":"카메라가 살짝 아래에서 위로 크래시 줌하며 전신 포즈를 강조, 모션 블러를 0.1초가량 남겨 속도감 연출",
 "prompt":"A chibi-style 2D animated nurse character striking a cute confident full-body pose, motion blur streaks, low angle framing, hospital room background"},

{"n":13,"cut_type":"dissolve","subj":"mixed","sz":"insert","ang":"정면(일러스트 리빌 전환)","cam":"고정(디졸브 전환)","speed":"1x",
 "act":"캐릭터 클로즈업 반응 컷에서 시작해, 화면이 저채도 역사화풍 정지 일러스트(전사 캐릭터와 황금빛 아이템)로 디졸브 전환되며 이 소동이 고전 신화 패러디임을 알리는 해설 자막이 뜬다.",
 "asmr":"역사화풍 리빌 드럼힛","sfx":"epic_hit","cap":"신화 해설","fx":"세피아톤 디졸브 전환",
 "role":"reveal","why":"hf_ratio_4k 0.033으로 오히려 낮아, 절정부가 오디오보다 시각적 리빌(정지 일러스트로의 색보정 전환)에 의존함을 보여준다.",
 "shoot":"캐릭터 컬러톤에서 세피아/저채도 역사화풍 일러스트로 1초 내 디졸브, 해설 자막은 큰 흰 글씨로 배치",
 "prompt":"A dissolve transition from a colorful chibi character close-up into a sepia-toned historical illustration of an ancient warrior figure and a glowing golden fruit icon, dramatic reveal lighting"},

{"n":14,"cut_type":"hard","subj":"face_hands","sz":"MS","ang":"정면 그룹샷","cam":"고정","speed":"1x",
 "act":"자칭 '제일 귀여운' 간호사들이 나란히 서서 편지를 함께 받쳐 든 모습으로 화면이 정리되고, 자막이 상단 고정 타이틀 바 문구와 다시 맞물리며 끝난다.",
 "asmr":"엔딩 루프 챠임","sfx":"chime","cap":"엔딩 루프","fx":"정지 프레임 홀드",
 "role":"loop","why":"idx14(19.95~22.79s, 2.84초)는 14컷 중 가장 길게 홀드되며 onsets_per_s 2.82로 대사 밀도도 다시 높아져, 여운을 주는 엔딩 앙상블 컷임을 뒷받침한다.",
 "shoot":"세 캐릭터를 좌우 대칭으로 배치하고 편지를 중앙에 배치, 마지막 0.5초는 완전 정지로 홀드해 루프 재생에 자연스럽게 이어지게 함",
 "prompt":"Several chibi-style 2D animated nurse characters standing together holding a folded letter, symmetrical group pose, soft pastel pink hospital background, freeze-frame ending"},
]

json.dump(shots, open(os.path.join(D, 'shots_part1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('shots written', len(shots))
