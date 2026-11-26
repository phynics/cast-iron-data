+++
id = "ref/arc-cleric/demonic-apostle"
kind = "archetype"
title = "Demonic Apostle"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Demonic%20Apostle"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demonic_apostle", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "advanced-race-guide"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "demonic-magic" },
  { anchor = "demonic-familiar", level = 1 },
  { anchor = "demonic-channel", level = 1 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["demonic-channel"] },
]
+++

In order to survive, the drow threw in their lot with demon lords. Thus, demon worship is common
among the drow, and so are ranks of demonic apostles, who gain magical insight from their dark lords
and crush their chaotic masters' enemies by channeling demonic energy. A demonic apostle has the
following class features.

## Demonic Magic {#demonic-magic}

A demonic apostle must choose to channel negative energy, and must select either the Chaos or Evil
domain or the Demon subdomain (_Advanced Player's Guide_ 89) as her sole domain.

## Demonic Familiar {#demonic-familiar}

At 1st level, a demonic apostle gains a [familiar](ref/ability/familiars) as a wizard equal to her
cleric level, or if she already has a familiar, her cleric levels stack to determine the familiar's
abilities. At 3rd level, her familiar gains the [fiendish](ref/template/fiendish) template. At 7th
level, the demonic apostle exchanges her familiar for a [quasit](ref/monster/demon-quasit) without
the need to take the [Improved Familiar](ref/feat/improved-familiar) feat.

## Demonic Channel (Su) {#demonic-channel}

At 1st level, a demonic apostle can channel demonic energy to damage creatures of lawful and good
alignment, or, at higher levels, bolster the abilities of chaotic evil allies.

Channeling this energy causes a 30-foot-radius [burst](ref/misc/burst) centered on the cleric.
Creatures within the burst that are lawful or good take 1d6 points of damage, plus 1d6 points of
damage for every two levels the cleric possesses beyond 1st (2d6 at 3rd, 3d6 at 5th, and so on).
Creatures that take damage from the channeled demonic energy receive a Fortitude save to halve the
damage. The DC of this save is equal to 10 + 1/2 the demonic apostle's level + the demonic apostle's
Charisma modifier. Lawful good creatures take a -2 penalty on this saving throw. At 5th level,
chaotic evil allies within the burst are affected as if targeted by a _[rage](ref/spell/rage)_ spell
with a duration of 1 round. At 9th level, lawful or good enemies are also
[sickened](ref/misc/sickened) for 1d6 rounds if they fail their saving throw against the demonic
channel. Channeling demonic energy is a standard action that does not provoke attacks of
opportunity. This ability replaces channel energy.
