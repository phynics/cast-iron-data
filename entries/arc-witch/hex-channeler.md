+++
id = "ref/arc-witch/hex-channeler"
kind = "archetype"
title = "Hex Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Hex%20Channeler"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hex_channeler", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "advanced-class-guide"
page = "132"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-energy", level = 2 },
]
trades = [
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["channel-energy"] },
]
+++

A hex channeler is a witch who devotes herself to either life—healing the wounded and destroying the
undead—or death, slaying the living and aiding undead.

## Channel Energy (Su) {#channel-energy}

At 2nd level, a hex channeler can call upon her patron to release a wave of energy from herself or
her familiar. A good witch channels positive energy (like a good cleric), and an evil witch channels
negative energy (like an evil cleric). A witch who is neither good nor evil must choose whether she
channels positive or negative energy; once this choice is made, it cannot be reversed.

Channeling energy causes a [burst](ref/misc/burst) that affects all creatures of one type (either
undead or living) in a 30-foot radius centered on the witch. The witch can
[channel energy](ref/ability/channel-energy) a number of times per day equal to 3 + her Charisma
modifier (minimum 1). This otherwise functions as a cleric using channel energy, except the witch
does not require a holy symbol to use this ability. The hex channeler uses her witch level as her
cleric level for all other effects dependent upon channel energy (except increasing the amount of
damage healed or dealt). The hex channeler can choose whether or not to include herself or her
familiar in this effect.

This burst heals or deals 1d6 points of damage. Every time the hex channeler is able to learn a new
hex (including major or grand hexes, but not hexes gained through the
[Extra Hex](ref/feat/extra-hex) feat), she can instead increase her channel energy amount by 1d6.
This ability replaces the hex gained at 2nd level.

## Hexes {#hexes}

The following witch hexes complement the hex channeler archetype: blight, healing, poison steep, and
ward.

## Major Hexes {#major-hexes}

The following major hexes complement the hex channeler archetype: agony, cook people, infected
wounds, major healing, and retribution.

## Grand Hexes {#grand-hexes}

The following grand hexes complement the hex channeler archetype: death curse, dire prophecy, life
giver, and summon spirit.
