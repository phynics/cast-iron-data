+++
id = "ref/spell/weird"
kind = "spell"
title = "Weird"
aon = "SpellDisplay.aspx?ItemName=Weird"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weird", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/phantasmal-killer" },
]
[[sources]]
publication = "core-rulebook"
page = "369"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "any number of creatures, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will disbelief, then Fortitude partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 9: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will disbelief, then Fortitude partial; see text
Spell resistance: yes
Targets: any number of creatures, no two of which can be more than 30 ft. apart
Subschool: Phantasm
Descriptors: emotion, fear, mind-affecting
:::

This spell functions like [phantasmal killer](ref/spell/phantasmal-killer), except it can affect
more than one creature. Only the affected creatures see the phantasmal creatures attacking them,
though you see the attackers as shadowy shapes.

If a subject's Fortitude save succeeds, it still takes 3d6 points of damage and is stunned for 1
round. The subject also takes 1d4 points of Strength damage.
