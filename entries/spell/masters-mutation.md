+++
id = "ref/spell/masters-mutation"
kind = "spell"
title = "Master's Mutation"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "masters_mutation", path = "json/spells14.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you and one summoned creature you control" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Druid, Hunter, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you and one summoned creature you control
Subschool: Polymorph
:::

You can mold the ephemeral substance of the Outer Planes, mutating one summoned creature that you
control to better suit your needs. Select up to two of the following abilities and grant them to the
target for the spell's duration: burrow 30 feet, climb 40 feet, constrict,
[darkvision](ref/rule/darkvision) 90 feet, ferocity, fly 60 feet (average maneuverability), grab,
jet, [low-light vision](ref/rule/low-light-vision), poison, rake, scent, swim 60 feet, trample,
trip, or water breathing. Additionally, instead of selecting an ability, you can replace one of the
target's primary natural attacks with another natural attack that deals the same amount of damage,
such as replacing a Medium target's bite attack (1d6) with a gore attack (1d6). If you choose to
alter a creature's natural attacks, all attacks of the chosen type are altered. A summoner can
target his eidolon with this spell.
