+++
id = "ref/spell/animate-dead-lesser"
kind = "spell"
title = "Lesser Animate Dead"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_dead_lesser", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/animate-dead" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)"
range = "touch"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)
Range: touch
Target: one corpse
Duration: instantaneous
Saving throw: none
Spell resistance: no
Descriptors: evil
:::

### Mythic Animate Dead

**Sources:** Mythic Adventures pg 84

Add your tier to your caster level when determining how many Hit Dice of undead you can animate with
a single casting of this spell. This doesn't increase the total number of Hit Dice worth of undead
you can control. By expending a second use of mythic power, you can ignore the spell's material
component cost.

_Augmented (6th):_ If you expend two uses of mythic power, any skeletons or zombies you create gain
either the [agile or savage mythic template](ref/rule/mythic-simple-templates). This template lasts
for a number of days equal to your tier.

Alternatively, if you're 8th tier and expend 10 uses of mythic power, any skeletons you create
permanently gain the [mythic skeleton](ref/template/mythic-skeleton) template.

### Lesser Animate Dead

**Sources:** Ultimate Magic pg 205

This spell functions as [animate dead](ref/spell/animate-dead), except you can only create a single
Small or Medium skeleton or zombie. You cannot create variant skeletons or zombies with this spell.
