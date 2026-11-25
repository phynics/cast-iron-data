+++
id = "ref/arc-familiar/protector"
kind = "archetype"
title = "Protector"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protector", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "212"
[[sources]]
publication = "familiar-folio"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "loyal-bodyguard" },
  { anchor = "shield-master", level = 5 },
  { anchor = "able-defender", level = 11 },
]
trades = [
  { replaces = "Alertness", by = ["loyal-bodyguard"] },
  { replaces = "improved evasion", by = ["loyal-bodyguard"] },
  { replaces = "Deliver touch spells", by = ["shield-master"] },
  { replaces = "speak with animals of its kind", by = ["shield-master"] },
  { replaces = "Spell resistance", by = ["able-defender"] },
]
+++

Protector familiars are so devoted that they would give their lives for their masters. A tumor
familiar can't be a protector.

## Loyal Bodyguard (Ex) {#loyal-bodyguard}

A protector gains [Bodyguard](ref/feat/bodyguard) and [Combat Reflexes](ref/feat/combat-reflexes) as
bonus feats. If the familiar is sharing its master's square, it can use Bodyguard to aid another to
improve its master's AC even if it doesn't threaten the attacking foe, though it still needs line of
effect to its master and the attacker.

This replaces alertness and improved evasion.

## Shield Master (Su) {#shield-master}

At 5th level, whenever a protector or its master takes hit point damage, as long as the protector
and its master are touching, its master can split the damage evenly between them as if under the
effects of _[shield other](ref/spell/shield-other)_.

This replaces deliver touch spells and speak with animals of its kind.

## Able Defender (Ex) {#able-defender}

At 11th level, a protector gains [In Harm's Way](ref/feat/in-harms-way) as a bonus feat. In
addition, the familiar's hit points are now equal to its master's total hit points (not including
temporary hit points), regardless of its actual Hit Dice.

This replaces [spell resistance](ref/rule/spell-resistance).
