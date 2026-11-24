+++
id = "ref/arc-ranger/urban-ranger"
kind = "archetype"
title = "Urban Ranger"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Urban%20Ranger"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_ranger", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "130"

[fields]
kind = "archetype"
features = [
  { anchor = "urban-ranger", level = 1 },
  { anchor = "favored-community", level = 3 },
  { anchor = "trapfinding", level = 3 },
  { anchor = "push-through", level = 7 },
  { anchor = "blend-in" },
  { anchor = "invisibility-trick", level = 17 },
]
trades = [
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["favored-community"] },
  { replaces = "Endurance", feature = "endurance", by = ["trapfinding"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["push-through"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["blend-in"] },
  { replaces = "Hide in plain sight", feature = "hide-in-plain-sight", by = ["invisibility-trick"] },
]
+++

For the urban ranger, the streets and sewers of the city are just as dangerous as the barren
wastelands or the deep forests. An urban ranger has the following class features.

**Gained class skills:** dd, kl

**Lost class skills:** ha, kna

## Urban Ranger {#urban-ranger}

At 1st level, an urban ranger adds Disable Device and Knowledge (local) to his list of class skills
and removes Handle Animal and Knowledge (nature) from his list of class skills.

## Favored Community (Ex) {#favored-community}

At 3rd level, the urban ranger forms a bond with a community. While inside the limits of this
community, he gains a +2 bonus on initiative checks and Knowledge (local), Perception, Stealth, and
Survival skill checks. An urban ranger traveling through his favored community leaves no trail and
cannot be tracked (although he may leave a trail if he so desires).

At 8th level, and every five levels thereafter, an urban ranger may select an additional favored
community. In addition, at each such interval, the skill bonus and initiative bonus in any one
favored community (including the one just selected, if so desired) increases by +2.

For the purposes of this ability, a community is any settlement consisting of 100 or more
individuals. The community may be larger than this minimum. Outlying farms, fields, and houses are
not considered part of a community. This ability replaces favored terrain.

## Trapfinding (Ex) {#trapfinding}

At 3rd level, an urban ranger can find and disable traps, as the rogue class feature of the
[same name](ref/ability/trapfinding). This ability replaces endurance.

## Push Through (Ex) {#push-through}

At 7th level, an urban ranger is never slowed by [difficult terrain](ref/rule/terrain-and-obstacles)
in his favored communities. In addition, he can move through the space occupied by local citizens as
if they were allies. This does not apply to creatures intent on harming the ranger. Areas that are
enchanted or magically manipulated to impede motion, however, still affect him. This replaces
woodland stride.

## Blend In (Ex) {#blend-in}

An urban ranger of 12th level or higher can use his Stealth bonus in place of a Disguise skill check
in any of his favored communities. This disguise does not take an action to don. He must make a
check whenever someone attempts to pick him out from the local citizens. If his check is successful,
he blends into the crowd. While not invisible, enemies do not notice his presence and take no
actions against him unless they are taking actions against the local citizens in general. This
replaces camouflage.

## Invisibility Trick (Sp) {#invisibility-trick}

At 17th level, the urban ranger can cast _[greater invisibility](ref/spell/invisibility-greater)_ on
himself as a wizard of his ranger level as a swift action. He can use this spell-like ability a
number of times per day equal to his Wisdom modifier (minimum 1). This ability replaces hide in
plain sight.
