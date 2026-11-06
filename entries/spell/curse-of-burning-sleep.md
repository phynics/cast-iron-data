+++
id = "ref/spell/curse-of-burning-sleep"
kind = "spell"
title = "Curse of Burning Sleep"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_burning_sleep", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse", "fire"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a feather and a drop of oil)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent until triggered (see text)"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Psychic, Red Mantis Assassin, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a feather and a drop of oil)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent until triggered (see text)
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
Descriptors: curse, fire
:::

**Sources:** Advanced Class Guide pg 179

You place a curse upon the target that triggers 1 hour after the next time it falls asleep. When the
curse is triggered, the creature bursts into flame, taking 1d6 points of fire damage per 2 caster
levels (maximum 8d6). Furthermore, it catches on fire, taking 2d6 points of fire damage per round at
the end of its turn each round until the creature dies or is quenched as normal. If the target is
still asleep, the fire damage from this spell wakes it.

Only one of these spells can be in place on a creature at any time. This has no effect on creatures
that don't sleep.
