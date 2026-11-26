+++
id = "ref/arc-monk/hamatulatsu-master"
kind = "archetype"
title = "Hamatulatsu Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Hamatulatsu%20Master"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hamatulatsu_master", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "inner-sea-combat"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "stunning-fist" },
  { anchor = "ki-pool" },
  { anchor = "infernal-resilience", level = 5 },
]
trades = [
  { replaces = "Purity of body", feature = "purity-of-body", by = ["infernal-resilience"] },
]
+++

Once part of the Sisterhood of Eiseth, the Sisterhood of the Golden Erinyes is an order of female
monks dedicated to emulating the painful strikes of the
[barbed devil](ref/monster/devil-barbed-devil-hamatula), leaving targets alive but permanently
scarred and broken by pain—a method called hamatulatsu. The sisters train equally hard to resist
their own techniques, and nearly all revere [Asmodeus](ref/faith/asmodeus).

## Alignment {#alignment}

A hamatulatsu master must be lawful neutral or lawful evil.

## Bonus Feats {#bonus-feats}

A hamatulatsu master replaces the normal monk bonus feats with the following:
[Deflect Arrows](ref/feat/deflect-arrows), [Dodge](ref/feat/dodge),
[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency),
[Improved Grapple](ref/feat/improved-grapple),
[Intimidating Prowess](ref/feat/intimidating-prowess), [Scorpion Style](ref/feat/scorpion-style), or
[Weapon Focus](ref/feat/weapon-focus). At 6th level, the following feats are added to the list:
[Gorgon's Fist](ref/feat/gorgons-fist), [Hamatulatsu](ref/feat/hamatulatsu),
[Improved Sunder](ref/feat/improved-sunder), [Mobility](ref/feat/mobility),
[Power Attack](ref/feat/power-attack). At 10th level, the following feats are added to the list:
[Critical Focus](ref/feat/critical-focus), [Impaling Critical](ref/feat/impaling-critical) (unarmed
strike), [Improved Critical](ref/feat/improved-critical), [Medusa's Wrath](ref/feat/medusas-wrath),
[Snatch Arrows](ref/feat/snatch-arrows). At 14th level, the following feat is added to the list:
[Improved Impaling Critical](ref/feat/improved-impaling-critical). Anytime a hamatulatsu master
would gain a bonus feat, she can instead choose to gain two additional uses of stunning fist per
day.

## Stunning Fist (Ex) {#stunning-fist}

A hamatulatsu master expands the conditions that she can apply to the target of her stunning fist
beyond merely stunning her target. At 4th level, she can choose to make the target
[shaken](ref/misc/shaken) for 1 minute. At 8th level, she can choose to deal 1d10 points of
nonlethal [bleed](ref/umr/bleed) damage. At 12th level, she can choose to make the target
[frightened](ref/misc/frightened) for 1d3 rounds. At 16th level, she can deal 2d12 points of
nonlethal bleed damage. The shaken and frightened conditions allow the target to attempt a Will save
to negate the effect instead of a Fortitude save. This ability otherwise functions as normal for a
monk of her level.

## Ki Pool (Su) {#ki-pool}

By spending 1 point from her ki pool as a swift action, a hamatulatsu master can make one additional
attack at her highest attack bonus when making a flurry of blows attack. Alternatively, she can
spend 1 ki point as a swift action to gain one additional use of her stunning fist ability that
round, though this does not grant her an additional attack. Finally, as an immediate action, a
hamatulatsu master can spend 1 ki point to make a single melee attack with a +2 bonus against a
creature that has damaged her with a natural melee attack, unarmed strike, or weapon without the
reach property. This ability otherwise functions as normal for a monk of her level.

## Infernal Resilience (Ex) {#infernal-resilience}

At 5th level, a hamatulatsu master gains immunity to all spells,
[spell-like abilities](ref/umr/spell-like-abilities), and effects with the pain descriptor, as well
as a +2 bonus on saving throws against effects that would sicken, nauseate, stagger, or stun her.
This ability replaces purity of body.
