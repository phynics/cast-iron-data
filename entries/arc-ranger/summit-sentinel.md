+++
id = "ref/arc-ranger/summit-sentinel"
kind = "archetype"
title = "Summit Sentinel"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Summit%20Sentinel"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summit_sentinel", path = "json/archetypes_ranger.json" },
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
  { anchor = "roots-of-the-mountain", level = 2 },
  { anchor = "mountain-mastery", level = 3 },
  { anchor = "spells" },
  { anchor = "rockslide", level = 8 },
  { anchor = "invincible", level = 17 },
]
trades = [
  { replaces = "Combat style feats", feature = "combat-style-feat", by = ["roots-of-the-mountain"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["rockslide"] },
  { replaces = "Hide in plain sight", feature = "hide-in-plain-sight", by = ["invincible"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["mountain-mastery"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
]
+++

Some rangers eschew the path of the swift skirmisher and embrace the implacable strength of the
mountain.

## Roots of the Mountain (Su) {#roots-of-the-mountain}

At 2nd level, a summit sentinel gains [Toughness](ref/feat/toughness) as a bonus feat.

Additionally, as a move action, she can enter a defensive stance for 1 minute. While in this stance,
the summit sentinel's speed is reduced to 5 feet, she gains a +2 enhancement bonus to her natural
armor, and she gains a +2 bonus to her CMD against maneuvers that would move her or knock her prone.
If the ranger loses contact with the ground or other solid surface, the stance ends immediately. The
ranger can enter this stance a number of times per day equal to 3 + her Constitution modifier.

At 6th level and every 4 levels thereafter, the enhancement bonus to natural armor increases by 1,
and the bonus to CMD increases by 2.

This replaces the ranger's combat style feats.

## Mountain Mastery (Ex) {#mountain-mastery}

At 3rd level, a summit sentinel must select mountains as her favored terrain, and she does not gain
additional favored terrains at higher levels. Every 5 levels beyond 5th, the bonus from this favored
terrain increases by 2.

At 8th level, a summit sentinel draws strength from the earth. When she and her target are both in
contact with the ground or an earthen floor, the summit sentinel gains a +1 bonus on attack and
damage rolls against the target. At 18th level, the bonus on attack and damage rolls increases to
+2.

This alters favored terrain.

## Spells {#spells}

A summit sentinel adds _[stoneskin](ref/spell/stoneskin)_ to the ranger spell list as a 4th-level
spell.

This alters the ranger's spells.

## Rockslide (Su) {#rockslide}

At 8th level, once per day as a standard action, a summit sentinel can create a rushing wave of
earth and stone. The summit sentinel chooses a point on the ground or floor within 30 feet. Rippling
waves of earth and stone emanate from the chosen point in a 25-foot cone in a direction of the
summit sentinel's choice. Each creature in the area takes 4d6 points of bludgeoning damage and is
pushed to the end of the cone. A target that succeeds at a Reflex save (DC = 10 + half the ranger's
level + the ranger's Wisdom modifier) takes half damage and is not pushed.

This replaces swift tracker.

## Invincible (Su) {#invincible}

At 17th level, a summit sentinel takes on the unyielding [hardness](ref/umr/hardness) of the
mountains. While in her roots of the mountain defensive stance, she is immune to critical hits and
precision damage.

This replaces hide in plain sight.
