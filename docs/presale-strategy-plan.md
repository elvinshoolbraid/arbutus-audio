# Arbutus-1 presale strategy: architecture, dependencies, legal

Status: planning spec and grilling. No implementation. Nothing on the site changes, no entity is
formed, no money is taken. Jurisdiction: British Columbia, Canada, selling direct worldwide.
Dated 2026-09-25. Legal sections are a map for a lawyer and an accountant, not advice.

## 1. The ask, in one paragraph

Launch Arbutus-1 the way a community-built building gets built: a presale with honest, published
timelines and regular updates; small refundable deposits the way Tesla and Framework take them;
a self-hosted Kickstarter-style campaign rather than Kickstarter; and hardware and software
developed in the open from the start so the community can contribute to and improve the design,
with clear messaging and a clear contract about what contributing means. Instagram carries the
story. The German large-timber precedents (co-op built, open collaboration) are the model for how
to talk about collaborative creation.

## 2. First finding: this is three projects, and two kinds of money

"An open, community-built synth with a refundable-deposit presale" bundles three things that need
separate rules and separate homes.

| Layer | What it is | Rules that govern it |
|---|---|---|
| A. The commons | ArbutusOS, the board files, print files, repair guides, the plugin API, the interaction matrix | Open licences, trademark, contributor terms |
| B. The product | A manufactured batch of Arbutus-1 units with batteries, shipped to consumers in several countries | Product safety and certification, battery transport, warranty, product liability |
| C. The money and crowd | Reservations, batch pre-orders, the mailing list, Instagram | BC consumer contract law, Competition Act, payment-processor terms, tax |

And the brief conflates two instruments that must stay distinct:

1. **The reservation** (Tesla, Framework): a small, fully refundable deposit that buys a place in a
   queue. It funds nothing. Its job is signal, motivation and ordering.
2. **The batch pre-order** (Kickstarter, Crowd Supply): a firm order at a fixed price for a specific
   batch, with a goal and a deadline, refunded if the goal is not met. Its job is funding the run.

The reservation can open early because it promises almost nothing. The batch pre-order can only
open once the product is real enough that the promise can be kept. Most hardware crowdfunding
failures come from opening the second instrument at the first instrument's level of readiness.

## 3. Precedents, and what each one teaches

### 3.1 Framework: the deposit model to copy

Framework takes a fully refundable US$100 deposit to hold a place in a batch, opens new batches with
later ship dates as earlier ones fill, and charges the balance only when the unit is about to ship.
The deposit can be cancelled for a full refund any time before the balance is charged. Source:
[Framework blog](https://frame.work/blog/framework-laptop-starting-at-999-pre-orders-are),
[Framework terms of sale](https://frame.work/terms-of-sale).

This is the exact mechanism the brief wants, already proven for a product with a comparable
audience. Copy it: small deposit, batch numbers, balance charged at ship. Charging at ship also
solves most of the chargeback and consumer-law exposure below.

### 3.2 Tesla Model 3: what made blind reservations work, and what it cost

Tesla had shipped two cars and built charging infrastructure before it took US$1,000 refundable
Model 3 reservations. The deposit was small relative to the price, refunds were honoured, and
updates were frequent. Deliveries then ran years late for most people. Lesson: reservations need a
shipped thing that proves competence, and honesty erodes when the audience gets large unless the
mechanism (section 4.3) does not depend on mood.

For Arbutus-1 the "already shipped car" does not exist yet. The nearest candidate is the emulator:
ArbutusOS running on a laptop, with real audio, tests and a screenshot harness. Publicly releasing
it before any deposit is taken is the single strongest trust move available.

### 3.3 Mutable Instruments: the open-hardware synth precedent

Mutable released hardware under CC BY-SA and firmware under GPL-3 or MIT, kept the name as a
registered trademark, and stated that derivatives must not carry the name. After the company closed
in 2022, clones from other makers kept the designs alive, including a full-size line from a major
manufacturer. Source:
[Mutable open source page](https://mutable-instruments.net/modules/elements/open_source/),
[Synthtopia on Behringer clones](https://www.synthtopia.com/content/2023/04/06/is-behringer-cloning-the-entire-mutable-instruments-line/).

Lessons: "designs free, name controlled" is the working model in this exact market; a reciprocal
licence does not stop a large company cloning; and the community outlived the company because the
files were public. The site already promises openness, so the clone question is not whether but
when, and it belongs in the grilling.

### 3.4 Kickstarter and Crowd Supply: why self-host, and the one alternative

Kickstarter pledges are non-refundable, all-or-nothing, and rewards cannot be equity or debt; the
creator must fulfil or refund. Source: [Kickstarter rules](https://www.kickstarter.com/rules).
Crowd Supply is the all-or-nothing platform built for open hardware: similar fees, a review process,
hands-on manufacturing and fulfilment help, and a permanent store page afterwards. Source:
[Crowd Supply on Wikipedia](https://en.wikipedia.org/wiki/Crowd_Supply),
[CrowdCrux comparison](https://www.crowdcrux.com/crowd-supply-vs-kickstarter/).

Self-hosting is right for the reservation instrument. For the batch pre-order, Crowd Supply is the
one alternative worth pricing before deciding to build fulfilment alone, because the site already
names "getting a niche hardware launch right: supply chain, manufacturing and the first production
run" as the biggest gap.

### 3.5 The community-built building precedent, mapped to a synth

The German large-timber apartment projects (Roots in Hamburg, Lynarstrasse in Berlin, the
Prinz-Eugen-Park quarter in Munich) were mostly built by co-ops and self-organised building groups,
with a professional developer on record and a city that sold land to groups on conditions. Sources:
[ubm magazin on Roots](https://www.ubm-development.com/magazin/en/back-to-the-roots/),
[binderholz on Lynarstrasse](https://www.binderholz.com/en-us/mass-timber-solutions/residential-building-lynarstrasse-berlin-germany/),
[binderholz on Prinz-Eugen-Park](https://www.binderholz.com/en-us/mass-timber-solutions/quartier-prinz-eugen-park-munich-germany/).
The open-design analogue is WikiHouse: designs under CC0, contributors owe nothing and are owed
nothing, liability disclaimed, and the name licensed separately. Source:
[WikiHouse terms](https://www.wikihouse.cc/terms).

| Building | Arbutus-1 |
|---|---|
| Future residents commit before the building exists | Reservation holders commit before the batch exists |
| The design is open; a licensed professional signs the real drawings | The design is open; a test lab and a manufacturer of record sign the real product |
| A developer with completed buildings gets the loan | A person who has shipped hardware gets the supplier terms and the trust |
| The city sells land to groups | Grants, accelerators and a co-op term supply the runway |
| Monthly co-op meeting | Monthly log post |
| "The house belongs to those who live in it" | "The instrument belongs to the people who play it" |

The messaging precedent to copy is one sentence long, both times. WikiHouse's "you owe us nothing,
we owe you nothing" and the Syndikat's "the house belongs to those who live in it" survived contact
with lawyers because they were short.

## 4. Architecture

### 4.1 Entity and money map

```
 Community (players, makers, tinkerers)
   |  reads the log, plays the emulator, contributes under DCO
   v
+----------------------------+          +-------------------------------+
| A. Commons                 | <------- | Contributors                  |
| ArbutusOS, boards, prints, |  DCO     | keep copyright, licence it,   |
| plugin API, repair guides  |          | get credit, get nothing else  |
| open licences, name is TM  |          +-------------------------------+
+-------------+--------------+
              | the commons is the source; the product is a build of it
              v
+----------------------------+          +-------------------------------+
| B. Arbutus Audio (BC corp) | <------- | Test lab (EMC, radio, battery)|
| manufacturer of record,    |          | Board assembler (JLCPCB)      |
| holds certifications,      |          | Print farm, fulfilment        |
| sells units and spares     |          | Insurer                       |
+-------------+--------------+          +-------------------------------+
              | two instruments, never mixed
              v
+----------------------------+   +-------------------------------------+
| C1. Reservation            |   | C2. Batch pre-order                 |
| small, refundable any time |   | fixed price, goal, deadline         |
| separate bank account,     |   | refunded if goal missed; balance    |
| never spent                |   | charged at ship, not at order       |
+----------------------------+   +-------------------------------------+
```

Two rules hold this together. Reservation money is never spent. The commons never becomes the
product without a certification and a manufacturer of record standing between them.

### 4.2 Stage gates, tied to the prototype ladder already on the site

The site's ladder (P0 to P6+) is the schedule. The presale attaches to it rather than inventing a
second timeline.

| Stage | Entry condition | What people can do | Money allowed |
|---|---|---|---|
| 0. Now | P2 done: emulator, look-alike, one working board | Join the list, play the emulator, contribute to the commons | None |
| 1. Reservations open | Corporation formed, bank account, payment processor, published terms; emulator public; P4 done (stack physically assembles) and a published price band with the BOM behind it | Pay a small refundable deposit for a numbered place in batch 1 | Deposit only, refundable any time, separate account, never spent |
| 2. Batch 1 pre-order | P5 done (integrated unit works), DVT pass, certification plan priced, unit cost known at batch size, ship date with confidence band | Convert reservation to a firm order at a fixed price; goal and deadline published | Goal held until met; refunded in full if missed; balance charged at ship |
| 3. Production | Certification passed, parts in hand, batch funded | Watch it get built; monthly cost and yield reporting | Balance charged when a unit is on the shelf for that order |
| 4. Shipping | Units tested, warranty and repair guides live | Receive, repair, contribute | Normal sales |
| 5. Open store | Batch 1 shipped and supported | Buy from stock; buy spares | Normal sales |

The gate the brief will want to skip is Stage 1's "P4 done and price band published". A deposit
taken on a rendering is a Kickstarter; a deposit taken on a stack that physically assembles, with
the BOM public, is a Framework. The difference is what the log will look like a year later.

### 4.3 The honest-timeline mechanism

Honesty here is a process the reader can audit, not a tone. Specify it.

- The prototype ladder stays the public schedule. Each rung carries a status, the question it
  answers, a date range and a stated confidence. Slips edit the ladder and get a log entry that
  names the cause.
- One log post a month, same day every month, even in exam season, even if it says nothing moved.
  The site currently promises "no newsletter cadence". Keep that for email; the log itself needs
  the cadence, because a reservation holder needs a heartbeat.
- One public numbers table: reservations held, money in the reservation account, refunds issued,
  current unit cost at batch size, target price, ship-date range and confidence. Unknown values say
  "unknown", never an estimate dressed as a number.
- Instagram carries only what is already in the log or the commons. A post that promises more
  than the log is a bug, and the rule is written down where followers can see it.
- A public kill list: the ranked risks that would stop the project (section 7 is the first draft),
  and the kill criterion: the condition under which all reservations are refunded and the project
  stops or pauses.

### 4.4 The contribution architecture (the commons)

- Repositories: `arbutus-os` (firmware, emulator, plugin API, tests), `arbutus-hardware` (KiCad
  boards, BOM, mechanical CAD, print files), `arbutus-docs` (interaction matrix, repair guides,
  decision log). The site already promises "print files, board files and repair guides published".
- Contributions arrive as proposals against a short written process: the problem, the change, the
  evidence, who reviewed it. Merging is a maintainer decision, not a vote. The site's promise that
  "the best community work gets folded back into the base product" needs a reciprocal licence and
  this process to be true.
- Developer Certificate of Origin (DCO) sign-off on every contribution. No contributor licence
  agreement. Contributors keep their copyright and licence it under the project licence.
- The plugin boundary is the strategic decision: if synth engines, effects and sequencers are
  plugins "anyone can write and share", the plugin API should be under a permissive licence so
  third parties can choose their own terms for plugins, while the core stays reciprocal. Decide
  this before the first public commit.
- The "manufacturer of record" boundary, written into the README: the commons is design
  documentation; the certified product is a specific build of it by Arbutus Audio; anyone building
  from the files does so at their own risk and must not use the name.
- What contributors get, stated in the first sentence of the contributing guide: credit in the
  repo and in the device's about screen, early queue access, and nothing that could be read as
  revenue share, equity or a discount tied to volume of work.

### 4.5 Platform

No custom software until a gate requires it.

- Stage 0: the existing static site, the mailing list, public repos, Instagram. Ship the emulator
  as a download or a web build.
- Stage 1: a hosted checkout for the deposit (Stripe Checkout or equivalent), a separate bank
  account for reservation money, a spreadsheet as the queue, and a published terms page.
- Stage 2: either the same checkout with a goal counter and manual refunds, or Crowd Supply. The
  choice is a cost and capacity decision, not a principle.
- Stage 3 onward: a simple store. Not before.

## 5. Dependencies

The critical path is hardware readiness, then certification, then money for the run. Community
and firmware work run in parallel and do not shorten it.

| Dependency | Blocks | Lead time | Status |
|---|---|---|---|
| P3 mule board: key layout and new parts proven | P4, P5, everything | Weeks to order and bring up | Next |
| Compute decision: Compute Module 4 vs Pi Zero 2 class | BOM, price, radio certification path, firmware performance | Decided on P3 data | Open |
| Battery pack design: three 21700 cells, in-house BMS | Product safety, certification, shipping, insurance | Safety-critical; may need a certified pack or protected cells instead | Open, high risk |
| Enclosure production method: printed PETG at volume vs moulded | Unit cost, throughput, appearance consistency | Print time per unit decides whether 200 units is weeks or months | Open |
| Keycap and switch interlock | Assembly, durability | Untested per the log | Open |
| Unit cost at 100 and at 500 units, all-in (parts, assembly, print, certification amortised, packaging, payment fees, warranty reserve) | Price band, Stage 1 | Days once the P3 BOM exists | Missing |
| Certification: EMC (ICES-003, FCC Part 15B), radio if wireless (RSS-247, FCC Part 15C, RED), CE and UKCA marking, RoHS | Selling in Canada, US, EU, UK | Lab booking plus fixes; budget in the low tens of thousands CAD | Missing |
| Battery transport: UN 38.3 test report for the cell or pack, dangerous goods packaging and carrier terms | Shipping any unit | Depends on cell supplier's existing report | Missing |
| BC corporation, bank account, GST registration, payment processor | Stage 1 | Weeks | Missing |
| Product liability insurance covering lithium consumer electronics | Shipping | Weeks; insurer will ask about the pack | Missing |
| Board assembler terms (JLCPCB) and minimum order quantities for every part | Batch size, cash needed | Days to quote | Missing |
| Runway for the batch itself: personal capital, grant (IRAP, Futurpreneur, regional accelerators), or the batch pre-order goal | Stage 3 | Months for grants | Missing |
| Firmware "done" definition for batch 1 | Stage 2 promise | A decision plus the interaction matrix | Undefined |
| Public emulator release with licence | Trust before Stage 1 | Days | Can start now |
| Licence and trademark for the commons | Stage 0 commons launch | Days to decide, months to register | Undecided |

Two dependencies dominate. The battery pack is the one that can end the project: an in-house
battery management circuit with user-accessible bare 21700 cells in a consumer product is the part
an insurer, a test lab and a carrier will each ask about first. The all-in unit cost is the one
that decides whether "under $500 CAD" is a promise or a hope, and it is unknown until P3.

## 6. Legal map (for the lawyer and accountant meeting)

### 6.1 Consumer contracts in BC: Business Practices and Consumer Protection Act (BPCPA)

- A deposit for goods delivered later is a "future performance contract", and an online sale is
  also a "distance sales contract". The Consumer Contracts Regulation prescribes what such a
  contract must contain (including a supply date) and gives cancellation rights, including the
  right to cancel if goods are not delivered within 30 days of the supply date. Sources:
  [Consumer Protection BC on selling now for future goods](https://www.consumerprotectionbc.ca/selling-now-for-future-goods-or-services-contract-rules-for-businesses/),
  [Consumer Contracts Regulation](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/272_2004).
  The Act was amended in 2025; verify the current text. Source:
  [DLA Piper on the 2025 amendments](https://www.dlapiper.com/en-us/insights/publications/2025/05/amendments-to-the-bc-business-practices-and-consumer-protection-act).
- Consequence: the reservation terms must state a supply date range and the cancellation rights,
  and "refundable any time" must be literally true. Charging the balance at ship rather than at
  order keeps the future-performance exposure to the deposit alone.
- Refunds must be issued within the statutory window after cancellation; publish a shorter one.

### 6.2 Advertising and representations

- The federal Competition Act prohibits false or misleading representations, which includes
  delivery claims and price claims. "Under $500 CAD" on the site is a representation. Instagram
  posts are advertising.
- The BC Sale of Goods Act implies conditions of merchantability and fitness that cannot be
  excluded for consumers. A written warranty adds to these; it does not replace them.

### 6.3 Payments, chargebacks and where the money sits

- Card networks allow disputes for months after the expected delivery date; pre-orders carry
  extended exposure, and processors may impose reserves or holds when late deliveries produce
  disputes. Source:
  [Chargeblast on pre-order chargeback risk](https://www.chargeblast.com/blog/what-stripe-shopify-wont-tell-about-chargeback-risk).
- Consequence: reservation money sits in its own account and is never spent, so a dispute is
  always just a refund. Batch pre-order balances are charged at ship. Processor terms on
  pre-orders and disclosed ship dates must be read before Stage 1.

### 6.4 Tax

- A deposit is not consideration for GST purposes until it is applied to the sale; tax is then
  due, and a forfeited deposit is taxed as if applied. Source:
  [CRA GST 300-6-8 Deposits](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/g300-6-8/deposits-gst-300-6-8.html).
  A fully refundable deposit that is never forfeited is clean. Register for GST before the batch
  pre-order rather than waiting for the small-supplier threshold, to recover input tax on parts and
  certification.
- BC PST on sales to BC customers; exports are zero-rated for GST. Sales into the US and EU raise
  duties, tariffs and marketplace or VAT registration questions that change year to year; price
  them per country before Stage 2, and state on the order page who pays.

### 6.5 Product safety, certification and batteries

- Electromagnetic compliance is required to sell in every target market: ICES-003 in Canada, FCC
  Part 15 in the US, CE marking in the EU (EMC, RoHS, WEEE, and the Radio Equipment Directive if
  wireless), UKCA in the UK. The Compute Module 4 and Pi Zero 2 W carry modular radio
  certifications that reduce but do not remove host-product testing. Source:
  [Raspberry Pi compliance portal](https://pip.raspberrypi.com/categories/636-approvals).
  A no-wireless variant removes the radio tests entirely and is worth costing.
- The EU Batteries Regulation (2023/1542) is moving toward requiring user-replaceable batteries in
  portable devices. "Bolts, not glue" and 21700 clips are on the right side of it; confirm the
  in-force dates for the batch ship window.
- Lithium cells: the cell or pack needs a UN 38.3 test report to ship; devices with installed
  cells under 100 Wh ship under UN3481 rules with carrier-specific packaging. Three 21700 cells is
  roughly 50 to 55 Wh, inside that limit. A home-designed battery management circuit is a
  safety-critical design; a lab or insurer will expect either a certified pack (IEC 62133 or
  equivalent) or protected cells with a proven charger and protection IC. This is the single
  largest legal and safety exposure in the product and it deserves its own decision.
- Canada Consumer Product Safety Act: the manufacturer must keep records and report incidents.
  Product liability insurance before the first unit ships.

### 6.6 Entity, liability and money hygiene

- Incorporate a BC company before taking any money. A sole proprietor taking deposits and shipping
  lithium products is personally exposed. The corporation is the manufacturer of record, the
  trademark owner, the seller and the warranty provider.
- Two accounts: reservation money, untouched; operating money, everything else.
- Nothing offered to anyone is an investment. No revenue share for contributors, no "fund the
  development" round with a promised return. That keeps securities law out of the project
  entirely; the moment a return is promised, it comes in.

### 6.7 The commons: licences, trademark, contributor terms, liability

- Licences, decided before the first public commit because relicensing later needs every
  contributor's consent:
  hardware under CERN-OHL-S 2.0 (reciprocal, designed for hardware) or CC BY-SA 4.0 (the Mutable
  choice, familiar to this market); firmware core under GPL-3; plugin API and SDK under MIT or
  Apache-2.0 so plugin authors choose their own terms; documentation under CC BY-SA 4.0. Source:
  [CERN OHL](https://ospo.docs.cern.ch/recommendations/licensing/).
- Trademark: register "Arbutus Audio" and "Arbutus-1" with CIPO, and check conflicts first since
  Arbutus is a common name in BC. The designs are free; the name is not. Derivatives must not use
  it. This is the Mutable, Arduino and Prusa model and it is the only protection against a clone
  carrying the name.
- Contributor terms: DCO sign-off; contributors keep copyright; credit; no compensation; a
  contributing guide that says so in its first sentence.
- Liability: a disclaimer in the WikiHouse shape (no liability for use of the files, except where
  law forbids the exclusion), localised by the lawyer, plus a plain statement that the files are
  not a certified product.
- Privacy: the mailing list and order records fall under BC's Personal Information Protection Act.
  Say what is collected, why, and where it is stored.

### 6.8 What does not apply

No real estate marketing law, no securities law (while nothing is an investment), and no Kickstarter
terms. The "German precedent" transfers as messaging and structure, not as law.

## 7. Spec: what the presale programme is

MUST is a hard rule; SHOULD is the default unless a reason is logged.

1. The programme MUST publish its stage gates (section 4.2) and MUST NOT open reservations before
   the Stage 1 entry conditions are all met and confirmed in the log.
2. The emulator MUST be publicly released under its licence before reservations open.
3. Every reservation MUST be refundable in full, on request, with no reason required, within 10
   business days, and MUST sit in a separate account that is never spent.
4. The reservation MUST NOT state a fixed price or a fixed ship date. It MAY state a price band,
   a batch number and a ship-date range with a confidence.
5. The batch pre-order MUST have a published goal, deadline, fixed price and ship-date range, MUST
   refund in full if the goal is missed, and MUST charge the balance at ship, not at order.
6. The site MUST show one numbers table (reservations, money held, refunds, unit cost, price,
   ship range) updated on a fixed monthly day, and MUST show a log post on the same day.
7. Every schedule slip MUST get a log entry naming the cause and an edit to the ladder the same day.
8. The programme MUST publish a kill list and a kill criterion before the first deposit.
9. Instagram MUST carry only content already in the log or the commons.
10. The commons MUST carry its licences, trademark notice, contributor guide and disclaimer before
    its first public commit; contributions MUST carry a DCO sign-off.
11. Contributors MUST NOT receive anything that could be read as revenue share, equity or a
    volume-linked discount.
12. No unit MUST ship without EMC certification for its destination market, a UN 38.3 report for
    its cells, product liability insurance, and a written warranty.
13. The battery pack MUST be either a certified pack or protected cells with a proven protection
    circuit, and the decision MUST be logged with the evidence.
14. The programme SHOULD name a second person who can issue refunds if Elvin is unavailable.
15. The programme SHOULD price Crowd Supply against self-hosting for the batch pre-order and log
    the comparison.

## 8. Grilling

Questions a supplier, an insurer, a sceptical maker or a future reservation holder will ask.
A good answer is a log entry. Ordered by how much depends on the answer.

### Existence

1. What is the Model 3 here? Tesla had shipped two cars. What has Arbutus shipped to strangers?
   If the answer is "the emulator, once it is public", when is that?
2. What does "under $500 CAD" rest on? Show the all-in unit cost at 100 units and at 500, with
   certification, printing time, packaging, payment fees and a warranty reserve included. If the
   number is not known, the price on the site is a hope.
3. What does "done" mean for batch 1 firmware? Which pages, which engines, which plugin API
   version, decided by the interaction matrix, not by feel.
4. Who has shipped hardware on this team? Paul has shipped a toy at Mattel scale. Who has shipped
   a lithium-powered consumer electronic device from a small batch, and are they on record?
5. Compute Module 4 or a Pi Zero 2 class part? The answer moves the BOM by about $100, changes
   the certification path and decides whether the firmware performance work is done or starting.

### Safety and product

6. Three bare 21700 cells in clips with a home-designed protection circuit: would an insurer
   write a policy on it today? If not, what changes: a certified pack, protected cells, or a
   sealed pack that contradicts "bolts, not glue"?
7. How many hours does one shell and 52 printed keycaps take on the printers available? Multiply
   by batch size. Is that weeks or months, and who runs the farm?
8. What is the certification budget, which lab, and what happens to the price if the first EMC
   pass fails and the board needs a spin?
9. Which countries in batch 1? Every added market adds a certification mark, a tax question and
   a shipping rule. Canada and US only is a defensible first answer.
10. What is the warranty, who does the repairs, and what is the spare-parts commitment in years?
    "Spare parts sold at fair prices" is a promise with a shelf-space cost.

### Money and trust

11. What is the deposit amount, and why that number? Small enough to refund without pain, large
    enough to mean something. Framework chose US$100 on a US$999 product.
12. What funds the batch? Reservation money funds nothing. If the answer is the batch pre-order,
    what is the goal in units, and what happens if 60 people order and the minimum order
    quantities need 150?
13. Who can issue a refund when Elvin is in an exam or on a co-op placement?
14. What is the kill criterion, in writing, before the first deposit?
15. What happens to reservation holders if the project pauses for a year? Refund all, or hold
    with a notice? Decide before it happens.

### Honesty mechanics

16. What is the first published ship-date range, and what confidence is attached? A single date is
    not honest yet.
17. The site currently promises "no newsletter cadence". Reservation holders need a heartbeat.
    Which promise wins, and how is the change explained?
18. When Instagram growth pressures the message toward hype, what is the written rule, and who
    enforces it?
19. What is the one-sentence promise?

### The commons

20. Why open, precisely? "Trust over value extraction" is a value; the strategic answer is what the
    community can do that one person cannot, and what happens when a large manufacturer clones
    it. Is that outcome acceptable? Mutable's was.
21. What can a contributor usefully contribute before P3 exists? Firmware and plugins, yes. Boards,
    no, until the footprint is frozen. Say which and when.
22. Reciprocal core plus permissive plugin API, or reciprocal everything? The first lets a maker
    sell a closed plugin; the second forbids it. Which community is wanted?
23. What do contributors get, and is "nothing that looks like money" written down before the first
    contribution arrives?
24. Is the name searched and filed? Arbutus is a Vancouver neighbourhood and a common BC business
    name.
25. Where is the line between the open files and the certified product, and what stops a
    reservation holder from believing a community build is the same thing?

### The person

26. What is the smallest batch that is real? A 50-unit run to the mailing list and Tectoria
    contacts is a product. A 500-unit run with worldwide shipping is a company. Which is being
    started?
27. What would make you stop, and would you say so in the log?

## 9. Decisions needed before anything else moves

Not tasks. Decisions.

- Emulator release: public before reservations, under which licence. Recommendation: yes, GPL-3,
  now.
- Licence set for the commons: CERN-OHL-S or CC BY-SA for hardware; GPL-3 core with a permissive
  plugin API. Recommendation: CC BY-SA for hardware (matches the market), GPL-3 core, MIT plugin
  SDK, CC BY-SA docs.
- Battery: certified pack, protected cells, or in-house pack with third-party review.
  Recommendation: protected cells and a proven protection IC for batch 1, revisit later.
- Compute: decided on P3 measurements, not preference.
- Stage 1 trigger: P4 plus a public price band, as specified, or earlier. Recommendation: hold the
  line at P4.
- Batch 1 markets: Canada and US only, or wider. Recommendation: Canada and US.
- Batch pre-order channel: self-hosted or Crowd Supply. Recommendation: price both, decide at
  Stage 2.
- Deposit amount: recommendation $50 CAD, revisited when the price band is real.

## 10. What was not verified

- The current text of BC's Consumer Contracts Regulation after the 2025 amendments, and the exact
  cancellation windows for future performance and distance sales contracts.
- The payment processor's current pre-order and delayed-delivery terms.
- Certification cost ranges; these vary by lab and by whether wireless is present.
- The EU Batteries Regulation in-force date for the replaceable-battery requirement.
- Whether "Arbutus Audio" or "Arbutus-1" conflicts with an existing mark.
- The German project named in the original brief ("Crea construction") did not resolve to a
  specific building; the precedents cited are the documented large-timber co-op projects.
