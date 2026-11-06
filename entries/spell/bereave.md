+++
id = "ref/spell/bereave"
kind = "spell"
title = "Bereave"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bereave", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a broken chain link)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "all creatures in a 15-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald\
4: Cleric, Oracle, Psychic, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a broken chain link)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: all creatures in a 15-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Temples pg 13

An overwhelming feeling of loss overcomes the targets, and their allies' words sound bleak and
hollow. Regardless of actual allegiances, affected creatures no longer count as allies for other
creatures and always count as enemies for the purposes of abilities, effects, and spells that
differentiate between allies and enemies, such as flanking or spells such as bane or bless. Allies
of an affected creature must succeed at a melee touch attack to affect the subject with touch
spells, and an affected creature cannot voluntarily fail a saving throw even if the effect is
harmless (such as cure light wounds). An affected creature still counts as her own ally and can
target herself with abilities, effects, and spells normally.
