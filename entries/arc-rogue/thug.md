+++
id = "ref/arc-rogue/thug"
kind = "archetype"
title = "Thug"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Thug"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thug", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "135"

[fields]
kind = "archetype"
features = [
  { anchor = "frightening", level = 1 },
  { anchor = "brutal-beating", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["frightening"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["brutal-beating"] },
]
+++

Some criminals steal with finesse, their victims only discovering the crime when the rogue is long
gone and the coin already spent. A thug, on the other hand, cares nothing for finesse. Through both
threat and violence, the thug gets what she wants by the promise of force, and has no problem making
good on that promise as needed.

## Frightening (Ex) {#frightening}

Whenever a thug successfully uses [Intimidate](ref/skill/intimidate) to demoralize a creature, the
duration of the [shaken](ref/misc/shaken) condition is increased by 1 round. In addition, if the
target is shaken for 4 or more rounds, the thug can instead decide to make the target
[frightened](ref/misc/frightened) for 1 round. This ability replaces trapfinding.

## Brutal Beating (Ex) {#brutal-beating}

At 3rd level, whenever a thug deals sneak attack damage, she can choose to forgo 1d6 points of sneak
attack damage to make the target [sickened](ref/misc/sickened) for a number of rounds equal to 1/2
her rogue level. This ability does not stack with itself—only the most recent duration applies. This
ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the thug archetype: offensive defense, powerful sneak, strong
impression, and weapon training.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the thug archetype: crippling strike, deadly sneak,
and knock-out blow.
