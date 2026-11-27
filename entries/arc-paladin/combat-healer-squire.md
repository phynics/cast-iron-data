+++
id = "ref/arc-paladin/combat-healer-squire"
kind = "archetype"
title = "Combat Healer Squire"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Combat%20Healer%20Squire"
source_ids = ["knights-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "combat_healer_squire", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "knights-of-the-inner-sea"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "careful-healer", level = 1 },
  { anchor = "dress-wounds", level = 2 },
  { anchor = "swift-healer", level = 3 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["careful-healer"] },
  { replaces = "Divine grace", feature = "divine-grace", by = ["dress-wounds"] },
  { replaces = "Divine health", feature = "divine-health", by = ["swift-healer"] },
]
+++

Always ready with bandages and potions, the combat healer squire keeps her knight on his feet
against all odds, and always has just the right remedy on hand.

## Careful Healer (Ex) {#careful-healer}

At 1st level, a combat healer squire provokes no attacks of opportunity when she uses the
[Heal](ref/skill/heal) skill to stabilize a creature or treat poison. In addition, when she
administers long-term care with the Heal skill, she can restore a total number of additional hit
points equal to her character level, divided as she wishes among those she is tending. This ability
replaces _detect evil_.

## Dress Wounds (Su) {#dress-wounds}

At 2nd level, a combat healer squire can hastily dress a deadly wound for her knight, temporarily
alleviating his suffering. This ability acts in all ways like using the Heal skill to treat deadly
wounds, except the combat healer squire only needs to take a full-round action to use this ability.
The hit points healed are temporary, and only last 10 minutes, but they are not lost first like
[temporary hit points](ref/rule/temporary-hit-points). A combat healer squire can only use this
ability on her knight, not other creatures. A knight cannot benefit from this ability more than once
per day, and cannot be treated for deadly wounds with the Heal skill within 24 hours of being
subjected to this ability. This ability replaces divine grace.

## Swift Healer (Ex) {#swift-healer}

At 3rd level, a combat healer squire becomes even more adept when treating wounds, and can use the
Heal skill to perform first aid or treat poison as a swift action. This ability replaces divine
health.
