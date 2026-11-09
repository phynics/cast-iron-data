+++
id = "ref/spell/vexing-miscalculation"
kind = "spell"
title = "Vexing Miscalculation"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vexing_miscalculation", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "245"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level or until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level or until discharged
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You frustrate an opponent with ill fortune that leads even its most accurate attacks astray. The
target is unable to score critical threats for the duration of this spell, even if the result of its
roll would normally be a critical threat. If the creature rolls a natural 20, the attack still hits
regardless of its opponent's AC, but the hit is not eligible for a critical confirmation roll. Once
a critical threat has been foiled by vexing miscalculation, the spell is discharged.
