+++
id = "ref/spell/purge-spirit"
kind = "spell"
title = "Purge Spirit"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "purge_spirit", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature or haunt" },
]
duration = "instantaneous"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium, Occultist, Spiritualist\
3: Psychic\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will partial
Spell resistance: yes
Target: one creature or haunt
:::

**Sources:** Occult Adventures pg 184

Purge spirit rips away at the target's spiritual substance, scattering it over a wide area and
hampering the target's ability to reform. The target takes 1d6 points of damage per caster level
(maximum 10d6) and is staggered for 1 round. On a successful saving throw, the target takes half
damage and is not staggered. This spell affects astrally projected creatures, ethereal creatures,
haunts, incorporeal creatures, mediums channeling a spirit, and phantoms, and at the GM's discretion
can affect other spirits or creatures made of ectoplasm. Incorporeal creatures take full damage from
purge spirit.
