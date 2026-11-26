+++
id = "ref/arc-arcanist/aeromancer"
kind = "archetype"
title = "Aeromancer"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Aeromancer"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aeromancer", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "air-mastery", level = 1 },
  { anchor = "wind-s-embrace", level = 5 },
  { anchor = "rebuking-gale", level = 11 },
]
trades = [
  { replaces = "The arcane exploit gained at 1st level", feature = "arcanist-exploits", levels = [1], by = ["air-mastery"] },
  { replaces = "The arcane exploit gained at 5th level", feature = "arcanist-exploits", levels = [5], by = ["wind-s-embrace"] },
  { replaces = "The arcane exploit gained at 11th level", feature = "arcanist-exploits", levels = [11], by = ["rebuking-gale"] },
]
+++

The Shory were the undisputed masters of wind and sky, and they unlocked numerous secrets of air
magic. The vast majority of these secrets were lost when their civilization collapsed, but a few of
their magical traditions have been preserved through the years. While the practice of aeromancy is
rare, some arcanists today are able to rival the aerial mastery of the ancient Shory aeromancers.

## Air Mastery (Su) {#air-mastery}

Aeromancers specialize in magic that manipulates the wind and sky. Whenever an aeromancer expends a
point from her arcane reservoir to increase the caster level of a spell with the air, cold,
electricity, or sonic descriptor, she increases that bonus by an additional 1. At 5th level, and
every 5 levels thereafter, the amount by which she increases the caster level of such spells further
increases by an additional 1 (to a maximum additional caster level increase from this ability of 5
at 20th level).

Alternatively, if the aeromancer expends a point from her arcane reservoir to increase the saving
throw DC of a spell with the air, cold, electricity, or sonic descriptor, she increases it by an
additional 1. At 10th level, she increases it by an additional 2 instead.

This replaces the arcane exploit gained at 1st level.

## Wind's Embrace (Su) {#wind-s-embrace}

At 5th level, an aeromancer can expend 2 points from her arcane reservoir to call upon the winds to
gently carry her through the air while protecting her from harm. She is affected as though by the
spell _[air walk](ref/spell/air-walk)_ and is surrounded by protective winds that function similarly
to a _[wind wall](ref/spell/wind-wall)_ spell, except the effect surrounds only the aeromancer and
moves with her wherever she goes. Both of these effects last for 1 minute.

This replaces the arcane exploit gained at 5th level.

## Rebuking Gale (Su) {#rebuking-gale}

At 11th level, by expending 3 points from her arcane reservoir, an aeromancer can release a powerful
blast of wind to push back her foes. This takes the form of either a 20-foot-radius
[burst](ref/misc/burst) centered on the aeromancer or a 40-foot cone originating from the
aeromancer's space. She can choose which form the wind takes each time she uses the ability. The
affected area is filled with hurricane-force [winds](ref/rule/winds) (75 mph). This makes normal
ranged attacks passing through this area impossible, imposes a -8 penalty on ranged attacks from
siege weapons that pass through the area, and imposes a -12 penalty on [Fly](ref/skill/fly) checks
attempted within the area. Additionally, Large creatures in the area are in danger of being checked
(_Pathfinder RPG Core Rulebook_ 439), and Medium or smaller creatures in the area are in danger of
being blown away. The winds created by this ability last for 1 round.

This replaces the arcane exploit gained at 11th level.
