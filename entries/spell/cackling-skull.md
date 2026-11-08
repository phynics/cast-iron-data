+++
id = "ref/spell/cackling-skull"
kind = "spell"
title = "Cackling Skull"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cackling_skull", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-mouth" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one skull" },
]
duration = "permanent until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent until discharged
Saving throw: Will negates
Spell resistance: yes
Target: one skull
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Ultimate Magic pg 210

This spell functions as [magic mouth](ref/spell/magic-mouth), except rather than creating an
illusory mouth on any surface, it affects a skull. In addition, when the skull's magic is triggered,
it releases wild and unnerving cackles before speaking its message. All creatures that can hear the
cackles must save or become shaken for 1d4 rounds.
