+++
id = "ref/arc-fighter/siegebreaker"
kind = "archetype"
title = "Siegebreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Siegebreaker"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siegebreaker", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "11"

[fields]
kind = "archetype"
replaces = ["The feat gained at 1st level", "Bravery", "The feat gained at 2nd level", "The bonus feat gained at 8th level", "Weapon mastery"]
alters = ["The feat gained at 4th level"]
replaces_features = ["bravery", "weapon-mastery"]
+++

The siegebreaker is trained to break through lines of enemy soldiers.

**Breaker Rush (Ex)**

**Ability:** A siegebreaker can attempt [bull rush](ref/rule/bull-rush) or
[overrun](ref/rule/overrun) combat maneuvers without provoking attacks of opportunity. When he
performs either combat maneuver, he deals an amount of bludgeoning damage equal to his Strength
bonus (minimum 1). If he has [Improved Bull Rush](ref/feat/improved-bull-rush) or
[Improved Overrun](ref/feat/improved-overrun), the damage dealt by the appropriate maneuver
increases by 2 and he adds any enhancement bonus from his armor or shield (though such enhancement
bonuses do not stack, if both armor and shield are magic).

**Gained:** At 1st Level

**Replaces:** The feat gained at 1st level

**Armored Vigor (Ex)**

**Gained:** At 2nd Level

**Replaces:** Bravery

**Special:** He can use this ability only while wearing armor.

**Swift:** A siegebreaker can gain 2 [temporary hit points](ref/rule/temporary-hit-points) that last
for 1 minute.

**Usage:** Con3 modifier times/day

At 8th level: The amount of temporary hit points 4.

At 14th level: The amount of temporary hit points 6.

At 20th level: The amount of temporary hit points 8.

**Breaker Momentum (Ex)**

**Free:** When a siegebreaker successfully bull rushes a foe, he can attempt an overrun combat
maneuver check against that foe.

**Gained:** At 2nd Level

**Replaces:** The feat gained at 2nd level

**Persistent Menace (Ex)**

**Alters:** The feat gained at 4th level

**Choice:** A siegebreaker must choose either [Step Up](ref/feat/step-up) or
[Disruptive](ref/feat/disruptive) as his bonus feat, but need not meet the prerequisites.

**Gained:** At 4th Level

**Disorienting Blow (Ex)**

**Immediate:** A siegebreaker can distract a foe he just hit with an attack or combat maneuver,
imposing a -2 penalty on the foe's attack rolls, caster level checks, or skill checks for 1 round.
The foe can negate this penalty with a successful Fortitude save (DC = 10 +
[half](ref/misc/fractions-and-rounding) the siegebreaker's fighter level + his Strength modifier).

**At 14th Level:** The penalty increases to -4.

**Gained:** At 8th Level

**Replaces:** The bonus feat gained at 8th level

**Masterful Distraction (Ex)**

**Ability:** A siegebreaker can [nauseate](ref/misc/nauseated) a foe he targets with his
_disorienting blow_ instead of inflicting a penalty.

**Gained:** At 20th Level

**Replaces:** Weapon mastery
