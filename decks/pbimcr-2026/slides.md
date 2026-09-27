<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/01.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 0:00 – 2:00 Pacing note: Advance to this slide, then hold for 5–8 seconds before speaking. Let them read it. Let the title sit. It's a question — give them a moment to wonder what the question means. Speaker Notes: "So. Someone asked me to give this talk a title before I knew exactly what the talk was going to be. [pause] Which, it turns out, is a fairly good way to summarise the project it's about. [pause] The title comes from something I actually said. Out loud. To a client. During a site visit. And not in a professional capacity. [small laugh expected here — deliver this deadpan, not as a setup to a punchline] I'm going to come back to that. But first — let me give you a bit of context about who I am, and about the project."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/02.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 2:00 – 3:30 Speaker Notes: "I’m Duncan Boyne, I build Power BI solutions — primarily for manufacturing and professional services businesses, but also anywhere someone has data they don't fully understand yet. My job description, as I've come to define it: I'm a storyteller of my customers' data. I take numbers. I find a narrative. I build dashboards that communicate that story clearly to the people who need it. [pause] Which sounds elegant. And often it is. Until the story you thought you were telling turns out to be... not quite the right one. [pause] This is the story of one of those projects."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/03.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 3:30 – 4:30 Speaker Notes: "The client: a manufacturing company. Precision-engineered components. The kind of parts that go into serious machinery — the type of product where tolerances are measured in micrometres and getting it wrong has real consequences. Smart engineers. Experienced team. Long track record. They'd been doing this for a long time, and they knew what they were doing. The project: build them Power BI reporting. Workshop dashboards. Operational visibility. Production and capacity planning. Classic stuff. Epicor ERP on the backend, some SQL views, a very old custom application that everyone was quietly terrified of. The usual. [pause] And the project was going really well. Data was clean-ish. The integrations were behaving. The dashboards were useful. [beat] In consultancy, this is normally the part just before something interesting happens."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/04.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 4:30 – 5:30 Speaker Notes: "The dashboards we'd built were telling a good story. Production on target. Quality metrics healthy. The operations team had visibility they hadn't had before — and they were actually using it, which is the real metric. [pause] The CEO would walk past the main dashboard in the morning and nod. You know that nod. The 'yes, this is working, the investment was justified' nod. [pause] And then we moved into phase two. Complaints, returns, and refunds reporting. Which, in hindsight, is where the project actually started."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/05.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 5:30 – 6:30 Pacing note: Let the number appear and breathe before speaking. Speaker Notes: "Here's a number. Zero point four percent. That is their internal test failure rate. For precision-engineered components, that is genuinely exceptional. [pause] Roughly four components in every thousand failing QA testing. The engineers were proud of it. Rightfully. It represents years of process refinement and accumulated expertise. [pause] And I remember thinking: yeah. This is a healthy business. The dashboards confirm it. The data confirms it. Everything points in the same direction. So we connected the complaints and returns data — expecting to see roughly the same picture."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/06.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 6:30 – 7:00 Pacing note: Read the slide, then pause. Let the audience sit with it. Speaker Notes: [read the slide, then:] "That's it. That's the whole slide. [pause] Because sometimes the data introduces itself."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/07.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 7:00 – 9:00 Pacing note: Advance to this slide, then hold silence for 3–5 seconds minimum. Do not speak immediately. The number needs to register. Speaker Notes: [silence — let the slide sit] "Up to fifteen percent. [pause] Not average. Maximum. But still. [pause] Customer replacement rate. Components that customers had to replace — either they failed in use, or they didn't perform to the expected specification. [beat] Let me put those two numbers next to each other."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/08.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 9:00 – 10:00 Speaker Notes: "Same company. Same products. Same period. [pause] One says: we're exceptional at quality. The other says: customers are replacing up to one in seven products. [pause] These two things cannot both be completely true and completely fine. Something is being hidden. Or something is being missed. Or both. [pause] So. Before I tell you what we found — I want to know what you would do."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/09.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 10:00 – 12:00 Pacing note: Give the full 2 minutes. Do not rush this. The audience participation is a feature of the talk, not a filler. Genuinely listen to responses. Speaker Notes: "I'm being serious — what would you investigate first? Turn to someone next to you. Sixty seconds. Go. [wait — let room noise happen — move to the edge of the stage, be relaxed] [After ~60 seconds, take 3–4 verbal responses from the room. Engage authentically with each one:] - "That's a really good instinct — yes, we did look at that early on." - "Interesting — why would you go there first?" - "That's actually exactly what we thought initially." - "Oh, that's a route we didn't take until later — flag that, we'll come back to it." [After taking responses:] Right. Let me take you through what we actually looked at. Some of it will overlap with what you said. Some of it was more... methodical. And some of it was fairly desperate."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/10.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 12:00 – 13:00 Speaker Notes: "Alright. Let me take you through the investigation chronologically — because I think the order matters. It tells you something about how these things actually unfold in real life, versus how they get presented retrospectively. The first thing you always check: is the data actually correct? Are systems being measured consistently? Are the return reason codes being used properly? Is there double-counting? Are we comparing like for like? [pause] This is the sensible, methodical, slightly boring thing to check first. And we did check it thoroughly. [pause] The data was fine. Annoyingly fine. Clean joins, consistent definitions, accurate codes. Matched to source systems. Nothing suspicious. [beat] Which, honestly, makes it worse. You want it to be a data quality problem. Those are easy. 'The data was wrong — here's the fix.' Everyone goes home on time. This was not that."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/11.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 13:00 – 14:00 Pacing note: The pause in the middle is intentional — deliver it as a slight deflation. The bracket notation on the slide can stay visible. Speaker Notes: [deliver with dry understatement — not big energy, just flat] "'The data is fine.' That's a sentence that sounds like good news. [pause] When the data is wrong, you fix the data. You know exactly where to look. There's a path forward. When the data is fine and the numbers still don't make sense — you're now in 'existential uncertainty' territory. Which is considerably less comfortable, and involves a lot more coffee."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/12.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 14:00 – 15:30 Speaker Notes: "Next: product lines. Was it specific types of components? A design flaw in a particular product family? And here's where it starts getting interesting. Some product lines were worse than others. But the pattern wasn't clean. It wasn't 'Product B has a structural problem.' It was inconsistent. [pause] Some product lines had high replacement rates — but only sometimes. Not always. And the timing was uneven. [pause] In data terms: we had a pattern. We didn't have a reason. Which is, incidentally, the most dangerous place to be. Because a pattern without a reason is also called a story without evidence. And the temptation to fill that gap with the nearest plausible explanation — without evidence — is how consultancy goes wrong."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/13.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 15:30 – 17:30 Pacing note: Again, genuine engagement. Take responses. Listen. Respond to what you actually hear. Speaker Notes: "You're looking at something seasonal. Irregular. The spikes don't match production cycles, they don't correlate with any internal event anyone can identify. What would you check next? [take 3–4 responses — actively engage with each] [If someone says 'customers':] "Oh — interesting. Why customers? Say more about that." [If someone says 'weather' or 'environment':] "Interesting. What aspect of the environment specifically?" [If someone says 'shipping' or 'logistics':] "Good instinct — keep that thread, we're going to come back to it." [After taking responses:] Right. The word 'customers' has come up — or maybe hasn't. Either way, let me show you what we found when we went there."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/14.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 17:30 – 19:30 Pacing note: Build this slide if possible — show the headline first, then the subtext. The two-part reveal matters. Speaker Notes: "Here it is. [pause] Five customers. Eighty-five percent of production. [pause] Now — on the surface, this is just a business fact. Customer concentration. It's a commercial risk, certainly, but it's not directly a quality issue. Lots of manufacturers have this. Except. [pause] When you have that level of concentration, and those large customers all buy predominantly in spring and autumn... Your aggregate metrics aren't 'company-wide' metrics. They're 'large customer' metrics. And what happens to the small customers — the fifteen percent of output spread across many smaller buyers — is almost completely invisible in your aggregated reporting. [pause] The failure spikes weren't evenly distributed. They were clustering with the smaller customers. Who bought mainly in summer and winter. [pause] The aggregated reporting wasn't wrong. It was accurate. It was just hiding the real story underneath the weight of five large buyers."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/15.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 19:30 – 21:00 Speaker Notes: "This is one of the most underrated problems in data work. The average was correct. I cannot stress this enough — the maths was right. The methodology was sound. But the average was completely useless for understanding what was happening to a subset of customers. [pause] This is a trap that dashboards make worse, not better. Because dashboards make averages look authoritative. A big number, displayed clearly, in an official-looking interface, carries a kind of false credibility. It suggests: this is representative. This is the full picture. [pause] Here, the 'average' was just the large customers. The small customers were statistical background noise. Arithmetically insignificant. Practically very significant. [pause] So now we know something. We know WHO is experiencing the problem. We know roughly WHEN. But we still don't know WHY."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/16.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 21:00 – 23:00 Speaker Notes: "Here's the pattern when you separate it out. Large customers: spring and autumn buyers, predominantly. Consistent, predictable, high volume. They plan their purchases, they order in advance. Small customers: summer and winter buyers. More ad-hoc, lower volume individually, less predictable. And the failure spikes: summer and winter. [pause] So the question is now very specific. What is different about components that are produced and shipped to small customers in summer and winter, versus components produced and shipped to large customers in spring and autumn? [pause] This is the question. Everything else is noise now. If we can answer this question, we understand the problem. [pause] And I remember sitting in a meeting room, looking at this pattern on a screen, and saying — almost to myself — a very obvious question. I'd like your help getting there."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/17.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 23:00 – 25:00 Pacing note: This is the most important audience interaction moment in the talk. Don't rush it. Let the room think. Be comfortable with silence. Speaker Notes: "We know who. We know when. The internal process is consistent — the engineers are doing nothing differently for small customer orders. Same machines, same people, same procedures. What are we missing? [take 3–4 responses from the audience — engage with each one] [If someone says 'environment' or 'storage' or 'warehouse':] "That's really interesting — what makes you go there?" [If someone says 'temperature' or 'climate':] "Oh. Say more about that. What specifically are you thinking?" [If someone says 'shipping' or 'logistics':] "Good — and what aspect of shipping? Because the products are all going through the same shipping provider..." [If nobody is getting close:] "Nobody's mentioned the physical space yet. The actual buildings. Let me tell you why that matters more than it sounds."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/18.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 25:00 – 26:30 Pacing note: Deliver this quietly. Almost as an aside. Not dramatic, not building to something — just conversational and slightly tentative. That's what makes it land. Speaker Notes: "This is the question I actually asked. Not a clever question. Not a technical insight. Not the product of sophisticated analysis. [pause] I just... said it. Because I was running out of obvious places to look, and because the words 'testing' and 'storage' had appeared as separate things in every conversation we'd had — but nobody had ever connected them or questioned whether that separation was relevant. [pause] And there was a pause. One of those pauses where you're not sure if you've said something obvious or something useful. [beat] And then someone said: 'Well... they're in different buildings.'"

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/19.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 26:30 – 28:30 Speaker Notes: "The workshop — where all testing happens — is a controlled environment. Temperature regulated. The precision engineering work takes place there. Everything is done properly, carefully, consistently. [pause] The warehouse — where finished components wait before shipping — is in a separate building on the same site. [pause] And between the two: a loading dock. Which is, essentially, just outside. [pause] Products leave the workshop on racks. They go through the loading dock. They sit in the warehouse waiting for collection. In summer: they travel from a cool, controlled environment into heat and humidity. In winter: they travel from a warm, controlled environment into cold. [pause] And the products bound for small customers — lower volume, less predictable demand, less regular collection — sat in that warehouse for longer. Waited more. Were exposed to more temperature variation. [pause] Nobody had modelled this. It wasn't in the ERP data. It wasn't in the process documentation. It was just... physical reality. The building layout. The way the site had always worked."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/20.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 28:30 – 30:30 Speaker Notes: "Here's the theory we arrived at. Components tested at controlled temperature. Then moved through an uncontrolled environment. Then potentially sitting in a warehouse that — it turns out — had no active temperature control at all. It was described, accurately, as 'basically a big shed.' [pause] For precision-engineered components — where tolerances are measured in micrometres — thermal cycling after manufacture can introduce micro-stresses. Dimensional changes. Vulnerabilities that only manifest under use conditions. The components were passing testing. Because at the time of testing, they were fine. [pause] The testing environment and the real-world post-testing conditions were completely different. And because testing happened in one building and storage happened in another, and because this was just how the site had always been laid out, nobody had ever thought to flag the gap as potentially significant. [pause] Now. I want to be very clear about what happens next. Because most case studies would pivot here to: 'And then I solved it heroically, and the numbers dropped to below half a percent, and everyone applauded.' [pause] That's not what I'm going to say."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/21.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 30:30 – 31:30 Pacing note: Pause before advancing to this slide. Let the previous slide's content settle. Then advance to this one slowly and hold for a beat before speaking. Speaker Notes: "The collective sound in the room when we drew this out on the whiteboard was essentially... [click — slide appears] [hold — let the room respond] Yeah. [pause] That sound. That exact sound. Because it's obvious in retrospect. Of course the warehouse temperature matters. Of course it does. Anyone with a reasonable understanding of materials science would look at this and nod. [beat] But nobody had asked. Because everyone inside that organisation had known about the two-building setup for years. It had ceased to be information. It was just the way things were. [pause] The gap between those two buildings was so familiar it had become invisible."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/22.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 32:00 – 35:00 Pacing note: Deliberate tone shift here. The energy comes down. This section is about honesty, not performance. Slow down. Speaker Notes: "I want to be honest with you about something — because I think it's the most important thing in this talk. This wasn't a masterclass in data analysis. I didn't develop a sophisticated model. I didn't write a brilliant DAX query that surfaced the insight. I didn't even formulate a particularly clever hypothesis. [pause] I asked a simple question at the right moment. And the reason I asked it is because I was curious, slightly stuck, and had run out of the obvious things to check. [pause] The engineers in that building were not stupid. They were brilliant. They knew those machines and those products better than I ever would. The dashboards were not wrong. They were accurate reflections of the data they'd been given. [pause] The problem was assumptions. Assumptions that were so deeply embedded in how the organisation operated that they'd stopped being visible as assumptions. They were just facts. Background. The way things are. [pause] 'Testing happens here. Storage happens there.' That's not a problem statement. That's a site layout. Nobody thinks to question it because nobody thinks it needs questioning. [pause] My job, accidentally, became asking whether 'the way things are' was part of the problem. And here's the uncomfortable truth: I only got there because I wandered into a cold warehouse and felt the temperature and said something entirely unprofessional."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/23.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 35:00 – 40:00 Pacing note: Walk through each question with context from the case study. This is the teach section, but keep it grounded in the story — don't let it become a lecture. Speaker Notes: "I've taken five questions from this experience. These aren't ground-breaking. They're not new. But they're the questions I didn't ask early enough — and asking them earlier would have saved weeks of investigation. [pause] One: What happens before this process? Before testing. Where did the components come from? Were there batch variations in materials? Were there upstream process changes that might introduce early vulnerabilities? You're not just looking at the process you've been given — you're looking at its edges. [pause] Two: What happens after it? This is the one that mattered most here. What happens after testing? What is the physical journey before the product reaches the customer? What environment does it pass through? What conditions does it encounter? We'd been given 'the process' and we'd modelled 'the process.' The problem lived outside the process. [pause] Three: Who experiences the problem differently? Not 'who has the problem.' Who experiences it differently. The large and small customers weren't having fundamentally different problems. They were experiencing the same underlying issue at different times, because of how their purchasing patterns interacted with environmental conditions. Segment before you aggregate. Always. [pause] Four: What changes over time? Seasonal patterns are a flag. They often indicate external environmental factors — temperature, daylight, supply cycles, human behaviour patterns. When you see a seasonal spike, the question isn't just 'why in winter' — it's 'what is different about winter?' And 'different' might mean something completely outside the dataset. [pause] Five: What 'obvious' thing has nobody questioned? This is the hardest one. Because by definition, it doesn't feel like a question. It feels like background. It feels like a given. Ask it anyway. Ask it especially when you feel slightly ridiculous for asking it. [pause] The answer to this entire case study lived in question five."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/24.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 40:00 – 43:00 Speaker Notes: "I keep coming back to this phrase: I'm a storyteller of my customers' data. I do believe it. I think it's an accurate description of what good data work actually is. [pause] But here's the thing about storytelling. If you're telling someone else's story, you need to understand the full story. Not just the chapter they've given you access to. Not just the data they thought to record. Not just the process they told you about. [pause] In this case, the data was the internal view of a manufacturing process. Clean, accurate, well-maintained. It told the story of what happened inside the workshop perfectly. But the story had a chapter that didn't exist anywhere in the data. It lived in the physical world. In the gap between two buildings. In the temperature on a loading dock on a February morning. [pause] The lesson isn't 'always go and look at the warehouse.' The lesson is: be curious about the edges of the data. Ask where the story starts. Ask where it ends. Ask who didn't make it into the dataset. Ask what happened before the first row. Ask what happens after the last row. [pause] Your customer will tell you the story they think you need. They'll describe their process, hand over their system access, give you what feels like everything. Your job is to notice when the story has chapters they haven't thought to mention. Because often those chapters are the ones that explain everything else."

---

<!-- .slide: data-background-image="https://raw.githubusercontent.com/DuncanBoyne/speakingdecks/main/decks/pbimcr-2026/slides/25.jpg" data-background-size="contain" data-background-color="#0E0E0E" -->

Notes:
Timing: 43:00 – 45:00 Pacing note: Slowest part of the entire talk. Short sentences. Real pauses. This is the landing — don't rush it. Speaker Notes: "Let me come back to the title. 'Can someone turn the heating on.' [pause] I said this during a site visit to that warehouse. I was cold, I was trying to understand the storage conditions for a different reason entirely, and I was genuinely uncomfortable. And someone said: 'It doesn't have heating. It's basically just a big shed.' [pause] And I said: 'Is that... normal? Is that just how warehouses work?' And they said: 'Yeah — it's always been like that.' [pause] And that was the moment. Not an algorithm. Not a DAX query. Not a sophisticated segmentation model. Just: oh. Oh, it's cold in there. [long pause] Every dataset you work with has a version of this. A thing that's just how it's always been. A process step that exists outside the system. A variable that nobody thought to log because it's just... the world. [pause] Your job — our job — is to be the person who asks the dumb question. Who says 'wait, hang on.' Who gets slightly cold on a site visit and turns that discomfort into a question. [pause] Be curious. Be observational. Be willing to look slightly foolish. Ask the question that everyone in the room already knows the answer to. Because sometimes they don't. And sometimes that answer is the whole story. [long pause — look out at the room] Thank you."
