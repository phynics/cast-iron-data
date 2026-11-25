+++
id = "ref/arc-ranger/stormwalker"
kind = "archetype"
title = "Stormwalker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Stormwalker"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stormwalker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "combat-style-feat", level = 2 },
  { anchor = "thundershot", level = 4 },
  { anchor = "wind-treader", level = 8 },
  { anchor = "flash-step", level = 11 },
  { anchor = "control-weather", level = 16 },
  { anchor = "flash-shot", level = 19 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["thundershot"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["wind-treader"] },
  { replaces = "Quarry", feature = "quarry", by = ["flash-step"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["control-weather"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["flash-shot"] },
  { alters = "Combat style", feature = "combat-style-feat", by = ["combat-style-feat"] },
]
+++

Rangers who walk in the tempest unafraid draw the power of the storm into themselves and become
stormwalkers.

## Combat Style Feat (Ex) {#combat-style-feat}

At 2nd level, a stormwalker must choose archery style.

This alters the ranger's [combat style](ref/ability/combat-styles).

## Thundershot (Su) {#thundershot}

At 4th level, a stormwalker can wreathe his weapon in lightning. As a standard action, he can grant
a single weapon he holds the _[shock](ref/magic-enh/shock)_ special ability for 1 minute; while
under this effect, the weapon counts as magic for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). A stormwalker can use this ability a number of times
per day equal to 3 + his Wisdom modifier. At 12th level, weapons affected by this ability gain the
_[shocking burst](ref/magic-enh/shocking-burst)_ special ability.

This replaces hunter's bond.

## Wind Treader (Ex) {#wind-treader}

At 8th level, a stormwalker becomes immune to the effects of strong [wind](ref/rule/winds). He can
move without hindrance in windy conditions, and his ranged attacks take no penalties from nonmagical
wind.

This replaces swift tracker.

## Flash Step (Su) {#flash-step}

At 11th level, a stormwalker can move across the battlefield like a bolt of lightning. As a
full-round action, he can transform into lightning and move to any unoccupied square within 60 feet
without provoking attacks of opportunity. He can make a single ranged attack before or after this
movement.

This replaces quarry.

## Control Weather (Sp) {#control-weather}

At 16th level, a stormwalker can cast _[control weather](ref/spell/control-weather)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day.

This replaces improved evasion.

## Flash Shot (Su) {#flash-shot}

At 19th level, when a stormwalker uses flash step, he can make a ranged attack both before and after
his movement. Both of these attacks are made at his highest base attack bonus.

This replaces improved quarry.
