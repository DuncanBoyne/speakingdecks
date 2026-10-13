<!-- .slide: data-background-gradient="linear-gradient(135deg, #0e0e10 0%, #161619 60%, #2a0c0c 100%)" -->
<style>
@import url('https://fonts.googleapis.com/css2?family=Host+Grotesk:wght@400;500;700&display=swap');
.reveal { font-family: 'Host Grotesk', system-ui, sans-serif; }
.reveal h1, .reveal h2, .reveal h3 { font-family: 'Host Grotesk', system-ui, sans-serif; text-transform: none; letter-spacing: -0.03em; font-weight: 600; }
.reveal .eyebrow { font-family: ui-monospace, Consolas, monospace; color: #ff3b3b; text-transform: uppercase; letter-spacing: .12em; font-size: .42em; margin-bottom: .6em; }
.reveal strong { color: #ff3b3b; }
.reveal table { font-size: .5em; }
.reveal table th { color: #ff3b3b; font-family: ui-monospace, Consolas, monospace; text-transform: uppercase; font-size: .8em; }
</style>
<div class="r-hstack" style="align-items:center; gap:30px">
<div style="flex:1; text-align:left">
<p class="eyebrow">PBIMCR x Data Decoded MCR</p>
<h1 style="font-size:2em">AI Can Build the Whole Report.<br><span style="color:#ff3b3b">Here's How.</span></h1>
<p style="font-size:0.7em">Duncan Boyne · Power BI Consultant / AI Strategist</p>
</div>
<img src="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/ai-for-power-bi-professionals/img/duncan-headshot.png" alt="Duncan Boyne" style="height:470px; margin:0; border:0; box-shadow:none; background:none">
</div>

Notes:
Almost all of tonight is a live demo. You'll see a few slides at the start, then I build, then two slides at the end.

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/shared/about-dark.jpg" data-background-size="contain" data-background-color="#161619" -->

Notes:
Quick one on who I am. Boyne Business Intelligence is my consultancy. Tugger is where I do AI strategy. NPPUG and the East of England Summit are the community side.

---

<p class="eyebrow">Tonight</p>

## Two builds, running at the same time

| Build | Input | Output |
| --- | --- | --- |
| **Power BI** | Six business systems through Tugger, into OData | A Power BI report: model, measures, pages |
| **Claude dashboard** | One screenshot of a Power BI report + a paragraph | The same report, rebuilt as a Claude dashboard |

No Desktop until the final check. <!-- .element: class="fragment" -->

Notes:
You've all seen the demos where one model makes one chart and it works first time. Real builds don't go like that. So tonight you get two real ones side by side, and the bits that go wrong stay in.

---

<p class="eyebrow">The client</p>

## Tugger & Bone Ltd, a UK pet supplies business

| System | What it holds |
| --- | --- |
| QuickBooks | 2025 accounts |
| Xero | 2026 accounts (live 01/01/2026) |
| Cin7 Omni | Stock and orders (Fareham Warehouse only) |
| Shopify | Web shop (into Xero from 15/01/2026) |
| HubSpot | CRM |
| BreatheHR | HR (@tuggerandbone.co.uk staff only) |

Every rule in that table is something the AI has to be **told**. <!-- .element: class="fragment" -->

Notes:
It's a fictional company, but the mess is real: two ledgers split at a go-live date, old test data in Cin7, non-staff records in HR. In the story, today is 30 September 2026. The first prompt checks all six connections before anything gets built.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #0e0e10 0%, #2a0c0c 100%)" -->

<p class="eyebrow">Live</p>

# Demo

Model · Design · Report <!-- .element: style="font-family:ui-monospace,Consolas,monospace; font-size:.6em; color:#ff3b3b" -->

Notes:
Switch to the demo. Two windows: Claude Code building the Power BI report from Tugger, and Claude rebuilding the screenshot as a dashboard. Come back here for the last two slides.

--

<p class="eyebrow">Fallback</p>

## Twelve things that broke, and the fifteen-second fixes

| What broke | Fix |
| --- | --- |
| `pbir new report` ignores your path | Find the .pbip, move it |
| Numeric column bound with no Sum | Wrap it in an Aggregation |
| Year filter written as `'2025'` | Make it `2025L` |
| `£` in a field name becomes `Â£` | Find and replace, or keep names ASCII |
| `pbir set` with a glob does nothing | Set each visual |
| Measure title lands on the wrong layer | Move it to `visualContainerObjects` |

Notes:
Fallback slide if the demo stalls, or to walk through after it. Second half is below.

--

<p class="eyebrow">Fallback</p>

## Twelve things that broke, continued

| What broke | Fix |
| --- | --- |
| TopN filter leaks into title share % | `CALCULATE(..., ALL(Sales))` |
| KPI visual shows the last point, not the total | Feed it YTD measures |
| Changed DAX doesn't reload | Close Desktop, reopen the PBIP |
| Fresh PBIP shows nothing | One Refresh. Never two at once |
| Save writes nothing | Refresh until it's dirty, then Save |
| `formatString` starting `"£"` won't load | Write `£#,0` |

Notes:
Every one of these is from a real Desktop-free build. None of them is hard to fix. All of them stop a demo dead if you don't know them.

---

<p class="eyebrow">The honest split</p>

## Ready today vs needs your hands

| Ready today | Needs your hands |
| --- | --- |
| Exploring the source data | The business rules: what to ignore |
| Star schema and measures | Checking the numbers are right |
| Pages, visuals, bindings, theme | Design taste |
| A dashboard from a screenshot | First refresh and credentials |
| Bulk formatting | The final check in Desktop |

Notes:
AI builds the whole report. You still own whether it's right. Everything in the right-hand column came up in the demo.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #0e0e10 0%, #161619 60%, #2a0c0c 100%)" -->

<p class="eyebrow">Thank you</p>

## Questions?

Duncan Boyne · **duncanboyne.co.uk**

Notes:
Take questions. Rob Sewell is on next or was on before: point at fabric-toolbox if anyone asks about tooling.
