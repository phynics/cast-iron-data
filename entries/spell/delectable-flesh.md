+++
id = "ref/spell/delectable-flesh"
kind = "spell"
title = "Delectable Flesh"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delectable_flesh", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "all creatures in a 15-foot-radius burst centered on a single living creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Sorcerer, Witch, Wizard\
7: Druid, Shaman
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Targets: all creatures in a 15-foot-radius burst centered on a single living creature
Subschool: Polymorph
Descriptors: mind-affecting
:::

**Sources:** Ultimate Wilderness pg 19

> _[Ghorans](ref/race/ghoran) have access to the following spell._

Choose a creature within range as the object of hunger. All other creatures within 15 feet of the
target that can see or smell the target's delectable flesh must succeed at a Will save or spiral
into a depraved state from which they gain a single purpose - to consume as much of the target's
delicious flesh as possible. The creature chosen as the target of this spell is not affected by this
depravity.

A depraved creature gains a bite attack, two claw attacks, and the scent ability if it didn't
already have them. It drops any items it was carrying and attacks the target of the spell with these
natural weapons, acting as if it were confused and the target had attacked it first. This effect
lasts for the spell's duration or until the depraved creature can no longer see or smell the object
of its hunger for a full minute. Additionally, a depraved creature can attempt a new saving throw to
end this effect at the end of any turn in which the affected creature makes an attack against the
object of its hunger. If a creature that eats for nourishment succeeds at a save to end the depraved
effect early, it takes a -2 penalty on ability checks, attack rolls,
[concentration](ref/rule/concentration) checks, saving throws, and skill checks whenever it is
within 15 feet of the target.
