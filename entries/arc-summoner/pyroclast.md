+++
id = "ref/arc-summoner/pyroclast"
kind = "archetype"
title = "Pyroclast"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Pyroclast"
source_ids = ["pathfinder-95-anvil-of-fire"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pyroclast", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "pathfinder-95-anvil-of-fire"
page = "72"

[fields]
kind = "archetype"
replaces = ["Maker's call", "Transposition"]
alters = ["Spells"]
+++

Pyroclasts harness the primal elemental energy of magma. Their eidolons often resemble elemental
beings.

**Diminished Spellcasting**

**Alters:** Spells

**Info:** A pyroclast receives one fewer spell per day of each level than normal. If this reduces
the number of spells for a level to 0, he can cast spells of that level only if his Charisma score
grants him [bonus spells](ref/rule/determine-bonuses) of that level.

**Bound to Fire (Ex)**

**At 10th Level:** A pyroclast's eidolon gains the [fire](ref/subtype/fire) subtype and
[immunity](ref/umr/immunity) to fire.

**At 5th Level:** This improves to resist fire 20.

**Passive:** A pyroclast's eidolon begins with [resist](ref/umr/resistance) fire 10 and
[vulnerability](ref/umr/vulnerabilities) to cold.

**Special:** This ability permanently reduces the eidolon's evolution pool by 1 point.

**Detonate (Su)**

**Ability:** A pyroclast can banish his eidolon in an explosion of fiery shards. This slays the
eidolon and deals 1d6 points of damage per Hit Die of the eidolon to every creature in a
20-foot-radius [burst](ref/misc/burst) (Reflex half, DC = 10 + 1/2 his summoner level + his Charisma
modifier). Half of this damage is fire, and the other half is piercing.

**At 12th Level:** The pyroclast can reduce the damage by 4d6 to increase the burst radius to 40
feet.

**Gained:** At 6th Level

**Replaces:** Maker's call

**Usage:** Once per day

**Usage:** Once per day

**Heart of Earth and Fire (Ex)**

**At 10th Level:** The pyroclast also grants these bonuses to his eidolon.

**Gained:** At 8th Level

**Passive:** A pyroclast grants any of his summoned creatures with the earth or fire subtypes a +1
morale bonus on attack rolls, saving throws, and weapon damage rolls when he is within 30 feet.

**Replaces:** Transposition
