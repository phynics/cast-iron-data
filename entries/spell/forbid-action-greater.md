+++
id = "ref/spell/forbid-action-greater"
kind = "spell"
title = "Greater Forbid Action"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forbid_action_greater", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/forbid-action" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Mesmerist\
5: Cleric, Inquisitor, Occultist, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

### Greater Forbid Action

**Sources:** Ultimate Magic pg 220

This spell functions as [forbid action](ref/spell/forbid-action), except up to one creature per
level may be affected. Each creature must receive the same forbidden action.
