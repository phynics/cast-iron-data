+++
id = "ref/arc-ranger/abendego-diver"
kind = "archetype"
title = "Abendego Diver"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Abendego%20Diver"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abendego_diver", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "ocean-s-blessing", level = 1 },
  { anchor = "deep-diver", level = 1 },
  { anchor = "aquatic-terrain", level = 3 },
  { anchor = "aquatic-adaptation", level = 7 },
  { anchor = "shark-sense", level = 8 },
  { anchor = "killer-of-the-deep", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["ocean-s-blessing"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["deep-diver"] },
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["aquatic-terrain"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["aquatic-adaptation"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["shark-sense"] },
  { replaces = "Master hunter", feature = "master-hunter", by = ["killer-of-the-deep"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

Named for the vicious and unending storm in the southern Arcadian Ocean, Abendego divers have pushed
their bodies to their limits, holding their breath to expand their lung capacity and swimming until
ocean travel is second nature to them.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An Abendego diver is not proficient with shields but is proficient with
[harpoons](ref/eq-weapon/harpoon) and [nets](ref/eq-weapon/net).

This alters the ranger's weapon and armor proficiencies.

## Ocean's Blessing {#ocean-s-blessing}

An Abendego diver adds _buoyancy_, _control water_, _elemental speech_ (water only), _hydraulic
push_, _hydraulic torrent_, _ride the waves_, _river whip_, _water breathing_, and _wave shield_ to
his ranger spell list at the same spell level as they appear on the cleric spell list or
sorcerer/wizard spell list, whichever is lower. He still must select them as spells known, as
normal.

This ability replaces track.

## Deep Diver (Ex) {#deep-diver}

At 1st level, an Abendego diver can [hold his breath](ref/misc/hold-your-breath) for twice as long
as usual (4 rounds times his Constitution score instead of the normal 2).

This ability replaces wild empathy.

## Aquatic Terrain (Ex) {#aquatic-terrain}

At 3rd level, an Abendego diver gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival skill checks while underwater.

Every 5 levels thereafter, the bonus on each of those checks increases by 2 while the Abendego diver
is underwater (to a maximum of +8 at 18th level).

This replaces favored terrain.

## Aquatic Adaptation (Ex) {#aquatic-adaptation}

At 7th level, an Abendego diver gains a swim speed equal to his unmodified base speed. Because he
has a swim speed, he gains the standard +8 bonus on Swim checks to perform a special action or evade
a hazard, the ability to take 10 on a Swim check even if distracted or threatened, and the ability
to use the run action while swimming if he swims in a straight line. If he already has a swim speed,
his swim speed increases by 10 feet.

This replaces woodland stride.

## Shark Sense (Ex) {#shark-sense}

At 8th level, an Abendego diver gains the [scent](ref/umr/scent) ability while underwater.

This ability replaces swift tracker.

## Killer of the Deep (Ex) {#killer-of-the-deep}

At 20th level, an Abendego diver is peerless at detecting prey underwater and delivering killing
blows. He can notice other creatures by scent in a 180-foot radius underwater and can detect blood
in the water up to a mile away. As a standard action, he can make a single attack against a favored
enemy at his full attack bonus while underwater. If the attack hits, the target takes damage
normally and must succeed at a Fortitude save or die. The DC of this save is equal to 10 + half the
ranger's level + the ranger's Wisdom modifier. An Abendego diver can instead deal an additional
amount of nonlethal damage equal to the creature's current hit points. A successful save negates
this damage. An Abendego diver can use this ability once per day against each of his favored enemy
types but not against the same creature more than once in a 24-hour period.

This ability replaces master hunter.
