# Google I/O '26 Keynote

## 개요

Google I/O '26 Keynote은 2026년 5월 19일에 진행된 약 3시간 분량의 Google 라이브 방송으로, Gemini Omni 멀티모달 모델, Gemini 3.5 Flash와 Antigravity 2.0 에이전트 개발 플랫폼, 개인 AI 에이전트 Gemini Spark, AI Search의 다음 챕터(새 검색창 · Search agents · Antigravity 기반 generative UI), 새로운 에이전트 커머스 스택(Universal Commerce Protocol · Agent Payments Protocol · Universal Cart), Neural Expressive로 재설계된 Gemini 앱, Pics · Stitch · Flow 크리에이티브 도구, 올가을 출시될 Samsung Android XR 오디오 안경(Warby Parker · Gentle Monster 디자인), 그리고 안전 · Gemini for Science · WeatherNext · Isomorphic Labs로 마무리하는 Demis Hassabis의 클로징을 다룹니다. Sundar Pichai가 진행하며 Demis Hassabis · Varun Mohan · Josh Woodward · Liz Reid · Robby Stein · Vidhya Srinivasan · Suz Chamber · Shahram Izadi · Nishtha Bhatia가 등장합니다.

## 다루는 주제

- Google은 현재 매월 3.2 quadrillion 토큰을 처리하며 작년 480 trillion · 2년 전 9.7 trillion 대비 1년 만에 약 7x 증가했습니다.
- 매월 8.5 million 이상 개발자가 Google 모델로 빌드하며, 모델 API는 분당 19 billion 토큰을 처리하고, 최근 12개월간 375개 이상 고객이 각각 1 trillion 이상의 토큰을 처리했습니다.
- 사용자 10억 이상 제품이 13개, 30억 이상 제품이 5개입니다.
- AI Overviews는 매월 2.5 billion 이상 사용자, AI Mode는 1년 만에 1 billion 사용자 돌파, Gemini 앱은 900 million MAU(전년 400M 대비 2배+)이며 일일 요청은 7배 이상 증가, Nano Banana로 50 billion 이상 이미지가 생성됐습니다.
- Maps는 10여 년 만의 최대 업데이트로 Ask Maps가 도입됐고, Ask YouTube는 대화형 검색으로 재설계되어 미국에서 올여름 광범위 출시되며, Docs Live는 음성 브레인덤프 후 Gemini가 문서를 작성하는 기능으로 Pro/Ultra 가입자 대상 올여름 출시 뒤 Gmail · Google Keep으로 확대됩니다.
- Google의 capex는 2022년 31 billion 달러에서 올해 180~190 billion 달러로 약 6배 증가합니다.
- Cloud Next에서 8세대 TPU가 발표됐으며 학습용 TPU 8t는 이전 세대 대비 거의 3배 연산을, 추론용 TPU 8i는 시연에서 약 1,500 tokens/second 속도를 보였고 두 칩 모두 와트당 성능이 2배 개선됐습니다.
- JAX · Pathways를 통해 1 million 이상 TPU를 전 세계 멀티 사이트로 확장합니다.
- Demis가 Gemini Omni를 공개 — 어떤 입력에서든 어떤 결과물을 만드는 새로운 모델로, kinetic energy · gravity 같은 직관 물리 시뮬레이션이 단계적으로 향상됐고 대화형 영상 편집을 지원합니다.
- Omni 패밀리의 첫 모델 Gemini Omni Flash가 오늘 Google 제품 전반에 제공되고 Omni Pro는 곧 공개됩니다.
- SynthID는 지금까지 100 billion 이미지 · 영상과 60,000년 분량 오디오에 워터마크했고, Content Credentials Verification이 제품 전반과 Search · Chrome으로 확장되며, OpenAI · Kakao · Eleven Labs가 NVIDIA에 이어 SynthID에 합류했습니다.
- Gemini 3.5 Flash가 오늘 출시 — 3.1 Pro 대비 거의 모든 벤치마크에서 우수하며 다른 frontier 모델 대비 4배 빠르고 Antigravity 내부에서는 12배까지 가속됩니다.
- Google 내부 일일 토큰 처리는 3월의 half a trillion에서 현재 3 trillion 이상으로 증가했습니다.
- Antigravity 2.0은 subagents · hooks · async task management를 갖춘 새 데스크톱 앱으로, 3.5 Flash와 함께 93개 subagents가 12시간 만에 운영체제를 처음부터 빌드했고 15,000회 이상 모델 요청 · 2.6 billion 토큰을 사용했으며 API 비용은 less than $1,000로 끝났습니다.
- 3.5 Flash는 비교 가능한 frontier 모델 대비 less than half 가격이고, 워크로드 80%를 3.5 Flash로 전환하면 over $1 billion/year를 절감할 수 있는 예시를 제시했습니다. Gemini 3.5 Pro는 약 1개월 후 공개됩니다.
- Gemini Spark는 Google Cloud의 dedicated VM에서 24/7 동작하는 개인 AI 에이전트로 3.5와 Antigravity Harness 위에서 돌아가고 MCP로 서드파티 도구와 연동됩니다.
- Spark는 이번 주 신뢰 테스터, 다음 주 미국 Google AI Ultra 가입자 베타로 시작되고, 새 Ultra 플랜이 $100/month로 출시되며 최상위 Ultra 플랜은 $250 → $200/month로 인하됩니다. Spark는 올여름 Chrome에 에이전트 브라우저로 들어오고, Android Halo는 폰의 에이전트 홈 베이스로 올해 후반 도착합니다.
- AI Mode는 오늘 Gemini 3.5로 업그레이드됐고, 텍스트 · 이미지 · 파일 · 영상을 받아 25년+ 만의 최대 검색창 업그레이드인 새 intelligent Search box가 도입되며, AI Overviews와 AI Mode가 하나의 seamless AI Search 경험으로 통합되어 오늘 전 세계 데스크톱 · 모바일에 적용됩니다.
- Search는 biotech 주식 · 아파트 검색 · 스니커즈 드롭 같은 작업을 24/7 수행하는 information agents를 올여름 도입하고, Antigravity와 Gemini 3.5 Flash 기반 generative UI가 모든 사용자에게 올여름 무료로 제공됩니다.
- Vidhya가 에이전트 커머스의 세 가지 building block 공개 — Universal Commerce Protocol(Amazon · Meta · Microsoft · Salesforce · Stripe가 창립 파트너에 합류한 오픈 표준), guardrail과 tamper-proof 디지털 mandate를 갖춘 Agent Payments Protocol, 그리고 머천트 · 서비스를 가로지르며 Google Wallet 기반 숨은 혜택을 찾아주는 Universal Cart.
- Shopping Graph는 over 60 billion 제품 목록을 보유하며, UCP는 호텔 · 로컬 음식 배달 등으로 확장되고 Canada · Australia · U.K.에 향후 몇 달 내 도입됩니다. Universal Cart는 올여름 미국에서 Search · Gemini 앱부터 시작되어 YouTube · Gmail로 확장됩니다.
- Gemini 앱은 230개 이상 국가 · 70개 이상 언어에 제공되며 NotebookLM은 1.5 billion 이상 notebooks · podcasts · slide decks를 생성했습니다.
- Gemini 앱이 Neural Expressive 디자인 언어로 완전 재설계됐고, Gemini Live는 즉시 인라인으로 열리며 지역 방언 지원이 곧 추가됩니다. Neural Expressive는 오늘 Android · iOS · Web 전 세계 배포됩니다.
- Gemini Omni가 오늘 유료 가입자 대상 Gemini 앱에 도착하고, 새 out-of-the-box 에이전트 Daily Brief가 받은편지함 · 캘린더 · 작업을 합쳐 아침 다이제스트를 만들어 오늘 미국 Google AI Plus · Pro · Ultra 가입자에게 제공됩니다.
- 네이티브 Gemini for Mac OS 앱은 Antigravity로 100일 이내에 100가지 이상의 기능을 출시했고, function 키 길게 누르기 음성 제어가 올여름 추가됩니다.
- Google Pics는 Google Workspace의 새 이미지 생성 · 편집 도구로 올여름 출시되고, Stitch는 지난 한 해 100 million 이상 UI 화면을 생성했으며 실시간 협업 · 코드/사이트 내보내기가 오늘 글로벌 출시됩니다.
- Google Flow에 Gemini Omni 스타일 변환, 한 장의 이미지로 16개 카메라 앵글 영상을 만드는 새 에이전트, 대규모 장면 편집, vibe-coded Flow tools, Google Flow Music이 모두 오늘 제공됩니다.
- Android XR은 Samsung과 함께 만들었고 Qualcomm Snapdragon에 최적화됐으며, 첫 Google 오디오 안경이 올가을 출시 — Gentle Monster · Warby Parker 디자인 · Samsung 하드웨어 · Google 소프트웨어가 결합되고 Android · iOS 모두에 페어링됩니다.
- 라이브 안경 데모에서 Personal Intelligence로 Maps 경로 안내, Koopa Cafe에서 DoorDash로 nitro cold brew 주문, 음소거된 텍스트 요약, 캘린더에 가족 저녁 일정 추가, Nano Banana 카툰 스타일 관객 셀카와 "Google I/O 2026" 비행선 합성을 시연합니다.
- CodeMender는 보안 취약점을 자동으로 찾아 수정하는 에이전트이고 새 CodeMender API가 일부 전문가 대상 테스트 중입니다. Gemini for Science · AlphaEarth Foundations · WeatherNext(2025년 Jamaica의 category 5 허리케인을 3일 미리 예측) · Isomorphic Labs(면역 질환 · 암에 대한 잠재적 치료제 pre-clinical 단계)가 소개됩니다.

## 인물 · 조직 · 제품

- 인물: Valkyrae, COURAGEJD, Sundar Pichai, Demis Hassabis, Varun Mohan, Josh Woodward, Liz Reid, Robby Stein, Vidhya Srinivasan, Suz Chamber, Shahram Izadi, Nishtha Bhatia, Jay Kim, Holly, Timmy.
- 조직: Google, Google DeepMind, Google Cloud, Anthropic, NVIDIA, OpenAI, Kakao, Eleven Labs, Samsung, Qualcomm, Warby Parker, Gentle Monster, Amazon, Meta, Microsoft, Salesforce, Stripe, Target, Isomorphic Labs, DoorDash, Hurricane Center.
- 제품: Gemini, Gemini 3.5 Flash, Gemini 3.5 Pro, Gemini Omni, Gemini Omni Flash, Gemini Spark, Gemini Live, Gemini for Science, Nano Banana, Veo, Genie, TPU 8t, TPU 8i, Snapdragon, Antigravity, Antigravity 2.0, Ask YouTube, Ask Maps, Docs Live, AI Overviews, AI Mode, Google Search, Universal Commerce Protocol, Agent Payments Protocol, Universal Cart, Google Pay, Google Wallet, Shopping Graph, Google AI Plus, Google AI Pro, Google AI Ultra, NotebookLM, Neural Expressive, Daily Brief, Android Halo, Android XR, Google Pics, Stitch, Google Flow, Google Flow Music, Personal Intelligence, SynthID, Content Credentials Verification, Pathways, JAX, Model Context Protocol, CodeMender, AlphaFold, AlphaGenome, AlphaEarth Foundations, WeatherNext, Infinite Scaler, WorkOnward, Circle to Search.

## 수치 및 데이터

- 3.2 quadrillion — 현재 월간 토큰 처리량.
- 480 trillion → 3.2 quadrillion — 1년간 약 7x 증가.
- 9.7 trillion — 2년 전 월간 토큰 처리량.
- over 8.5 million — 월간 Gemini API 개발자 수.
- 19 billion — API 분당 토큰 처리량.
- over 375 — 1년간 각자 1 trillion 토큰 이상 처리한 고객 수.
- 13 / 5 — 사용자 10억+ 제품 수 / 30억+ 제품 수.
- over 2.5 billion — AI Overviews 월간 사용자.
- 1 billion — AI Mode 월간 사용자.
- over 900 million — Gemini 앱 MAU.
- 50 billion — Nano Banana로 생성된 이미지 수.
- $31 billion → $180~190 billion — 2022 → 2026 capex (약 6배).
- 3x — TPU 8t 이전 세대 대비 연산 성능.
- over 1 million — JAX · Pathways로 확장 가능한 TPU 수.
- 1,500 tokens/sec — TPU 8i 시연 출력 속도.
- 2x — TPU 8t · 8i 와트당 성능 개선.
- 100 billion / 60,000 years — SynthID 워터마크 이미지·영상 / 오디오 분량.
- 4x / 12x — 3.5 Flash가 다른 frontier 대비 / Antigravity 내 속도.
- half a trillion → 3 trillion — Google 내부 일일 토큰 처리.
- 93 / 15,000 / 2.6 billion / less than $1,000 — 운영체제 빌드의 서브에이전트 수 / 모델 요청 / 토큰 / API 비용.
- less than half / over $1 billion/year — 3.5 Flash 가격 / 80% 전환 시 절감액.
- $100 / month — 새 Ultra 플랜 가격.
- $250 → $200 / month — 최상위 Ultra 가격 인하.
- over 25 years — Search box 최대 업그레이드 이래 경과 시간.
- 60 billion / 1 billion/day — Shopping Graph 제품 목록 / Google 일일 쇼핑 검색.
- 230 / over 70 — Gemini 앱 제공 국가 / 언어.
- 1.5 billion — NotebookLM 산출물 수.
- 100 million — 지난 한 해 Stitch UI 화면 수.
- over 100 features / less than 100 days — Mac 앱 출시 기능 수 / 개발 기간.
- category 5 / 3 days — WeatherNext가 미리 예측한 Jamaica 허리케인 등급 / 사전 경보 일수.
- this fall — 첫 오디오 안경 출시 시점.
- 20,000 / 163 countries — Infinite Scaler 사전 행사 참여자 / 국가 수.

## 주요 인용

- Sundar Pichai: "It's been 10 years since we pivoted the company to be AI first."
- Sundar Pichai: "that number has jumped seven times to 3.2 quadrillion tokens per month."
- Sundar Pichai: "Never imagined I would say quadrillion in an I/O keynote, but here we are."
- Sundar Pichai: "AI Overviews now has over 2.5 billion monthly users"
- Sundar Pichai: "Today, we have surpassed 900 million, more than doubling in a year."
- Sundar Pichai: "more than 50 billion images have been generated with our Nano Banana model."
- Sundar Pichai: "if you learn anything in 27 years of working on Search, it's that latency matters."
- Demis Hassabis: "AI capabilities have leaped forwards."
- Demis Hassabis: "I'm excited to announce Gemini Omni."
- Demis Hassabis: "Anything becomes a canvas for creating entirely new realities."
- Sundar Pichai: "SynthID has now watermarked 100 billion images and videos, along with 60,000 years of audio assets."
- Sundar Pichai: "today, I'm excited to introduce Gemini 3.5 Flash, our first in a series of models combining frontier intelligence with action."
- Varun Mohan: "We've moved beyond AI tools that help us write, to agents that help us act."
- Varun Mohan: "Over 12 hours, 93 subagents working in parallel made over 15,000 model requests and processed 2.6 billion tokens to take an initially empty project to the core of a functioning operating system"
- Varun Mohan: "Multiday engineering efforts are collapsing into hours, if not minutes."
- Sundar Pichai: "Introducing Gemini Spark."
- Sundar Pichai: "It runs on dedicated virtual machines on Google Cloud, and it is 24/7. And yes, you can close your laptop."
- Josh Woodward: "Spark will catch them and then run with them."
- Liz Reid: "Google Search is AI Search through and through."
- Liz Reid: "This is the biggest upgrade to our iconic Search box since its debut over 25 years ago."
- Liz Reid: "We're entering the era of Search agents."
- Robby Stein: "This is agentic coding at the scale of Search."
- Vidhya Srinivasan: "UCP does for agentic commerce what HTTP did for the web"
- Vidhya Srinivasan: "I'm excited to announce the Universal Cart, a truly intelligent shopping cart."
- Josh Woodward: "More than 900 million users are coming to the Gemini app every month"
- Josh Woodward: "Gemini Omni is coming to the Gemini app for paid subscribers today."
- Suz Chamber: "the real breakthrough isn't the technology; it's what you do with it."
- Suz Chamber: "the world used Stitch to generate over 100 million UI screens."
- Shahram Izadi: "our first audio glasses will arrive this fall."
- Shahram Izadi: "You've got the world's top eyewear designers at Gentle Monster and Warby Parker creating iconic designs."
- Demis Hassabis: "AGI is now on the horizon and it will be the most profound and impactful technology ever invented."
- Demis Hassabis: "Our mission is to reimagine the drug discovery process with the goal of one day solving all disease."
- Demis Hassabis: "we will realize that we were standing in the foothills of the singularity."
