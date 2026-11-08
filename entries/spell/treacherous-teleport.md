+++
id = "ref/spell/treacherous-teleport"
kind = "spell"
title = "Treacherous Teleport"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "treacherous_teleport", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/teleport" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "personal and touch"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Medium, Summoner\
5: Arcanist, Magus, Occultist, Psychic, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: personal and touch
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Target: you and touched objects or other touched willing creatures
Subschool: Teleportation
:::

### Treacherous Teleport

**Sources:** Ultimate Intrigue pg 227

This spell functions as [teleport](ref/spell/teleport) except that you can opt to intentionally
cause any number of the creatures traveling with you to suffer a mishap or arrive in a specific
different location you visualize simultaneously with the original destination, or both.

Attempts to identify treacherous teleport with a skill check incorrectly identify it as teleport.
