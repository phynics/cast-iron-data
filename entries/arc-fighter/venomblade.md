+++
id = "ref/arc-fighter/venomblade"
kind = "archetype"
title = "Venomblade"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Venomblade"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venomblade", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "potions-and-poisons"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "venom-projection", level = 1 },
  { anchor = "sneak-attack", level = 6 },
  { anchor = "viper-strike", level = 12 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["venom-projection"] },
  { replaces = "Bonus feat gained at 6th level", feature = "bonus-feats", levels = [6], by = ["sneak-attack"] },
  { replaces = "Bonus feat gained at 12th level", feature = "bonus-feats", levels = [12], by = ["viper-strike"] },
  { alters = "Bonus feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["venom-projection"] },
]
+++

The venomblade has learned to take full advantage of his toxic spittle, blinding his targets and
then rushing in to cut them down where they stand. The venomblade is an archetype of the fighter
class that is available to nagaji characters.

## Venom Projection (Ex) {#venom-projection}

The venomblade must take the [Spit Venom](ref/feat/spit-venom) nagaji racial feat as his 1st-level
fighter bonus feat if he does not already have that ability. At 2nd level, he does not provoke an
attack of opportunity for using the ability granted by the Spit Venom feat. At 4th level, he can use
the ability granted by the Spit Venom feat as a standard action; at 8th level, he can use it as a
move action; and at 12th level, he can use it as a swift action.

This replaces bravery and alters the bonus feat gained at 1st level.

## Sneak Attack (Ex) {#sneak-attack}

At 6th level, a venomblade deals 1d6 additional points of damage to targets within 30 feet that he
flanks or that are denied their Dexterity bonus to AC against him. This damage increases by 1d6
every 4 levels beyond 6th.

This replaces the bonus feat gained at 6th level.

## Viper Strike (Ex) {#viper-strike}

At 12th level, upon making a successful attack with a slashing or piercing weapon, the venomblade
can spend a use of the ability granted by the Spit Venom feat as a swift action to spray his toxin
into the wound. This imposes a -4 penalty on the victim's saving throw against the poison and causes
the target to take 1d6 additional points of damage from all successful attacks for 1 round. This is
a poison effect.

This replaces the bonus feat gained at 12th level.
