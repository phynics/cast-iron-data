+++
id = "ref/spell/conjure-deadfall"
kind = "spell"
title = "Conjure Deadfall"
aon = "SpellDisplay.aspx?ItemName=Conjure%20Deadfall"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conjure_deadfall", path = "json/spells12.json" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "30"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (fistful of mithral tacks)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "see text" },
  { label = "Effect", value = "one spiked, falling block" },
]
duration = "instantaneous"
saving_throw = "Reflex negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Sorcerer, Wizard\
5: Magus
Casting time: 1 standard action
Components: V, S, M (fistful of mithral tacks)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Reflex negates (see text)
Spell resistance: yes
Area: see text
Effect: one spiked, falling block
Subschool: Creation
:::

You conjure a large metal cube covered in sharp spikes. If you conjure the block so that it appears
in midair, it immediately plummets downward onto all creatures below it. When you cast this spell,
you select the size of the square area you wish it to affect. If you choose to create a deadfall
over a single 5-foot square, the block deals 1d6 points of bludgeoning damage per caster level
(maximum 15d6) to each creature in the area. A deadfall over a 10-foot square deals 1d6 points of
bludgeoning damage per 2 caster levels (maximum 7d6), a deadfall over a 15-foot square deals 1d6
points of bludgeoning damage per 3 caster levels (maximum 5d6), and so on, to a maximum size of a
25-foot square. Only creatures that are on the outer edge of the area affected by a conjure deadfall
spell can attempt Reflex saves to avoid the effect; creatures whose space does not touch the edge of
the deadfall do not receive a save.

In order to deal damage, the conjured deadfall must start at least 10 feet above the tallest
creature in the area to be affected. A conjured deadfall is as tall as it is wide, and the spell
fails if you attempt to conjure a deadfall in an area already occupied by a creature or object
(including the ceiling). Regardless, a deadfall conjured by this spell disappears as soon as it
deals damage or strikes the ground.
