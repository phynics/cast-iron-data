+++
id = "ref/arc-cavalier/qadiran-horselord"
kind = "archetype"
title = "Qadiran Horselord"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Qadiran%20Horselord"
source_ids = ["adventurers-guide", "inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qadiran_horselord", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "adventurers-guide"
page = "12"
[[sources]]
publication = "inner-sea-combat"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "mount", level = 1 },
  { anchor = "desert-wind", level = 1 },
  { anchor = "desert-mastery", level = 3 },
  { anchor = "sand-storm", level = 6 },
  { anchor = "as-one", level = 9 },
  { anchor = "sand-scourge", level = 17 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Tactician", feature = "tactician", by = ["desert-wind"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["desert-mastery"] },
  { replaces = "The bonus feat gained at 6th level", feature = "bonus-feat", levels = [6], by = ["sand-storm"] },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["as-one"] },
  { replaces = "Master tactician", feature = "master-tactician", by = ["sand-scourge"] },
  { alters = "Mount", feature = "mount", by = ["mount"] },
]
+++

The traditions of the Qadiran horselords are now spread throughout Qadira and the lands beyond in
the Inner Sea region, but they originated among the horse-breeders and mounted-combat specialists of
the [Al-Zabriti](ref/rule/aff-deserts); the name "horselord" was applied by outlanders. Qadiran
horselords pride themselves on their mobility and endurance—qualities also found in the breed of
horses they ride. While they don't command the same presence as a host of Lastwall cavalry, Qadiran
horselords can get to a battleground in half the time and on a third of the rations. In battle, they
are skirmishers, ducking in and out of combat with brutal, precise slashes of their scimitars.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A Qadiran horselord is proficient with all simple and martial weapons, with light and medium armor,
and with shields (except tower shields).

This replaces the cavalier's normal weapon and armor proficiencies.

## Mount (Ex) {#mount}

A Qadiran horselord must select a [horse](ref/companion/horse) or [pony](ref/companion/pony) as his
mount. At the GM's discretion, a different mount can be selected.

This ability alters the cavalier mount class feature.

## Desert Wind (Ex) {#desert-wind}

The speed of a Qadiran horselord's mount increases by 5 feet. Its speed increases by an additional 5
feet at 5th level and every 5 cavalier levels thereafter.

This ability replaces tactician.

## Desert Mastery (Ex) {#desert-mastery}

At 3rd level, a Qadiran horselord gains [favored terrain](ref/ability/favored-terrain) (desert) as
per the [ranger](ref/class/ranger) ability of the same name. At 8th level and every 5 levels
thereafter, the granted bonus on initiative and skill checks increases by 2, but the Qadiran
horselord never selects additional favored terrains. Additionally, his mount gains all the benefits
of the favored terrain ability.

This ability replaces cavalier's charge.

## Sand Storm (Ex) {#sand-storm}

At 6th level, a Qadiran horselord gains the benefits of the [Mobility](ref/feat/mobility) feat so
long as he is mounted.

Additionally, he deals double damage while using a one-handed slashing weapon from the back of a
charging mount, as though using a [lance](ref/eq-weapon/lance).

This ability replaces the bonus feat gained at 6th level.

## As One (Ex) {#as-one}

At 9th level, a Qadiran horselord gains the benefits of the [Spring Attack](ref/feat/spring-attack)
feat so long as he is mounted. He uses his mount's movement for this action, and neither he nor his
mount provokes attacks of opportunity from the target. When he makes a single attack with a
one-handed slashing weapon in this way, the attack deals 1d6 additional points of damage. This bonus
damage increases to 3d6 at 17th level. This ability counts as the Spring Attack feat for the purpose
of meeting feat prerequisites, but only while the Qadiran horselord is mounted.

This replaces greater tactician.

## Sand Scourge (Ex) {#sand-scourge}

At 17th level, a Qadiran horselord and his mount can make a tactical rush through enemy ranks as a
full-round action. His mount can move up to twice its normal speed in a straight line. The Qadiran
horselord can make a single attack against each creature he threatens during his mount's movement,
up to his normal number of attacks per round. These attacks use his full base attack bonus and take
a -2 penalty; this is not a charge, and these attacks deal normal damage. The Qadiran horselord
provokes attacks of opportunity during this movement, but his mount does not.

This ability replaces master tactician.
