# Google I/O '26 Keynote — 핵심 정리

채널: Google · 길이: 2h 57m · 업로드: 2026-05-19 · URL: https://www.youtube.com/watch?v=wYSncx9zLIU

## 한눈에

- Google의 월간 토큰 처리량이 2년 만에 9.7 trillion → 3.2 quadrillion으로 약 330배 증가했고, 이번 키노트의 모든 발표가 그 규모 위에서 동작하도록 설계됨.
- 출시 즉시: Gemini Omni Flash, Gemini 3.5 Flash, Antigravity 2.0, AI Mode/Overviews 통합, Neural Expressive UI, Gemini Omni in 앱, Daily Brief.
- 올여름: Spark Ultra 베타, Search 정보 에이전트, Antigravity generative UI, Docs Live, Ask YouTube, Universal Cart.
- 올가을 ~ 올해 후반: Android XR 첫 오디오 안경 (Warby Parker · Gentle Monster), Spark in Chrome, Android Halo.

## 1. 인프라 & 모델

- **3.2 quadrillion 토큰/월** (작년 480T, 재작년 9.7T). 7배/년 증가, "token maxing" 농담까지.
- **TPU 8 (8세대, dual-chip)**: 학습용 8t는 이전 세대 대비 3배 연산, 추론용 8i는 시연에서 1,500 tokens/sec, 둘 다 와트당 성능 2배.
- **1,000,000+ TPU 글로벌 학습 클러스터** (JAX · Pathways 기반).
- **Capex** 2022 $31B → 2026 $180–190B (약 6배).
- **Gemini Omni**: 모든 입력 → 모든 출력. kinetic energy · gravity 같은 직관 물리에서 단계적 향상. 대화형 영상 편집.
  - Omni Flash 오늘 출시 / Omni Pro 곧 출시.
- **Gemini 3.5 Flash 오늘 출시**: 3.1 Pro 대비 거의 모든 벤치마크 우위, 다른 frontier 대비 4x 속도 · 가격 절반 이하, Antigravity 안에서는 12x.
- **Gemini 3.5 Pro**: 약 한 달 후.

## 2. 에이전트 & 개발자 도구

- **Antigravity 2.0** (오늘 전 세계 출시): 스탠드얼론 데스크톱 앱, subagents · hooks · async task management, full CLI + SDK + 음성 + Android/Firebase/AI Studio 통합.
- 데모: 93개 subagents가 12시간 동안 **운영체제를 처음부터 빌드** — 15,000+ 모델 요청, 2.6 billion 토큰, less than $1,000 API 비용. 결과물로 Doom 구동.
- **Gemini Spark** (Sundar 발표 → Josh 데모): Google Cloud의 dedicated VM에서 24/7 동작하는 개인 에이전트. 3.5 + Antigravity Harness 기반. MCP로 서드파티 도구 연동.
  - 이번 주: 신뢰 테스터.
  - 다음 주: 미국 Google AI Ultra 가입자 베타.
  - 올여름: Chrome 안의 agentic browser.
  - 올해 후반: Android Halo (폰의 에이전트 홈 베이스).
- **CodeMender**: 보안 취약점 자동 탐지 · 수정 에이전트. 새 API가 전문가 대상 테스트 중.

## 3. AI Search 재정의

- **AI Mode 1B MAU 돌파**, 출시 후 매분기 쿼리 2배 이상 증가. 오늘 Gemini 3.5로 업그레이드.
- **AI Overviews 2.5B 월 사용자**.
- **새 intelligent Search box** (25년 만의 최대 업그레이드): 텍스트 · 이미지 · 파일 · 영상을 함께 받음, AI 제안 · 확장형 입력, 오늘부터 롤아웃.
- **AI Overviews + AI Mode 통합** seamless 경험으로 오늘 전 세계 데스크톱 · 모바일 적용.
- **Search 정보 에이전트** (올여름): biotech 주식 추적, 아파트 검색, 스니커즈 드롭 알림 같은 24/7 백그라운드 작업.
- **Antigravity 기반 generative UI** (올여름, 무료): 질문에 맞춰 즉석에서 인터랙티브 컴포넌트 빌드. 블랙홀 시각화 · weekend planner 데모.

## 4. Agentic Commerce

- **Universal Commerce Protocol (UCP)**: 에이전트 커머스용 오픈 표준. 창립 파트너 + Amazon · Meta · Microsoft · Salesforce · Stripe.
  - 호텔 · 로컬 음식 배달 · YouTube 확장.
  - Canada · Australia · U.K. 도입 예정.
- **Agent Payments Protocol (AP2)**: 브랜드 · 제품 · 지출 한도 같은 strict guardrails, tamper-proof 디지털 mandate. Gemini Spark부터 도입.
- **Universal Cart**: 머천트 · 서비스를 가로지르는 지능형 장바구니. 가격 추적 · 가격 이력 · 재입고 알림 · 호환성 추론, Google Wallet 기반 숨은 혜택 자동 적용.
  - 올여름 미국 Search · Gemini 앱부터, 이후 YouTube · Gmail.
- **Shopping Graph**: 600억+ 제품 목록, 하루 10억+ 쇼핑 검색.

## 5. Gemini 앱 재설계 & 크리에이티브 도구

- **900M MAU** (전년 400M 대비 2배+, 일일 요청 7x).
- **230개국 · 70+ 언어** — 세계에서 가장 널리 제공되는 AI 시스템.
- **Neural Expressive 디자인 언어**: 유려한 애니메이션 · 새 타이포그래피 · 햅틱 피드백. 오늘 Android · iOS · Web 전 세계 배포.
- **Gemini Live**: 즉시 인라인 오픈, 곧 지역 방언 지원 (Liverpool 액센트 시연).
- **Gemini Omni in 앱**: 오늘 Google AI Plus · Pro · Ultra 가입자에게 제공 (영상 스타일 · 카메라 앵글 변환).
- **Daily Brief 에이전트**: 받은편지함 · 캘린더 · 작업 → 아침 다이제스트. 오늘 미국 Plus · Pro · Ultra 가입자에게 출시.
- **Gemini for Mac**: 100일 이내 100+ 기능 출시, function 키 음성 제어 올여름.
- **Personal Intelligence**: 지난주 전 세계로 확장.
- **NotebookLM**: 1.5B+ notebooks · podcasts · slide decks 생성됨.
- **Google Pics**: Workspace의 새 이미지 생성/편집 도구. 객체 인식 · hover-to-remove · 다국어 번역. 모든 출력에 SynthID 워터마크. 올여름.
- **Stitch**: 지난해 1억+ UI 화면 생성. 실시간 협업 · 코드/사이트 내보내기 오늘 글로벌 출시.
- **Google Flow + Flow Music** (오늘): Omni 스타일 변환, 한 이미지에서 16개 카메라 앵글 영상 생성 에이전트, 대규모 장면 편집, vibe-coded Flow tools, 원곡 생성.

## 6. Android XR 오디오 안경

- **첫 오디오 안경 올가을 출시** — 인이어 음성으로 Gemini와 종일 핸즈프리 대화.
- **파트너**: Warby Parker + Gentle Monster (디자인), Samsung (하드웨어), Google (소프트웨어), Qualcomm Snapdragon. Android · iOS 모두 페어링.
- **라이브 데모** (Shahram · Nishtha): Maps 경로 안내, Personal Intelligence로 cold brew DoorDash 주문, 음소거 텍스트 요약, 캘린더에 가족 저녁 추가, Nano Banana 카툰 셀카 + "Google I/O 2026" 비행선.
- **Display glasses**는 올해 후반 Trusted Tester 확대.

## 7. 신뢰 · 안전 · 과학

- **SynthID**: 1,000억 이미지 · 영상 + 6만년 분량 오디오 워터마크. OpenAI · Kakao · Eleven Labs가 NVIDIA에 이어 합류.
- **Content Credentials Verification**: 출처(AI · 카메라 · 생성형 편집)를 제품 전반 + Search + Chrome에서 확인.
- **Gemini for Science**: 논문 추적 · 연구 목표 → 코드 · 가설 생성 Labs 프로토타입.
- **AlphaEarth Foundations**: 지구의 디지털 트윈에 가장 가까운 모델, 산림 · 식량 안보 문제 지원.
- **WeatherNext**: 2025년 Jamaica의 category 5 허리케인을 3일 미리 더 정확히 예측 → 인명 구조.
- **AlphaFold + AlphaGenome**: 전 세계 수백만 과학자의 표준 도구.
- **Isomorphic Labs**: 면역 질환 · 암 등 여러 프로젝트가 pre-clinical 단계 — "one day solving all disease" 목표.
- Demis: AGI is now on the horizon. "we will realize that we were standing in the foothills of the singularity."

## 8. 한 줄 가용성 매트릭스

| 항목 | 언제 / 어디 |
|---|---|
| Gemini Omni Flash | 오늘, Google 제품 전반 |
| Omni in Gemini 앱 | 오늘, Google AI Plus · Pro · Ultra |
| Gemini 3.5 Flash | 오늘, 전 사용자 + API |
| Antigravity 2.0 | 오늘, 전 세계 |
| Neural Expressive | 오늘, Android · iOS · Web 전 세계 |
| 새 Search box · AI Search 통합 | 오늘, 전 세계 데스크톱 · 모바일 |
| Daily Brief | 오늘, 미국 Plus · Pro · Ultra |
| Stitch 업데이트 | 오늘, 전 세계 |
| Google Flow · Flow Music 업데이트 | 오늘 |
| Spark 신뢰 테스터 | 이번 주 |
| Spark Ultra 베타 (미국) | 다음 주 |
| Gemini 3.5 Pro | 약 한 달 후 |
| 새 Ultra 플랜 $100/mo / 최상위 Ultra $250 → $200/mo | 즉시 |
| Docs Live (Pro · Ultra) | 올여름 |
| Ask YouTube (미국) | 올여름 |
| Search 정보 에이전트 | 올여름 |
| Antigravity generative UI in Search (무료) | 올여름 |
| Universal Cart (미국, Search + Gemini 앱) | 올여름 |
| Google Pics | 올여름 |
| Mac 앱 function 키 음성 제어 | 올여름 |
| Spark in Chrome | 올여름 |
| Android XR 첫 오디오 안경 | 올가을 |
| Display glasses 트러스트드 테스터 확대 | 올해 후반 |
| Android Halo | 올해 후반 |
| UCP — Canada · Australia · U.K. | 향후 몇 달 |
| AP2 (Google 제품, Spark부터) | 향후 몇 달 |
| Universal Cart on YouTube · Gmail | Universal Cart 출시 이후 |
