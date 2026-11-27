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
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "bound-to-fire" },
  { anchor = "detonate", level = 6 },
  { anchor = "heart-of-earth-and-fire", level = 8 },
]
trades = [
  { replaces = "Maker's call", feature = "maker-s-call", by = ["detonate"] },
  { replaces = "Transposition", feature = "transposition", by = ["heart-of-earth-and-fire"] },
  { alters = "Spells", feature = "spells", by = ["diminished-spellcasting"] },
]
+++

Pyroclasts harness the primal elemental energy of magma. Their eidolons often resemble elemental
beings.

## Diminished Spellcasting {#diminished-spellcasting}

A pyroclast receives one fewer spell per day of each level than normal. If this reduces the number
of spells for a level to 0, he can cast spells of that level only if his Charisma score grants him
[bonus spells](ref/rule/determine-bonuses) of that level. This alters the summoner's spells.

## Bound to Fire (Ex) {#bound-to-fire}

A pyroclast's eidolon begins with [resist](ref/umr/resistance) [fire](ref/subtype/fire) 10 and
[vulnerability](ref/umr/vulnerabilities) to cold. This improves to resist fire 20 when the pyroclast
reaches 5th level. A pyroclast's eidolon gains the fire subtype and [immunity](ref/umr/immunity) to
fire when he reaches 10th level. This ability permanently reduces the eidolon's evolution pool by 1
point.

## Detonate (Su) {#detonate}

At 6th level, a pyroclast can banish his eidolon in an explosion of fiery shards. This slays the
eidolon and deals 1d6 points of damage per Hit Die of the eidolon to every creature in a
20-foot-radius [burst](ref/misc/burst) (Reflex half, DC = 10 + 1/2 his summoner level + his Charisma
modifier). Half of this damage is fire, and the other half is piercing. At 12th level, the pyroclast
can reduce the damage by 4d6 to increase the burst radius to 40 feet. The pyroclast can use this
ability once per day. This ability replaces maker's call.

## Heart of Earth and Fire (Ex) {#heart-of-earth-and-fire}

At 8th level, a pyroclast grants any of his summoned creatures with the earth or fire subtypes a +1
morale bonus on attack rolls, saving throws, and weapon damage rolls when he is within 30 feet. At
10th level, the pyroclast also grants these bonuses to his eidolon. This ability replaces
transposition.
