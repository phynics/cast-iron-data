+++
id = "ref/arc-brawler/snakebite-striker"
kind = "archetype"
title = "Snakebite Striker"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Snakebite%20Striker"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snakebite_striker", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "88"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "sneak-attack", level = 1 },
  { anchor = "snake-feint", level = 3 },
  { anchor = "opportunist", level = 11 },
]
trades = [
  { replaces = "Martial flexibility", feature = "martial-flexibility", by = ["sneak-attack"] },
  { replaces = "Maneuver training gained at 3rd and 7th levels", feature = "maneuver-training", levels = [3, 7], by = ["snake-feint"] },
  { replaces = "Maneuver training gained at 11th and 19th levels", feature = "maneuver-training", levels = [11, 19], by = ["opportunist"] },
]
+++

With her lightning quickness and guile, a snakebite striker keeps her foes' attention focused on
her, because any one of her feints might be an actual attack. By giving up some of a brawler's
versatility, she increases her damage potential and exposes opponents to deadly and unexpected
strikes.

## Class Skills {#class-skills}

The snakebite striker gains Bluff and Stealth as class skills, but does not gain Intimidate as a
class skill.

## Sneak Attack (Ex) {#sneak-attack}

At 1st level, the snakebite striker can make a [sneak attack](ref/ability/sneak-attack). This is as
the rogue ability of the same name. At 1st level, her sneak attack damage is +1d6. This increases by
1d6 at 6th, 10th, 12th, and 20th levels. If she gets a sneak attack bonus from another source, the
bonuses on damage stack. This ability replaces martial flexibility.

## Snake Feint (Ex) {#snake-feint}

At 3rd level, a snakebite striker who uses a standard action to move can combine that move with a
feint. If she is able to feint as a move action (such as from having the
[Improved Feint](ref/feat/improved-feint) feat), she can combine a move action to move with her
feint. At 11th level, once per round she can declare her square and one adjacent square as the
origin of her attacks until her next turn (allowing her to use one or both squares to determine
whether she or allies are flanking an opponent). At 15th level, she counts an additional adjacent
square for this purpose. This ability replaces maneuver training gained at 3rd and 7th levels.

## Opportunist (Ex) {#opportunist}

At 11th level, once per round the snakebite striker can make an attack of opportunity against an
opponent who has just been struck for damage in melee by another character. This attack counts as an
attack of opportunity for that round. She cannot use this ability more than once per round, even if
she has the [Combat Reflexes](ref/feat/combat-reflexes) feat or a similar ability. At 19th level,
she can use this ability twice per round. This ability replaces the maneuver training gained at 11th
and 19th levels.
