+++
id = "ref/arc-fighter/roughrider"
kind = "archetype"
title = "Roughrider"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Roughrider"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "roughrider", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-players-guide"
page = "106"

[fields]
kind = "archetype"
features = [
  { anchor = "steadfast-mount", level = 2 },
  { anchor = "armored-charger", level = 3 },
  { anchor = "mounted-mettle", level = 5 },
  { anchor = "leap-from-the-saddle", level = 7 },
  { anchor = "relentless-steed", level = 11 },
  { anchor = "ride-them-down", level = 15 },
  { anchor = "unavoidable-onslaught", level = 15 },
  { anchor = "indomitable-steed", level = 19 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["steadfast-mount"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["armored-charger"] },
  { replaces = "Weapon training 1, 2, 3, and 4", feature = "weapon-training", levels = [5, 9, 13, 17], by = ["mounted-mettle"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["leap-from-the-saddle"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["relentless-steed"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["ride-them-down", "unavoidable-onslaught"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["indomitable-steed"] },
]
+++

Roughriders study and practice the fine points of mounted combat, drilling endlessly with
warbeasts—from noble thoroughbreds to trained monsters—to form a perfect synergy between rider and
steed.

## Steadfast Mount (Ex) {#steadfast-mount}

At 2nd level, after a roughrider has spent 1 hour practicing with a mount, the mount gains a +1
dodge bonus to AC and a +1 morale bonus on saves, but only while the roughrider is mounted on it or
adjacent to it. This bonus increases by +1 for every four levels after 2nd. This ability replaces
bravery.

## Armored Charger (Ex) {#armored-charger}

At 3rd level, a roughrider no longer suffers armor check penalties on Ride skill checks. His mount's
speed is not reduced when carrying a medium load or wearing medium barding. This ability replaces
armor training 1.

## Mounted Mettle (Ex) {#mounted-mettle}

At 5th level, a roughrider and his mount gain a +1 bonus on attack and damage rolls when he is
mounted or adjacent to his mount. This bonus increases by +1 for every four levels after 5th. This
ability replaces weapon training 1, 2, 3, and 4.

## Leap from the Saddle (Ex) {#leap-from-the-saddle}

At 7th level, after a roughrider's mount takes a single move, he may attempt a fast dismount (DC 20
Ride check). If he succeeds, he can take a [full attack](ref/rule/full-attack) action. This ability
replaces armor training 2.

## Relentless Steed (Ex) {#relentless-steed}

At 11th level, a roughrider's mount does not reduce its speed when wearing heavy barding or carrying
a heavy load. The roughrider may also reroll a Ride skill check or a saving throw made by the mount
once per day, but must use the second roll even if it is worse. This ability may be used one
additional time per day for every four levels beyond 11th. This ability replaces armor training 3.

## Ride Them Down (Ex) {#ride-them-down}

At 15th level, can spur his mount on while readying an attack. If a roughrider's mount takes a
single move, the roughrider can make a full attack, taking his attacks at any point during his
mount's movement. If he has the [Trample](ref/feat/trample) feat, he may substitute an
[overrun](ref/rule/overrun) combat maneuver for each of his attacks. This movement provokes attacks
of opportunity against the roughrider but not his mount. This ability replaces armor training 4.

## Unavoidable Onslaught (Ex) {#unavoidable-onslaught}

At 15th level, a roughrider's mounted charge is not blocked by friendly creatures or
[difficult terrain](ref/rule/terrain-and-obstacles). This ability replaces armor training 4.

## Indomitable Steed (Ex) {#indomitable-steed}

At 19th level, a roughrider and his steed gain DR 5/— when mounted. This ability replaces armor
mastery.
