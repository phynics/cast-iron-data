+++
id = "ref/arc-barbarian/jungle-rager"
kind = "archetype"
title = "Jungle Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Jungle%20Rager"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jungle_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "inner-sea-combat"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "home-ground-advantage", level = 2 },
  { anchor = "jungle-endurance", level = 3 },
  { anchor = "home-ground-supremacy", level = 5 },
  { anchor = "damage-reduction", level = 8 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["home-ground-advantage"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["jungle-endurance"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["home-ground-supremacy"] },
  { alters = "Damage reduction", feature = "damage-reduction", by = ["damage-reduction"] },
]
+++

More "civilized" folk sometimes scoff at the people of the Mwangi Expanse, dismissing them as
primitives with inferior technology. Although some tribes do rely on wood and bone over metal, their
greatest advantage comes from mastery of the terrain. A jungle rager can disappear from sight,
strike from hiding, and use the environment to shield herself from harm.

## Home Ground Advantage (Ex) {#home-ground-advantage}

At 2nd level, a jungle rager learns how to make optimal use of the natural [cover](ref/rule/cover)
of her homeland. She chooses a specific terrain type from the ranger list of
[favored terrains](ref/ability/favored-terrain). When in this terrain, she increases her bonus to AC
and on Reflex saving throws gained from cover, partial cover, and improved cover (but not soft
cover) by 1. In this terrain, she also increases the miss chance caused by
[concealment](ref/rule/concealment) for attacks against her by 5%. This ability replaces uncanny
dodge.

## Jungle Endurance (Ex) {#jungle-endurance}

At 3rd level, a jungle rager gains a +1 bonus on Fortitude saves to resist the effects of
[hot weather](ref/rule/heat-dangers) and diseases. This bonus increases by +1 every 3 barbarian
levels after 3rd. This ability replaces trap sense.

## Home Ground Supremacy (Ex) {#home-ground-supremacy}

At 5th level, a jungle rager becomes even more capable when navigating and fighting in her preferred
terrain. She gains the [woodland stride](ref/ability/woodland-stride) ranger ability, though this
ability works only in the terrain she selected for the home ground advantage ability. In this
terrain, she gains an additional +1 bonus to AC when benefiting from cover or improved cover (but
not soft cover). This ability replaces improved uncanny dodge.

## Damage Reduction (Ex) {#damage-reduction}

A jungle rager gains this ability at 8th level, except her effective barbarian level for the ability
is equal to her barbarian level - 1. In addition, this [damage reduction](ref/rule/damage-reduction)
is doubled against damage dealt by creatures with the swarm subtype. This ability otherwise
functions as the barbarian ability of the same name.

## Rage Powers {#rage-powers}

The following rage powers complement the jungle rager archetype:
[animal fury](ref/ragepower/animal-fury), [bestial climber](ref/ragepower/bestial-climber),
[hive totem](ref/ragepower/hive-totem), [internal fortitude](ref/ragepower/internal-fortitude),
[low-light vision](ref/ragepower/low-light-vision), [night vision](ref/ragepower/night-vision),
[raging climber](ref/ragepower/raging-climber), [scent](ref/ragepower/scent),
[sharpened accuracy](ref/ragepower/sharpened-accuracy), and
[surprise accuracy](ref/ragepower/surprise-accuracy).
