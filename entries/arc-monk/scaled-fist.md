+++
id = "ref/arc-monk/scaled-fist"
kind = "archetype"
title = "Scaled Fist"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Scaled%20Fist"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scaled_fist", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "draconic-might" },
  { anchor = "draconic-mettle", level = 3 },
  { anchor = "draconic-fury", level = 3 },
  { anchor = "draconic-breath", level = 15 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["draconic-mettle"] },
  { replaces = "Maneuver training", feature = "maneuver-training", by = ["draconic-fury"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["draconic-breath"] },
  { alters = "Bonus feats", feature = "bonus-feat", by = ["draconic-might"] },
]
+++

Steeped in traditions that trace their origins to the warrior-monks who trained under the tutelage
of draconic masters in Tian Xia, scaled fists eschew passive introspection in favor of unshakable
confidence. Scaled fists learn to combine brutal intimidation with the brazen ferocity of an ancient
wyrm to devastate their foes.

## Draconic Might {#draconic-might}

Any of the scaled fist's class abilities that make calculations based on her Wisdom (including bonus
feats with DCs or uses per day, such as [Stunning Fist](ref/feat/stunning-fist), but not
Wisdom-based skills or Will saving throws) are instead based on her Charisma.

## Bonus Feats {#bonus-feats}

A scaled fist adds [Dragon Style](ref/feat/dragon-style) and
[Intimidating Prowess](ref/feat/intimidating-prowess) to her list of bonus feats at 1st level. At
6th level, she adds [Dazzling Display](ref/feat/dazzling-display) and
[Dragon Ferocity](ref/feat/dragon-ferocity). At 10th level, she adds
[Disheartening Display](ref/feat/disheartening-display), [Dragon Roar](ref/feat/dragon-roar) and
[Shatter Defenses](ref/feat/shatter-defenses).

This ability modifies bonus feats.

## Draconic Mettle (Su) {#draconic-mettle}

At 3rd level, a scaled fist gains a +2 bonus on saving throws attempted against all fear, paralysis,
and sleep effects.

This ability replaces the still mind ability. For the unchained monk from _Pathfinder RPG Pathfinder
Unchained_, this ability is gained at 4th level.

## Draconic Fury (Su) {#draconic-fury}

At 3rd level, the scaled fist has gained some control over the draconic energies she studies. She
must select one type of energy: acid, cold, electricity, or fire. Once this choice is made, it
cannot be changed. The scaled fist can expend 1 point from her ki pool as a swift action to imbue
her natural attacks with this energy, causing them to deal an extra 1d6 points of damage of the
chosen energy type for a number of rounds equal to 1/2 her monk level.

This ability replaces maneuver training. For the unchained monk from _Pathfinder Unchained_,
draconic fury is the elemental fury ki power, and is gained in place of the ki power normally gained
at 4th level.

## Draconic Breath (Su) {#draconic-breath}

At 15th level, a scaled fist can spend 3 points from her ki pool to make a breath weapon attack as a
standard action. This breath weapon deals 1d6 points of damage of her energy type per monk level in
a 30-foot cone. Those caught in the area of the breath can attempt a Reflex save (DC = 10 + 1/2 the
scaled fist's monk level + her Charisma modifier) to halve the normal damage.

This ability replaces quivering palm. For the unchained monk from _Pathfinder Unchained_, this
ability is gained at 12th level and replaces the ki power gained at that level.
