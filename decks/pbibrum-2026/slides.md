<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/01.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
COVER. Walk in, pause, let the room settle. "This is a talk about a decision. Not a technology. The technology is Deneb. The decision is when to stop fighting your tools and start telling them what you want."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/shared/about-dark.jpg" data-background-size="contain" data-background-color="#161619" -->

Notes:
Quick one on who I am. Boyne Business Intelligence is my consultancy. Tugger is where I work on AI strategy. NPPUG and the East of England Summit are the community side.

From the original speaker slide: SECTION TITLE · THE WALL. Don't dwell. "Every Power BI developer has a moment. Someone asks for something. The data is right. The model is clean. And the tool just... won't."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/03.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
AUDIENCE QUESTION. Pause before asking. "Quick check — hands up if you've ever spent more than 30 minutes trying to format a native visual into something it doesn't want to be." Wait. Count hands. React to the room.

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/04.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
THREE NATIVE LIMITATIONS. Reference lines: "You want a reference line that says Average: £142k. You get 'Line.' That's it." Conditional colouring: "You want bars red below target and green above. Native gives you a dropdown with three options. None of them are what you want." Small multiples: "You have one slider: rows per page. That is your creative canvas."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/05.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
THE MOMENT. "The moment that pushed me: a client needed a bullet chart. Two hours of stacked invisible bars later, I had something that looked like a bullet chart if you squinted." Set up callback: "I'm going to give you a one-line phrase to get stuck in your head. We'll get there."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/06.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
MEET DENEB. "Daniel Marsh-Patrick, Australian developer, free custom visual, AppSource. Embeds Vega and Vega-Lite from the University of Washington's Interactive Data Lab." "The Power BI team uses Vega internally for some native visuals. You're not going off-road. You're using the road they use."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/07.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
DECLARATIVE vs IMPERATIVE. Slow down. Land this. "Imperative: you're negotiating with the tool. Declarative: you're describing the outcome. The tool has no opinions about your colour choices." "First time you get frustrated with Deneb it will be because you wrote the wrong thing, not because the tool won't let you."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/08.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
PATTERN LIBRARY SECTION. "Five patterns. What it is, what native can't do, how many lines of JSON, one with the actual spec." "One of these will resonate. I don't know which one. But one of them is the chart you've been putting off."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/09.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
HERO EXAMPLE — SLOPE CHART. [Image: deneb_category_slope, page deneb_trends_lab, RetailSales.pbip] "Revenue by product category, comparing the last two years. Crossing lines show which categories gained, lost, swapped rank." "In native: separate line charts per category, manually positioned labels, invisible axes, breaks on filter change." "This is a real visual from the RetailSales report — open deneb_category_slope in the spec editor and you can read it." "Let me show you the actual spec."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/10.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
CODE REVEAL. Read the code slowly. "Two layers: line layer and point layer. That is the slope chart." "x: Year ordinal. y: Revenue quantitative. color: Category nominal. The opacity encoding responds to __selected__ — that is how cross-filtering works in Deneb." "Point layer adds the dots, same encodings." Final beat: "You wrote DAX. This is easier than DAX."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/11.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
PATTERN LIBRARY GRID. All four are real visuals in RetailSales.pbip. "Bullet chart — deneb_region_bullet on deneb_trends_lab. Three marks: background bar, actual bar, target tick. Native cannot layer them with independent sizing." "YoY variance — deneb_yoy_variance on deneb_showcase. Each bar independently red or teal based on the measure value. Native only colours a whole series." "Waffle — deneb_region_waffle on deneb_composition_lab. 10x10 grid, each cell 1% of revenue, coloured by region." "Calendar heatmap — deneb_revenue_calendar on deneb_distribution_lab. Every cell is a single day."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/12.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
AUDIENCE QUESTION 2. "Quick question. Which of those would you build this week?" [Pause — rhetorical, don't wait for answers] "And would you have tried it in Deneb, or would you have fought through native?"

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/13.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
BEFORE/AFTER BULLET CHART. [Left: native clustered bar workaround. Right: deneb_region_bullet, page deneb_trends_lab] "Left: two bars side by side or one bar with a reference line. No independent sizing. Floating text box for the target label. 90 minutes." "Right: deneb_region_bullet. Background bar, teal actual bar, red target tick. Three marks, independently sized. Everything from measures. Cross-filter works. 20 minutes first time, 5 minutes every time after."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/14.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
INTEGRATION SECTION. "The fear is that Deneb lives outside the report, ignores your model, breaks when someone clicks a slicer. That fear is reasonable. And it's wrong for Deneb."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/15.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
INTEGRATION FEATURES. "Cross-filtering: click a bar, the page filters. No configuration. Bookmarks: capture state correctly. Tooltips: report-page tooltips work — you can put other Deneb visuals on the tooltip page. Conditional formatting: reference a measure in the spec, the measure drives the visual encoding."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/16.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
WHEN IT FEELS NATIVE. Slow down. Warmer tone. "A client interacts with the report and doesn't notice the visual is different. They ask 'can we add one more category?' not 'how does this visual work?' That's the tell. The visual disappears into the report."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/17.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
TRADE-OFFS SECTION. "The honest part. There are real costs. I'm going to tell you what they are."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/18.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
TRADE-OFF TABLE. Be direct. Don't oversell mitigations. "Learning curve: real. Mobile: check your usage stats. Accessibility: if you have formal requirements, know them. Handoff: a process failure, not a Deneb failure."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/19.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
WHEN NOT TO USE DENEB. "Three cases. Standard bar that just needs a colour change: stay native. Primary mobile audience: validate first. Requirements changing every two weeks: get stable requirements first." "The goal is not to put everything in Deneb. The goal is to know which charts need it."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/20.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
DECISION FRAMEWORK. Walk left to right. "Five questions. Can native do this without a workaround? Stable chart? Desktop audience? Accessibility requirement? Someone who can maintain JSON?" "Screenshot this slide. Use it next time someone asks why you're reaching for Deneb."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/21.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
AUDIENCE QUESTION 3. Lower your voice. "What would you build if the syntax wasn't the barrier?" Pause. Long pause — 20-30 seconds. "The chart you've been putting off. Hold that thought."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/22.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
START MONDAY SECTION. "You don't need to learn Vega-Lite cold. You need one working example and the ability to modify it."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/23.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
THE SKILL. Conversational. Not a sales pitch. "I built this because I kept writing the same specs over and over. You describe the visual in plain English. Claude writes the spec. You modify it from there. You learn by reading specs that work, not by typing from scratch." QR code and URL are on the slide.

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/24.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
MONDAY PLAN. Practical. Almost a checklist. "Install Deneb. Pick one chart. Use a template or the skill. Connect to your real model. Show someone." "The learning curve compresses dramatically the moment real data appears in something you built."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/25.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
CLOSING. Pause before the final slide. Let the transition breathe. "Stop fighting the visual. Start declaring what you want." That's literally what Deneb does — you declare, the renderer draws. But it's also the larger instruction." "Go build it." [Hold the beat. Don't add anything after this. Let the applause start.]

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbibrum-2026/slides/26.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
-
