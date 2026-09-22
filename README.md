# Speaking decks

Conference and user-group decks, authored as markdown and presented through
[slides.mightora.io](https://slides.mightora.io) (a hosted Reveal.js platform).

The platform renders decks straight out of this repo — there is no build step and
nothing to deploy. Push to `main` and the deck is live.

## Presenting a deck

```text
https://slides.mightora.io/r/<owner>/speaking-decks/<deck-id>/presenter   # you
https://slides.mightora.io/r/<owner>/speaking-decks/<deck-id>/follower    # the room
```

The first slide in presenter mode shows a QR code and the follower URL. Put it up
while people arrive. Followers then move with you automatically, fragments
included, and cannot skip ahead during the session.

## Adding a deck

```text
decks/
└── my-talk/
    ├── meta.json
    └── slides.md
```

The folder name is the deck id in the URL. Lowercase letters, numbers and hyphens
only. Then validate before you push:

```bash
python validate-deck.py            # all decks
python validate-deck.py my-talk    # one deck
```

`validate-deck.py` checks the things that actually break on stage: BOMs, missing
blank lines around separators, duplicate `Notes:` blocks, unclosed code fences,
misspelled diagram fences, unknown themes and relative asset paths.

### meta.json

```json
{
  "title": "Shown on the landing page",
  "description": "Also shown on the landing page",
  "published": true,
  "theme": "black",
  "autoFragment": false,
  "availableFrom": "2026-09-23T09:00:00Z",
  "selfExploreFrom": "2026-09-23T17:00:00Z",
  "defaultBackground": { "gradient": "linear-gradient(135deg, #0b0b0d, #1a1a1f)" }
}
```

- `published: false` hides the deck from the landing page but the URL still works —
  use it for a deck you are still writing.
- `autoFragment: true` turns *every* list item into a click-to-reveal. Leave it
  off and add `<!-- .element: class="fragment" -->` where you actually want it.
- `availableFrom` / `selfExploreFrom` gate a live event: before `availableFrom` the
  deck is locked, and after `selfExploreFrom` followers get their own controls, so
  they can page back through it on the train home.
- `theme` is one of the twelve Reveal themes: black, white, league, beige, sky,
  night, serif, simple, solarized, blood, moon, dracula.

### slides.md

- A line containing only `---` starts a new horizontal slide
- A line containing only `--` starts a vertical child slide (down-arrow detail)
- `Notes:` begins speaker notes — **one block per slide**, everything after it
  until the next separator is hidden from the audience
- Blank lines above and below every separator, or the slides merge
- Per-slide options go in an HTML comment on the first line:
  `<!-- .slide: data-background-gradient="..." id="..." data-visibility="uncounted" -->`

## On stage

Presenter HUD gives you: follower count and names, send-a-message-to-every-phone
(text plus a link with an Open button), a synced Excalidraw whiteboard, a break
overlay with countdown and rejoin QR, inline notes, and speaker view with next
slide and timer.

Two standalone utilities need no deck at all:

| Utility | URL |
| --- | --- |
| Countdown timer | `slides.mightora.io/timer?target=14:30` |
| Wi-Fi QR code | `slides.mightora.io/wifi?ssid=Guest&password=secret` |

## Constraints worth knowing before you rely on this

1. **The repo must be public and the branch must be `main`.** Decks are fetched
   from `raw.githubusercontent.com`. Nothing client-confidential goes in here —
   no client names, data, screenshots or unreleased work.
2. **Presenter mode needs a password set by the platform owner** (mightora /
   Ian Tweedie), not by you. Get it before a session, and have a fallback.
3. **It needs the internet.** Both the platform and this repo are fetched live.
   Always carry an offline PDF or PPTX export.
4. **Only `slides.md` works remotely.** `slides.html` is for decks hosted on the
   platform itself.
5. **Use absolute URLs for images and video.** Relative paths resolve against
   slides.mightora.io, not this repo:
   `https://raw.githubusercontent.com/<owner>/speaking-decks/main/decks/<deck-id>/hero.png`
   (or the same path via `cdn.jsdelivr.net/gh/<owner>/speaking-decks@main/...`).
6. **Design control is markdown-level.** Twelve stock themes plus per-slide
   backgrounds. For a deck that has to carry full brand typography and layout,
   the hand-authored HTML decks under `Desktop\My Everything else folder\
   Conference Talk - *` still win. This platform wins when the *audience* needs
   to be in the deck with you.

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| "metadata not found" | `decks/<deck-id>/meta.json` missing on `main`, or the repo is private |
| Images missing | Relative path — use an absolute URL |
| Slides merged together | No blank line above/below `---` |
| Notes showing on screen | More than one `Notes:` block on that slide |
| Diagram renders blank | Fence language must be exactly `mermaid` or `plantuml` |
| Deck loads but is locked | `availableFrom` is in the future |

## Decks

| Deck id | Talk | Run at |
| --- | --- | --- |
| `ai-for-power-bi-professionals` | AI for Power BI Professionals: The Prompt Pack That Actually Makes You Better at Your Job | CollabDays Bletchley Park, 23 Sep 2026 |

Ported from `talk-deck.html` and deliberately event-neutral, so the same deck
re-runs without edits. Conference-mandated brand slides (the ELUK ones in the
original) are not in here — add them per event if the organiser requires them.
