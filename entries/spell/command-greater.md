+++
id = "ref/spell/command-greater"
kind = "spell"
title = "Greater Command"
aon = "SpellDisplay.aspx?ItemName=Command%2C%20Greater"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "command_greater", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/command" },
]
[[sources]]
publication = "core-rulebook"
page = "257"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Medium", level = 4 },
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
Level: 4: Medium, Mesmerist\
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

### Greater Command

This spell functions like [command](ref/spell/command), except that up to one creature per level may
be affected, and the activities continue beyond 1 round. At the start of each commanded creature's
action after the first, it gets another Will save to attempt to break free from the spell. Each
creature must receive the same command.
