+++
id = "ref/arc-cavalier/hussar"
kind = "archetype"
title = "Hussar"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Hussar"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hussar", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "agile-warrior" },
  { anchor = "fast-mount", level = 1 },
  { anchor = "skillful-rider", level = 6 },
  { anchor = "maneuverable-mount", level = 9 },
  { anchor = "sudden-swerve", level = 17 },
]
trades = [
  { replaces = "The cavalier's normal armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { replaces = "Tactician", feature = "tactician", by = ["fast-mount"] },
  { replaces = "banner", feature = "banner", by = ["fast-mount"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["fast-mount"] },
  { replaces = "Bonus feats gained at 6th, 12th, and 18th levels", feature = "bonus-feat", levels = [6, 12, 18], by = ["skillful-rider"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["maneuverable-mount"] },
  { replaces = "Master tactician", feature = "master-tactician", by = ["sudden-swerve"] },
]
+++

Agile and maneuverable cavalry, hussars make up for their relatively light armor with their speed
and cunning. They are known for doggedly pursuing their foes even in tight spaces, across rooftops,
and in other places that mounted cavalry could normally never reach.

## Armor Proficiency {#armor-proficiency}

A hussar is proficient with light armor, but not with medium or heavy armor or with shields.

This replaces the cavalier's normal armor proficiencies.

## Agile Warrior (Ex) {#agile-warrior}

A hussar gains Acrobatics, Escape Artist, Stealth, and Survival as class skills.

This alters the cavalier's class skills.

## Fast Mount (Ex) {#fast-mount}

A hussar is able to spur on any mount that he rides to faster speeds than other riders. The base
speed of any creature that the hussar is riding increases by 10 feet. This applies to all forms of
movement that the mount possesses. At 5th level and every 5 cavalier levels thereafter, this bonus
increases by an additional 5 feet (to a maximum increase of 30 feet at 20th level).

This ability replaces tactician, banner, and greater banner.

## Skillful Rider (Ex) {#skillful-rider}

At 6th level, a hussar and his mount work in tandem to achieve amazing accomplishments of dexterity
while riding. As long as the hussar is mounted, whenever he or his mount is required to attempt an
Acrobatics, Climb, Escape Artist, Fly, Stealth, or Swim check, he can use his own modifier or his
mount's, whichever is higher. Additionally, regardless of whose bonus is used, the hussar gains an
additional +2 bonus on all skill checks to overcome obstacles as part of a chase. At 12th level,
this bonus increases to +4, and at 18th level, it increases to +6.

This ability replaces the bonus feats gained at 6th, 12th, and 18th levels.

## Maneuverable Mount (Ex) {#maneuverable-mount}

At 9th level, a hussar is able to maneuver his mount with exceptional grace and poise, even in areas
that would normally be a difficult fit for such a creature. Any creature that the hussar is riding
can [squeeze](ref/misc/squeezing) into a space that is at least half as wide as its normal space
without taking the normal penalties on attack rolls and AC for doing so, though it still moves at
half speed. If the mount attempts to squeeze into a space less than half its space's width, it must
use the Escape Artist skill to do so, and takes the normal penalties.

This ability replaces greater tactician.

## Sudden Swerve (Ex) {#sudden-swerve}

At 17th level, a hussar's control over his mount is advanced enough to allow the mount to turn on
the spot, even when charging forward at full speed. Whenever the hussar makes the
[charge](ref/rule/charge) or [run](ref/rule/run) action while mounted, he can make a single turn of
up to 90 degrees at any one point during this movement.

This ability replaces master tactician.
