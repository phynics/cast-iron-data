+++
id = "ref/arc-ranger/ilsurian-archer"
kind = "archetype"
title = "Ilsurian Archer"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Ilsurian%20Archer"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ilsurian_archer", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "bullseye-shot", level = 1 },
  { anchor = "archery-style", level = 2 },
  { anchor = "vicious-aim", level = 4 },
  { anchor = "iomedae-s-influence", level = 8 },
  { anchor = "pinpoint-targeting", level = 11 },
  { anchor = "quarry", level = 19 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["bullseye-shot"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["bullseye-shot"] },
  { replaces = "Spellcasting ability", feature = "spells", by = ["vicious-aim"] },
  { replaces = "Swift tracking", feature = "swift-tracker", by = ["iomedae-s-influence"] },
  { replaces = "Quarry", feature = "quarry", by = ["pinpoint-targeting"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["quarry"] },
  { alters = "Combat style", feature = "combat-style-feat", by = ["archery-style"] },
]
+++

Ilsurian archers maintain the strong tradition of archery first developed by soldiers in the service
of Ilsur, who raised a small army with which he intended to overthrow the monarch of Korvosa after
the fall of the Chelish Empire. Though Ilsur's Arena teaches only the basics of these techniques, a
few dedicated students strive toward true mastery in each generation.

## Bullseye Shot (Ex) {#bullseye-shot}

At 1st level, an Ilsurian archer gains the [Bullseye Shot](ref/feat/bullseye-shot) feat as a bonus
feat. He need not meet its prerequisites. This ability replaces track and wild empathy.

## Archery Style (Ex) {#archery-style}

At 2nd level, an Ilsurian archer must select the archery [combat style](ref/ability/combat-styles).
This modifies the ranger's combat style feat class feature.

## Vicious Aim (Ex) {#vicious-aim}

At 4th level, an Ilsurian archer adds half his highest favored enemy bonus to all attack rolls and
damage rolls for attacks made with ranged weapons. This does not stack with his normal favored enemy
bonus when targeting a creature that qualifies as a favored enemy. This ability replaces all
spellcasting, and the Ilsurian ranger is not considered to have a caster level.

## Iomedae's Influence (Ex) {#iomedae-s-influence}

At 8th level, an Ilsurian archer gains [Weapon Focus](ref/feat/weapon-focus) with the longsword as a
bonus feat, due to the influence the church of [Iomedae](ref/faith/iomedae) has over Ilsurian
causes. This ability replaces swift tracking.

## Pinpoint Targeting (Ex) {#pinpoint-targeting}

At 11th level, an Ilsurian ranger gains [Pinpoint Targeting](ref/feat/pinpoint-targeting) as a bonus
feat, even if he does not meet its prerequisites. This replaces quarry.

## Quarry (Ex) {#quarry}

At 19th level, an Ilsurian ranger gains the quarry class feature. This ability replaces improved
quarry.
