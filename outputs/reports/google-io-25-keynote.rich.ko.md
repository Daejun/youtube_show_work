# Google I/O '25 Keynote

## 메타데이터

| 항목 | 값 |
|---|---|
| 채널 | Google |
| 업로드 | 2025-05-20 |
| 길이 | 1h 55m 16s |
| URL | https://www.youtube.com/watch?v=o8NiE3XMPrM |
| 자막 출처 | auto (en) |

## 핵심 요약

Google I/O '25 Keynote은 2025년 5월 20일에 진행된 1시간 55분 분량의 Google 라이브 방송으로, dozen이 넘는 Gemini 모델 · 연구 업데이트, Google Beam 공개, Project Mariner와 Agent Mode를 통한 에이전트 기능 확장, Google Search의 AI Mode 도입, 새 Gemini 앱 기능과 Google AI Pro · Ultra 구독 플랜, 생성형 미디어 출시(Imagen 4, Veo 3, Lyria 2, Flow), 그리고 Samsung의 Project Muhaan 헤드셋과 Gentle Monster · Warby Parker가 합류한 시제품 안경을 포함한 Android XR을 다룹니다.

핵심 메시지는 "연구가 대규모 제품으로 이전됐다"입니다. Sundar Pichai는 9.7 trillion → 480 trillion으로 1년 만에 약 50x 증가한 월간 토큰 처리량과 400 million MAU의 Gemini 앱을 들며 시작합니다. Demis Hassabis와 Tulsi는 LM Arena 전 카테고리 1위의 Gemini 2.5 Pro와 새 Deep Think 모드 · Gemini Diffusion을 소개합니다. Liz Reid는 personal context · deep search · agentic checkout · virtual try-on · Search Live를 갖춘 AI Mode를 공개합니다. Josh Woodward는 같은 날 출시되는 Veo 3 · Imagen 4 · Gemini in Chrome을, Jason과 Josh는 Flow 영화 제작 도구를 선보입니다. Sriram과 Nishtha는 Samsung의 Project Muhaan과 Gentle Monster · Warby Parker가 합류한 안경을 통한 Android XR로 마무리합니다.

## 다루는 주제

### 오프닝 (00:00–02:17)

영상 인트로와 Sundar Pichai의 인사.

- Sundar는 Shoreline 현장과 전 세계 시청자를 맞이합니다.

### Sundar의 인트로 (02:17–19:29)

Gemini 모멘텀, 인프라, 첫 번째 제품 발표 묶음.

#### 모멘텀

- Google은 지난 I/O 이후 a dozen 이상의 모델 · 연구 성과를 발표하고 20개 이상의 주요 AI 제품 · 기능을 출시했습니다.
- Elo 점수는 첫 Gemini Pro 이후 300점 이상 상승했고 Gemini 2.5 Pro는 Elo Arena 모든 카테고리를 석권했습니다.
- 업데이트된 2.5 Pro는 Web Dev Arena 1위로 이전 버전을 142 Elo 포인트 앞섭니다.
- Cursor에서 Gemini는 올해 가장 빠르게 성장하는 모델로 분당 hundreds of thousands of lines of accepted code를 생성합니다.
- Gemini는 Pokémon Blue를 완주해 여덟 개의 배지 · Victory Road · Elite Four · Champion을 모두 격파했습니다.

#### 인프라

- 7세대 TPU Ironwood는 thinking과 inference를 대규모로 처리하기 위해 설계된 첫 칩으로 10x 성능과 한 pod당 42.5 exaflops 연산을 제공합니다.
- Ironwood는 올해 후반 Google Cloud 고객에게 제공됩니다.
- Google은 현재 매월 480 trillion 토큰을 처리하며 1년 전 9.7 trillion 대비 약 50x 증가했습니다.

#### 도입

- over 7 million 개발자가 Google AI Studio와 Vertex AI에서 Gemini API로 빌드했고 지난 I/O 대비 5x 이상 성장했습니다.
- Vertex AI의 Gemini 사용량은 지난해 대비 40x 이상 늘었습니다.
- Gemini 앱은 over 400 million MAU이며 2.5 Pro 사용량은 45% 증가했습니다.
- AI overviews는 매월 1.5 billion 사용자를 넘었습니다.

#### Google Beam

- Google Beam은 2D 영상 스트림을 사실적인 3D 경험으로 변환하는 새로운 AI-우선 영상 통신 플랫폼입니다.
- 6개의 카메라가 다양한 각도에서 사용자를 포착하고 AI가 3D light field 디스플레이에 렌더링합니다.
- 헤드 트래킹은 밀리미터 단위, 60 frames per second로 동작합니다.
- HP와 협력한 첫 Google Beam 디바이스는 올해 후반 얼리 고객에게 제공됩니다.

#### 음성 번역과 Project Astra

- Google Meet의 실시간 음성 번역은 가입자 대상 English · Spanish로 시작되며 추가 언어가 곧, 기업용은 올해 후반 도입됩니다.
- Project Astra의 카메라 · 화면 공유를 탑재한 Gemini Live가 오늘 Android · iOS 전체에 배포됩니다.

#### Project Mariner와 에이전트 생태계

- Project Mariner는 최대 10개 동시 작업을 관리하는 멀티태스킹을 도입했습니다.
- teach-and-repeat 기능으로 한 번의 시연으로 작업 계획을 학습합니다.
- Mariner의 computer-use 기능은 Gemini API를 통해 개발자에게 제공되며 Automation Anywhere · UiPath가 테스트 중이고 여름에 폭넓게 공개됩니다.
- Google의 open agent-to-agent 프로토콜은 Cloud Next에서 60개 이상 파트너의 지지로 시작됐습니다.
- Gemini SDK는 Anthropic의 Model Context Protocol(MCP) 도구와 호환됩니다.

#### Agent Mode와 personal context

- Gemini 앱의 Agent Mode는 Project Mariner를 활용해 Zillow 같은 사이트에서 아파트를 찾습니다.
- 실험판 Agent Mode가 곧 가입자에게 제공됩니다.
- Gmail의 personalized smart replies는 Drive · 과거 이메일 · Docs에서 personal context를 가져오며 올해 여름 가입자에게 제공됩니다.

### Google DeepMind · 개발자용 Gemini (19:29–46:04)

Demis Hassabis와 Tulsi가 Gemini 2.5 · 개발자 기능 · 딥 리서치 · DeepMind 과학 성과를 소개합니다.

#### Gemini 2.5

- Gemini 2.5 Pro는 Web Dev Arena 1위, Learn LM 통합으로 학습 모델 1위, LM Arena 전 카테고리 1위입니다.
- 업데이트된 2.5 Flash는 LM Arena에서 2.5 Pro에 이은 2위이며 6월 초 정식 출시, 2.5 Pro는 곧 이어집니다.

#### 개발자 기능

- 텍스트-투-스피치 프리뷰는 멀티스피커 지원(두 음성)을 갖추고 24개 이상 언어에서 동작합니다.
- Live API에 2.5 Flash 네이티브 오디오 대화 프리뷰가 오늘 추가되어 화자와 배경 음성을 구분합니다.
- Gemini 2.5는 indirect prompt injection 방어가 강화된 Google의 가장 안전한 모델입니다.
- 2.5 Pro와 Flash 모두 Gemini API · Vertex AI에서 thought summaries를 제공합니다.
- 업데이트된 2.5 Flash는 동일 성능에 22% 적은 토큰을 사용합니다.
- thinking budgets가 2.5 Pro에도 도입되어 정식 출시와 함께 몇 주 안에 제공됩니다.
- 2.5 Pro 데모는 American Museum of Natural History 인터랙티브의 3D 버전을 Google AI Studio에서 37 seconds 사고 후 생성합니다.

#### Jules와 Gemini Diffusion

- Jules는 GitHub와 연동되는 비동기 코딩 에이전트로 jules.google에서 공개 베타로 시작합니다.
- Gemini Diffusion은 2.0 Flashlight보다 5x 빠르면서 코딩 성능을 유지하는 실험적 텍스트 확산 모델입니다.

#### Deep Think와 world model

- Deep Think는 병렬 사고 기법을 사용하는 2.5 Pro의 새 모드입니다.
- Deep Think는 USAMO 2025 · Live Code Bench · MMMU에서 강력한 결과를 보입니다.
- Deep Think는 Gemini API를 통해 신뢰 테스터에게 먼저 제공된 뒤 폭넓게 공개됩니다.
- Gemini는 Genie 2를 기반으로 사용자가 상호작용 가능한 시뮬레이션을 만들 수 있는 world model로 확장되고 있습니다.
- Gemini Robotics는 로봇이 잡기 · 지시 따르기 · 새로운 작업 적응을 학습하도록 하는 전용 파인튠 모델입니다.

#### Project Astra와 DeepMind 과학

- Project Astra 데모는 음성 · 웹 검색 · 영상 · 이메일 · 통화로 자전거를 수리하는 시나리오를 보여줍니다.
- DeepMind 과학 성과로 AlphaProof(math olympiad silver) · Co-scientist · AlphaEvolve · AMY · AlphaFold 3 · Isomorphic Labs가 있습니다.
- AlphaFold는 2.5 million 이상의 연구자가 사용 중입니다.
- Google은 Aira와 협력해 Astra 기술을 시각장애인 · 저시력 커뮤니티의 보행 지원에 적용했습니다.

### Search (46:04–01:11:06)

Liz Reid가 deep search · agentic actions · multimodal Search Live · shopping · 맞춤형 Gemini 2.5를 갖춘 AI Mode를 공개합니다.

#### AI Overviews와 Lens

- AI overviews는 200개 이상 국가 · 지역에서 매월 1.5 billion 사용자를 넘었습니다.
- US와 India에서 AI overviews는 해당 쿼리 유형의 over 10% 성장을 이끌고 있습니다.
- Google Lens는 전년 대비 65% 성장과 over 100 million 시각 검색을 기록했으며 전체 사용자는 over 1.5 billion 월간 사용자를 넘었습니다.

#### AI Mode

- AI Mode는 Gemini 2.5를 기반으로 한 재설계 검색으로 오늘부터 US 전체에 새 탭으로 배포됩니다.
- AI Mode는 query fan-out 기법으로 knowledge graph · shopping graph · 500 million Maps 기여자에 걸쳐 다중 검색을 수행합니다.
- personal context는 Gmail부터 연결되며 사용자가 언제든 연결 · 해제할 수 있고 올여름 도입됩니다.
- Deep Search는 dozens 또는 hundreds의 검색을 발사해 전문가 수준의 인용 보고서를 몇 분 안에 생성합니다.
- Project Mariner의 에이전트 기능은 AI Mode로 들어와 event tickets · restaurant reservations · 지역 서비스 약속을 처리합니다.
- Search Live는 Project Astra의 라이브 카메라 기능을 AI Mode로 가져오며, 아이들과 함께한 elephant-toothpaste 데모로 시연됐습니다.

#### 쇼핑

- Search 쇼핑은 over 50 billion 제품 목록의 shopping graph 위에서 동작합니다.
- 새 virtual try-on은 패션 전용으로 학습된 맞춤형 이미지 생성 모델과 3D 형상 이해를 사용합니다.
- 새 agentic checkout은 가격을 추적하고 목표가에 카트에 담아 Google Pay로 결제하며 사용자의 안내를 따릅니다.
- virtual try-on은 오늘 Labs에서 시작되고 visual shopping · agentic checkout은 몇 달 안에 출시됩니다.

#### 맞춤형 Gemini 2.5

- 맞춤형 Gemini 2.5는 이번 주에 AI Overviews와 AI Mode에 적용됩니다.

### Gemini 앱 (01:11:06–01:24:02)

Josh Woodward가 personal context · Gemini Live · Deep Research · Canvas · Gemini in Chrome · Imagen 4 · Veo 3를 시연합니다.

#### Gemini Live

- Gemini Live는 over 45개 언어 · 150개 이상 국가에서 동작하며 음성 대화는 텍스트 대비 5배 더 깁니다.
- 카메라 · 화면 공유를 포함한 Gemini Live가 오늘 무료로 Android · iOS의 Gemini 앱에 배포됩니다.
- 몇 주 안에 Calendar · Maps · Keep · Tasks와 연동됩니다.

#### Deep Research와 Canvas

- Deep Research는 사용자가 직접 파일을 업로드할 수 있게 됐고 곧 Drive · Gmail로 확장됩니다.
- Canvas는 보고서를 한 번에 dynamic webpage · infographic · quiz · 45개 언어 팟캐스트로 변환합니다.

#### Gemini in Chrome

- Gemini in Chrome은 이번 주 미국의 Gemini 가입자를 시작으로 배포되며 페이지의 맥락을 자동으로 이해합니다.

#### Imagen 4와 Veo 3

- Imagen 4는 더 풍부한 디테일과 더 나은 텍스트 · 타이포그래피를 갖춘 Google의 새 이미지 모델로 오늘 Gemini 앱에 도착합니다.
- Imagen 4 빠른 변형은 이전 모델보다 10x 더 빠릅니다.
- Veo 3는 sound effects · 배경음 · 대사 등 native audio generation을 탑재한 최신 영상 모델로 오늘 출시됩니다.

### 생성형 미디어 (01:24:02–01:37:37)

Lyria 2 · SynthID · Aronofsky 협업 · Flow · 새 AI 구독 플랜.

- Lyria 2는 보컬 · 솔로 · 합창을 포함한 고품질 음악을 생성하며 오늘 enterprises · YouTube creators · 음악가에게 제공됩니다.
- 지금까지 over 10 billion 콘텐츠가 SynthID로 워터마크됐습니다.
- SynthID Detector는 이미지 · 오디오 · 텍스트 · 비디오에서 SynthID를 식별하며 오늘 얼리 테스터에게 배포됩니다.
- Google은 감독 Darren Aronofsky의 Primordial Soup과 협력해 Veo를 영화 제작 도구로 다듬으며 단편 3편을 계획 중입니다.
- 감독 Eliza McNitt의 단편 Ancestor는 실사 연기와 Veo 영상을 결합합니다.
- Flow는 Veo · Imagen · Gemini를 결합한 AI 영화 제작 도구로 캐릭터 · 장면 일관성과 정밀 카메라 제어를 제공하며 오늘 출시됩니다.
- Google AI Pro(전 세계 제공)와 Google AI Ultra(미국 우선, 글로벌 곧) 두 구독으로 개편됩니다.
- Ultra는 Deep Think · Veo 3와 Flow · YouTube Premium · 대용량 스토리지를 포함합니다.

### Android XR (01:37:37–01:51:09)

Sriram이 Android XR과 Samsung의 Project Muhaan 헤드셋 · 시제품 안경을 공개합니다.

#### Android XR 플랫폼

- Android XR은 Gemini 시대에 맞춰 빌드된 첫 Android 플랫폼으로 헤드셋부터 안경까지 다양한 기기를 지원합니다.
- Android XR은 Samsung과 한 팀으로 만들었으며 Qualcomm Snapdragon에 최적화됐습니다.

#### Project Muhaan 헤드셋

- Samsung의 Project Muhaan은 첫 Android XR 디바이스로 올해 후반 출시됩니다.

#### Android XR 안경

- Android XR 안경은 카메라 · 마이크 · 스피커 · 선택형 in-lens 디스플레이를 갖춘 종일 착용 디자인이며 사용자의 폰과 연동됩니다.
- 안경 데모는 Gemini가 메시지 · 이전에 본 커피숍 검색 · 내비게이션 · 사진 촬영 · 캘린더 일정을 처리하는 모습을 보여줍니다.
- 안경의 실시간 채팅 번역이 Nishtha의 Hindi와 Sriram의 Farsi 사이에서 시연됐고 무대에는 영어 자막이 함께 노출됐습니다.
- 시제품 안경은 이미 신뢰 테스터의 손에 있고 개발자는 올해 후반부터 안경 빌드를 시작할 수 있습니다.
- Gentle Monster와 Warby Parker가 첫 안경 파트너로 합류합니다.

### 마무리 (01:51:09–01:55:16)

Sundar가 Fire Sat · Wing 재난 구호 · 부모님과의 Waymo 탑승으로 마무리합니다.

- Fire Sat는 멀티스펙트럼 위성 이미지와 AI로 270 square feet 크기까지 산불을 탐지하는 위성 군집입니다.
- 첫 위성은 궤도에 있으며 본격 가동 시 갱신 주기가 12 hours에서 20 minutes로 단축됩니다.
- Hurricane Helene 당시 Wing은 Walmart · Red Cross와 협력해 North Carolina의 YMCA 쉘터에 음식 · 의약품을 드론으로 배달했습니다.

## 인물 · 조직 · 제품 · 장소

### 인물

- Sundar
- Demis
- Tulsi
- Liz
- Rajan
- Vidhya
- Bidya
- Josh
- Jason
- Sriram
- Nishtha
- Darren Aronofsky
- Eliza McNitt
- Shankar Mahadevan

### 조직

- Google
- Google DeepMind
- Anthropic
- HP
- Samsung
- Qualcomm
- Automation Anywhere
- UiPath
- Cursor
- Zillow
- Aira
- Isomorphic Labs
- Primordial Soup
- Gentle Monster
- Warby Parker
- Walmart
- Red Cross

### 제품

- Gemini
- Gemini 2.5 Pro
- Gemini 2.5 Flash
- Deep Think
- Gemini Diffusion
- TPU Ironwood
- Google Beam
- Project Astra
- Project Mariner
- Agent Mode
- Gemini API
- Vertex AI
- Google AI Studio
- Jules
- Learn LM
- Gemini Live
- Gemini Robotics
- AlphaFold 3
- AlphaProof
- Co-scientist
- AlphaEvolve
- Genie 2
- AI Overviews
- AI Mode
- Google Lens
- Search Live
- Deep Search
- Google Pay
- Imagen 4
- Veo 3
- Lyria 2
- SynthID
- SynthID Detector
- Flow
- Google AI Pro
- Google AI Ultra
- YouTube Premium
- Android XR
- Project Muhaan
- Snapdragon
- Fire Sat
- Wing
- Waymo
- Gemini in Chrome
- Canvas
- Deep Research
- Model Context Protocol

### 장소

- Shoreline
- Austin
- Utah
- Zion National Park
- Nashville
- North Carolina
- California
- San Francisco

## 수치 및 데이터

| 값 | 맥락 |
|---|---|
| over a dozen | 지난 I/O 이후 발표된 모델 · 연구 성과 수 |
| over 20 | 지난 I/O 이후 출시된 주요 AI 제품 · 기능 수 |
| more than 300 | 첫 Gemini Pro 이후 Elo 점수 상승 폭 |
| 142 | Web Dev Arena에서 업데이트된 2.5 Pro가 이전 버전을 앞선 Elo 차이 |
| 10x | 이전 세대 대비 TPU Ironwood 성능 |
| 42.5 exaflops | TPU Ironwood pod당 연산량 |
| 9.7 trillion | 1년 전 월간 토큰 처리량 |
| 480 trillion | 현재 월간 토큰 처리량 |
| 50x | 1년간 월간 토큰 처리 증가율 |
| over 7 million | Gemini API로 빌드한 개발자 수 |
| over 5x | 지난 I/O 대비 Gemini API 개발자 성장률 |
| more than 40 times | 지난해 대비 Vertex AI의 Gemini 사용량 증가 |
| over 400 million | Gemini 앱 MAU |
| 45% | 2.5 Pro 사용자의 Gemini 앱 사용량 증가 |
| 1.5 billion | AI overviews 월간 사용자 |
| 200 | AI overviews 제공 국가 · 지역 수 |
| over 10% | US · India 시장에서 AI overviews 노출 쿼리 성장률 |
| 65% | Google Lens 전년 대비 성장률 |
| more than 100 million | 올해 Lens 시각 검색 수 |
| six | Google Beam에서 사용자를 포착하는 카메라 수 |
| 60 frames per second | Beam 헤드 트래킹 프레임율 |
| up to 10 | Project Mariner 동시 작업 수 |
| $1,200 a month | Agent Mode 데모의 Austin 룸메이트당 예산 |
| over 60 | agent-to-agent 프로토콜 출시 파트너 수 |
| 24 languages | Gemini 멀티스피커 TTS 지원 언어 |
| 22% | 업데이트된 2.5 Flash 효율 개선 |
| 37 seconds | 3D 스케치 → 코드 데모의 2.5 Pro 사고 시간 |
| five times faster | Gemini Diffusion vs 2.0 Flashlight |
| 2.5 million | AlphaFold를 사용하는 전 세계 연구자 수 |
| over 1.5 billion | Google Lens 월간 사용자 |
| 500 million | Maps 커뮤니티 기여자 수 |
| over 50 billion | shopping graph 제품 목록 수 |
| 45 languages | Gemini Live 지원 언어 수 |
| more than 150 countries | Gemini Live 지원 국가 수 |
| five times longer | 텍스트 대비 Gemini Live 음성 대화 길이 |
| 10 times faster | Imagen 4 빠른 변형 vs 이전 모델 |
| 10 billion | SynthID로 워터마크된 콘텐츠 수 |
| 270 square feet | Fire Sat가 탐지 가능한 최소 산불 크기 |
| 20 minutes | Fire Sat 본격 가동 시 갱신 주기 |
| 12 hours | 현재 위성 이미지 갱신 주기 |
| over 10 years | Google이 안경을 만들어 온 기간 |

## 주요 인용

> Every day is Gemini season here at Google.
> — Sundar

> in our Gemini era, we're just as likely to ship our most intelligent model on a random Tuesday in March or a really cool breakthrough like Alpha Evolve just a week before.
> — Sundar

> Now, we are processing 480 trillion monthly tokens.
> — Sundar

> The Gemini app now has over 400 million monthly active users.
> — Sundar

> Google Search is bringing generative AI to more people than any other product in the world.
> — Sundar

> Introducing Google Beam, a new AI first video communications platform.
> — Sundar

> we think of agents as systems that combine the intelligence of advanced AI models with access to tools.
> — Sundar

> We're living through a remarkable moment in history, where AI is making possible an amazing new future.
> — Demis

> Gemini 2.5 Pro is our most intelligent model ever, and the best foundation model in the world.
> — Demis

> I'm thrilled to announce that we're releasing an updated version of 2.5 Flash.
> — Tulsi

> Today, we're making 2.5 Pro even better by introducing a new mode we're calling Deep Think.
> — Demis

> we're working hard to extend it to become what we call a world model.
> — Demis

> To transform it into a universal AI assistant. An AI that's personal, proactive, and powerful.
> — Demis

> AI mode is coming to everyone in the US starting today.
> — Sundar

> This is the future of Google Search, a search that goes beyond information to intelligence.
> — Liz

> AI mode is Search transformed with Gemini 2.5 at its core.
> — Liz

> It's like having my very own sports analyst right in Search.
> — Rajan

> I have to say I love a live demo when it works.
> — Vidhya

> We couldn't be more excited about this chapter of Google Search where you can truly ask anything.
> — Liz

> It's called Imagine 4 and it's a big leap forward.
> — Josh

> V O 3 comes with native audio generation.
> — Josh

> generative media is expanding the boundaries of creativity.
> — Jason

> We're calling it Flow, and it's launching today.
> — Josh

> It's the first Android platform built in the Gemini era
> — Sriram

> Gentle Monster and Warby Parker will be the first eyewear partners to build glasses with Android XR.
> — Sriram

> Together with an amazing group of partners, we are building something called Fire Sat.
> — Sundar

> It can detect fires as small as 270 square feet, about the size of a one-car garage.
> — Sundar
