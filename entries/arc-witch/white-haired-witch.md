+++
id = "ref/arc-witch/white-haired-witch"
kind = "archetype"
title = "White-Haired Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20White-Haired%20Witch"
source_ids = ["dragon-empires-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "white_haired_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "dragon-empires-primer"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "white-hair", level = 1 },
  { anchor = "constrict", level = 2 },
  { anchor = "trip", level = 4 },
  { anchor = "pull", level = 6 },
  { anchor = "strangle", level = 8 },
  { anchor = "rogue-talents", level = 10 },
]
trades = [
  { replaces = "Hex", feature = "hex", by = ["strangle"] },
  { replaces = "Major hex", feature = "major-hex", by = ["rogue-talents"] },
  { replaces = "grand hex", feature = "grand-hex", by = ["rogue-talents"] },
]
+++

A white-haired witch concentrates her mysterious powers on improving her prowess in melee, using
feats of agility and her prehensile hair to deal extreme damage. Rogue talents and advanced rogue
talents marked with an asterisk (\*) can be found in the _Pathfinder RPG Advanced Player's Guide_.
The white-haired witch is an archetype of the witch class.

## White Hair (Su) {#white-hair}

At 1st level, a white-haired witch gains the ability to use her hair as a weapon. This functions as
a primary [natural attack](ref/umr/natural-attacks) with a reach of 5 feet. The hair deals 1d4
points of damage (1d3 for a Small witch) plus the witch's Intelligence modifier. In addition,
whenever the hair strikes a foe, the witch can attempt to [grapple](ref/rule/grapple) that foe with
her hair as a free action without provoking an attack of opportunity, using her Intelligence
modifier in place of her Strength modifier when making the combat maneuver check. When a
white-haired witch grapples a foe in this way, she does not gain the
[grappled](ref/rule/grapple-conditions) condition.

At 4th level and every four levels thereafter, a white-haired witch's hair adds 5 feet to its reach,
to a maximum of 30 feet at 20th level.

The hair cannot be [sundered](ref/rule/sunder) or attacked as a separate creature. In addition, a
white-haired witch further improves her ability to control her hair as she progresses in level,
gaining the following abilities.

## Constrict (Ex) {#constrict}

At 2nd level, when the white-haired witch's hair successfully grapples an opponent, it can begin
constricting her victim as a free action, dealing damage equal to that of its attack.

## Trip (Ex) {#trip}

At 4th level, a white-haired witch who successfully strikes a foe with her hair can attempt a combat
maneuver check to [trip](ref/rule/trip) the creature as a free action.

## Pull (Ex) {#pull}

At 6th level, a white-haired witch who successfully strikes a foe with her hair can attempt a combat
maneuver check to pull the creature 5 feet closer to her as a free action.

## Strangle (Ex) {#strangle}

At 8th level, when the white-haired witch's hair is grappling with an opponent, that creature is
considered [strangled](ref/umr/strangle), and cannot speak or cast spells with verbal components.

This ability replaces hex.

## Rogue Talents {#rogue-talents}

At 10th level, a white-haired witch learns a rogue talent, using her white-haired witch level in
place of her rogue level. At 12th level and for every two levels thereafter, she gains an additional
rogue talent. A white-haired witch cannot select an individual rogue talent more than once, and can
select from among the following: [assault leader](ref/talent/assault-leader)\*,
[combat trick](ref/talent/combat-trick), [finesse rogue](ref/talent/finesse-rogue),
[major magic](ref/talent/major-magic), [minor magic](ref/talent/minor-magic),
[positioning attack](ref/talent/positioning-attack)\*, [resiliency](ref/talent/resiliency),
[surprise attack](ref/talent/surprise-attack), and [weapon training](ref/talent/weapon-training). At
18th level and 20th level, a white-haired witch can choose from among the following advanced rogue
talents: [another day](ref/talent/another-day)\*, [defensive roll](ref/talent/defensive-roll),
[improved evasion](ref/talent/improved-evasion), [opportunist](ref/talent/opportunist),
[redirect attack](ref/talent/redirect-attack)\*, [slippery mind](ref/talent/slippery-mind), and
[thoughtful reexamining](ref/talent/thoughtful-reexamining)\*. This ability replaces major hex and
grand hex.
