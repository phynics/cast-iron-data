+++
id = "ref/arc-companion/elemental-companion"
kind = "archetype"
title = "Elemental Companion"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-type" },
  { anchor = "lesser-elemental-manifestation", level = 2 },
  { anchor = "greater-elemental-manifestation", level = 9 },
]
trades = [
  { replaces = "Evasion", by = ["lesser-elemental-manifestation"] },
  { replaces = "Improved Evasion", by = ["lesser-elemental-manifestation"] },
  { replaces = "Multiattack", by = ["greater-elemental-manifestation"] },
]
+++

The heart of this companion beats with primal energy.

## Elemental Type (Ex) {#elemental-type}

An elemental companion gains a subtype that matches its element: air, earth, fire, or water.

## Lesser Elemental Manifestation (Ex) {#lesser-elemental-manifestation}

At 2nd level, an elemental companion gains one or more special abilities based on its element. An
air companion gains a 20% miss chance against ranged attacks. An earth companion gains DR
1/adamantine, and this [damage reduction](ref/rule/damage-reduction) increases by 1 for every 4
druid levels the master has. A fire companion can see through fire, fog, and smoke without penalty,
and it gains [Nimble Moves](ref/feat/nimble-moves) as a bonus feat. A water companion can breathe
underwater, gains a swim speed of 20 feet, and gains a +2 dodge bonus to AC against attacks of
opportunity; a water companion that already has a swim speed instead increases its swim speed by 10
feet.

This replaces evasion and improved evasion.

## Greater Elemental Manifestation (Su) {#greater-elemental-manifestation}

At 9th level, an elemental companion gains an additional ability based on its element. An air
companion gains a fly speed of 20 feet (good maneuverability); an air companion that already has a
fly speed instead improves its maneuverability by one category. An earth companion's natural attacks
overcome [damage reduction](ref/rule/damage-reduction) as though they were adamantine, cold iron,
and silver weapons. For a fire companion, choose one natural attack; that attack deals an additional
1d6 points of fire damage for every 5 Hit Dice the companion has. For a water companion, choose one
melee natural attack; that attack gains the [push (10 feet)](ref/umr/push) special ability.

This replaces multiattack.
