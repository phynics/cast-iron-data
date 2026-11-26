+++
id = "ref/arc-summoner/counter-summoner"
kind = "archetype"
title = "Counter-Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Counter-Summoner"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "counter_summoner", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "counter-summon", level = 1 },
  { anchor = "detect-summons", level = 2 },
  { anchor = "weaken-summons", level = 10 },
  { anchor = "improved-weaken-summons", level = 18 },
]
trades = [
  { replaces = "Summon monster", feature = "summon-monster-i", by = ["counter-summon"] },
  { replaces = "Bond senses", feature = "bond-senses", by = ["detect-summons"] },
  { replaces = "Aspect", feature = "aspect", by = ["weaken-summons"] },
  { replaces = "Greater aspect", feature = "greater-aspect", by = ["improved-weaken-summons"] },
]
+++

While most summoners excel at conjuring monsters, there are those who focus instead on disrupting
the conjurations of opponents. The counter-summoner harnesses powerful abjuration magic to instantly
thwart the conjuration and summoning abilities of other casters, though at the cost of weakening his
own powers of conjuration.

## Counter-Summon (Su) {#counter-summon}

At 1st level, a counter-summoner can attempt to counter a conjuration spell cast by another
creature. He must identify the spell being cast as normal for
[counterspelling](ref/rule/counterspells). If he does so, he can attempt to counter the spell as a
swift or immediate action. To counter the spell, the counter-summoner must attempt a dispel check as
if using _[dispel magic](ref/spell/dispel-magic)_. If the spell being countered is a
_[summon monster](ref/spell/summon-monster)_ or
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell, the counter-summoner gains a +5 bonus
on the dispel check. The counter-summoner can use this ability a number of times per day equal to
3 + his Charisma modifier. This replaces _summon monster_.

## Detect Summons (Su) {#detect-summons}

At 2nd level, as a swift action, a counter-summoner can target a single creature he can see and
determine if it has been summoned to its current plane from another. This ability reveals whether
the target has been conjured by a conjuration (summoning) or (calling) spell, and allows the
counter-summoner to attempt a Spellcraft check to identify the spell that conjured it (using the
same DC as if the counter-summoner had witnessed the spell being cast). This ability replaces bond
senses.

## Weaken Summons (Su) {#weaken-summons}

At 10th level, as a standard action, a counter-summoner can attempt to weaken a summoned or called
creature within 60 feet. The targeted creature takes a -2 penalty on attack and damage rolls and to
Armor Class for 1 minute per summoner level. A successful Will save (DC = 10 + 1/2 the
counter-summoner's class level + his Charisma modifier) negates this effect. A given summoned
creature can't be targeted by this ability more than once per 24-hour period. This ability replaces
aspect.

## Improved Weaken Summons (Su) {#improved-weaken-summons}

At 18th level, the penalty for the counter-summoner's weaken summons ability changes to -4. This
ability replaces greater aspect.
