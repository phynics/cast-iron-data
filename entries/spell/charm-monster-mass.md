+++
id = "ref/spell/charm-monster-mass"
kind = "spell"
title = "Mass Charm Monster"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_monster_mass", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/charm-monster" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "One or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Mesmerist, Occultist, Skald, Summoner\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Targets: One or more creatures, no two of which can be more than 30 ft. apart
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Charm
Descriptors: mind-affecting
:::

## Charm Monster

**Sources:** PRPG Core Rulebook pg 254

This spell functions like charm person, except that the effect is not restricted by creature type or
size.

### Mass Charm Monster

**Sources:** PRPG Core Rulebook pg 254

This spell functions like [charm monster](ref/spell/charm-monster), except that mass charm monster
affects a number of creatures whose combined HD do not exceed twice your level, or at least one
creature regardless of HD. If there are more potential targets than you can affect, you choose them
one at a time until you must choose a creature with too many HD to affect.
