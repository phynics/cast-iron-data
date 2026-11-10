+++
id = "ref/spell/ki-arrow"
kind = "spell"
title = "Ki Arrow"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ki_arrow", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "225"

[fields]
kind = "spell"
school = "conjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "1 arrow touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bard, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: touch
Duration: instantaneous
Saving throw: Fortitude (object)
Spell resistance: yes (object)
Target: 1 arrow touched
:::

You imbue an arrow with your power and throw it at a target up to 100 feet away. Make a ranged
attack roll. If it hits, the target takes damage from the arrow as if you had hit it with a single
unarmed strike (including your Strength bonus).
