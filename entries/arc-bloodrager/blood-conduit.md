+++
id = "ref/arc-bloodrager/blood-conduit"
kind = "archetype"
title = "Blood Conduit"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Blood%20Conduit"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_conduit", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "contact-specialist", level = 1 },
  { anchor = "spell-conduit", level = 5 },
  { anchor = "reflexive-conduit", level = 14 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["contact-specialist"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["spell-conduit"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["spell-conduit"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["reflexive-conduit"] },
  { alters = "Bloodline feats", feature = "bloodline", power = "bloodline feat", by = ["contact-specialist"] },
]
+++

Blood conduits learn to channel their arcane might directly through their flesh, without the need
for mystical words or gestures.

## Contact Specialist (Ex) {#contact-specialist}

At 1st level, a blood conduit selects a bonus feat from the following:
[Improved Bull Rush](ref/feat/improved-bull-rush), [Improved Grapple](ref/feat/improved-grapple),
[Improved Reposition](ref/feat/improved-reposition), [Improved Trip](ref/feat/improved-trip), and
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike). He does not need to meet the
prerequisites to take this feat. He also adds those feats to his list of bloodline feats. This
ability replaces fast movement and alters bloodline feats.

## Spell Conduit (Su) {#spell-conduit}

At 5th level, as long as a blood conduit is wearing light or no armor, he can deliver bloodrager
spells with a range of touch through bodily contact. When he succeeds at a
[combat maneuver](ref/rule/combat-maneuvers) check to bull rush, grapple, pin, reposition, or trip
an opponent, or makes an unarmed strike against an enemy, he can as a swift action cast a touch
spell on the creature that he affected with the combat maneuver, requiring no further touch attack
roll. If this spell would usually require a successful touch attack, his successful combat maneuver
check counts as this attack. This ability replaces uncanny dodge and improved uncanny dodge.

## Reflexive Conduit (Ex) {#reflexive-conduit}

At 14th level, a blood conduit can discharge his power into foes that attempt bodily contact with
him. While wearing light or no armor, when the blood conduit is subject to a combat maneuver check
made to bull rush, grapple, pin, reposition, or trip him, as an immediate action he can target his
attacker with a bloodrager spell that has a range of touch. If the spell would normally require a
touch attack, a blood conduit can attempt a combat maneuver check for this attack instead. This
ability replaces indomitable will.
