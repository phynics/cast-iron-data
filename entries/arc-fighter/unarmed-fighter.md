+++
id = "ref/arc-fighter/unarmed-fighter"
kind = "archetype"
title = "Unarmed Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Unarmed%20Fighter"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unarmed_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "unarmed-style", level = 1 },
  { anchor = "harsh-training", level = 2 },
  { anchor = "tough-guy", level = 3 },
  { anchor = "weapon-training", level = 5 },
  { anchor = "clever-wrestler", level = 7 },
  { anchor = "trick-throw", level = 8 },
  { anchor = "takedown", level = 12 },
  { anchor = "eye-gouge", level = 13 },
  { anchor = "sucker-punch", level = 17 },
  { anchor = "sheer-toughness", level = 19 },
  { anchor = "weapon-mastery" },
]
trades = [
  { replaces = "The bonus feat at 1st level", feature = "bonus-feats", levels = [1], by = ["unarmed-style"] },
  { replaces = "Bravery", feature = "bravery", by = ["harsh-training"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["tough-guy"] },
  { replaces = "Weapon training 1, 2, 3, and 4", by = ["weapon-training"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["clever-wrestler"] },
  { replaces = "The 8th-level bonus feat", feature = "bonus-feats", levels = [8], by = ["trick-throw"] },
  { replaces = "The 12th-level bonus feat", feature = "bonus-feats", levels = [12], by = ["takedown"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["eye-gouge"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["sucker-punch"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["sheer-toughness"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

Not all fighters need weapons to make their mark on the world. The unarmed fighter picks up a weapon
only rarely, and when he does, he prefers the weapons of the monk. There are even those who mistake
them for monks, but these fighters enter the fight without ki, and instead have a tough perseverance
that few can rival.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An unarmed fighter is not proficient with medium armor, heavy armor, or shields. An unarmed fighter
is proficient with all [monk](ref/class/monk) weapons, including exotic monk weapons.

## Unarmed Style {#unarmed-style}

At 1st level, a unarmed fighter gains the
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) feat and any single style feat (see
Chapter 3) as a bonus feat. The unarmed fighter need not meet all the prerequisites of the style
feat he chooses, but style feats that grant additional uses of the
[Elemental Fist](ref/feat/elemental-fist) feat cannot be taken until the unarmed fighter has that
feat. This ability replaces the bonus feat at 1st level.

## Harsh Training (Ex) {#harsh-training}

At 2nd level, an unarmed fighter gains a +1 bonus on saving throws against effects that cause the
exhausted, fatigued, or staggered conditions or temporary penalties to ability scores. This bonus
increases by +1 for every four levels after 2nd (to a maximum of +5 at 18th level). This ability
replaces bravery.

## Tough Guy (Ex) {#tough-guy}

At 3rd level, an unarmed fighter gains DR/—equal to [half](ref/misc/fractions-and-rounding) his
fighter level against nonlethal damage or damage taken while he is
[grappled](ref/rule/grapple-conditions). This ability replaces armor training 1.

## Weapon Training (Ex) {#weapon-training}

At 5th level, an unarmed fighter gains a +1 bonus on attack and damage rolls with weapons in the
monk and natural [weapon groups](ref/ability/weapon-groups), improving by +1 for every four levels
beyond 5th (to a maximum of +4 at 17th level). This ability replaces weapon training 1, 2, 3, and 4.

## Clever Wrestler (Ex) {#clever-wrestler}

At 7th level, an unarmed fighter takes no penalties to Dexterity or on attack rolls while grappled,
and retains his Dexterity bonus to AC while pinning an opponent. The unarmed fighter can make
attacks of opportunity even when grappled and even against creatures attempting to
[grapple](ref/rule/grapple) him if the opponent has the
[Improved Grapple](ref/feat/improved-grapple) feat or the [grab](ref/umr/grab) ability. This ability
replaces armor training 2.

## Trick Throw (Ex) {#trick-throw}

At 8th level, when an unarmed fighter successfully [trips](ref/rule/trip) an opponent with an
unarmed attack, he can attempt a [dirty trick](ref/rule/dirty-trick) combat maneuver against that
creature (before the opponent becomes prone) as an immediate action that does not provoke attacks of
opportunity. This ability replaces the 8th-level bonus feat.

## Takedown (Ex) {#takedown}

At 12th level, if an unarmed fighter succeeds on a [drag](ref/rule/drag) maneuver, he can attempt a
trip maneuver against the same target as a swift action that does not provoke attacks of
opportunity. At 15th level, he may do so after a successful grapple check. This ability replaces the
12th-level bonus feat.

## Eye Gouge (Ex) {#eye-gouge}

At 13th level, if an unarmed fighter confirms a critical hit with his unarmed strike or begins his
turn grappled, he may attempt a dirty trick maneuver to [blind](ref/misc/blinded) his target as a
swift action that does not provoke attacks of opportunity. A target more than one size category
larger is unaffected. This ability replaces weapon training 3.

## Sucker Punch (Ex) {#sucker-punch}

At 17th level, when an unarmed fighter strikes a creature that is denied its Dexterity bonus to AC,
or that he has successfully pinned with a grapple check, he can attempt a dirty trick or trip combat
maneuver against that target as a swift action. This ability replaces armor training 4.

## Sheer Toughness (Ex) {#sheer-toughness}

At 19th level, an unarmed fighter becomes immune to nonlethal damage and the exhausted, fatigued,
and staggered conditions. This ability replaces armor mastery.

## Weapon Mastery (Ex) {#weapon-mastery}

This ability applies to unarmed strikes only.
