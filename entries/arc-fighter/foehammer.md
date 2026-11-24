+++
id = "ref/arc-fighter/foehammer"
kind = "archetype"
title = "Foehammer"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Foehammer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "foehammer", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-race-guide"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "sledgehammer", level = 3 },
  { anchor = "weapon-training", level = 5 },
  { anchor = "hammer-to-the-ground", level = 7 },
  { anchor = "rhythmic-blows", level = 9 },
  { anchor = "piledriver", level = 11 },
  { anchor = "ground-breaker", level = 13 },
  { anchor = "hammer-master", level = 17 },
  { anchor = "devastating-blow", level = 19 },
  { anchor = "weapon-mastery" },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["sledgehammer"] },
  { replaces = "Armor training 2 and 4", feature = "armor-training", levels = [7, 15], by = ["hammer-to-the-ground"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["rhythmic-blows"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["piledriver"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["ground-breaker"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["hammer-master"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["devastating-blow"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

While the axe is the most famous dwarven weapon, the hammer is at the heart of dwarves' heritage as
forgemasters and warriors alike.

**Prerequisites:** Dwarf

## Sledgehammer (Ex) {#sledgehammer}

At 3rd level, a foehammer wielding a hammer gains a +2 circumstance bonus on combat maneuver checks
made to [bull rush](ref/rule/bull-rush), [overrun](ref/rule/overrun), [sunder](ref/rule/sunder), or
[trip](ref/rule/trip). This ability replaces armor training 1.

## Weapon Training (Ex) {#weapon-training}

At 5th level, a foehammer must select hammers and does not gain weapon training with
[other groups](ref/ability/weapon-groups), though his weapon training bonus improves by +1 every
four levels after 5th.

## Hammer to the Ground (Ex) {#hammer-to-the-ground}

At 7th level, when a foehammer succeeds at a bull rush combat maneuver, he can make a trip combat
maneuver at the end of the bull rush. If he does not move with the target, the force of his blow may
still trip his foe, but he takes a -5 penalty on the combat maneuver check to trip.

At 15th level, any creature a foehammer successfully bull rushes is automatically knocked
[prone](ref/rule/prone) at the end of the bull rush. This ability replaces armor training 2 and 4.

## Rhythmic Blows (Ex) {#rhythmic-blows}

At 9th level, each time that a foehammer hits a target, he gains a +1 bonus on attack rolls against
that target. This bonus stacks with each hit against that target, but lasts only until the end of
the foehammer's turn. This ability replaces weapon training 2.

## Piledriver (Ex) {#piledriver}

At 11th level, as a standard action, a foehammer may make a single melee attack with a weapon from
the hammer weapon training group. If the attack hits, he may make a bull rush or trip combat
maneuver against the target of his attack as a free action that does not provoke an attack of
opportunity. This ability replaces armor training 3.

## Ground Breaker (Ex) {#ground-breaker}

At 13th level, as a full-round action, a foehammer may strike the ground with his hammer. If the
attack deals more damage than the floor's [hardness](ref/umr/hardness), the space he occupies and
all adjacent squares become [difficult terrain](ref/rule/terrain-and-obstacles). Creatures in those
squares, except for the foehammer, are knocked prone (DC 15 Reflex negates). This ability replaces
weapon training 3.

## Hammer Master (Ex) {#hammer-master}

At 17th level, any combat feats a foehammer has learned with any weapon from the hammer weapon
training group (e.g., [Improved Critical](ref/feat/improved-critical),
[Weapon Focus](ref/feat/weapon-focus)) apply to all weapons from that group. This ability replaces
weapon training 4.

## Devastating Blow (Ex) {#devastating-blow}

At 19th level, as a standard action, a foehammer may make a single melee attack with a weapon from
the hammer weapon training group at a -5 penalty. If the attack hits, it is treated as a critical
threat. Weapon special abilities that only activate on a critical hit do not activate if this
critical hit is confirmed. This ability replaces armor mastery.

## Weapon Mastery (Ex) {#weapon-mastery}

A foehammer must choose a weapon from the hammer group.
