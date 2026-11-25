+++
id = "ref/arc-ranger/wave-warden"
kind = "archetype"
title = "Wave Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wave%20Warden"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_warden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "194"

[fields]
kind = "archetype"
features = [
  { anchor = "deep-sentinel", level = 1 },
  { anchor = "aquatic-prowess-feat", level = 2 },
  { anchor = "favored-terrain", level = 3 },
  { anchor = "seaborn", level = 7 },
  { anchor = "watery-summons", level = 8 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["deep-sentinel"] },
  { replaces = "Standard ranger's combat style bonus feats, including the limitations on armor worn", feature = "combat-style-feat", by = ["aquatic-prowess-feat"] },
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["favored-terrain"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["seaborn"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["watery-summons"] },
]
+++

The wave warden patrols beneath the sea, preserving the safety and secrets of merfolk communities.
Though he fares best beneath the water, dry land is no haven to his quarry.

## Deep Sentinel (Ex) {#deep-sentinel}

A wave warden adds half his level (minimum +1) on Perception checks made to notice creatures
underwater. This ability replaces track.

## Aquatic Prowess Feat (Ex) {#aquatic-prowess-feat}

At 2nd level and every four levels thereafter, a wave warden selects a bonus feat that improves his
prowess in aquatic environments. He can choose these feats even if he does not meet the
prerequisites. Initially, he may choose from the following feats: [Dodge](ref/feat/dodge),
[Mobility](ref/feat/mobility), [Net Adept](ref/feat/net-adept) (_Ultimate Combat_),
[Net and Trident](ref/feat/net-and-trident) (_Ultimate Combat_),
[Net Maneuvering](ref/feat/net-maneuvering) (_Ultimate Combat_),
[Precise Shot](ref/feat/precise-shot), [Rapid Reload](ref/feat/rapid-reload),
[Sea Hunter](ref/feat/sea-hunter), and [Two-Weapon Fighting](ref/feat/two-weapon-fighting). At 6th
level, he adds [Improved Two-Weapon Fighting](ref/feat/improved-two-weapon-fighting),
[Net Trickery](ref/feat/net-trickery) (_Ultimate Combat_), and
[Spring Attack](ref/feat/spring-attack) to the list. At 10th level, he adds
[Greater Two-Weapon Fighting](ref/feat/greater-two-weapon-fighting) and
[Improved Precise Shot](ref/feat/improved-precise-shot) to the list. This ability otherwise
functions like and replaces the standard ranger's combat style bonus feats, including the
limitations on armor worn.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a wave warden gains water as a favored terrain. At 8th level and every five levels
thereafter, his bonus in aquatic terrain increases by +2. He does not gain additional favored
terrains. This otherwise functions like the standard ranger's favored terrain ability and replaces
that ability.

## Seaborn (Ex) {#seaborn}

At 7th level, a wave warden may move through any sort of aquatic growth (such as coral or seaweed)
or across a wet surface at his normal speed and without taking damage or suffering any other
impairment. Obstacles that are enchanted or magically manipulated to impede motion still affect him.
This ability replaces woodland stride.

## Watery Summons (Sp) {#watery-summons}

At 8th level, a wave warden can summon allies once per day as a full-round action. This functions as
_[summon nature's ally III](ref/spell/summon-natures-ally-3)_, except it can only be used to summon
creatures with the aquatic or water subtypes. At 11th level, this ability improves to _summon
nature's ally IV_, with this progression continuing every three levels thereafter. The warden's
caster level is equal to his ranger level. This ability replaces swift tracker.
