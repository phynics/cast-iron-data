+++
id = "ref/spell/gravity-sphere"
kind = "spell"
title = "Gravity Sphere"
source_ids = ["people-of-the-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravity_sphere", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a marble)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "30-ft.-radius sphere of altered gravity" },
]
duration = "1 round/level (D)"
saving_throw = "none (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Sorcerer, Wizard\
6: Druid, Hunter
Casting time: 1 standard action
Components: V, S, M (a marble)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none (see text)
Spell resistance: no
Effect: 30-ft.-radius sphere of altered gravity
:::

**Sources:** People of the Stars pg 28

You affect the local gravity field in a 30-foot-radius sphere around the spell's designated point of
origin. Creatures in the affected area can be weighed down by high gravity, lightened by low
gravity, or left to float in an area with no gravity, depending on the effect you choose for your
gravity sphere. See below for rules on the effects of high, low, and no gravity.

Creatures that fall within the area of a gravity sphere spell take more damage from the fall if the
gravity within is higher and less damage if the gravity within is lower. However, if the creature
falls through a gravity sphere and continues to fall in a non-affected area, the rest of the fall
damage is calculated normally. For instance, if a creature falls through 20 feet of a lowgravity
sphere and an additional 30 feet outside the sphere, it would take 1d6 points of damage for the 20
feet of low gravity plus 3d6 points of damage as normal for the 30 feet outside the sphere (for a
total of 4d6 points of damage).

This spell doesn't counteract or negate the effects of other spells that affect gravity; both
effects occur simultaneously. For instance, a no-gravity gravity sphere spell cast within the area
of a [reverse gravity](ref/spell/reverse-gravity) spell would simply mean that creatures float about
until the gravity sphere's duration expires or they exit the gravity sphere, at which point they
return to the top of the reverse gravity effect's area. If both gravity-altering magical effects
could not feasibly take place simultaneously (at the GM's discretion), the gravity sphere spell
supersedes the previous effect (if it's higher-level than the previous effect) or simply fails (if
it's lower-level).

**Sources:** People of the Stars pg 18

**Standard Gravity (×1):** The gravity mimics that of Golarion.

**Low Gravity (×1/2):** Characters can jump twice as high and as far and can lift twice as much.
Movement speed is unaffected. Each range increment for ranged weapons is doubled. Creatures that
fall within an area of low gravity take 1d6 points of damage for every 20 feet fallen.

**High Gravity (×2):** Characters can move at no more than half speed, jump no more than half as
high or as far as normal, and lift no more than half as much as normal. Each range increment for
ranged weapons is halved. Creatures that fall within an area of high gravity take 1d6 points of
damage for every 5 feet fallen.

**No Gravity (×0):** Without magical flight, moving in an area with no gravity is difficult. A
character with a surface to push off from can move up to half speed in any direction. A double move
or charge can be performed this way, but not a run. A character can move at his full climb speed or
his full land speed by succeeding at a DC 20 Climb check as long as he remains adjacent to a surface
with sufficient handholds. He adds his Dexterity modifier (minimum 0) on this Climb check in
addition to his Strength modifier. Once a character starts moving, he continues moving at the same
speed in the same direction each round without using an action until he latches onto an object to
stop himself, pushes off in another direction, or creates thrust somehow (each of which requires a
move action). Creatures with nonmagical means of flight lose the ability to fly for 2d6 rounds after
entering a no gravity area. A character in a no gravity environment can lift and carry 10 times his
normal limit. Ranged weapons have no maximum range, and their range increment distances are
multiplied by 10.
