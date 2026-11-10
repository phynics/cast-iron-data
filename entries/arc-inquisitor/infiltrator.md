+++
id = "ref/arc-inquisitor/infiltrator"
kind = "archetype"
title = "Infiltrator"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infiltrator", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-magic"
page = "45"

[fields]
kind = "archetype"
replaces = ["Monster lore", "Track", "Discern lies"]
alters = ["Stern gaze"]
+++

This inquisitor uses guile and deception to blend in among the enemies of the faith rather than
confronting them head-on.

**Misdirection (Sp)**

**Ability:** Each day when the infiltrator prepares spells, she may choose an alignment. She detects
as that alignment as if she had used [misdirection](ref/spell/misdirection) on a creature with that
alignment (this does not change any divination results about her other than her alignment).

**Alters:** Stern gaze

**Gained:** At 1st Level

**Guileful Lore (Ex)**

**Flavor:** The infiltrator's will is bent toward subterfuge and deception.

**Gained:** At 1st Level

**Passive:** She adds her Wisdom modifier on Bluff and Diplomacy skill checks in addition to the
normal ability score modifiers.

**Replaces:** Monster lore

**Forbidden Lore (Ex)**

**Ability:** An infiltrator can cast spells of an alignment opposed to her or her deity (ignoring
the restriction in the Chaotic, Evil, Good, and Lawful Spells class ability).

**Flavor:** While other inquisitors learned to track unbelievers, an infiltrator learns how to cast
their spells.

**Replaces:** Track

**Necessary Lies (Su)**

**Passive:** An infiltrator adds her class level on saving throws against abilities that detect lies
or reveal or force the truth, such as [discern lies](ref/spell/discern-lies) and
[zone of truth](ref/spell/zone-of-truth).

**Replaces:** Discern lies
