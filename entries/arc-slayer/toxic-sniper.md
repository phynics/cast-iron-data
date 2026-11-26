+++
id = "ref/arc-slayer/toxic-sniper"
kind = "archetype"
title = "Toxic Sniper"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Toxic%20Sniper"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_sniper", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "scrapper-s-gun", level = 1 },
  { anchor = "sharpshooter-s-study" },
  { anchor = "toxic-grit", level = 2 },
  { anchor = "toxic-shots", level = 4 },
  { anchor = "marksman", level = 6 },
  { anchor = "precise-toxin", level = 10 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["scrapper-s-gun"] },
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["toxic-grit"] },
  { replaces = "Slayer talent gained at 4th level", feature = "slayer-talents", levels = [4], by = ["toxic-shots"] },
  { replaces = "Slayer talents gained at 6th, 8th, 12th, 14th, 16th, 18th, and 20th levels", feature = "slayer-talents", levels = [6, 8, 12, 14, 16, 18, 20], by = ["marksman"] },
  { replaces = "Slayer talent gained at 10th level", feature = "slayer-talents", levels = [10], by = ["precise-toxin"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Studied target", feature = "studied-target", by = ["sharpshooter-s-study"] },
]
+++

Followers of the daemonic harbinger [Cixyron](ref/faith/cixyron) hide throughout the Mana Wastes,
scavenging for guns. With significant firepower in hand, the Furious Thunder's snipers bring
poisonous death to the wastes.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A toxic sniper is proficient with all simple weapons and firearms. He is proficient with light
armor.

This alters the toxic sniper's weapon and armor proficiency.

## Scrapper's Gun {#scrapper-s-gun}

A toxic sniper gains the [Gunsmithing](ref/feat/gunsmithing) feat, a battered gun identical to that
gained by a 1st-level [gunslinger](ref/class/gunslinger), and the ability to restore his battered
gun as if he were a gunslinger.

This replaces track.

## Sharpshooter's Study (Ex) {#sharpshooter-s-study}

A toxic sniper's focus makes him extremely deadly with ranged weapons. He gains a bonus on attack
and damage rolls against his studied target only when attacking with a ranged weapon.

This alters studied target.

## Toxic Grit (Ex) {#toxic-grit}

At 2nd level, the toxic sniper gains the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat as a
bonus feat.

This replaces the slayer talent gained at 2nd level.

## Toxic Shots (Ex) {#toxic-shots}

At 4th level, a toxic sniper can coat his ammunition in poison without requiring a
[pitted bullet](ref/eq-weapon/pitted-bullet). He is trained in applying poison in this way and
cannot accidentally poison himself when applying poison to his ammunition. The toxic sniper can
create a number of toxic shots per day equal to [half](ref/misc/fractions-and-rounding) his slayer
level plus his Wisdom modifier. The penetrating nature of a toxic shot increases the DC of any
poisons applied in this way by 2. A toxic sniper cannot create a toxic shot that is part of an
[alchemical cartridge](ref/eq-weapon/alchemical-cartridge).

This replaces the slayer talent gained at 4th level.

## Marksman (Ex) {#marksman}

At 6th level, a toxic sniper reduces the penalty on Stealth checks while sniping by 5. He reduces
the penalty by 5 again at 12th level and at 18th level. At 8th level, he increases the distance from
which he can deliver a ranged sneak attack against his studied target by 10 feet. This increases by
10 feet again at 14th level and at 20th level.

This replaces slayer talents gained at 6th, 8th, 12th, 14th, 16th, 18th, and 20th levels.

## Precise Toxin (Ex) {#precise-toxin}

At 10th level, a toxic sniper can deliver a toxic shot to especially vulnerable areas. When he hits
an opponent with a toxic shot and deals sneak attack damage, he can forgo all his bonus damage to
increase the DC of the his toxic shot's poison. The DC increases by 1 for every 2d6 points of sneak
attack damage he forgoes in this way.

This replaces the slayer talent gained at 10th level.
