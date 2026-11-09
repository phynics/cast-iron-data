+++
id = "ref/spell/lighten-object-mass"
kind = "spell"
title = "Mass Lighten Object"
source_ids = ["inner-sea-gods", "faiths-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lighten_object_mass", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/lighten-object" },
]
[[sources]]
publication = "inner-sea-gods"
page = "236"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, M (goose down)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "multiple objects totaling up to 1 cubic ft./level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Cleric, Magus, Oracle, Sorcerer, Summoner, Unchained Summoner, Warpriest
Casting time: 1 standard action
Components: V, M (goose down)
Range: close (25 ft. + 5 ft./2 levels)
Target: multiple objects totaling up to 1 cubic ft./level, no two of which can be more than 30 ft. apart
Duration: 10 minutes/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
:::

### Mass Lighten Object

This spell functions like [lighten object](ref/spell/lighten-object), except that it affects a
number of objects equal to half your caster level.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
