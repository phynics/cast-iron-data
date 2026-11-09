+++
id = "ref/spell/ear-piercing-scream"
kind = "spell"
title = "Ear-Piercing Scream"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ear_piercing_scream", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "218"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous; see text"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Bard, Inquisitor, Medium, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous; see text
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one creature
Descriptors: sonic
:::

You unleash a powerful scream, inaudible to all but a single target. The target is dazed for 1 round
and takes 1d6 points of sonic damage per two caster levels (maximum 5d6). A successful save negates
the daze effect and halves the damage.
