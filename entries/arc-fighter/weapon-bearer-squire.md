+++
id = "ref/arc-fighter/weapon-bearer-squire"
kind = "archetype"
title = "Weapon Bearer Squire"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Weapon%20Bearer%20Squire"
source_ids = ["knights-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_bearer_squire", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "knights-of-the-inner-sea"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "weapon-rack", level = 1 },
  { anchor = "swift-sharpening", level = 2 },
  { anchor = "combat-repairs", level = 3 },
]
trades = [
  { replaces = "The 1st-level fighter bonus combat feat", feature = "bonus-feats", levels = [1], by = ["weapon-rack"] },
  { replaces = "The 2nd-level fighter bonus combat feat", feature = "bonus-feats", levels = [2], by = ["swift-sharpening"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["combat-repairs"] },
]
+++

With myriad weapons, armor, and useful gear always on hand, the weapon bearer squire ensures her
knight is equipped for any task.

## Weapon Rack (Ex) {#weapon-rack}

At 1st level, once per round, a knight can retrieve an item carried by his weapon bearer squire as a
move action that does not provoke attacks of opportunity. In addition, a weapon bearer squire can
pick up items dropped by her knight as an immediate action without provoking attacks of opportunity.

The knight and the weapon bearer squire must be adjacent to each other and must both be able to move
and communicate to use these abilities. This ability replaces the 1st-level fighter bonus combat
feat.

## Swift Sharpening (Ex) {#swift-sharpening}

At 2nd level, a weapon bearer squire can quickly hone her lord's weapons to make them more effective
in combat. As a full-round action, a weapon bearer squire can use a
[whetstone](ref/eq-misc/whetstone) to sharpen a weapon she is holding, granting whoever wields the
weapon a +1 circumstance bonus on his next attack roll with that weapon. In addition, she can apply
a [weapon blanch](ref/eq-misc/weapon-blanch-adamantine) (see _Ultimate Equipment_) to a weapon she
is holding as a standard action, instead of a full-round action. This ability replaces the 2nd-level
fighter bonus combat feat.

## Combat Repairs (Ex) {#combat-repairs}

At 3rd level, a weapon bearer squire can ensure her liege never goes unarmed, even if his weapon has
all but shattered. As a full-round action, a weapon bearer squire can make rapid repairs to a weapon
she is holding and is proficient with by succeeding at a DC 20 Craft (weapons) check. The item does
not regain any hit points, but loses the [broken](ref/misc/broken) condition for a number of rounds
equal to the weapon bearer squire's class level. This ability replaces armor training 1.
