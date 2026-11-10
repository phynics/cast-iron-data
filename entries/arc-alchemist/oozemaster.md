+++
id = "ref/arc-alchemist/oozemaster"
kind = "archetype"
title = "Oozemaster"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Oozemaster"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oozemaster", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "17"

[fields]
kind = "archetype"
replaces = ["Brew Potion", "Poison resistance", "poison immunity"]
replaces_features = ["brew-potion", "poison-resistance"]
+++

The oozemaster is a specialized alchemist who fights and ensnares oozes. An oozemaster carefully
studies the characteristics of the oozes he hunts to help him create new and more effective mutagens
and bombs.

**Gained class skills:** kd

**Lost class skills:** kna

**Ooze Bomb (Su)**

**Ability:** An oozemaster's bombs deal acid damage instead of fire damage, and they deal damage
only on a direct hit; they do not splash. A creature damaged by an ooze bomb takes additional acid
damage equal to the oozemaster's Intelligence modifier at the start of the oozemaster's next turn. A
creature can take this delayed damage only once per round; additional hits extend the duration of
the ongoing damage by 1 round each.

**Replaces:** Brew Potion

**Special:** An oozemaster cannot select discoveries that change the type of damage dealt by his
bombs, nor those that affect the bomb's splash radius. An oozemaster can still select
[Brew Potion](ref/feat/brew-potion) without meeting the feat's prerequisites, but he doesn't gain it
as a bonus feat.

**Ooze Resistance**

**At 11th Level:** The bonus becomes +5.

**At 14th Level:** The bonus becomes +6.

**At 17th Level:** The bonus becomes +7.

**At 20th Level:** The bonus becomes +8.

**At 5th Level:** The bonus becomes +3.

**At 8th Level:** The bonus becomes +4.

**Gained:** At 2nd Level

**Passive:** He gains a +2 bonus on saving throws against the extraordinary and supernatural
abilities of oozes.

**Replaces:** Poison resistance, poison immunity

**Discoveries:** The following discoveries complement the oozemaster archetype:
[bottled ooze](ref/discovery/bottled-ooze), [ooze blight](ref/discovery/ooze-blight), and
[splitting mutagen](ref/discovery/splitting-mutagen).
