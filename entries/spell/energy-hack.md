+++
id = "ref/spell/energy-hack"
kind = "spell"
title = "Energy Hack"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_hack", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-class-origins"
page = "31"

[fields]
kind = "spell"
school = "transmutation [acid, cold, electricity, or fire]"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (see below)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[acid, cold, electricity, or fire\]
Level: 4: Arcanist, Sorcerer, Wizard
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round/level (see below)
Saving throw: none
Spell resistance: no
Target: you
:::

You can cast this spell only when you take 10 or more points of acid, cold, electricity, or fire
damage from a spell or spell-like ability-this spell has the same energy descriptors as the damaging
effect. When you use a spell or [spell-like ability](ref/umr/spell-like-abilities) with the acid,
cold, electricity, or fire descriptor or use an arcanist exploit, arcane school power, bloodline
power, magus arcana, or hex that deals acid, cold, electricity, or fire damage, you can choose to
change the energy type and descriptor to match one of the descriptors of energy hack. Any other
effect of that spell or power remains the same.

If you have the arcane reservoir class feature, if you take another 10 points of acid, cold,
electricity, or fire damage while under the effect of energy hack, as a free action you can expend 1
point from your arcane reservoir to reset the duration of energy hack to 1 round per level and add
the new type of damage you took to the list of energy types you can choose to substitute. You can
expend points in this way multiple times as long as you do so before the duration expires.
