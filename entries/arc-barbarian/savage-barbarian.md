+++
id = "ref/arc-barbarian/savage-barbarian"
kind = "archetype"
title = "Savage Barbarian"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Savage%20Barbarian"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "savage_barbarian", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "naked-courage", level = 3 },
  { anchor = "natural-toughness", level = 7 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["naked-courage"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["natural-toughness"] },
]
+++

Some barbarians are truly savage, having little training in modern arms. These savage barbarians
learn to avoid blows and toughen up their skin. A savage barbarian has the following class features.

## Naked Courage (Ex) {#naked-courage}

At 3rd level, the savage barbarian gains a +1 dodge bonus to AC and a +1 morale bonus on saving
throws against fear when wearing no armor (shields are allowed). This bonus increases by +1 for
every six levels after 3rd. This ability replaces trap sense.

## Natural Toughness (Ex) {#natural-toughness}

At 7th level, the savage barbarian gains a +1 natural armor bonus to AC when wearing no armor
(shields are allowed). This bonus increases by +1 for every three levels beyond 7th. This ability
replaces [damage reduction](ref/rule/damage-reduction).

## Rage Powers {#rage-powers}

The following rage powers complement the savage barbarian archetype:
[flesh wound](ref/ragepower/flesh-wound), [guarded stance](ref/ragepower/guarded-stance)\*,
[increased damage reduction](ref/ragepower/increased-damage-reduction)\*,
[intimidating glare](ref/ragepower/intimidating-glare)\*,
[rolling dodge](ref/ragepower/rolling-dodge)\*, [superstition](ref/ragepower/superstition)\*, and
[terrifying howl](ref/ragepower/terrifying-howl)\*.
