+++
id = "ref/arc-monk/scaled-fist"
kind = "archetype"
title = "Scaled Fist"
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
replaces = ["Still mind", "Maneuver training", "Quivering palm"]
alters = ["Bonus feats"]
+++

Steeped in traditions that trace their origins to the warrior-monks who trained under the tutelage
of draconic masters in Tian Xia, scaled fists eschew passive introspection in favor of unshakable
confidence. Scaled fists learn to combine brutal intimidation with the brazen ferocity of an ancient
wyrm to devastate their foes.

**Draconic Might**

**Info:** Any of the scaled fist's class abilities that make calculations based on her Wisdom
(including bonus feats with DCs or uses per day, such as [Stunning Fist](ref/feat/stunning-fist),
but not Wisdom-based skills or Will saving throws) are instead based on her Charisma.

**Bonus Feats**

**Alters:** Bonus feats

**At 1st Level:** A scaled fist adds [Dragon Style](ref/feat/dragon-style) and
[Intimidating Prowess](ref/feat/intimidating-prowess) to her list of bonus feats.

**At 10th Level:** She adds [Disheartening Display](ref/feat/disheartening-display),
[Dragon Roar](ref/feat/dragon-roar) and [Shatter Defenses](ref/feat/shatter-defenses).

**At 6th Level:** She adds [Dazzling Display](ref/feat/dazzling-display) and
[Dragon Ferocity](ref/feat/dragon-ferocity).

**Draconic Mettle (Su)**

**Gained:** At 3rd Level

**Passive:** A scaled fist gains a +2 bonus on saving throws attempted against all fear, paralysis,
and sleep effects.

**Replaces:** Still mind

**Draconic Fury (Su)**

**Choice:** The scaled fist has gained some control over the draconic energies she studies. She must
select one type of energy: acid, cold, electricity, or fire. Once this choice is made, it cannot be
changed.

**Gained:** At 3rd Level

**Replaces:** Maneuver training

**Swift:** The scaled fist can expend 1 point from her _ki pool_ to imbue her natural attacks with
this energy, causing them to deal an extra 1d6 points of damage of the chosen energy type for a
number of rounds equal to 1/2 her monk level.

**Draconic Breath (Su)**

**Gained:** At 15th Level

**Replaces:** Quivering palm

**Standard:** A scaled fist can spend 3 points from her _ki pool_ to make a breath weapon attack
that deals 1d6 points of damage of her energy type per monk level in a 30-foot cone. Those caught in
the area of the breath can attempt a Reflex save (DC = 10 + 1/2 the scaled fist's monk level + her
Charisma modifier) to halve the normal damage.
