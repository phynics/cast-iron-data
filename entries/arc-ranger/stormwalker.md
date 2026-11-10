+++
id = "ref/arc-ranger/stormwalker"
kind = "archetype"
title = "Stormwalker"
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
replaces = ["Hunter's bond", "Swift tracker", "Quarry", "Improved evasion", "Improved quarry"]
alters = ["Combat style"]
replaces_features = ["hunter-s-bond", "swift-tracker", "quarry", "improved-evasion", "improved-quarry"]
+++

Rangers who walk in the tempest unafraid draw the power of the storm into themselves and become
stormwalkers.

**Combat Style Feat (Ex)**

**Ability:** A stormwalker must choose the archery [combat style](ref/ability/combat-styles).

**Alters:** Combat style

**Gained:** At 2nd Level

**Thundershot (Su)**

**Flavor:** A stormwalker can wreathe his weapon in lightning.

**At 12th Level:** Weapons affected by this ability gain the
[shocking burst](ref/magic-enh/shocking-burst) special ability, instead.

**Gained:** At 4th Level

**Replaces:** Hunter's bond

**Standard:** He can grant a single weapon he holds the [shock](ref/magic-enh/shock) special ability
for 1 minute; while under this effect, the weapon counts as magic for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction).

**Usage:** Wisdom3 modifier times/day

**Wind Treader (Ex)**

**Gained:** At 8th Level

**Passive:** A stormwalker becomes immune to the effects of strong [wind](ref/rule/winds). He can
move without hindrance in windy conditions, and his ranged attacks take no penalties from nonmagical
wind.

**Replaces:** Swift tracker

**Flash Step (Su)**

**Flavor:** A stormwalker can move across the battlefield like a bolt of lightning.

**Fullround:** He can transform into lightning and move to any unoccupied square within 60 feet
without provoking attacks of opportunity. He can make a single ranged attack before or after this
movement.

**Gained:** At 11th Level

**Replaces:** Quarry

**Control Weather (Sp)**

**Ability:** A stormwalker can cast [control weather](ref/spell/control-weather) as a
[spell-like ability](ref/umr/spell-like-abilities) once per day.

**Gained:** At 16th Level

**Replaces:** Improved evasion

**Flash Shot (Su)**

**Ability:** When a stormwalker uses _flash step,_ he can make a ranged attack both before and after
his movement. Both of these attacks are made at his highest base attack bonus.

**Gained:** At 19th Level

**Replaces:** Improved quarry
