+++
id = "ref/spell/animate-dead-lesser"
kind = "spell"
title = "Lesser Animate Dead"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_dead_lesser", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)"
range = "touch"
effects = [
  { label = "Targets", value = "one or more corpses touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Adept, Antipaladin, Cleric, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Targets: one or more corpses touched
Descriptors: evil
:::

## Animate Dead

**Sources:** PRPG Core Rulebook pg 241

This spell turns corpses into undead [skeletons](ref/template/skeleton) or
[zombies](ref/template/zombie) that obey your spoken commands.

The undead can be made to follow you, or they can be made to remain in an area and attack any
creature (or just a specific kind of creature) entering the place. They remain animated until they
are destroyed. A destroyed skeleton or zombie can't be animated again.

Regardless of the type of undead you create with this spell, you can't create more HD of undead than
twice your caster level with a single casting of animate dead. The desecrate spell doubles this
limit.

The undead you create remain under your control indefinitely. No matter how many times you use this
spell, however, you can control only 4 HD worth of undead creatures per caster level. If you exceed
this number, all the newly created creatures fall under your control, and any excess undead from
previous castings become uncontrolled. You choose which creatures are released. Undead you control
through the Command Undead feat do not count toward this limit.

> _Skeletons:_ A skeleton can be created only from a mostly intact corpse or skeleton. The corpse
> must have bones. If a skeleton is made from a corpse, the flesh falls off the bones.
>
> _Zombies:_ A zombie can be created only from a mostly intact corpse. The corpse must be that of a
> creature with a physical anatomy.

Other publications have added more creatures that can be created by this spell. They include:

- [Beheaded](ref/monster/beheaded)
- [Exoskeleton](ref/template/exoskeleton)
- [Frostfallen Creature](ref/template/frostfallen-creature)
- [Isitoq](ref/monster/isitoq)
- [Necrocraft](ref/monster/necrocraft)
- [Sunbaked Zombie](ref/template/sunbaked-zombie)

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

This spell functions as animate dead, except you can only create a single Small or Medium skeleton
or zombie. You cannot create variant skeletons or zombies with this spell.
