+++
id = "ref/arc-fighter/thunderstriker"
kind = "archetype"
title = "Thunderstriker"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Thunderstriker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thunderstriker", path = "json/archetypes_fighter2.json" },
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
  { anchor = "strapped-shield", level = 3 },
  { anchor = "hardbuckler", level = 7 },
  { anchor = "knockback-smash", level = 11 },
  { anchor = "hammer-and-anvil", level = 13 },
  { anchor = "buckler-defense", level = 15 },
  { anchor = "balanced-bashing", level = 17 },
  { anchor = "improved-buckler-defense", level = 19 },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["strapped-shield"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["hardbuckler"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["knockback-smash"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["hammer-and-anvil"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["buckler-defense"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["balanced-bashing"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["improved-buckler-defense"] },
]
+++

The thunderstriker adopts an unusual fighting style, gripping a heavy weapon with both hands and
switching to a defensive posture with weapon and buckler, lashing out with the shield with
surprising speed and power.

## Strapped Shield (Ex) {#strapped-shield}

At 3rd level, a thunderstriker takes no penalty on attack rolls when using a weapon in two hands
while wearing a [buckler](ref/eq-armor/buckler). This ability replaces armor training 1.

## Hardbuckler (Ex) {#hardbuckler}

At 7th level, a thunderstriker may make [shield bash](ref/misc/shield-bash) attacks with a buckler
as if it were a light shield. This ability replaces armor training 2.

## Knockback Smash (Ex) {#knockback-smash}

At 11th level, when a thunderstriker uses his buckler to attack, he gains a bonus equal to the
enhancement bonus of the buckler on both attack and damage rolls. This ability replaces armor
training 3.

## Hammer and Anvil (Ex) {#hammer-and-anvil}

At 13th level, a thunderstriker suffers only half the normal penalties for two-weapon fighting when
using a buckler as his off-hand weapon. This ability replaces weapon training 3.

## Buckler Defense (Ex) {#buckler-defense}

At 15th level, a thunderstriker retains partial use of his buckler even when using a weapon in both
hands or in each hand (rather than losing his shield bonus until the beginning of his next turn). He
gains a +1 shield bonus to AC and may apply the benefits of any feats he knows that require the use
of a shield, but does not benefit from any magical properties his shield may possess. This ability
replaces armor training 4.

## Balanced Bashing (Ex) {#balanced-bashing}

At 17th level, a thunderstriker no longer suffers two-weapon fighting penalties when using a buckler
as his off-hand weapon. This ability replaces weapon training 4.

## Improved Buckler Defense (Ex) {#improved-buckler-defense}

At 19th level, a thunderstriker does not forfeit his shield bonus to AC from a buckler when fighting
two-handed. This ability replaces armor mastery.
