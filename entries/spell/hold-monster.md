+++
id = "ref/spell/hold-monster"
kind = "spell"
title = "Hold Monster"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_monster", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Inquisitor, Medium, Mesmerist, Occultist, Skald, Summoner\
5: Arcanist, Psychic, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (one hard metal bar or rod, which can be as small as a three-penny nail)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 296

This spell functions like hold person, except that it affects any living creature that fails its
Will save.

### Mass Hold Monster

**Sources:** PRPG Core Rulebook pg 296

This spell functions like hold person, except that it affects multiple creatures and holds any
living creature that fails its Will save.
