+++
id = "ref/arc-witch/alley-witch"
kind = "archetype"
title = "Alley Witch"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alley_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "20"

[fields]
kind = "archetype"
replaces = ["1st-level hex", "6th-level hex"]
alters = ["Patron", "patron spells"]
alters_features = ["patron-spells"]
+++

Some witches find their spark of magic in the long, dark shadows and forgotten places within the
city.

**Gained class skills:** bluff, kl

**Lost class skills:** kna, kp

**Crowd Patron**

**Alters:** Patron, patron spells

**Info:** An alley witch draws power not from a patron, but from the crowd of minds around her. She
doesn't select a patron at 1st level; instead, she gains the following bonus spells at the listed
witch levels.

**Spells:** Mage's private sanctum

**Spells:** Heroes' feast

**Spells:** Limited wish

**Spells:** Create demiplane

**Spells:** Shades

**Spells:** Ears of the city

**Spells:** Alter self

**Spells:** Witness

**Spells:** Shadow step

**Speak to the City**

**Choice:** At 1st level, she can select one settlement whose type is
[large town size or larger](ref/rule/the-settlement-stat-block).

**Flavor:** An alley witch builds a special rapport with a single city.

**Passive:** Within this settlement, she gains a +2 bonus on initiative checks, as well as Knowledge
(local), Perception, Stealth, and Sense Motive checks.

**Replaces:** 1st-level hex

**Special:** The alley witch can build a rapport with a new city after 30 days of remaining there;
this severs her bond to her previous settlement.

At 6th level: This bonus +4.

At 11th level: This bonus +6.

At 16th level: This bonus +8.

**Hex Trader**

**Fullround:** Once per day, an alley witch can bind a hex she knows into a feather, bead, or other
small token. Any creature holding this token can use that hex once as if using a potion, targeting
itself or a creature it touches.

**Gained:** At 6th Level

**Replaces:** 6th-level hex

**Special:** While a hex is sealed into a token, the alley witch loses her ability to use that hex
until the token is used or she can recover the token. If a hex can be used in increments (like the
[disguise](ref/hex/disguise) hex), the alley witch decides how many increments the token contains
when making it. If a hex has no set duration, it lasts for 1 minute once activated.
