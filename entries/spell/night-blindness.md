+++
id = "ref/spell/night-blindness"
kind = "spell"
title = "Night Blindness"
source_ids = ["black-markets", "dark-markets-a-guide-to-katapesh"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "night_blindness", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Arcanist, Bloodrager, Bard, Skald, Sorcerer, Witch, Wizard\
2: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 1 day/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no
Target: one living creature
Descriptors: curse
:::

**Sources:** Black Markets pg 19, Dark Markets - A Guide to Katapesh pg 57

Your target's vision becomes impaired as if the light level were one step lower, treating bright
light as normal light, normal light as dim light, and dim light as darkness. In addition, the
subject gains no benefit from [darkvision](ref/rule/darkvision),
[low-light vision](ref/rule/low-light-vision), or the see in darkness ability. The subject gains a
+4 bonus on saving throws to resist the blind or dazzled condition caused by bright light (such as
flare). Remove blindness/deafness dispels [night blindness](ref/spell/night-blindness).
