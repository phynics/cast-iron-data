+++
id = "ref/spell/forced-repentance"
kind = "spell"
title = "Forced Repentance"
aon = "SpellDisplay.aspx?ItemName=Forced%20Repentance"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forced_repentance", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "224"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 4 },
  { class = "Paladin", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one evil creature without the evil subtype" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Inquisitor, Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one evil creature without the evil subtype
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You force an evil creature that does not have the evil subtype to momentarily reflect on its past
actions and be overcome by grief and conscience. The target immediately drops prone and begins to
loudly confess all of its sins and transgressions to the caster for the duration of the spell. The
spell immediately ends if you move out of line of sight or if the target is attacked.
