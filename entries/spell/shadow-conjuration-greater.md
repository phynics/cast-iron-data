+++
id = "ref/spell/shadow-conjuration-greater"
kind = "spell"
title = "Greater Shadow Conjuration"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_conjuration_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shadow-conjuration" },
]
[[sources]]
publication = "core-rulebook"
page = "340"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief (if interacted with); varies; see text"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Effect: see text
Duration: see text
Saving throw: Will disbelief (if interacted with); varies; see text
Spell resistance: yes; see text
Subschool: Shadow
Descriptors: shadow
:::

### Greater Shadow Conjuration

This spell functions like [shadow conjuration](ref/spell/shadow-conjuration), except that it
duplicates any sorcerer or wizard conjuration (summoning) or conjuration (creation) spell of 6th
level or lower. The illusory conjurations created deal three-fifths (60%) damage to nonbelievers,
and non-damaging effects are 60% likely to work against nonbelievers.
