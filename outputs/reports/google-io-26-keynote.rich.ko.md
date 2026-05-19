# Google I/O '26 Keynote

## 메타데이터

| 항목 | 값 |
|---|---|
| 채널 | Google |
| 업로드 | 2026-05-19 |
| 길이 | 2h 57m 25s |
| URL | https://www.youtube.com/watch?v=wYSncx9zLIU |
| 자막 출처 | manual (en) |

## 핵심 요약

Google I/O '26 Keynote은 2026년 5월 19일에 진행된 약 3시간 분량의 Google 라이브 방송으로, Sundar Pichai가 진행을 맡습니다. 키노트를 관통하는 한 줄 — Google의 월간 토큰 처리량이 2년 만에 9.7 trillion에서 3.2 quadrillion으로 도약했고, 이번 세대 제품들은 그 규모 위에 설계됐다는 것입니다.

대표 발표는 8세대 TPU(학습용 TPU 8t · 추론용 TPU 8i), Gemini Omni 멀티모달 생성 모델(Omni Flash 오늘 출시), Gemini 3.5 Flash와 Antigravity 2.0 에이전트 개발 플랫폼(93개 subagents가 12시간에 운영체제를 less than $1,000로 빌드), Google Cloud에서 24/7 동작하는 Gemini Spark 개인 에이전트, 근본적으로 새로워진 AI Search(새 검색창 · Search agents · Antigravity 기반 generative UI), 에이전트 커머스 스택(Universal Commerce Protocol · Agent Payments Protocol · Universal Cart에 Amazon · Meta · Microsoft · Salesforce · Stripe 합류), Neural Expressive 디자인 언어 · Omni · Daily Brief를 갖춘 재설계된 Gemini 앱, Google Pics · Stitch · Flow 크리에이티브 도구, 올가을 도착하는 Android XR 오디오 안경(Warby Parker · Gentle Monster 디자인), 그리고 CodeMender 보안 · Gemini for Science · WeatherNext · Isomorphic Labs의 면역 질환 · 암 pre-clinical로 마무리하는 Demis Hassabis의 클로징입니다.

## 다루는 주제

### 사전 행사 — Infinite Scaler 관객 게임 (00:00–55:51)

YouTube 크리에이터 Valkyrae와 CourageJD가 관객 참여형 게임을 진행합니다.

- Infinite Scaler는 QR 코드로 참여하는 크라우드 빌드 탑 점프 게임이며 다운로드 없이 즉시 플레이 가능합니다.
- 레벨은 사용자의 프롬프트를 Gemini가 다듬고 Nano Banana가 배경 · 전경 sprite sheets · depth map을 렌더링해 3D 효과를 만듭니다.
- 사전 행사 동안 163개국 over 20,000명이 참여하고 최고 점수는 800+ 레벨에 이릅니다.

### Sundar 오프닝 — 토큰 · capex · TPU 8 (01:06:52–01:20:50)

Sundar가 토큰 성장 · 인프라 투자 · 8세대 TPU로 한 해의 핵심을 정리합니다.

#### 도입

- Google은 현재 매월 3.2 quadrillion 토큰을 처리하며 작년 480 trillion · 2년 전 9.7 trillion 대비 1년 만에 약 7x 증가했습니다.
- 매월 over 8.5 million 개발자가 Google 모델로 빌드합니다.
- 모델 API는 분당 19 billion 토큰을 처리합니다.
- 지난 12개월 동안 over 375 고객이 각각 1 trillion 이상 토큰을 처리했습니다.
- 사용자 over 1 billion 제품이 13개, more than 3 billion 제품이 5개입니다.
- AI Overviews는 매월 over 2.5 billion 사용자입니다.
- AI Mode는 1년 만에 1 billion 사용자를 돌파했습니다.
- Gemini 앱은 over 900 million MAU(전년 400M 대비 2배 이상)이며 일일 요청은 over seven times 증가했습니다.
- Nano Banana로 over 50 billion 이미지가 생성됐습니다.

#### 제품 전반의 대화형 AI

- Maps가 10여 년 만의 최대 업데이트와 함께 Ask Maps를 도입했습니다.
- Ask YouTube는 대화형 · 후속 질문 친화적 답변으로 영상의 가장 관련된 지점으로 점프하며 올여름 미국에서 광범위 출시됩니다.
- Docs Live는 음성으로 자유롭게 말한 내용을 Gemini가 문서로 정리하며 올여름 Pro · Ultra 가입자에게 출시되고 이후 Gmail · Google Keep으로 확장됩니다.

#### Capex와 TPU 8

- Google의 capex는 2022년 about $31 billion에서 올해 approximately $180 to $190 billion으로 약 6배 증가합니다.
- 8세대 TPU는 Cloud Next에서 공개됐으며 학습용 TPU 8t와 추론용 TPU 8i로 구성됩니다.
- TPU 8t는 이전 세대 대비 거의 3배 raw compute를 제공합니다.
- JAX와 Pathways를 통해 over 1 million TPU를 전 세계 다중 사이트로 확장합니다.
- 곧 출시될 Flash 모델은 TPU 8i에서 약 1,500 tokens per second 속도로 시연됐습니다.
- TPU 8t · 8i 모두 와트당 성능이 up to two times 개선됐습니다.

### Gemini Omni와 SynthID 확장 (01:20:50–01:28:00)

Demis가 새 멀티모달 생성 패밀리와 콘텐츠 출처 확인의 다음 라운드를 소개합니다.

#### Gemini Omni

- Demis는 AGI가 just a few years away라고 말합니다.
- Gemini Omni는 어떤 입력에서든 어떤 결과물을 만드는 새 모델로 Gemini 지능과 Google 생성형 미디어 모델의 최고를 결합해 영상 · 이미지 · 인터랙티브 시뮬레이션을 만듭니다.
- Omni는 kinetic energy · gravity 같은 직관 물리 시뮬레이션에서 단계적 향상을 보입니다.
- Omni는 대화형 언어로 영상을 편집할 수 있게 해주며, 셀카 장면에 black hole을 추가하거나 배경을 바꾸는 프롬프트로 시연됩니다.
- Omni 패밀리의 첫 모델 Gemini Omni Flash가 오늘 Google 제품 전반에 제공되고 Omni Pro는 곧 공개됩니다.

#### SynthID와 Content Credentials

- 사람들은 고품질 deepfake 영상을 약 4분의 1만 정확히 식별합니다.
- SynthID는 지금까지 100 billion 이미지 · 영상과 60,000년 분량 오디오에 워터마크했습니다.
- Content Credentials Verification이 제품 전반에 적용되며 콘텐츠 출처(AI · 카메라 · 생성형 편집 여부)를 알려줍니다.
- SynthID와 Content Credentials Verification은 Circle to Search와 Chrome 우클릭을 통해 Search · Chrome으로 확장됩니다.
- NVIDIA가 작년에 합류한 데 이어 OpenAI · Kakao · Eleven Labs가 SynthID에 합류합니다.

### Gemini 3.5 Flash와 Antigravity 2.0 (01:28:00–01:39:30)

Sundar가 3.5 Flash를 소개하고 Varun Mohan이 Antigravity 2.0으로 운영체제를 빌드해 보입니다.

#### Gemini 3.5 Flash

- 3.5 Flash는 agentic coding · long-horizon tasks · real-world workflows에 집중한 첫 모델 시리즈로 frontier intelligence와 action을 결합합니다.
- Gemini 3.1 Pro 대비 거의 모든 벤치마크에서 우수하며 GDP val에서 큰 폭의 점프를 보였습니다.
- 출력 tokens per second 기준 다른 frontier 모델 대비 four times 빠릅니다.
- Google 내부 일일 토큰 처리량은 3월의 half a trillion에서 현재 more than 3 trillion으로 증가했습니다.

#### Antigravity 2.0

- Antigravity는 full CLI · SDK · 네이티브 음성 지원과 함께 Android · Firebase · Google AI Studio 통합으로 확장됩니다.
- Antigravity 2.0은 새 스탠드얼론 데스크톱 앱으로 agent-produced artifacts와 multi-agent orchestration에 집중하며 subagents · hooks · async task management를 갖췄습니다.
- 3.5 Flash와 함께 93개 subagents가 병렬로 12시간 만에 처음부터 운영체제를 빌드 — over 15,000 모델 요청 · 2.6 billion 토큰을 사용했습니다.
- 운영체제 빌드 비용은 less than $1,000 API 크레딧입니다.
- Antigravity 내에서 Flash는 12 times 빠르게 최적화됐고 외부 기준 4x보다 큰 폭입니다.
- Antigravity 2.0은 오늘 전 세계에 출시됐습니다.

#### 가격과 로드맵

- 3.5 Flash는 비교 가능 frontier 모델 대비 less than half 가격에 frontier 성능을 제공합니다.
- 워크로드 80%를 3.5 Flash로 전환하면 연간 over $1 billion 절감이 가능한 예시가 제시됐습니다.
- Gemini 3.5 Pro는 약 1개월 후 공개됩니다.

### Gemini Spark (01:39:30–01:47:30)

Sundar가 Spark를 소개하고 Josh Woodward가 노트북과 폰에서 데모합니다.

- Spark는 Google Cloud의 dedicated VM에서 24/7 동작하는 개인 AI 에이전트로 사용자는 노트북을 닫아도 됩니다.
- Spark는 Gemini 3.5와 Antigravity Harness 위에서 동작하고 Google 도구로 시작하며 몇 주 안에 MCP로 서드파티 도구와 연동됩니다.
- Spark가 Docs · 이메일 · 채팅을 가로질러 정보를 모아 개인 "ghost writer" skill로 이메일 초안을 작성하는 데모.
- block party 데모에서 Gmail 연동 Google Sheets로 RSVP 추적 · 미응답자에게 후속 메일 발송 · Google Slides의 "hype deck" 생성 · Drive 파일에서 HOA 규정을 반영하는 모습.
- Spark는 Android · iPhone에 걸쳐 동기화됩니다.
- Spark는 이번 주 신뢰 테스터, 다음 주 미국 Google AI Ultra 가입자 베타로 시작됩니다.
- 새 Ultra 플랜이 $100 a month에 출시되고 최상위 Ultra 플랜은 $250 a month에서 $200 a month로 인하됩니다.
- Spark는 올여름 Chrome 내부에서 agentic browser로 동작합니다.
- Android Halo는 폰의 에이전트 홈 베이스로 올해 후반 출시됩니다.

### AI Search의 다음 챕터 (01:47:30–02:03:30)

Liz Reid와 Robby Stein이 새 AI Search를 공개합니다.

#### AI Mode와 새 Search box

- AI Mode가 오늘 Gemini 3.5로 업그레이드됩니다.
- AI Mode는 over 1 billion 월간 사용자를 돌파했고 출시 이후 매 분기 쿼리가 more than doubling, 지난 분기에는 Search 쿼리가 사상 최고치를 기록했습니다.
- 새 intelligent Search box는 사용자의 호기심에 맞게 확장되고 자동 완성을 넘어선 AI 제안을 제공하며 텍스트 · 이미지 · 파일 · 영상을 함께 받습니다 — over 25 years 만의 최대 Search box 업그레이드로 오늘 출시됩니다.
- AI Overviews와 AI Mode는 메인 결과 페이지에서 AI Mode 후속 질문으로 매끄럽게 흐르는 하나의 seamless AI Search 경험으로 통합되며 오늘 전 세계 데스크톱 · 모바일에 적용됩니다.

#### Search agents · agentic coding

- Search는 biotech 주식 · 아파트 검색 · 스니커즈 드롭 같은 작업을 24/7 백그라운드로 수행하는 information agents를 올여름 도입합니다.
- Antigravity와 Gemini 3.5 Flash가 Search에 들어와 즉석에서 generative UI를 만듭니다.
- Robby Stein이 AI Overview 안에서 만들어지는 interactive black-hole 시각화와 후속 gravitational-wave 시뮬레이션을 시연합니다.
- Antigravity 기반 generative UI는 올여름 모든 사용자에게 무료로 출시됩니다.
- Search는 도구 · 트래커 · 대시보드 같은 stateful custom 경험을 빌드 — Gmail · Photos · Calendar를 연동한 weekend planner 데모.

### 에이전트 커머스 (02:03:30–02:11:00)

Vidhya Srinivasan이 세 가지 building block을 공개합니다.

#### Universal Commerce Protocol

- 사람들은 Google 전반에서 하루 over a billion 번 쇼핑합니다.
- Shopping Graph는 over 60 billion 제품 목록을 보유하며 지속 업데이트됩니다.
- UCP는 에이전트 커머스를 위한 오픈 소스 표준으로 창립 파트너에 더해 Amazon · Meta · Microsoft · Salesforce · Stripe가 합류했습니다.
- UCP는 호텔 · 로컬 음식 배달 등 더 많은 버티컬과 YouTube · 더 많은 제품으로 확장되고 Canada · Australia · U.K.에 향후 몇 달 내 도입됩니다.

#### Agent Payments Protocol

- AP2는 특정 브랜드 · 제품 · 지출 한도 같은 strict guardrails를 설정해 조건이 만족될 때만 구매하도록 합니다.
- AP2는 privacy-preserving 기술과 tamper-proof 디지털 mandate로 사용자 · 머천트 · 결제 처리기 간 영구 기록을 남깁니다.
- AP2는 향후 몇 달 동안 Gemini Spark를 시작으로 Google 제품에 도입됩니다.

#### Universal Cart

- Universal Cart는 머천트 · 서비스를 가로지르는 새 intelligent shopping cart입니다.
- 사용자는 Search · Gemini · YouTube · Gmail을 둘러보면서 아이템을 담을 수 있습니다.
- Universal Cart는 가격 인하 · 가격 이력 · 재입고를 감지하고 호환성 같은 지능적 추론을 적용합니다.
- Universal Cart는 Google Wallet 위에 빌드되어 Target 등 파트너의 숨은 혜택을 찾아냅니다.
- 올여름 미국 Search · Gemini 앱부터 시작되어 YouTube · Gmail로 확장됩니다.

### 재설계된 Gemini 앱 · Omni · Daily Brief (02:13:00–02:26:45)

Josh Woodward가 다시 등장해 새 앱 경험을 출시합니다.

#### 도달과 Neural Expressive

- Gemini 앱에 매월 more than 900 million 사용자가 옵니다.
- Personal Intelligence가 지난주 전 세계 사용자로 확장됐습니다.
- NotebookLM은 more than 1.5 billion notebooks · podcasts · slide decks 등을 생성했습니다.
- Gemini 앱은 more than 230 countries · over 70 languages에 제공됩니다.
- Neural Expressive는 유려한 애니메이션 · 생생한 컬러 · 새 타이포그래피 · 햅틱 피드백을 갖춘 새 디자인 언어로 오늘 Android · iOS · Web 전 세계 배포됩니다.
- Gemini Live는 즉시 인라인으로 열리며 지역 방언(Liverpool 액센트 시연 포함)이 곧 추가됩니다.

#### Omni와 Daily Brief

- Gemini Omni가 오늘 유료 가입자 대상 Gemini 앱에 도착 — Sashu라는 아티스트가 raw 영상에 360도 카메라 앵글을 적용하는 데모.
- 새 out-of-the-box 에이전트 Daily Brief가 받은편지함 · 캘린더 · 작업을 합쳐 아침 다이제스트를 만들어 오늘 미국 Google AI Plus · Pro · Ultra 가입자에게 제공됩니다.

#### Mac 앱과 음성 제어

- 네이티브 Gemini for Mac OS 앱은 Antigravity로 less than 100 days에 over 100 features를 출시했습니다.
- 새 function 키 길게 누르기 음성 제어로 행동을 받아쓰고 선택한 파일을 멀티모달로 읽습니다 — 백신 PDF에서 데이터를 추출해 강아지 호텔 이메일 초안을 작성하는 데모.
- 이 새 Gemini Spark 음성 기능은 올여름 Mac 앱에 도착합니다.

### Pics · Stitch · Flow 크리에이티브 도구 (02:28:37–02:37:25)

Suz Chamber가 세 가지 출시를 안내합니다.

- Google Pics는 객체 인식 · hover-to-remove · 원클릭 번역을 갖춘 Google Workspace의 새 이미지 생성/편집 도구이며 출력은 SynthID로 워터마크되고 올여름 출시됩니다.
- Stitch는 지난 한 해 over 100 million UI 화면을 생성했으며 음성 · 텍스트 실시간 협업과 원클릭 코드/사이트 내보내기가 오늘 글로벌 출시됩니다.
- Google Flow에 Gemini Omni 스타일 변환 · 한 이미지에서 16개 카메라 앵글 영상을 만드는 새 에이전트 · 대규모 장면 편집 · vibe-coded Flow tools · Google Flow Music이 모두 오늘 제공됩니다.

### Android XR Intelligent Eyewear (02:37:45–02:49:25)

Shahram Izadi가 오디오 안경을 공개하고 라이브 Gemini 데모를 진행합니다.

- Android XR은 Samsung과 함께 빌드되어 Qualcomm Snapdragon에 최적화됐습니다.
- 두 종류의 AI 안경이 폰에 연결됩니다 — in-lens 디스플레이를 갖춘 display glasses와 디스플레이가 없는 audio glasses.
- 첫 Google 오디오 안경은 올가을 도착하며 Gemini가 하루 종일 귀에 사적으로 말해주는 도움을 제공합니다.
- 오디오 안경 파트너는 Gentle Monster · Warby Parker(아이웨어), Samsung(하드웨어), Google(소프트웨어)입니다.
- 안경은 Android · iOS 모두에 페어링됩니다.
- 무대 데모에서 Personal Intelligence로 Maps 경로 안내(Redwood Grove Natural Preserve), Koopa Cafe에서 DoorDash로 nitro cold brew 주문, 음소거된 텍스트 요약, 가족 저녁 일정 캘린더 추가, "Google I/O 2026" 비행선과 함께 Nano Banana 카툰 스타일 관객 셀카를 시연합니다.
- Display glasses는 올해 후반 Trusted Tester Program이 확대됩니다.

### Demis 클로징 — 안전 · Gemini for Science · Isomorphic Labs (02:49:25–02:55:48)

Demis Hassabis가 안전과 과학 응용으로 마무리합니다.

- CodeMender는 Google의 Code Security Agent로 보안 취약점을 자동으로 찾아 수정하며 새 CodeMender API가 일부 전문가 대상 테스트 중입니다.
- Gemini for Science는 새 Labs 프로토타입(논문 따라잡기 · 연구 목표를 코드로 · 가설 생성)을 갖춘 연구 가속 도구 묶음입니다.
- AlphaEarth Foundations는 deforestation · food security 같은 문제에 도움을 주는 지구의 디지털 트윈에 가장 가까운 것으로 설명됩니다.
- WeatherNext는 2025년에 Jamaica의 category 5 허리케인을 3일 미리 더 정확하게 예측했습니다.
- AlphaFold · AlphaGenome은 전 세계 수백만 과학자가 표준 도구로 사용 중입니다.
- Isomorphic Labs는 면역 질환 · 암을 포함한 여러 프로젝트에서 pre-clinical 단계에 있습니다.

## 인물 · 조직 · 제품 · 장소

### 인물

- Sundar Pichai
- Demis Hassabis
- Varun Mohan
- Josh Woodward
- Liz Reid
- Robby Stein
- Vidhya Srinivasan
- Suz Chamber
- Shahram Izadi
- Nishtha Bhatia
- Jay Kim
- Valkyrae
- COURAGEJD
- Holly
- Timmy

### 조직

- Google
- Google DeepMind
- Google Cloud
- Anthropic
- NVIDIA
- OpenAI
- Kakao
- Eleven Labs
- Samsung
- Qualcomm
- Warby Parker
- Gentle Monster
- Amazon
- Meta
- Microsoft
- Salesforce
- Stripe
- Target
- Isomorphic Labs
- DoorDash
- Hurricane Center

### 제품

- Gemini
- Gemini 3.5 Flash
- Gemini 3.5 Pro
- Gemini Omni
- Gemini Omni Flash
- Gemini Spark
- Gemini Live
- Gemini for Science
- Nano Banana
- Veo
- Genie
- TPU 8t
- TPU 8i
- Snapdragon
- Antigravity
- Antigravity 2.0
- Ask YouTube
- Ask Maps
- Docs Live
- AI Overviews
- AI Mode
- Google Search
- Universal Commerce Protocol
- Agent Payments Protocol
- Universal Cart
- Google Pay
- Google Wallet
- Shopping Graph
- Google AI Plus
- Google AI Pro
- Google AI Ultra
- NotebookLM
- Neural Expressive
- Daily Brief
- Android Halo
- Android XR
- Google Pics
- Stitch
- Google Flow
- Google Flow Music
- Personal Intelligence
- SynthID
- Content Credentials Verification
- Pathways
- JAX
- Model Context Protocol
- CodeMender
- AlphaFold
- AlphaGenome
- AlphaEarth Foundations
- WeatherNext
- Infinite Scaler
- WorkOnward
- Circle to Search

### 장소

- Shoreline
- Jamaica
- New York City
- South Korea
- Liverpool
- Canada
- Australia
- U.K.
- Redwood Grove Natural Preserve

## 수치 및 데이터

| 값 | 맥락 |
|---|---|
| 3.2 quadrillion | 현재 월간 Google 서비스 전반 토큰 처리량 |
| 480 trillion | 작년 I/O 시점 월간 토큰 처리량 |
| 9.7 trillion | 2년 전 월간 토큰 처리량 |
| seven times | 1년간 월간 토큰 증가율 |
| over 8.5 million | 월간 Google 모델 빌드 개발자 수 |
| 19 billion | 분당 API 토큰 처리량 |
| over 375 | 1년간 각자 1 trillion 토큰 이상 처리한 고객 수 |
| 13 products | 사용자 10억+ Google 제품 수 |
| 5 | 사용자 30억+ Google 제품 수 |
| over 2.5 billion | AI Overviews 월간 사용자 |
| 1 billion | AI Mode 월간 사용자 (1년 만에) |
| over 900 million | Gemini 앱 MAU |
| seven times | 1년간 Gemini 앱 일일 요청 증가 |
| 50 billion | Nano Banana 생성 이미지 수 |
| $31 billion | 2022년 연간 capex |
| $180 to $190 billion | 2026년 예상 연간 capex |
| six times | 2022 → 2026 capex 배수 |
| three times | TPU 8t 이전 세대 대비 연산 |
| over 1 million | JAX · Pathways로 확장한 TPU 수 |
| 1,500 tokens per second | TPU 8i Flash 시연 속도 |
| two times | TPU 8t · 8i 와트당 성능 |
| 100 billion | SynthID 워터마크 이미지 · 영상 |
| 60,000 years | SynthID 워터마크 오디오 분량 |
| about a quarter | 사람들이 고품질 deepfake를 식별하는 비율 |
| four times | 3.5 Flash가 다른 frontier 대비 빠른 정도 |
| 12 times | Antigravity 내 3.5 Flash 가속 |
| half a trillion | Google 내부 일일 토큰 처리(3월) |
| more than 3 trillion | Google 내부 일일 토큰 처리(현재) |
| 93 | OS 빌드에 사용된 subagents 수 |
| over 15,000 | OS 빌드 모델 요청 수 |
| 2.6 billion | OS 빌드 토큰 사용량 |
| less than $1,000 | OS 빌드 API 크레딧 |
| less than half | 비교 frontier 대비 3.5 Flash 가격 |
| over $1 billion | 80% 워크로드 전환 시 연간 절감 예시 |
| $100 a month | 새 Google AI Ultra 플랜 가격 |
| $250 a month to $200 a month | 최상위 Ultra 플랜 인하 |
| over 1 billion | Search가 분당 업데이트하는 fact 수 |
| more than doubling | 출시 이후 AI Mode 쿼리 분기별 증가 |
| over 25 years | 새 Search box 도입 전 경과 시간 |
| 1 billion | Google 일일 쇼핑 검색 수 |
| over 60 billion | Shopping Graph 제품 목록 |
| 230 | Gemini 앱 제공 국가 수 |
| over 70 languages | Gemini 앱 언어 수 |
| more than 1.5 billion | NotebookLM 생성물 수 |
| over 100 million | 지난 한 해 Stitch UI 화면 수 |
| over 100 features | Mac 앱 출시 기능 수 |
| over 13,000 | WorkOnward 사용자(New York City) |
| category 5 | WeatherNext가 미리 예측한 Jamaica 허리케인 등급 |
| three days | WeatherNext의 사전 경보 일수 |
| this fall | 첫 오디오 안경 출시 시점 |
| 20,000 | Infinite Scaler 사전 행사 참여자 수 |
| 163 countries | Infinite Scaler 참여 국가 수 |

## 주요 인용

> It's been 10 years since we pivoted the company to be AI first.
> — Sundar Pichai

> that number has jumped seven times to 3.2 quadrillion tokens per month.
> — Sundar Pichai

> Never imagined I would say quadrillion in an I/O keynote, but here we are.
> — Sundar Pichai

> Some out there might call this token maxing, and there's probably some truth to it.
> — Sundar Pichai

> AI Overviews now has over 2.5 billion monthly users
> — Sundar Pichai

> Today, we have surpassed 900 million, more than doubling in a year.
> — Sundar Pichai

> more than 50 billion images have been generated with our Nano Banana model.
> — Sundar Pichai

> if you learn anything in 27 years of working on Search, it's that latency matters.
> — Sundar Pichai

> AI capabilities have leaped forwards.
> — Demis Hassabis

> I'm excited to announce Gemini Omni.
> — Demis Hassabis

> Anything becomes a canvas for creating entirely new realities.
> — Demis Hassabis

> SynthID has now watermarked 100 billion images and videos, along with 60,000 years of audio assets.
> — Sundar Pichai

> It's obviously fake. I don't eat hamburgers.
> — Sundar Pichai

> today, I'm excited to introduce Gemini 3.5 Flash, our first in a series of models combining frontier intelligence with action.
> — Sundar Pichai

> We've moved beyond AI tools that help us write, to agents that help us act.
> — Varun Mohan

> Like I said: Unabashedly agent first.
> — Varun Mohan

> Over 12 hours, 93 subagents working in parallel made over 15,000 model requests and processed 2.6 billion tokens to take an initially empty project to the core of a functioning operating system
> — Varun Mohan

> Multiday engineering efforts are collapsing into hours, if not minutes.
> — Varun Mohan

> Introducing Gemini Spark.
> — Sundar Pichai

> It runs on dedicated virtual machines on Google Cloud, and it is 24/7. And yes, you can close your laptop.
> — Sundar Pichai

> Spark will catch them and then run with them.
> — Josh Woodward

> we're introducing a new Ultra plan for $100 a month.
> — Josh Woodward

> as of today, we're upgrading it on Gemini 3.5.
> — Liz Reid

> Google Search is AI Search through and through.
> — Liz Reid

> This is the biggest upgrade to our iconic Search box since its debut over 25 years ago.
> — Liz Reid

> We're entering the era of Search agents.
> — Liz Reid

> We're bringing Antigravity and the agentic coding capabilities of Gemini
> — Robby Stein

> This is agentic coding at the scale of Search.
> — Robby Stein

> It now has over 60 billion listings and they are constantly updated.
> — Vidhya Srinivasan

> UCP does for agentic commerce what HTTP did for the web
> — Vidhya Srinivasan

> I'm excited to announce the Universal Cart, a truly intelligent shopping cart.
> — Vidhya Srinivasan

> just think of it as shopping with superpowers.
> — Vidhya Srinivasan

> More than 900 million users are coming to the Gemini app every month
> — Josh Woodward

> we've completely redesigned the Gemini experience from the ground up.
> — Josh Woodward

> Gemini Omni is coming to the Gemini app for paid subscribers today.
> — Josh Woodward

> agents don't just answer questions; they proactively work on your behalf.
> — Josh Woodward

> I discovered Gemini could help me with a lot of things.
> — Holly

> the real breakthrough isn't the technology; it's what you do with it.
> — Suz Chamber

> Introducing Google Pics, a new product in Google Workspace.
> — Suz Chamber

> the world used Stitch to generate over 100 million UI screens.
> — Suz Chamber

> This is such an exciting time for XR.
> — Shahram Izadi

> our first audio glasses will arrive this fall.
> — Shahram Izadi

> You've got the world's top eyewear designers at Gentle Monster and Warby Parker creating iconic designs.
> — Shahram Izadi

> AGI is now on the horizon and it will be the most profound and impactful technology ever invented.
> — Demis Hassabis

> If built right, it could propel human progress and flourishing beyond our imagination.
> — Demis Hassabis

> Building on this momentum, I'm excited to announce Gemini for Science.
> — Demis Hassabis

> Our mission is to reimagine the drug discovery process with the goal of one day solving all disease.
> — Demis Hassabis

> we will realize that we were standing in the foothills of the singularity.
> — Demis Hassabis
