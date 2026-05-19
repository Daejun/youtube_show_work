# Google I/O '25 Keynote

## Metadata

| Field | Value |
|---|---|
| Channel | Google |
| Uploaded | 2025-05-20 |
| Duration | 1h 55m 16s |
| URL | https://www.youtube.com/watch?v=o8NiE3XMPrM |
| Transcript source | auto (en) |

## Executive summary

Google I/O '25 Keynote is a 1-hour 55-minute Google livestream from May 20, 2025 covering more than a dozen Gemini model and research updates, the introduction of Google Beam, the expansion of agentic capabilities through Project Mariner and Agent Mode, the rollout of AI Mode in Google Search, new Gemini app features and subscription plans (Google AI Pro and Ultra), generative-media releases (Imagen 4, Veo 3, Lyria 2, the Flow filmmaking tool), and Android XR including Samsung's Project Muhaan headset and prototype glasses with Gentle Monster and Warby Parker.

The throughline is that research has moved into production at scale. Sundar Pichai opens with 50x year-over-year growth in monthly token processing (9.7T to 480T) and a 400 million-MAU Gemini app. Demis Hassabis and Tulsi present Gemini 2.5 Pro topping every LM Arena leaderboard plus the new Deep Think mode and Gemini Diffusion. Liz Reid debuts AI Mode in Search with personal context, deep search, agentic checkout, virtual try-on, and Search Live. Josh Woodward ships Veo 3 with native audio, Imagen 4, and Gemini in Chrome the same day. Jason and Josh introduce the Flow filmmaking tool. Sriram and Nishtha close with Android XR running on Samsung's Project Muhaan headset and prototype glasses partnered with Gentle Monster and Warby Parker.

## Topics covered

### Opening (00:00–02:17)

A sizzle video and Sundar Pichai's welcome at Shoreline.

- Sundar greets the audience at Shoreline and viewers around the world.

### Introduction (02:17–19:29)

Sundar's macro update on Gemini momentum, infrastructure, and the first set of product news.

#### Momentum

- Google has announced over a dozen models and research breakthroughs and released over 20 major AI products and features since the last I/O.
- Elo scores are up more than 300 points since the first generation of Gemini Pro, and Gemini 2.5 Pro sweeps the Elo Arena leaderboard in all categories.
- The updated 2.5 Pro reached number one on Web Dev Arena and surpasses the previous version by 142 Elo points.
- On Cursor, Gemini is the fastest growing model of the year, producing hundreds of thousands of lines of accepted code every single minute.
- Gemini completed Pokémon Blue, earning all eight badges, traveling Victory Road, and defeating the Elite Four and the Champion.

#### Infrastructure

- The 7th generation TPU Ironwood is the first designed to power thinking and inference at scale, delivering 10x performance over the previous generation and 42.5 exaflops of compute per pod.
- Ironwood is coming to Google Cloud customers later this year.
- Google now processes 480 trillion monthly tokens across products and APIs, up from 9.7 trillion a month a year ago — about a 50x increase in a year.

#### Adoption

- Over 7 million developers have built with the Gemini API across Google AI Studio and Vertex AI, over 5x growth since last I/O.
- Gemini usage on Vertex AI is up more than 40 times since last year.
- The Gemini app has over 400 million monthly active users, with 2.5 Pro usage in the app up 45%.
- AI overviews have more than 1.5 billion users every month.

#### Google Beam

- Google Beam is a new AI-first video communications platform that turns 2D video streams into a realistic 3D experience.
- Six cameras capture the user from different angles and AI renders them on a 3D light field display.
- Near-perfect head tracking runs down to the millimeter at 60 frames per second.
- In collaboration with HP, the first Google Beam devices will be available for early customers later this year.

#### Speech translation and Project Astra

- Real-time speech translation is launching in Google Meet — English and Spanish for subscribers now, more languages in the next few weeks, and enterprises later this year.
- Gemini Live's Project Astra camera and screen-sharing capabilities roll out to everyone on Android and iOS starting today.

#### Project Mariner and the agent ecosystem

- Project Mariner now does multi-tasking and can oversee up to 10 simultaneous tasks.
- A new teach-and-repeat feature lets Mariner learn a plan from one demonstration.
- Mariner's computer-use capabilities are coming to developers via the Gemini API, with Automation Anywhere and UiPath testing, and broader availability this summer.
- Google's open agent-to-agent protocol launched at Cloud Next with the support of over 60 technology partners.
- The Gemini SDK is now compatible with Anthropic's Model Context Protocol (MCP) tools.

#### Agent Mode and personal context

- Agent Mode in the Gemini app uses Project Mariner to do apartment hunting on sites like Zillow.
- An experimental version of Agent Mode is coming soon to subscribers.
- Personalized smart replies in Gmail use Gemini personal context, drawing from Drive notes, past emails, and Docs, and arrives this summer for subscribers.

### Google DeepMind and Gemini for Developers (19:29–46:04)

Demis Hassabis and Tulsi cover Gemini 2.5 capabilities, developer features, deep research, and DeepMind science.

#### Gemini 2.5

- Gemini 2.5 Pro tops the popular coding leaderboard Web Dev Arena, incorporates Learn LM for learning, and is number one across all the leaderboards on LM Arena.
- The updated 2.5 Flash is better across reasoning, code, and long context and is second only to 2.5 Pro on the LM Arena leaderboard.
- 2.5 Flash will be generally available in early June and 2.5 Pro will follow soon after.

#### Developer features

- Text-to-speech previews offer multi-speaker support for two voices built on native audio output, working in over 24 languages.
- The Live API will get a 2.5 Flash preview of native audio dialogue later today, able to distinguish speaker from background voices.
- Gemini 2.5 is Google's most secure model yet with strengthened protections against indirect prompt injections.
- Both 2.5 Pro and Flash include thought summaries via the Gemini API and Vertex AI.
- Updated 2.5 Flash uses 22% fewer tokens for the same performance.
- Thinking budgets are coming to 2.5 Pro alongside its generally available model in the coming weeks.
- A 2.5 Pro demo built a 3D version of an American Museum of Natural History interactive in Google AI Studio after thinking for 37 seconds.

#### Jules and Gemini Diffusion

- Jules, an asynchronous coding agent that integrates with GitHub, is now in public beta at jules.google.
- Gemini Diffusion is an experimental text diffusion model that generates five times faster than 2.0 Flashlight while matching its coding performance.

#### Deep Think and the road to a world model

- Deep Think is a new mode in 2.5 Pro that uses parallel thinking techniques.
- Deep Think posts strong results on USAMO 2025, Live Code Bench, and MMMU.
- Deep Think is going to trusted testers via the Gemini API before broader availability.
- Gemini is being extended into a world model that can plan and imagine experiences, building on prior work like Genie 2.
- Gemini Robotics is a specialized fine-tune teaching robots to grasp, follow instructions, and adjust to novel tasks.

#### Project Astra and DeepMind science

- A Project Astra demo shows the universal AI assistant fixing a bike using voice, web search, video, email, and phone calls.
- DeepMind science breakthroughs include AlphaProof (math olympiad silver level), Co-scientist, AlphaEvolve, AMY, AlphaFold 3, and Isomorphic Labs.
- AlphaFold has over 2.5 million researchers worldwide using it in their critical work.
- Google partnered with Aira to use Astra technology to help the blind and low-vision community navigate the world.

### Search (46:04–01:11:06)

Liz Reid debuts AI Mode in Search, with deep search, agentic actions, multimodal Search Live, shopping, and a custom Gemini 2.5.

#### AI Overviews and Lens

- AI overviews have scaled to over 1.5 billion users every month in more than 200 countries and territories.
- In the US and India, AI overviews are driving over 10% growth in the types of queries that show them.
- Google Lens grew 65% year over year with more than 100 million visual searches already this year, and surpasses 1.5 billion monthly users overall.

#### AI Mode

- AI Mode is a reimagined search experience using Gemini 2.5 and rolls out as a new tab to everyone in the US starting today.
- AI Mode uses a query fan-out technique that breaks a question into subtopics and issues many simultaneous queries across the knowledge graph, shopping graph, and Maps community of over 500 million contributors.
- Personal context in AI Mode draws from past searches and connected Google apps starting with Gmail, with controls to connect or disconnect at any time, and arrives this summer.
- Deep Search issues dozens or hundreds of searches and produces an expert-level fully cited report in minutes.
- Project Mariner's agentic capabilities are coming to AI Mode for event tickets, restaurant reservations, and appointments for local services.
- Search Live brings Project Astra's live camera capabilities into AI Mode, used in a kid-friendly elephant-toothpaste demo.

#### Shopping

- Search shopping uses Google's shopping graph of over 50 billion product listings.
- A new virtual try-on feature uses a custom image generation model trained for fashion with advanced 3D shape understanding.
- A new agentic checkout tracks price, adds items to cart at the target price, and buys with Google Pay under the user's guidance.
- Virtual try-on starts in Labs today; visual shopping and agentic checkout roll out in the coming months.

#### Custom Gemini 2.5

- A custom version of Gemini 2.5 is coming to both AI Overviews and AI Mode later this week.

### Gemini app (01:11:06–01:24:02)

Josh Woodward demonstrates personal context, Gemini Live, Deep Research, Canvas, Gemini in Chrome, Imagen 4, and Veo 3.

#### Gemini Live

- Gemini Live works in over 45 languages and more than 150 countries, with conversations five times longer than text conversations in the app.
- Gemini Live with camera and screen sharing is rolling out free of charge in the Gemini app on Android and iOS today.
- In the coming weeks, Gemini Live will connect to favorite apps like Calendar, Maps, Keep, and Tasks.

#### Deep Research and Canvas

- Deep Research now lets users upload their own files and will soon research across Google Drive and Gmail.
- Canvas transforms a report with one tap into a dynamic webpage, an infographic, a quiz, or a custom podcast in 45 languages.

#### Gemini in Chrome

- Gemini in Chrome is starting to roll out this week to Gemini subscribers in the US, understanding the context of the page automatically.

#### Imagen 4 and Veo 3

- Imagen 4 is Google's new image-generation model with richer detail, better text and typography, and comes to the Gemini app today.
- A fast variant of Imagen 4 is 10 times faster than the previous model.
- Veo 3 is Google's new state-of-the-art video model that ships with native audio generation — sound effects, background sounds, and dialogue — and is available today.

### Generative Media (01:24:02–01:37:37)

Lyria 2 music, SynthID, the Aronofsky filmmaking partnership, the Flow tool, and new AI subscription plans.

- Lyria 2 generates high-fidelity music with vocals, solos, and choirs and is available today for enterprises, YouTube creators, and musicians.
- Over 10 billion pieces of content have been watermarked with SynthID to date.
- A new SynthID Detector identifies whether an image, audio track, text, or video has SynthID embedded, and rolls out to early testers today.
- Google partnered with director Darren Aronofsky's Primordial Soup to shape Veo as a filmmaking tool, with three short films planned.
- Director Eliza McNitt's short film Ancestor combines live-action performance with Veo-generated video.
- Flow is a new AI filmmaking tool that combines Veo, Imagen, and Gemini, includes character and scene consistency and precise camera controls, and launches today.
- Google is upgrading subscriptions to Google AI Pro (available globally) and Google AI Ultra (in the US today, rolling out globally soon).
- Ultra includes Deep Think access, Flow with Veo 3, YouTube Premium, and a massive amount of storage.

### Android XR (01:37:37–01:51:09)

Sriram presents Android XR, Samsung's Project Muhaan headset, and prototype glasses.

#### Android XR platform

- Android XR is the first Android platform built in the Gemini era, supporting a spectrum of devices from headsets to glasses.
- Android XR was built with Samsung as one team and optimized for Snapdragon with Qualcomm.

#### Project Muhaan headset

- Samsung's Project Muhaan is the first Android XR device and will be available for purchase later this year.

#### Android XR glasses

- Android XR glasses are designed for all-day wear with a camera, microphones, speakers, and an optional in-lens display, and they work with the user's phone.
- The glasses demo shows Gemini handling messaging, searching for a coffee shop seen earlier, navigation, photo capture, and calendar events.
- Live chat translation on Android XR glasses is demoed between Hindi (Nishtha) and Farsi (Sriram) with English captions.
- Glasses prototypes are already in trusted-tester hands, and developers will be able to start building for glasses later this year.
- Gentle Monster and Warby Parker will be the first eyewear partners to build glasses with Android XR.

### Closing (01:51:09–01:55:16)

Sundar closes with Fire Sat, Wing for disaster relief, and a Waymo ride with his parents.

- Fire Sat is a constellation of satellites using multi-spectral satellite imagery and AI to detect fires as small as 270 square feet.
- Fire Sat's first satellite is in orbit now, and when fully operational, imagery will be updated every 20 minutes instead of every 12 hours.
- During Hurricane Helene, Google's Wing in partnership with Walmart and the Red Cross provided drone deliveries of food and medicine to a YMCA shelter in North Carolina.

## People, organizations, products, places

### People

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

### Organizations

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

### Products

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

### Places

- Shoreline
- Austin
- Utah
- Zion National Park
- Nashville
- North Carolina
- California
- San Francisco

## Numbers and data points

| Value | Context |
|---|---|
| over a dozen | models and research breakthroughs since last I/O |
| over 20 | major AI products and features since last I/O |
| more than 300 | Elo score improvement since first Gemini Pro |
| 142 | Elo points by which updated 2.5 Pro surpasses previous on Web Dev Arena |
| 10x | TPU Ironwood performance over previous generation |
| 42.5 exaflops | compute per TPU Ironwood pod |
| 9.7 trillion | monthly tokens processed a year ago across products and APIs |
| 480 trillion | current monthly tokens across products and APIs |
| 50x | increase in monthly tokens in a year |
| over 7 million | developers built with the Gemini API across AI Studio and Vertex AI |
| over 5x | developer growth on Gemini API since last I/O |
| more than 40 times | Gemini usage growth on Vertex AI since last year |
| over 400 million | monthly active users of the Gemini app |
| 45% | usage increase for 2.5 Pro users in the Gemini app |
| 1.5 billion | monthly users of AI overviews |
| 200 | countries and territories where AI overviews are available |
| over 10% | growth in queries that show AI overviews in markets like US and India |
| 65% | year-over-year growth in Google Lens |
| more than 100 million | visual searches on Lens this year |
| six | cameras that capture you for Google Beam |
| 60 frames per second | Beam head tracking refresh rate |
| up to 10 | simultaneous tasks Project Mariner can oversee |
| $1,200 a month | Agent Mode apartment demo budget per roommate in Austin |
| over 60 | technology partners supporting the agent-to-agent protocol at launch |
| 24 languages | Gemini text-to-speech multi-speaker language support |
| 22% | efficiency gains in updated 2.5 Flash |
| 37 seconds | time 2.5 Pro thought to update 3D code from a sketch |
| five times faster | Gemini Diffusion vs 2.0 Flashlight |
| 2.5 million | researchers worldwide using AlphaFold |
| over 1.5 billion | monthly users of Google Lens |
| 500 million | Maps community contributors |
| over 50 billion | product listings in Google's shopping graph |
| 45 languages | languages Gemini Live works in |
| more than 150 countries | countries where Gemini Live is available |
| five times longer | Gemini Live voice conversations vs text in the app |
| 10 times faster | fast variant of Imagen 4 vs previous model |
| 10 billion | pieces of content watermarked with SynthID |
| 270 square feet | smallest fire size Fire Sat can detect |
| 20 minutes | Fire Sat refresh frequency when fully operational |
| 12 hours | current satellite imagery refresh interval |
| over 10 years | how long Google has been building glasses |

## Notable quotes

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
