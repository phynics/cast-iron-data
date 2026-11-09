+++
id = "ref/arc-witch/hex-channeler"
kind = "archetype"
title = "Hex Channeler"
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
replaces = ["2nd-level hex"]
+++

A hex channeler is a witch who devotes herself to either life - healing the wounded and destroying
the undead - or death, slaying the living and aiding undead.

**Channel Energy (Su)**

**Ability:** A hex channeler can call upon her patron to release a wave of energy from herself or
her familiar. A good witch channels positive energy (like a good cleric), and an evil witch channels
negative energy (like an evil cleric). A witch who is neither good nor evil must choose whether she
channels positive or negative energy; once this choice is made, it cannot be reversed.

_Channeling energy_ causes a [burst](ref/misc/burst) that affects all creatures of one type (either
undead or living) in a 30-foot radius centered on the witch. This otherwise functions as a cleric
using [channel energy](ref/ability/channel-energy), except the witch does not require a holy symbol
to use this ability. The hex channeler uses her witch level as her cleric level for all other
effects dependent upon _channel energy_ (except increasing the amount of damage healed or dealt).
The hex channeler can choose whether or not to include herself or her familiar in this effect.

**Gained:** At 2nd Level

**Replaces:** 2nd-level hex

**Special:** This burst heals or deals 1d6 points of damage. Every time the hex channeler is able to
learn a new hex (including _major_ or _grand hexes,_ but not hexes gained through the
[Extra Hex](ref/feat/extra-hex) feat), she can instead increase her channel energy amount by 1d6.

**Usage:** Charisma3 modifier times/day (minimum 1)

**The following witch hexes complement this archetype:** Blight, healing, poison steep, ward

**The following major hexes complement this archetype:** Agony, cook people, infected wounds, major
healing, retribution

**The following grand hexes complement this archetype:** Death curse, dire prophecy, life giver,
summon spirit
