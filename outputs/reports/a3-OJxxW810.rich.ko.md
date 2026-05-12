# The Android Show | XR Edition

## 메타데이터

| 항목 | 값 |
|---|---|
| 채널 | Android Developers |
| 업로드 | 2025-12-08 |
| 길이 | 29분 47초 |
| URL | https://www.youtube.com/watch?v=a3-OJxxW810 |
| 자막 소스 | manual (en) |

## 핵심 요약

이 쇼는 **Android XR**을 확장 현실 기기를 위한 업계 최초의 통합 플랫폼으로 자리매김시키며, Samsung 및 Qualcomm과 함께 만들었고, XR을 몰입형 헤드셋부터 가벼운 AI Glasses까지의 스펙트럼으로 모델링한다. 실질적인 발표는 네 갈래로 나뉜다: *Galaxy XR 기능 업데이트*(PC Connect, Likeness, travel mode가 오늘 배포되며 시스템 수준 autospatialization은 내년 도입); optical-see-through 렌즈와 tethered puck을 갖춘 XREAL의 wired XR Glasses *Project Aura* 미리보기, 내년 출시; **Warby Parker**와 **Gentle Monster**와 함께 만든 프로토타입 AI Glasses, 내년 출시; 그리고 새 Jetpack 라이브러리 *Glimmer*·*Projected*와 AI Glasses용 Gemini Live API 지원을 포함하는 **Android XR SDK Developer Preview 3**.

## 다루는 주제

### XR 이전 맥락 (00:00–02:40)

최근 Android 업데이트와 Android XR로 이어지는 "유니버설 어시스턴트" 프레이밍.

- Sameer는 팀이 Pixel에 몇 달 전 출시한 새 디자인 언어 Material 3 Expressive를 공개했다고 말한다.
- Sameer는 Gemini on Android가 long press로 접근 가능한 screen share와 visual guidance 기능을 추가했다고 말한다.
- Sameer는 Gemini 앱의 Nano Banana 이미지 편집 모델을 언급한다.
- Sameer는 유니버설 어시스턴트를 *사용자를 이해하고, 한 발 앞서며, 잡일을 처리해주는* 존재로 설명하며, 기술과 상호작용하는 방식의 근본적 변화로 묘사한다.
- Sameer는 이 모든 것이 처음 모이는 곳이 새 Android XR 플랫폼이라고 말한다.

### Android XR 포지셔닝 (02:41–07:00)

Android XR이 무엇인지, 누가 만드는지, 어떤 폼팩터 스펙트럼을 겨냥하는지.

- Android XR은 확장 현실 기기를 위한 업계 최초의 통합 플랫폼이다.
- Android XR은 Samsung·Qualcomm과 함께 만들어졌으며, Google Play의 익숙한 앱들과 어시스턴트 역할의 Gemini를 사용할 수 있다.
- XR은 헤드셋부터 안경까지의 기기 스펙트럼으로 정의된다.
- 헤드셋은 3D 영화 시청, 게임 플레이, 작업 등 짧고 더 몰입적인 컴퓨팅 작업을 위한 강력한 기기로 특징지어진다.
- AI Glasses는 가볍고, 종일 착용 가능하며, 정보에 빠르게 접근할 수 있는 기기로 특징지어진다.
- 중간 영역의 기기는 두 가지를 혼합한다.
- Samsung Galaxy XR 헤드셋은 현재 출시되어 있다.
- AI Glasses는 Samsung과 협력해 만들고 있으며, 첫 공개는 같은 해 TED와 Google I/O였다.
- Google은 착용감이 좋은 안경을 디자인하기 위해 Warby Parker · Gentle Monster와 파트너십을 맺고 있다.
- XREAL의 Project Aura는 Android XR 생태계를 확장하는 새 폼팩터다.

### Galaxy XR 기능 업데이트 (07:00–11:42)

10월의 Galaxy XR 출시, 헤드셋의 첫 출시 기능 업데이트, 그리고 autospatialization 예고.

- Galaxy XR은 10월에 Android XR로 구동되는 첫 기기로 출시되었고, 고해상도와 멀티모달 AI 입력, 선택형 컨트롤러를 갖추고 있다.
- 출시 시 Explorer Pack은 **Google AI Pro**, **YouTube Premium**, **Google Play Pass**, 그리고 미국 기준 **3개월간 월 $1의 YouTube TV**와 **NBA League Pass**, 한국 기준 **TVING**과 **Coupang Play Sports Pass**를 포함한다.
- 독점 Android XR 콘텐츠로 Doug Liman 감독의 영화 *Asteroid*와 공간 비디오 편집용 Adobe의 Project Pulsar가 포함된다.
- 출시 한 달 만에 Google Play 스토어에 Demeo를 포함한 60개 이상의 made-for-XR 앱·게임이 등록되었다.
- **PC Connect**는 노트북의 창을 헤드셋으로 끌어오며, Katherine이 자신의 PC에서 스트리밍되는 City Skylines II를 시연한다.
- **Likeness**는 Google Meet에서 사용자의 포토리얼리스틱 버전을 보여주고, Google Meet뿐 아니라 영상 회의 앱 전반에서 동작한다.
- 헤드셋은 일반 2D 콘텐츠를 여러 앱에서 실시간으로 3D로 변환할 수 있으며, **autospatialization**은 헤드셋에서 실행되기 때문에 사실상 거의 모든 앱에서 동작한다.
- 오늘 배포되는 첫 업데이트에는 **PC Connect**, **Likeness**, **travel mode**가 포함된다.
- **시스템 수준 autospatialization은 내년에 도입된다**.

### 출시 예정: Project Aura (11:42–14:42)

Android XR 위에서 동작하는 XREAL의 *Project Aura*, 곧 출시될 wired XR Glasses 기기.

- Project Aura는 가볍고 휴대 가능한, 곧 출시될 기기로 새로운 wired XR Glasses 경험을 Android XR 가족에 더한다.
- 렌즈는 *optical-see-through* — 사용자는 투명 렌즈로 실제 세계를 보며, Project Aura가 가상 경험을 시야로 투사한다. 상호작용은 Android XR 헤드셋처럼 손으로 한다.
- Project Aura는 메인 컴퓨팅과 배터리를 담고 동시에 트랙패드 역할을 하는 **tethered puck**으로 구동된다.
- Aura는 헤드셋처럼 Google Play 앱을 실행한다.
- Aura는 노트북에 연결해 노트북 앱을 거대한 공간 윈도우로 확장할 수도 있다. Andrea가 이 방식으로 Lightroom을 사용한다.
- Lightroom 데모에서 Andrea가 Gemini에게 bokeh 효과를 추가하는 법을 묻자, Gemini는 Lens Blur 패널로 가서 Apply를 눌러 AI가 피사체를 자동 감지하게 한 뒤 Blur Amount 슬라이더로 강도를 조절하라고 안내한다.
- **Project Aura는 내년 출시된다**.

### Warby Parker · Gentle Monster와 함께하는 AI Glasses (14:42–21:52)

두 가지 안경 등급, 안경 파트너 Warby Parker · Gentle Monster의 발언, 그리고 프로토타입 안경 데모.

- Google은 Samsung과 함께 Warby Parker · Gentle Monster와 협력해 두 가지 등급을 만든다.
- **AI Glasses**는 내장 스피커, 카메라, 마이크를 갖춰 Gemini와 대화하고, 음악을 듣고, 전화를 걸고, 사진을 찍을 수 있다.
- **Display AI Glasses**는 도움이 되는 정보를 개인적으로 표시해주는 소형 디스플레이를 추가한다.
- Warby Parker는 안경을 사람들이 가장 먼저 보는 것이자, 많은 이들이 얼굴에 유일하게 착용하는 강력한 자기표현 수단으로 묘사한다.
- Gentle Monster는 자사를 AI가 결합된 패션 안경을 만드는 글로벌 아이웨어 브랜드로 소개한다.
- 프로토타입 안경 데모에서 Gemini가 한 봉지의 **Ppushu Ppushu Bulgogi Flavor** 라면 과자를 식별하며, 면을 부수고 시즈닝 패킷을 섞어 먹는 인기 있는 한국 과자라고 설명한다.
- Nano Banana를 사용해 단체 사진을 찍고 전신과 선글라스를 갖춘 Android bot을 추가한다.
- Gemini는 간식 테이블에서 단백질이 높은 옵션으로 edamame를 지목한다.
- Samsung의 Jin과 함께 한국어로 **Live Translate**가 시연된다.
- **GetYourGuide**에 안경 한 쌍이 제공되어 여행 활용을 시험하며, Rose는 East Village Sandwich Tour에서 안경으로 Google에 근처 푸드 투어를 묻고 장소를 저장한다.

### 개발자 업데이트 (21:52–28:00)

Android XR SDK Developer Preview 3 변경 사항, 안경용 새 Jetpack 라이브러리, 그리고 Uber-on-glasses 데모.

- **Android XR SDK Developer Preview 3**이 발표된다.
- 헤드셋용 새 기능에는 **soft head locking**과 전환이 포함된 공간 애니메이션, 그리고 dialogs와 navigation bars 같이 자동으로 공간 XR 요소로 변환되는 Material 3 컴포넌트가 포함된다.
- 새로운 API로 앱이 기기의 시야각을 감지할 수 있으며, 개발자는 **Android Studio의 XR Emulator**에서 다양한 시야각을 테스트할 수 있다.
- **오늘부터 AI Glasses와 Display AI Glasses 모두 개발이 열린다**.
- ARCore for Jetpack XR이 **지오스페이셜 기능**을 추가한다: **Visual Positioning Service**는 방향 기반 길안내를 제공하고, **Geospatial API**는 콘텐츠 트리거와 위치별 액션을 가능케 하며, ARCore 모션 트래킹은 head tilt 같은 사용자 움직임에 반응하는 동작을 가능케 한다.
- **Jetpack Glimmer**는 AI Glasses용 Compose UI 툴킷으로, 투명 디스플레이용으로 설계된 cards, lists, stacks 같은 컴포넌트를 포함한다.
- **Jetpack Projected Library**는 기존 Android 모바일 앱을 AI Glasses로 바로 가져오게 해주며, 코어 모바일 앱에서 오디오 구성과 안경 카메라 접근을 관리할 수 있게 한다.
- 팀은 **Firebase AI Logic 팀**과 협력해 **Gemini Live API**가 AI Glasses에서 동작하도록 만들었다.
- Uber의 라이더 제품 팀을 이끄는 Amit이 안경 위 Uber를 시연한다: 예약 후 라이더의 **시야에 trip status와 ETA**가 표시되며, 공항에서는 **wayfinding**이 간단한 컨텍스추얼 길안내를 제공하고, 픽업 커브에서는 안경이 **운전자의 license-plate 번호**를 보여주고 필요하면 운전자에게 전화하는 것도 돕는다.

## 인물 · 조직 · 제품 · 장소

### 인물

- Sameer
- Shahram
- Kihwan
- Austin
- Katherine
- Juston
- Andrea Colaco
- Neil
- Dave
- Isaac
- Jin
- Rose
- Matthew
- Amit
- Doug Liman

### 조직

- Google
- Samsung
- Qualcomm
- Warby Parker
- Gentle Monster
- XREAL
- Adobe
- GetYourGuide
- Uber
- Firebase AI Logic team

### 제품

- Android XR
- Samsung Galaxy XR
- Project Aura
- Explorer Pack
- Google AI Pro
- YouTube Premium
- Google Play Pass
- YouTube TV
- NBA League Pass
- TVING
- Coupang Play Sports Pass
- Asteroid
- Project Pulsar
- Demeo
- PC Connect
- Likeness
- Lightroom
- Live Translate
- Android XR SDK
- ARCore for Jetpack XR
- Visual Positioning Service
- Geospatial API
- Jetpack Glimmer
- Jetpack Projected Library
- Gemini Live API
- Android Studio
- Material 3 Expressive
- Gemini
- Nano Banana
- Ppushu Ppushu Bulgogi Flavor

### 장소

- Korea
- United States
- East Village
- New York City

## 수치 및 데이터

| 값 | 맥락 |
|---|---|
| October | Galaxy XR 출시 월 |
| $1 a month for three months | Explorer Pack의 YouTube TV 가격 |
| over 60 | 출시 1개월 만에 Google Play의 made-for-XR 앱·게임 수 |
| Developer Preview 3 | 오늘 발표된 Android XR SDK 릴리스 |
| 70-degree field of view | Project Aura wired XR Glasses의 시야각 |
| next year | 시스템 수준 autospatialization 도입 시점 |
| next year | Project Aura 출시 시점 |
| next year | Warby Parker · Gentle Monster의 AI Glasses 출시 시점 |

## 주요 인용

> Android XR is the industry's
> first unified platform for extended reality devices.
> — Shahram

> We see XR as a spectrum of devices,
> from headsets to glasses.
> — Kihwan

> Yes, our AI Glasses are eyewear first.
> — Kihwan

> In October, we launched Galaxy XR, the first device
> to be powered by Android XR, giving you access to Gemini.
> — Austin

> Just one month after launch, there are now over 60
> made for XR apps and games on the Google Play store,
> — Katherine

> System-level autospatialization comes next year.
> — Katherine

> It's powered by a tethered puck, which holds
> the main compute and battery.
> — Juston

> Aura runs apps from Google Play just like a headset.
> — Andrea Colaco

> There's AI Glasses that have built-in speakers, a camera,
> — Juston

> Glasses are the first thing that somebody sees.
> — Neil

> Gentle Monster is a global eyewear brand
> — Isaac

> That's a bag of Ppushu Ppushu Bulgogi Flavor
> — Gemini

> If you're developing for Android,
> you're already developing for XR.
> — Matthew

> Today, we're announcing Developer Preview 3
> of the Android XR SDK.
> — Matthew

> We're bringing the Uber experience
> to glasses with Android XR,
> — Amit
