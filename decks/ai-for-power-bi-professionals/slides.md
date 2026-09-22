<!-- .slide: data-background-gradient="linear-gradient(135deg, #0b0b0d 0%, #2a0a0a 55%, #0b0b0d 100%)" -->
# AI for Power BI Professionals

### The prompt pack that actually makes *you* better at your job

Duncan Boyne — Power BI consultant & trainer

Notes:
Hold this slide while people arrive — in presenter mode it shows the join QR code, so point at it and tell the room to scan if they want the slides on their own phone. Set expectations early: 30 minutes, live demo inside, and they leave with prompts they can paste on Monday.

---

## What this is

This is **not** "AI will change everything."

It's the actual prompt pack I rely on. <!-- .element: class="fragment" -->

The prompts that save hours, improve quality, and make you feel like you have a junior dev, a documentation assistant and a design coach sitting next to you. <!-- .element: class="fragment" -->

Notes:
Name the thing they are afraid of and put it down. No hype, no "10x your output", no pitch that AI replaces developers. It doesn't — it makes good ones faster.

--

### What you'll leave with, and what you won't

| You'll leave with | You won't get |
| --- | --- |
| Prompts you can steal and use on Monday | Hype or "10x your output" |
| Modelling, DAX, docs, design, stakeholder comms | A pitch that AI replaces developers |

Notes:
This is the contract for the session. If anyone is here for a Copilot licensing conversation, this is the moment they know it isn't that talk.

---

## The reframe

AI isn't here to replace Power BI developers.

### It's here to make us dangerously efficient.

Everyone's talking about **Copilot**. Fine. But the tools doing the heavy lifting in my day are **ChatGPT, Claude, Grok and Gemini** — used well, with the right prompts.

The job isn't going away. **The slow parts of it are.** <!-- .element: class="fragment highlight-red" -->

Notes:
This is the spine of the whole talk. Land "the job isn't going away, the slow parts of it are" and pause. Everything after this is evidence for that sentence.

---

## Four general AI tools. Not just Copilot.

- **ChatGPT** — the fast default. Drafting and rewriting at speed.
- **Claude** — my pick for DAX, long context and careful reasoning over a model.
- **Grok** — quick, current, conversational. A fast second opinion.
- **Gemini** — strong on images and design tasks. Useful for wireframes.

You don't need all four. You need **one you trust** and a habit of reaching for it. <!-- .element: class="fragment" -->

Notes:
Do not let this become a tool-comparison talk. Thirty seconds, then move. The point is the habit, not the brand.

---

## Where AI actually earns its place

- **Modelling** — star-schema sanity checks, naming, relationship logic
- **DAX** — variations, validation, rewriting gnarly measures
- **Documentation** — data dictionaries and measure explanations on demand
- **Design** — report layouts and SVG wireframes before you build
- **Debugging** — explaining errors, finding the broken filter context
- **Stakeholders** — rambling turned into structured acceptance criteria

We'll take the five I lean on hardest, with the exact prompts. Then go live.

Notes:
Signpost clearly: six areas on the board, five prompts coming, then a demo. People relax when they know the shape.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #1a0505 0%, #0b0b0d 100%)" -->
## Prompt 01 — DAX
### Generate three variations, then pick

```text
Here's my measure and model context.
Give me 3 ways to write [Sales YoY %]
- one readable, one fastest, one most
defensive against blanks.
Explain the trade-off in one line each.
```

Notes:
Read the prompt out loud. The magic words are "three ways" and "explain the trade-off" — that is what turns a code generator into a teaching tool.

--

### Why it works

- **You stay in control** — AI proposes, you choose the one that fits your model
- **You learn the patterns** — reading three versions teaches more than writing one
- **Edge cases surface early** — the "defensive" version flags blanks you'd have shipped

Notes:
The third bullet is the one that wins people over. Ask the room how many have shipped a measure that broke on a blank.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #1a0505 0%, #0b0b0d 100%)" -->
## Prompt 02 — Validate
### Make it argue with your own logic

```text
Here's a measure and what I THINK it
returns. Don't fix it yet.
Walk the filter context step by step
and tell me where my mental model is
wrong, if it is.
```

Notes:
"Don't fix it yet" is the whole prompt. Without it the model rewrites your measure and you learn nothing. Say that explicitly.

--

### Why it works

- **Catches the silent bug** — the number that looks right and isn't
- **Filter context, explained** — it narrates CALCULATE the way a senior dev would
- **"Don't fix it yet"** stops it rewriting before you understand the problem

Notes:
This is the highest-value prompt in the pack for anyone past beginner. If the room is senior, spend the extra minute here.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #1a0505 0%, #0b0b0d 100%)" -->
## Prompt 03 — Refactor
### Rewrite the measure you inherited and hate

```text
Refactor this measure for readability
without changing the result.
Use VAR names a human understands.
Keep my formatting style.
Then list what you changed and why.
```

Notes:
Everyone has inherited a measure they hate. Get a show of hands — it earns the next ninety seconds.

--

### Why it works

- **Same answer, half the confusion** — behaviour preserved, names that read in English
- **It explains itself** — the change-list is the documentation you never wrote
- **Your house style survives** — tell it your conventions and it keeps them

Notes:
"The change-list is the documentation you never wrote" is the line that gets quoted back to you afterwards.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #1a0505 0%, #0b0b0d 100%)" -->
## Prompt 04 — Design
### Wireframe the report before you build it

```text
I have these measures and dimensions,
audience is exec.
Give me an SVG wireframe of a
single-page layout - grid, visual types,
what goes top-left.
Greyscale, no real data.
```

Notes:
"Greyscale, no real data" does two jobs: it keeps the conversation about layout instead of colour, and it keeps client data out of the prompt. Say both.

--

### Why it works

- **You sketch in seconds** — five layouts to react to beats a blank canvas
- **The argument moves up** — debate the layout before you've sunk an afternoon into it
- **Paste the SVG anywhere** — drop it in a doc and walk a stakeholder through it

Notes:
This is the bridge to the design talk if anyone asks afterwards. Good design wins adoption; wireframing is how you get there cheaply.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #1a0505 0%, #0b0b0d 100%)" -->
## Prompt 05 — Requirements
### Turn stakeholder rambling into a spec

```text
Here's my messy notes from the workshop.
Turn them into acceptance criteria using
"Given / When / Then".
Flag anything ambiguous as an open
question I need to ask back.
```

Notes:
The open-questions list is the part to emphasise — that is what stops scope creep, and it is the bit people do not think to ask for.

--

### Why it works

- **Rambling becomes structure** — forty minutes of talk into a list you can sign off
- **The gaps get named** — the open-questions list is what stops scope creep
- **Faster workshops** — draft criteria live, confirm them in the room

Notes:
Mention that you do this live in workshops now, with the client watching. It changes the room when they see their own words become criteria.

---

## When to trust it — and when not to

| Trust it for | Don't trust it for |
| --- | --- |
| Drafts, variations and rewrites you'll review | A final number you haven't validated yourself |
| Explaining code, errors and filter context | Anything touching real data it shouldn't see |
| Structure: docs, criteria, naming, layout | Confident DAX that "looks" right |

Treat it like a fast junior: **brilliant first drafts, never merged without review.** <!-- .element: class="fragment highlight-red" -->

Notes:
Do not skip this slide to save time. It is the slide that makes the rest of the talk credible, and it is the one the sceptics in the room are waiting for.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #2a0a0a 0%, #0b0b0d 100%)" -->
# Live demo

Three prompts from the pack, run live against a real measure.

**~10 minutes · real model · no nets**

Notes:
Switch to the browser now. DAX variations, a validation pass, and a stakeholder ramble turned into criteria. If the wifi dies, fall back to the appendix and narrate it.

---

## What just happened in ten minutes

1. **Three DAX options** — generated, compared, one chosen on its merits
2. **A bug, narrated** — filter context walked step by step until the wrong assumption showed up
3. **A spec, from a ramble** — messy notes turned into Given/When/Then with open questions flagged

None of it replaced judgement. All of it removed the slow part **before** the judgement. <!-- .element: class="fragment highlight-red" -->

Notes:
Close the loop back to the reframe. Same sentence, different words: the job didn't go away, the slow part did.

---

## Steal these. Screenshot this slide.

| # | The prompt, in one line |
| --- | --- |
| 01 | "Give me 3 ways: readable, fastest, defensive." |
| 02 | "Don't fix it. Walk the filter context and find my error." |
| 03 | "Rewrite for readability, same result, list what changed." |
| 04 | "SVG layout for this exec page, greyscale, no real data." |
| 05 | "Turn these notes into Given/When/Then, flag every ambiguity." |

Notes:
Stop talking and let them photograph it. Count to ten in your head. This is also the moment to send the prompt-pack link to every follower's phone from the Controls panel.

---

<!-- .slide: data-background-gradient="linear-gradient(135deg, #0b0b0d 0%, #2a0a0a 55%, #0b0b0d 100%)" -->
## Get the full prompt pack

Every prompt from today, written out and ready to paste.

Connect on **LinkedIn** — that's where I post Power BI + AI workflows.

Message me **"prompt pack"** and I'll send it straight over.

Notes:
Send the link as a follower message now if you have not already — the overlay gives everyone an Open link button, which beats reading a URL out loud. Then take questions.

---

# Thank you

**Duncan Boyne** — Power BI consultant & trainer

Please rate the session — 30 seconds, it genuinely helps.

Notes:
Leave this up through Q&A so your name stays on screen.

---

<!-- .slide: data-visibility="uncounted" -->
## Appendix — if the demo dies

| Symptom | Fallback |
| --- | --- |
| No wifi | Narrate the "What just happened" slide from memory |
| AI tool down | Switch provider — that is why there are four on the toolkit slide |
| Out of time | Cut prompts 03 and 04, keep 01, 02 and 05 |

Notes:
Uncounted, so it does not appear in the progress bar. Know the cut order before you walk on stage.
