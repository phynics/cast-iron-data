+++
id = "ref/spell/fleshcurdle"
kind = "spell"
title = "Fleshcurdle"
source_ids = ["inner-sea-magic", "mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleshcurdle", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (scrap of pickled flesh)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living or undead creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (scrap of pickled flesh)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living or undead creature
Subschool: Polymorph
:::

**Sources:** Inner Sea Magic pg 55

You warp the target creature's flesh, discoloring it and causing it to become misshapen and
impairing its function. When you cast this spell, you must choose one of three types of effects to
inflict on the target-movement, attacks, or defense.

_Attacks:_ One of the creature's natural attacks takes a -2 penalty on attack and damage rolls, only
scores a critical hit on a natural 20, and only deals ×2 damage on a confirmed critical hit.

_Defense:_ The creature's natural armor bonus decreases by -4, to a minimum bonus of +0.

_Movement:_ One of the creature's movement speeds (chosen by you) is halved.

Most undead are susceptible to fleshcurdle, but amorphous creatures and creatures without flesh are
immune (such as elementals, oozes, plants, gaseous or incorporeal creatures, and skeletons).

### Mythic Fleshcurdle

**Sources:** Mythic Origins pg 12\
You can choose two effects instead of one effect, or may choose to enhance one effect. If you
enhance the attack effect, all of the creature's natural attacks are affected. If you enhance the
defense effect, in addition to fleshcurdle's normal effect on natural armor bonus, any critical
threats against the creature gain a +4 bonus on the confirmation roll. If you enhance the movement
effect, all of the creature's movement speeds are halved.

_Augmented (6th):_ If you expend two uses of mythic power, you can choose two enhanced effects to
inflict upon the target.
