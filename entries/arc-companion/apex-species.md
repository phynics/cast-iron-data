+++
id = "ref/arc-companion/apex-species"
kind = "archetype"
title = "Apex Species"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "apex_species", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "wilderness-origins"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "native-environment" },
  { anchor = "favored-terrain", level = 3 },
  { anchor = "natural-selection", level = 6 },
  { anchor = "master-of-the-wild", level = 9 },
]
trades = [
  { replaces = "Share Spells", by = ["native-environment"] },
  { replaces = "Evasion", by = ["favored-terrain"] },
  { replaces = "Devotion", by = ["natural-selection"] },
  { replaces = "Improved Evasion", by = ["natural-selection"] },
  { replaces = "Multiattack", by = ["master-of-the-wild"] },
]
+++

Some animals have no serious competitors and no real predators. They are masters of their habitats,
perfectly evolved to take advantage of their native terrain. They need not be predators, of
course—some herbivores are just as lethally suited to their homes.

## Native Environment (Ex) {#native-environment}

An apex species selects a specific terrain type from the ranger list of
[favored terrains](ref/ability/favored-terrain). While in that terrain, the apex species gains a
bonus equal to [half](ref/misc/fractions-and-rounding) its level on checks and saves to deal with
environmental hazards. An apex species may not select a plane as its native environment.

This replaces share spells.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, the apex species gains the ranger's [favored terrain](ref/ability/favored-terrain)
ability for the terrain that matches its native environment, except that the bonus is +1 instead of
the ranger's +2. The bonus improves by 1 at 8th, 13th, and 18th levels, but the animal companion
does not gain additional favored terrains.

This replaces evasion.

## Natural Selection (Ex) {#natural-selection}

At 6th level, the apex species gains an ability based on their favored terrain, as follows:

_Cold:_ The apex species gains cold resistance 5, increasing to 15 at 15th level.

_Desert:_ The apex species gains fire resistance 5, increasing to 15 at 15th level.

_Forest, Jungle:_ The apex species gains a +1 dodge bonus to CMD, increasing to +3 at 15th level.

_Mountains, Plains:_ The apex species gains electricity resistance 5, increasing to 15 at 15th
level.

_Water, Underground:_ The apex species gains acid resistance 5, increasing to 15 at 15th level.

_Swamp, Urban:_ The apex species gains a +4 racial bonus on saves against disease and poison. At
15th level, the apex species becomes immune to disease and poison.

This replaces devotion and improved evasion.

## Master of the Wild (Ex) {#master-of-the-wild}

At 9th level, the apex species gains an ability based on its favored terrain, as follows.

_Cold:_ The apex species can see through weather conditions (including blizzards, rain, fog, and
mist) without penalty, ignoring any cover or concealment from such effects. If the effect is created
by magic, the apex species instead triples the distance it can see without penalty.

_Desert:_ The apex species gains a +4 morale bonus on Will saves against illusion spells and
effects.

_Forest, Urban:_ The apex species gains [Skill Focus](ref/feat/skill-focus) (Stealth) as a bonus
feat.

_Jungle, Mountains:_ The apex species gains a climb speed equal to half its base land speed, or
increases its existing climb speed by 10 feet.

_Plains:_ The apex species increases its base land speed by 10 feet.

_Swamp, Water:_ The apex species gains a swim speed equal to half its base land speed, or increases
its existing swim speed by 10 feet.

_Underground:_ The apex species gains a burrow speed equal to half its base land speed, or increases
its existing burrow speed by 10 feet.

This replaces multiattack.
