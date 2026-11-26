+++
id = "ref/arc-fighter/dragonheir-scion"
kind = "archetype"
title = "Dragonheir Scion"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Dragonheir%20Scion"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragonheir_scion", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "draconic-bloodline", level = 1 },
  { anchor = "eldritch-strikes", level = 1 },
  { anchor = "fearful-might", level = 1 },
  { anchor = "draconic-defenses", level = 3 },
  { anchor = "draconic-strike", level = 3 },
  { anchor = "draconic-presence", level = 5 },
  { anchor = "wings", level = 15 },
  { anchor = "might-of-wyrms", level = 20 },
]
trades = [
  { replaces = "The bonus feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["eldritch-strikes"] },
  { replaces = "Bravery", feature = "bravery", by = ["fearful-might"] },
  { replaces = "Armor training 1, 2, and 3", feature = "armor-training", levels = [3, 7, 11], by = ["draconic-defenses"] },
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["draconic-strike"] },
  { replaces = "Bonus feat gained at 5th level", feature = "bonus-feats", levels = [5], by = ["draconic-presence"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["wings"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["wings"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["might-of-wyrms"] },
  { alters = "Class skills" },
]
+++

Dragonheir scions are the martially inclined humanoid descendants of those influenced by draconic
power. Unlike their sorcerous brethren, dragonheir scions manifest their heritage in ways more
suited to strength of arms and skill with steel than arcane energies. Those who follow this path are
often the children of mighty dragon-blooded sorcerers and others who drew energy from their dragon
blood, though they themselves might not exhibit spellcasting ability.

## Class Skills {#class-skills}

The dragonheir scion adds Knowledge (arcana) and Use Magic Device to her list of class skills,
instead of Handle Animal or Ride.

This alters the fighter's class skills.

## Draconic Bloodline (Su) {#draconic-bloodline}

Each dragonheir scion can draw her lineage back to the influence of a great draconic progenitor. At
1st level, a dragonheir scion must select one of the chromatic or metallic dragon types. Once
chosen, this cannot be changed. A number of dragonheir scion's abilities deal damage and grant
resistances based on her dragon type, as noted below. If a dragonheir scion takes a level in another
class that grants a bloodline, the bloodlines must be of the same type, even if that means that the
bloodline of one of the classes must change. Subject to GM discretion, the dragonheir scion can
change her former bloodline to make them conform.

|Chromatic Dragon Type|Energy Type|
| --- | --- |
|Black|Acid|
|Blue|Electricity|
|Green|Acid|
|Red|Fire|
|White|Cold|

|Metallic Dragon Type|Energy Type|
| --- | --- |
|Brass|Fire|
|Bronze|Electricity|
|Copper|Acid|
|Gold|Fire|
|Silver|Cold|

## Eldritch Strikes (Su) {#eldritch-strikes}

At 1st level, a dragonheir scion gains [Arcane Strike](ref/feat/arcane-strike) as a bonus feat. She
does not need to meet its prerequisites.

This ability replaces the bonus feat gained at 1st level.

## Fearful Might (Ex) {#fearful-might}

At 1st level, a dragonheir scion gains a +1 bonus on Intimidate checks to demoralize a foe. This
bonus increases to +2 at 6th level and by an additional 1 every 4 fighter levels thereafter to a
maximum of +5 at 18th level.

This ability replaces bravery.

## Draconic Defenses (Su) {#draconic-defenses}

At 3rd level, a dragonheir scion gains a +1 natural armor bonus and energy resistance 5 against her
energy type. At 7th level, this increases to a +2 natural armor bonus and energy resistance 10; at
13th level, it increases to a +3 natural armor bonus and energy resistance 20.

This ability replaces armor training 1, 2, and 3.

## Draconic Strike (Su) {#draconic-strike}

At 3rd level, whenever the dragonheir scion damages a target with an attack augmented by Arcane
Strike, the attack deals an additional 1d4 points of damage of the dragonheir scion's energy type.

This ability replaces the bonus feat gained at 3rd level.

## Draconic Presence (Su) {#draconic-presence}

At 5th level, the dragonheir scion receives [Dazzling Display](ref/feat/dazzling-display) as a bonus
feat. She does not need a weapon in hand to use this ability, and can use it as a standard action.

This ability replaces the bonus feat gained at 5th level.

## Wings (Su) {#wings}

At 15th level, a dragonheir scion can grow leathery dragon wings from her back as a standard action,
granting her a fly speed of 60 feet with average maneuverability. She can dismiss the wings as a
free action.

This ability replaces armor training 4 and armor mastery.

## Might of Wyrms (Su) {#might-of-wyrms}

At 20th level, a dragonheir scion's draconic heritage becomes manifest. She gains
[immunity](ref/umr/immunity) to paralysis, sleep, and damage of her energy type, as well as
[blindsense](ref/umr/blindsense) with a range of 60 feet.

This ability replaces weapon mastery.
