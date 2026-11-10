+++
id = "ref/spell/expel-blood"
kind = "spell"
title = "Expel Blood"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "expel_blood", path = "json/spells4.json" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "13"

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["evil", "water"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 round"
components = "V, S, M (a drop of blood from each of three different creatures)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one Small or larger living creature" },
]
duration = "instantaneous and 1 round/level; see text"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Summoner, Unchained Summoner\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a drop of blood from each of three different creatures)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous and 1 round/level; see text
Saving throw: Fortitude negates
Spell resistance: yes
Target: one Small or larger living creature
Descriptors: evil, water
:::

You animate a portion of the target's blood, causing it to force itself out of the victim's body and
form a corrupted water elemental. The target takes 2d4 points of Constitution damage unless it
succeeds at a Fortitude saving throw. Additionally, if the target fails the saving throw, blood (or
an analogous internal fluid, such as ichor) pours from the target's body and pools in an empty
adjacent square of your choice. The fluids immediately form into a fiendish water elemental of the
same size as the target (but not larger than a Large fiendish water elemental). This fiendish water
elemental does not have the vortex ability, but it has the blood drain special attack, which deals
1d3 points of Constitution damage at the end of the water elemental's turn if it grapples a foe. The
elemental gains [Improved Grapple](ref/feat/improved-grapple) as a bonus feat. You have no control
over the fiendish water elemental once it is summoned, though the water elemental does not attack
you under any circumstances.

This spell does not affect creatures that are Small or smaller or those that don't have blood or
some analogous internal fluid.
