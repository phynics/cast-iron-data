+++
id = "ref/spell/debilitating-speech"
kind = "spell"
title = "Debilitating Speech"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "debilitating_speech", path = "json/spells3.json" },
]
[[sources]]
publication = "disciples-doctrine"
page = "10"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "see below"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "1 or more living creatures/level, no two of which may be more than 30 feet apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Sorcerer, Wizard
Casting time: see below
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: 1 or more living creatures/level, no two of which may be more than 30 feet apart
Descriptors: language-dependant, mind-affecting
:::

By speaking eloquently on the subject of your opponents' ineptitude in combat, past failures,
personal hygiene, or other faults, you sap their will to fight.

This spell can be cast as a standard action or as a full-round action. If cast as a standard action,
it takes effect in 1d4 rounds following the spell's casting. If cast as a full-round action, it
takes effect 1 round after its casting. Enemies with 4 Hit Dice or fewer are panicked, enemies with
5-8 Hit Dice are cowering, and enemies with more than 8 Hit Dice are shaken.
