+++
id = "ref/arc-hunter/forester"
kind = "archetype"
title = "Forester"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Forester"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forester", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-focus", level = 1 },
  { anchor = "favored-terrain", level = 5 },
  { anchor = "bonus-feat", level = 2 },
  { anchor = "tactician", level = 3 },
  { anchor = "evasion", level = 4 },
  { anchor = "camouflage", level = 7 },
  { anchor = "breath-of-life", level = 10 },
  { anchor = "improved-evasion", level = 11 },
  { anchor = "hide-in-plain-sight", level = 14 },
]
trades = [
  { replaces = "Precise companion", feature = "precise-companion", by = ["bonus-feat"] },
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["tactician"] },
  { replaces = "Improved empathic link", feature = "improved-empathic-link", by = ["evasion"] },
  { replaces = "Animal companion", feature = "animal-companion", by = ["favored-terrain"] },
  { replaces = "Bonus tricks", feature = "bonus-tricks", by = ["camouflage"] },
  { replaces = "Raise animal companion", feature = "raise-animal-companion", by = ["breath-of-life"] },
  { replaces = "Speak with master", feature = "speak-with-master", by = ["improved-evasion"] },
  { replaces = "Greater empathic link", feature = "greater-empathic-link", by = ["hide-in-plain-sight"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["animal-focus"] },
]
+++

While all hunters have a bond with the natural world, a forester has a stronger tie to her
environment than to the animals within it. While most foresters feel strong bonds with woodland
regions, the archetype functions well in other terrains as well.

In such cases, a forester might refer to herself by a different name that more accurately reflects
her chosen terrain. For example, a forester who favors bogs and marshes might call herself a
"swamper," while one who favors frozen regions might call herself a "glacier guardian." As foresters
gain levels and take on new favored terrains, they often eschew such titles completely, viewing them
as unnecessary, and merely refer to themselves as guardians of the wild or champions of nature's
will—but regardless of the name, their devotion remains.

## Animal Focus (Su) {#animal-focus}

As a forester has no animal companion, the aspects granted by this ability always apply to the
forester herself, just as if a normal hunter's companion were dead.

This alters animal focus.

## Favored Terrain (Ex) {#favored-terrain}

A forester gains the ranger's [favored terrain](ref/ability/favored-terrain) ability. She gains her
first favored terrain at 5th level and a new favored terrain every 4 levels thereafter. In addition,
at each such interval, the bonuses on initiative checks and skill checks in one favored terrain
(including the one just selected, if so desired) increase by 2. Starting at 5th level, a forester
adds [half](ref/misc/fractions-and-rounding) her favored terrain bonus on damage rolls while in her
favored terrain and fighting a creature native to that terrain.

This replaces animal companion.

## Bonus Feat (Ex) {#bonus-feat}

At 2nd level, a forester gains one bonus combat feat. She must meet the prerequisites for this feat
as normal. She gains an additional bonus combat feat at 7th, 13th, and 19th levels.

This replaces precise companion.

## Tactician (Ex) {#tactician}

At 3rd level as a standard action, a forester can grant the benefits of one teamwork feat to all
allies within 30 feet who can see and hear her. Allies retain the use of this bonus feat for 3
rounds plus 1 round for every 2 levels the forester has. Allies do not need to meet the
prerequisites of these bonus feats. The forester can use this ability once per day at 3rd level,
plus one additional time per day at 7th level and every 5 levels thereafter.

This replaces hunter tactics.

## Evasion (Ex) {#evasion}

At 4th level, a forester can avoid even magical and unusual attacks with great agility. If she makes
a successful Reflex saving throw against an attack that normally deals half damage on a successful
save, she instead takes no damage. Evasion can be used only if the forester is wearing light armor,
medium armor, or no armor. A [helpless](ref/misc/helpless) forester does not gain the benefit of
evasion.

This replaces improved empathic link.

## Camouflage (Ex) {#camouflage}

At 7th level, a forester can use the Stealth skill to hide in any of her favored terrains, even if
the terrain doesn't grant [cover](ref/rule/cover) or [concealment](ref/rule/concealment).

This replaces bonus tricks.

## Breath of Life (Sp) {#breath-of-life}

At 10th level, a forester can cast _[breath of life](ref/spell/breath-of-life)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities).

This replaces raise animal companion.

## Improved Evasion (Ex) {#improved-evasion}

At 11th level, a forester's evasion improves. Improved evasion works like evasion, except while the
forester still takes no damage on a successful Reflex saving throw against attacks, she takes only
half damage on a failed save. A helpless forester does not gain the benefit of improved evasion.

This replaces speak with master.

## Hide in Plain Sight (Ex) {#hide-in-plain-sight}

At 14th level, while in any of her favored terrains, a forester can use the Stealth skill even while
being observed.

This replaces greater empathic link.
