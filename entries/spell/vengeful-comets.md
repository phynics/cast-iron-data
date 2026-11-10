+++
id = "ref/spell/vengeful-comets"
kind = "spell"
title = "Vengeful Comets"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vengeful_comets", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "62"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "1 comet per 4 levels" },
]
duration = "1 round/level or until completely discharged (see below)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/level or until completely discharged (see below)
Saving throw: none
Spell resistance: yes
Effect: 1 comet per 4 levels
Descriptors: cold
:::

This spell causes a number of miniature comets (up to one per four caster levels) to orbit in the
air above your head. Bits of snow and cold wind drift down from the orbiting comets, granting you a
circumstance bonus equal to the number of comets on all saving throws against fire effects.

The actual use for the comets, though, is to make vengeful strikes against foes who dare to target
you with offensive spells. As an immediate action whenever you are affected by a spell cast by
another creature, you can fire one of your vengeful comets as a bolt of icy retribution (provided
the source of the offensive spell is within range of your vengeful comet, of course). The comet
requires a ranged touch attack to hit. If it hits, a comet deals 1d6 points of bludgeoning damage
and 3d6 points of cold damage to the target, plus an additional amount of cold damage equal to the
level of the spell you are retaliating against. If the spell you're retaliating against had the fire
descriptor, you may opt to fire two comets instead of one.
