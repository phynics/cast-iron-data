+++
id = "ref/arc-oracle/spirit-guide"
kind = "archetype"
title = "Spirit Guide"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Spirit%20Guide"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_guide", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-class-guide"
page = "106"

[fields]
kind = "archetype"
features = [
  { anchor = "bonded-spirit", level = 3 },
]
trades = [
  { replaces = "Bonus class skills gained from the oracle's mystery", feature = "mystery", power = "class skills" },
  { replaces = "Revelations gained at 3rd, 7th, and 15th levels", feature = "revelation", levels = [3, 7, 15], by = ["bonded-spirit"] },
]
+++

Through her exploration of the universe's mysteries, a spirit guide opens connections to the spirit
world and forms bonds with the entities that inhabit it.

## Class Skills {#class-skills}

A spirit guide gains all Knowledge skills as class skills. This replaces the bonus class skills
gained from the oracle's mystery.

## Bonded Spirit (Su) {#bonded-spirit}

At 3rd level, a [spirit](ref/ability/shaman-spirits) guide can form a temporary bond with a spirit,
as the [shaman's](ref/class/shaman) wandering spirit class feature (see page 37). She must make this
selection each day when she refreshes her spells. A spirit guide cannot bond with a spirit that is
incompatible with her alignment, ethos, or mystery (GM's discretion).

A spirit guide gains one hex of her choice from the list of hexes available from that spirit. She
uses her oracle level as her shaman level, and she switches Wisdom for Charisma and vice versa for
the purpose of determining the hex's effects.

At 4th level, she adds the bonded spirit's spirit magic spells to her oracle spells known for that
day, but only of spell levels she can cast. At 7th level, she gains the spirit ability of her
current bonded spirit. At 15th level, she gains the greater spirit ability of her current bonded
spirit.

This ability replaces the revelations gained at 3rd, 7th, and 15th levels.

## Recommended Mysteries {#recommended-mysteries}

[Ancestor](ref/mystery/ancestor), [heavens](ref/mystery/heavens), [lore](ref/mystery/lore).
