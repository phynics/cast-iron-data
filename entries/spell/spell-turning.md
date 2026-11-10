+++
id = "ref/spell/spell-turning"
kind = "spell"
title = "Spell Turning"
aon = "SpellDisplay.aspx?ItemName=Spell%20Turning"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_turning", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "347"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a small silver mirror)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "until expended or 10 min./level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Summoner\
6: Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a small silver mirror)
Range: personal
Duration: until expended or 10 min./level
Saving throw: none
Spell resistance: no
Target: you
:::

Spells and spell-like effects targeted on you are turned back upon the original caster. The
abjuration turns only spells that have you as a target. Effect and area spells are not affected.
Spell turning also fails to stop touch range spells. From seven to ten (1d4+6) spell levels are
affected by the turning. The exact number is rolled secretly.

When you are targeted by a spell of higher level than the amount of spell turning you have left,
that spell is partially turned. Subtract the amount of spell turning left from the spell level of
the incoming spell, then divide the result by the spell level of the incoming spell to see what
fraction of the effect gets through. For damaging spells, you and the caster each take a fraction of
the damage. For non-damaging spells, each of you has a proportional chance to be the one who is
affected. If you and a spellcasting attacker are both warded by spell turning effects in operation,
a resonating field is created. Roll randomly to determine the result.

|d%|Effect|
| --- | --- |
|01-70|Spell drains away without effect.|
|71-80|Spell affects both of you equally at full effect.|
|81-97|Both turning effects are rendered non-functional for 1d4 minutes.|
|98-100|Both of you go through a rift into another plane.|
