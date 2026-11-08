+++
id = "ref/spell/possession-greater"
kind = "spell"
title = "Greater Possession"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "possession_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/possession" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Occultist, Spiritualist\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target: one creature
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
:::

### Greater Possession

**Sources:** Occult Adventures pg 181

This spell functions as [possession](ref/spell/possession), but when you possess a host, you enter
the host's body and your physical body vanishes. You are ejected to the closest empty square upon
expiration of the spell or upon the host's death.
