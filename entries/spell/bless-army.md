+++
id = "ref/spell/bless-army"
kind = "spell"
title = "Bless Army"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bless_army", path = "json/spells12.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "29"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "1 hex"
effects = [
  { label = "Target", value = "one army" },
]
duration = "1 battle"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 1 hex
Duration: 1 battle
Saving throw: none
Spell resistance: yes
Target: one army
Subschool: Compulsion
Descriptors: mind-affecting
:::

Bless army fills an army with courage. The army gains a +1 bonus on OM and Morale checks.
