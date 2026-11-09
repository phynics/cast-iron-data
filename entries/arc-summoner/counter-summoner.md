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
replaces = ["Summon monster", "Bond senses", "Aspect", "Greater aspect"]
+++

While most summoners excel at conjuring monsters, there are those who focus instead on disrupting
the conjurations of opponents. The counter-summoner harnesses powerful abjuration magic to instantly
thwart the conjuration and summoning abilities of other casters, though at the cost of weakening his
own powers of conjuration.

**Counter-Summon (Su)**

**Ability:** A counter-summoner can attempt to counter a conjuration spell cast by another creature.
He must identify the spell being cast as normal for [counterspelling](ref/rule/counterspells). If he
does so, he can attempt to counter the spell as a **swift** or **immediate action**. To counter the
spell, the counter-summoner must attempt a dispel check as if using
[dispel magic](ref/spell/dispel-magic). If the spell being countered is a
[summon monster](ref/spell/summon-monster) or [summon nature's ally](ref/spell/summon-natures-ally)
spell, the counter-summoner gains a +5 bonus on the dispel check.

**Gained:** At 1st Level

**Replaces:** Summon monster

**Usage:** Charisma3 modifier times/day

**Detect Summons (Su)**

**Gained:** At 2nd Level

**Replaces:** Bond senses

**Swift:** A counter-summoner can target a single creature he can see and determine if it has been
summoned to its current plane from another. This ability reveals whether the target has been
conjured by a conjuration (summoning) or (calling) spell, and allows the counter-summoner to attempt
a Spellcraft check to identify the spell that conjured it (using the same DC as if the
counter-summoner had witnessed the spell being cast).

**Weaken Summons (Su)**

**Gained:** At 10th Level

**Replaces:** Aspect

**Standard:** A counter-summoner can attempt to weaken a summoned or called creature within 60 feet.
The targeted creature takes a -2 penalty on attack and damage rolls and to Armor Class for 1 minute
per summoner level. A successful Will save (DC = 10 1/2 the counter-summoner's class level his
Charisma modifier) negates this effect. A given summoned creature can't be targeted by this ability
more than once per 24-hour period.

**Improved Weaken Summons (Su)**

**Ability:** The penalty for the counter-summoner's _weaken summons_ ability changes to -4.

**Gained:** At 18th Level

**Replaces:** Greater aspect
