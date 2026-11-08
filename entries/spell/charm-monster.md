+++
id = "ref/spell/charm-monster"
kind = "spell"
title = "Charm Monster"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_monster", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald, Summoner\
4: Arcanist, Occultist, Psychic, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Charm
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 254

This spell functions like charm person, except that the effect is not restricted by creature type or
size.
