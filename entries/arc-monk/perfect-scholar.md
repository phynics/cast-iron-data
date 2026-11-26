+++
id = "ref/arc-monk/perfect-scholar"
kind = "archetype"
title = "Perfect Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Perfect%20Scholar"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perfect_scholar", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "lore", level = 3 },
  { anchor = "learn-from-failure", level = 4 },
  { anchor = "eye-of-the-sun-and-moon", level = 17 },
  { anchor = "walk-with-the-master", level = 20 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["lore"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["learn-from-failure"] },
  { replaces = "Tongue of the sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["eye-of-the-sun-and-moon"] },
  { alters = "Perfect self", feature = "perfect-self", by = ["walk-with-the-master"] },
  { alters = "Class skills" },
]
+++

Perfect scholars, often worshipers of Irori, hone their minds and bodies through the accumulation of
knowledge. They study and annotate the holy texts of Irori and other philosophies as well as collect
lore on anatomy, medicine, philosophy, martial arts, and history, among other topics of erudition.

## Class Skills {#class-skills}

A perfect scholar adds Knowledge (all) and Linguistics to his list of class skills, instead of
Intimidate and Perform.

This ability alters the monk's class skills.

## Lore (Ex) {#lore}

At 3rd level, the perfect scholar gains a bonus equal to 1/2 his monk level on Knowledge checks and
can attempt Knowledge checks untrained.

This ability replaces still mind. For the monk from _Pathfinder Unchained_, this ability is gained
at 4th level.

## Learn from Failure (Ex) {#learn-from-failure}

At 4th level, when the perfect scholar misses with an attack roll or fails a
[Research check](ref/rule/research), he gains a +1 insight bonus on his next attack roll or Research
check against the same target attempted in the next 24 hours. An individual target cannot be
affected by this ability more than once in a 24-hour period. At 6th level, and every 2 monk levels
thereafter, this bonus increases by 1.

This ability replaces slow fall. For the monk from _Pathfinder Unchained_, this ability replaces the
ki power gained at 4th level.

## Eye of the Sun and Moon (Ex) {#eye-of-the-sun-and-moon}

At 17th level, a perfect scholar can read all languages and write all languages he has read or
heard.

This ability replaces tongue of the sun and moon. For the monk from _Pathfinder Unchained_, this
ability is gained at 13th level.

## Walk with the Master (Su) {#walk-with-the-master}

At 20th level, the perfect scholar has mastered his spiritual resonance, allowing him to travel as
if using _[etherealness](ref/spell/etherealness)_, _[plane shift](ref/spell/plane-shift)_, or
_[shadow walk](ref/spell/shadow-walk)_ at his monk level by spending only 1 point from his ki pool.
He cannot bring other creatures with him. He is treated as an [outsider](ref/type/outsider) rather
than his original type, although he can be brought back to life as if he were still of his former
type.

This ability alters perfect self.
