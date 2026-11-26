+++
id = "ref/arc-bard/court-fool"
kind = "archetype"
title = "Court Fool"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Court%20Fool"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "court_fool", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "buffoonery", level = 1 },
  { anchor = "bardic-performance" },
  { anchor = "distracting-motley", level = 1 },
  { anchor = "defuse-tension", level = 3 },
  { anchor = "caper-and-jeer", level = 5 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["buffoonery"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["distracting-motley"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["defuse-tension"] },
  { replaces = "Lore master", feature = "lore-master", by = ["caper-and-jeer"] },
]
+++

Arguably the oldest and most widespread role for a court entertainer is that of the court jester or
fool. This role arose from the need to offset the intense, even deadly, seriousness of court
business. The court fool serves as an outlet for the constant pressure of aristocratic dealings,
relieving tensions through humor. The motley clad acrobat is a good example of this style of court
fool, using physical comedy to generate belly laughs and raise spirits. In other courts, the court
fool might ridicule social conventions with bawdy songs or engage in biting satire, parodying
manners or even mocking individuals to spread good cheer. The court fool holds up an unflattering
mirror to those in charge or speaks truths, however veiled, that no one else can safely utter.

## Buffoonery (Ex) {#buffoonery}

A court fool gains a bonus equal to 1/2 his bard level on Acrobatics, Bluff, Climb, and Disguise
checks (minimum +1).

This replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A court fool gains the following types of bardic performance.

## Distracting Motley (Su) {#distracting-motley}

At 1st level, a court fool can startle his allies back to their senses with erratic capering or by
fluttering multicolored clothing. Each round, he attempts an Acrobatics check. Any ally (including
the court fool) within 30 feet can use this check in place of her own saving throw against confusion
and fascination effects. Those already under a confusion or fascination effect can attempt a new
save each round using the court fool's Acrobatics check. A court fool wearing an
[entertainer's outfit](ref/eq-misc/entertainers-outfit) gains a +2 bonus on these Acrobatics checks.
Distracting motley doesn't work on effects that don't allow saves. This is a mind-affecting effect
that uses visual components.

This performance replaces countersong.

## Defuse Tension (Su) {#defuse-tension}

At 3rd level, a court fool can use a silly performance to comfort a beleaguered ally. That ally must
be within 30 feet and be able to see the court fool. The ally ignores the
[fatigued](ref/misc/fatigued) and [shaken](ref/misc/shaken) conditions (but not more extreme
conditions, such as exhausted or frightened) as long as she continues to see the court fool's
performance. This performance affects one additional creature at 7th level and every 4 bard levels
thereafter. A court fool can't use defuse tension on himself. Defuse tension relies on visual
components.

This performance replaces inspire competence.

## Caper and Jeer (Ex) {#caper-and-jeer}

At 5th level, a court fool can take 10 on Acrobatics and Bluff checks, even when in danger or
distracted, and can use Bluff to create a diversion to hide (as per the [Stealth](ref/skill/stealth)
skill) as a swift action. He can take 20 on an Acrobatics or Bluff check once per day, plus one time
per 6 levels beyond 5th, even when in danger or distracted.

This ability replaces lore master.
