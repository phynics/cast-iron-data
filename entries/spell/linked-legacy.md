+++
id = "ref/spell/linked-legacy"
kind = "spell"
title = "Linked Legacy"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "linked_legacy", path = "json/spells6.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "9"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "two willing creatures plus another creature per 6 levels, no two of which can be more than 30 feet apart" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: yes
Targets: two willing creatures plus another creature per 6 levels, no two of which can be more than 30 feet apart
:::

This spell helps build community and ensure a shared vision for the future. When any of the affected
creatures succeeds at a Knowledge check to answer a question within its field of study or identify a
monster and its special powers or vulnerabilities, as a free action the affected creature can share
any information gained automatically with all targets of the spell. If any of the targets move out
of the spell's range, the spell ceases to function for all of them until they are all within close
range of you again.
