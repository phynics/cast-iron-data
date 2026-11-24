+++
id = "ref/arc-arcanist/white-mage"
kind = "archetype"
title = "White Mage"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20White%20Mage"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "white_mage", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "spontaneous-healing", level = 1 },
  { anchor = "greater-exploit", level = 11 },
]
trades = [
  { replaces = "The arcanist exploits gained at 1st and 9th levels", feature = "arcanist-exploits", levels = [1, 9], by = ["spontaneous-healing"] },
]
+++

A white mage is an arcanist touched by a divine power and gifted with the ability to heal others.

## Spontaneous Healing (Su) {#spontaneous-healing}

At 1st level, a white mage can expend 1 point from her arcane reservoir to use one of her spell
slots to cast a cure spell (any spell with "cure" in its name) from the cleric spell list as if it
were on her spell list and prepared. The spell must be of a level the arcanist can cast. At 10th
level, the white mage can expend 5 points from her arcane reservoir and a spell slot of at least 5th
level to cast _[breath of life](ref/spell/breath-of-life)_. This ability replaces the arcanist
exploits gained at 1st and 9th levels.

## Greater Exploit {#greater-exploit}

At 11th level, a white mage can select the following greater exploit.

### Fast Healing (Su) {#fast-healing}

A white mage can spend 1 point from her arcane reservoir and expend a spell slot of at least 2nd
level to grant her allies the [fast healing](ref/umr/fast-healing) ability. Allies within 30 feet
gain [fast healing](ref/umr/fast-healing) (_Bestiary_ 300) equal to 1/2 the level of the spell slot
sacrificed. This effect lasts for a number of rounds equal to the arcanist's Charisma modifier
(minimum 1).
