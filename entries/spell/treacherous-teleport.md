+++
id = "ref/spell/treacherous-teleport"
kind = "spell"
title = "Treacherous Teleport"
aon = "SpellDisplay.aspx?ItemName=Treacherous%20Teleport"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "treacherous_teleport", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/teleport" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "227"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
descriptors = ["ruse"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
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
Level: 6: Arcanist, Magus, Occultist, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: personal and touch
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Target: you and touched objects or other touched willing creatures
Subschool: teleportation
Descriptors: ruse
:::

### Treacherous Teleport

This spell functions as [teleport](ref/spell/teleport) except that you can opt to intentionally
cause any number of the creatures traveling with you to suffer a mishap or arrive in a specific
different location you visualize simultaneously with the original destination, or both.

Attempts to identify treacherous teleport with a skill check incorrectly identify it as teleport.
