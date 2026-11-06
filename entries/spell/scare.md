+++
id = "ref/spell/scare"
kind = "spell"
title = "Scare"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scare", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a bone from an undead creature)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one living creature per three levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level or 1 round; see text for cause fear"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a bone from an undead creature)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level or 1 round; see text for cause fear
Saving throw: Will partial
Spell resistance: yes
Targets: one living creature per three levels, no two of which can be more than 30 ft. apart
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 336

This spell functions like cause fear, except that it causes all targeted creatures of less than 6 HD
to become frightened.
