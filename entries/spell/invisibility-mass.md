+++
id = "ref/spell/invisibility-mass"
kind = "spell"
title = "Mass Invisibility"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility" },
]
[[sources]]
publication = "core-rulebook"
page = "302"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (an eyelash encased in gum arabic)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Targets", value = "any number of creatures, no two of which can be more than 180 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Summoner\
6: Mesmerist, Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (an eyelash encased in gum arabic)
Range: long (400 ft. + 40 ft./level)
Targets: any number of creatures, no two of which can be more than 180 ft. apart
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Glamer
Descriptors: glamer
:::

### Mass Invisibility

This spell functions like [invisibility](ref/spell/invisibility), except that the effect moves with
the group and is broken when anyone in the group attacks. Individuals in the group cannot see each
other. The spell is broken for any individual who moves more than 180 feet from the nearest member
of the group. If only two individuals are affected, the one moving away from the other one loses its
invisibility. If both are moving away from each other, they both become visible when the distance
between them exceeds 180 feet.
