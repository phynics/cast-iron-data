+++
id = "ref/spell/vestment-of-the-champion"
kind = "spell"
title = "Vestment of the Champion"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vestment_of_the_champion", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Paladin", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "armor or shield touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Antipaladin, Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: armor or shield touched
:::

**Sources:** Ultimate Magic pg 247

This functions as [magic vestment](ref/spell/magic-vestment), except it only affects armor or a
shield you are wearing or carrying. If the armor or shield is worn or carried by anyone other than
you, the spell has no effect, but resumes its effect when you are wearing or carrying it again.
