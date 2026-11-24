+++
id = "ref/arc-ranger/dusk-stalker"
kind = "archetype"
title = "Dusk Stalker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Dusk%20Stalker"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dusk_stalker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "110"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "shadow-guide" },
  { anchor = "shadow-bond", level = 4 },
  { anchor = "dark-sight", level = 12 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["shadow-bond"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["dark-sight"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["shadow-guide"] },
]
+++

Hunters and guides through the Shadow Plane, dusk stalkers are rangers that thrive in shadow. Adept
at hunting in dusk, darkness, and twilight, these rangers excel at manipulating shadows.

## Class Skills {#class-skills}

The dusk stalker adds Knowledge (planes) to his list of class skills and removes Knowledge (nature)
from his list of class skills.

## Shadow Guide {#shadow-guide}

When a dusk stalker gains the favored terrain ability, that ability is modified in the following
ways. At 3rd level, a dusk stalker picks his primary terrain normally, but only gains a +1 bonus on
those checks while on a plane other than the Shadow Plane, and gains a +3 bonus on those checks
while on the Shadow Plane. Each time he chooses to add a bonus in a favored terrain, he gains a +1
bonus on those checks while on a plane other than the Shadow Plane, and gains a +3 bonus on those
checks while on the Shadow Plane. This ability modifies favored terrain.

## Shadow Bond (Su) {#shadow-bond}

At 4th level, a dusk stalker creates a mystical bond with shadows. The shadows around a dusk stalker
weave and swirl, confusing his enemies. When a dusk stalker is fighting in
[dim light](ref/rule/vision-and-light) or darkness (magical or otherwise), he gains a +4 insight
bonus on Acrobatics checks made to move through an enemy's threatened area or through its space.
Furthermore, a number of times per day equal to his Wisdom modifier, the dusk stalker can manipulate
shadows in a 5-foot square within 30 feet. That square must be in an area of dim light or darkness
(magical or otherwise). Enemies with an Intelligence score within or adjacent to that 5-foot square
take a -2 penalty to AC and on Reflex saving throws. The harassing shadows last for 1 round. This is
a mind-affecting fear effect. This ability replaces hunter's bond.

## Dark Sight (Su) {#dark-sight}

At 12th level, a dusk stalker gains the [see in darkness](ref/umr/see-in-darkness) ability. This
ability replaces camouflage.
