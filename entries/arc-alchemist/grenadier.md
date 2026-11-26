+++
id = "ref/arc-alchemist/grenadier"
kind = "archetype"
title = "Grenadier (PSFG)"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grenadier", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-weapon-proficiency", level = 1 },
  { anchor = "alchemical-weapon", level = 2 },
  { anchor = "precise-bombs", level = 2 },
  { anchor = "directed-blast", level = 6 },
  { anchor = "staggering-blast", level = 10 },
]
trades = [
  { replaces = "Brew Potion", feature = "brew-potion", by = ["martial-weapon-proficiency"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["alchemical-weapon"] },
  { replaces = "Poison use", feature = "poison-use", by = ["precise-bombs"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["directed-blast"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["staggering-blast"] },
]
+++

Grenadiers train to exercise their talents in the thick of battle, even when not under the influence
of their mutagens. They learn methods of combining weapon attacks with their alchemical magic, and
sacrifice skill with poisons in order to become more adept at using alchemical bombs or using
alchemical items in conjunction with their martial skills. As an unusual side effect of their skill
at handling bombs and alchemical items with increased speed, grenadiers master the ability to drink
potions, elixirs, and mutagens quickly and safely, without exposing themselves to peril while doing
so. A grenadier has the following class features.

## Martial Weapon Proficiency {#martial-weapon-proficiency}

At 1st level, a grenadier picks one martial weapon to become proficient in the use of. This ability
replaces Brew Potion.

## Alchemical Weapon (Su) {#alchemical-weapon}

At 2nd level, a grenadier can infuse a weapon or piece of ammunition with a single harmful
alchemical liquid or powder, such as [alchemist's fire](ref/eq-weapon/alchemists-fire) or
[sneezing powder](ref/eq-weapon/sneezing-powder), as a move action. This action consumes the
alchemical item, but transfers its effect to the weapon in question.

The alchemical item takes full effect on the next creature struck by the weapon, but does not
splash, spread, or otherwise affect additional targets. Any extra damage added is treated like bonus
dice of damage, and is not doubled on a critical hit. The alchemical treatment causes no harm to the
weapon treated, and wears off 1 minute after application if no blow is struck. At 6th level, a
grenadier can use her alchemical weapon ability as a swift action. At 15th level, this ability
becomes a free action. This ability replaces poison resistance.

## Precise Bombs (Ex) {#precise-bombs}

At 2nd level, a grenadier gains the [precise bombs](ref/discovery/precise-bombs) alchemist discovery
as a bonus discovery. This ability replaces poison use.

## Directed Blast (Su) {#directed-blast}

At 6th level, a grenadier can detonate a bomb so that it splashes in a 20-foot cone rather than
affecting a radius. The cone starts at the alchemist and extends away from her in the direction she
chooses. The alchemist designates one creature in the squares affected by the cone to be the target
of the bomb and makes her attack roll against that creature; all other squares in the cone take
splash damage. If the alchemist has the [explosive bomb](ref/discovery/explosive-bomb) discovery and
throws an explosive directed blast, the cone of splash damage is 30 feet long instead of 20 feet.
This ability replaces swift poisoning.

## Staggering Blast (Su) {#staggering-blast}

At 10th level, a grenadier's bombs become particularly overwhelming when they explode. Whenever a
grenadier scores a successful critical hit with a bomb, the creature directly struck by that bomb is
[staggered](ref/misc/staggered) for 1d4+1 rounds. A successful Fortitude save (DC equals the bomb's
Reflex save DC to avoid splash damage) reduces the duration to 1 round. The effects of this ability
stack with a [frost bomb's](ref/discovery/frost-bomb) staggering effect, but not with the effects of
the [Staggering Critical](ref/feat/staggering-critical) feat. Additional hits from a staggering
blast add to the effect's overall duration. This ability replaces poison immunity.
