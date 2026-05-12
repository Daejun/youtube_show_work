# The Android Show | XR Edition

## Metadata

| Field | Value |
|---|---|
| Channel | Android Developers |
| Uploaded | 2025-12-08 |
| Duration | 29m 47s |
| URL | https://www.youtube.com/watch?v=a3-OJxxW810 |
| Transcript source | manual (en) |

## Executive summary

The show positions **Android XR** as the industry's first unified platform for extended reality devices, built with Samsung and Qualcomm, and models XR as a spectrum from immersive headsets to lightweight AI Glasses. The substantive announcements split into four blocks: a *Galaxy XR feature drop* (PC Connect, Likeness, travel mode rolling out today; system-level autospatialization next year); a preview of XREAL's wired-XR Glasses *Project Aura* with optical-see-through lenses and a tethered puck launching next year; prototype AI Glasses built with **Warby Parker** and **Gentle Monster**, launching next year; and **Developer Preview 3 of the Android XR SDK** with new Jetpack libraries — *Glimmer* and *Projected* — plus Gemini Live API support for glasses.

## Topics covered

### Pre-XR context (00:00–02:40)

Recent Android updates and the universal-assistant framing that motivates Android XR.

- Sameer says the team unveiled an all-new design language, Material 3 Expressive, that launched on Pixel a few months earlier.
- Sameer says Gemini on Android added new screen share and visual guidance capabilities accessible via a long press.
- Sameer references the Nano Banana image editing model in the Gemini app.
- Sameer describes a universal assistant that *gets you, is a step ahead, and handles your busy work*, framed as a fundamental change in how people interact with technology.
- Sameer says the first place this comes together is on the new Android XR platform.

### Android XR positioning (02:41–07:00)

What Android XR is, who builds it, and the spectrum of form factors it targets.

- Android XR is the industry's first unified platform for extended reality devices.
- Android XR is built with Samsung and Qualcomm; favorite apps from Google Play are available, along with Gemini as an assistant.
- XR is described as a spectrum of devices, from headsets to glasses.
- Headsets are characterized as powerful devices for shorter, more immersive computing tasks like watching 3D movies, playing games, and getting work done.
- AI Glasses are characterized as lightweight, providing all day wear with quick access to information.
- Devices in the middle blend the two.
- The Samsung Galaxy XR headset is out now.
- AI Glasses are being built in collaboration with Samsung; the first look was earlier in the year at TED and Google I/O.
- Google is partnering with Warby Parker and Gentle Monster to design glasses that are great to wear.
- XREAL's Project Aura is a new form factor that expands the Android XR ecosystem.

### Galaxy XR feature drop (07:00–11:42)

The October Galaxy XR launch, the headset's first shipping feature drop, and a sneak peek at autospatialization.

- Galaxy XR launched in October as the first device powered by Android XR, with high-quality resolution, multimodal AI input, and optional controllers.
- The Explorer Pack at launch includes **Google AI Pro**, **YouTube Premium**, and **Google Play Pass**, plus **YouTube TV at $1 a month for three months** and **NBA League Pass** in the US, or **TVING** and **Coupang Play Sports Pass** in Korea.
- Exclusive Android XR experiences include Doug Liman's film *Asteroid* and Adobe's Project Pulsar for spatial video editing.
- Over 60 made-for-XR apps and games are on the Google Play store one month after launch, including Demeo.
- **PC Connect** pulls a window from a laptop into the headset; Katherine demos City Skylines II streamed from her PC.
- **Likeness** shows a photorealistic version of the user on Google Meet and works across video conferencing apps, not just Google Meet.
- The headset can turn regular 2D content into 3D in real time across multiple apps, and the **autospatialization** feature works with pretty much any app because it runs on the headset.
- The first update rolling out today includes **PC Connect**, **Likeness**, and **travel mode**.
- **System-level autospatialization comes next year**.

### Upcoming: Project Aura (11:42–14:42)

XREAL's *Project Aura*, an upcoming wired XR Glasses device on Android XR.

- Project Aura is a lightweight, portable, upcoming device that will bring a new wired XR Glasses experience to the Android XR family.
- The lenses are *optical-see-through* — the user sees the real world through transparent lenses while Project Aura projects virtual experiences into the field of view; users interact with hands, like an Android XR headset.
- Project Aura is powered by a **tethered puck** that holds the main compute and battery and also doubles as a trackpad.
- Aura runs apps from Google Play just like a headset.
- Aura can also be plugged into a laptop to extend its apps as a giant spatial window; Andrea demos using Lightroom this way.
- In a Lightroom demo, Andrea asks Gemini how to add a bokeh effect; Gemini instructs to use the Lens Blur panel, click Apply for AI auto-detect, and use the Blur Amount slider.
- **Project Aura launches next year**.

### AI Glasses with Warby Parker and Gentle Monster (14:42–21:52)

The two glasses tiers, remarks from eyewear partners Warby Parker and Gentle Monster, and a prototype-glasses demo.

- Google is working with Warby Parker and Gentle Monster, in collaboration with Samsung, on two tiers.
- **AI Glasses** have built-in speakers, a camera, and microphones for talking with Gemini, listening to music, making calls, and taking photos.
- **Display AI Glasses** add a small display that privately shows helpful information.
- Warby Parker frames glasses as the first thing people see and the only thing many people wear on their face, a powerful form of self-expression.
- Gentle Monster describes itself as a global eyewear brand creating fashion eyewear equipped with AI.
- In a prototype-glasses demo, Gemini identifies a bag of **Ppushu Ppushu Bulgogi Flavor** noodle snack, a popular Korean snack eaten by crushing the noodles and mixing in the seasoning packet.
- Nano Banana is used to take a group photo and add an Android bot with a full body and sunglasses.
- Gemini identifies edamame on the snack table as a high-protein option.
- **Live Translate** is demoed with Jin from Samsung speaking Korean.
- A pair of glasses was given to **GetYourGuide** for travel use cases; Rose demos the glasses on the East Village Sandwich Tour, asking Google for nearby food tours and saving spots.

### Developer updates (21:52–28:00)

Android XR SDK Developer Preview 3 changes, new Jetpack libraries for glasses, and an Uber-on-glasses demo.

- **Android XR SDK Developer Preview 3** is announced.
- New features for headsets include spatial animations with **soft head locking** and transitions, and Material 3 components like dialogs and navigation bars that automatically transform into spatial XR elements.
- New APIs let apps detect a device's field of view; developers can test fields of view in the **XR Emulator in Android Studio**.
- **Development opens today for both AI Glasses and Display AI Glasses**.
- ARCore for Jetpack XR adds **geospatial capabilities**: the **Visual Positioning Service** provides directions based on orientation, the **Geospatial API** enables content triggers and location-specific actions, and ARCore motion tracking enables responses to user movement like a head tilt.
- **Jetpack Glimmer** is a Compose UI Toolkit for AI Glasses with components like cards, lists, and stacks, designed for transparent displays.
- **Jetpack Projected Library** lets developers bring an existing Android mobile app directly to AI Glasses and manage audio configurations and the glasses camera from a core mobile app.
- The team collaborated with the **Firebase AI Logic team** to make the **Gemini Live API** work with AI Glasses.
- Amit, who leads the rider-product team at Uber, demos Uber on glasses: after booking, the rider sees **trip status and ETA in view**; at the airport, **wayfinding** provides simple contextual directions; at the pickup curb, the glasses show the **driver's license-plate number** and can help call the driver.

## People, organizations, products, places

### People

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

### Organizations

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

### Products

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

### Places

- Korea
- United States
- East Village
- New York City

## Numbers and data points

| Value | Context |
| --- | --- |
| October | Month Galaxy XR launched |
| $1 a month for three months | YouTube TV pricing in the Explorer Pack |
| over 60 | made-for-XR apps and games on Google Play one month after launch |
| Developer Preview 3 | Android XR SDK release announced today |
| 70-degree field of view | Project Aura wired XR Glasses field of view |
| next year | When system-level autospatialization arrives |
| next year | When Project Aura launches |
| next year | When AI Glasses with Warby Parker and Gentle Monster launch |

## Notable quotes

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
