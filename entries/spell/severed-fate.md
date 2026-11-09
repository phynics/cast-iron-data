+++
id = "ref/spell/severed-fate"
kind = "spell"
title = "Severed Fate"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "severed_fate", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "324"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Witch\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
:::

You curse the target, preventing it from drawing upon the powers of destiny. The target is shaken
and cannot use hero points for the duration of the spell. This effect can be removed by
[dispel magic](ref/spell/dispel-magic), [remove curse](ref/spell/remove-curse), or other similar
effects.
