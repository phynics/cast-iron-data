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
features = [
  { anchor = "breaker-rush", level = 1 },
  { anchor = "armored-vigor", level = 2 },
  { anchor = "breaker-momentum", level = 2 },
  { anchor = "persistent-menace", level = 4 },
  { anchor = "disorienting-blow", level = 8 },
  { anchor = "masterful-distraction", level = 20 },
]
trades = [
  { replaces = "The feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["breaker-rush"] },
  { replaces = "Bravery", feature = "bravery", by = ["armored-vigor"] },
  { replaces = "The feat gained at 2nd level", feature = "bonus-feats", levels = [2], by = ["breaker-momentum"] },
  { replaces = "The bonus feat gained at 8th level", feature = "bonus-feats", levels = [8], by = ["disorienting-blow"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["masterful-distraction"] },
  { alters = "The feat gained at 4th level", feature = "bonus-feats", levels = [4], by = ["persistent-menace"] },
]
+++

The siegebreaker is trained to break through lines of enemy soldiers.

## Breaker Rush (Ex) {#breaker-rush}

At 1st level, a siegebreaker can attempt [bull rush](ref/rule/bull-rush) or
[overrun](ref/rule/overrun) combat maneuvers without provoking attacks of opportunity. When he
performs either combat maneuver, he deals an amount of bludgeoning damage equal to his Strength
bonus (minimum 1). If he has [Improved Bull Rush](ref/feat/improved-bull-rush) or
[Improved Overrun](ref/feat/improved-overrun), the damage dealt by the appropriate maneuver
increases by 2 and he adds any enhancement bonus from his armor or shield (though such enhancement
bonuses do not stack, if both armor and shield are magic). This ability replaces the feat gained at
1st level.

## Armored Vigor (Ex) {#armored-vigor}

At 2nd level as a swift action, a siegebreaker can gain 2
[temporary hit points](ref/rule/temporary-hit-points) that last for 1 minute. He can use this
ability a number of times per day equal to 3 + his Constitution modifier (minimum 1 per day), but
only while wearing armor. At 6th level and every 4 levels thereafter, the number of temporary hit
points the siegebreaker gains increases by 2, to a maximum of 10 at 18th level. This ability
replaces bravery.

## Breaker Momentum (Ex) {#breaker-momentum}

At 2nd level, when a siegebreaker successfully bull rushes a foe, he can attempt an overrun combat
maneuver check against that foe as a free action. This ability replaces the feat gained at 2nd
level.

## Persistent Menace (Ex) {#persistent-menace}

At 4th level, a siegebreaker must choose either [Step Up](ref/feat/step-up) or
[Disruptive](ref/feat/disruptive) as his bonus feat, but need not meet the prerequisites.

## Disorienting Blow (Ex) {#disorienting-blow}

At 8th level, as an immediate action, a siegebreaker can distract a foe he just hit with an attack
or combat maneuver, imposing a -2 penalty on the foe's attack rolls, caster level checks, or skill
checks for 1 round. The foe can negate this penalty with a successful Fortitude save (DC = 10 + 1/2
the siegebreaker's fighter level + his Strength modifier). At 14th level, the penalty increases to
-4. This ability replaces the bonus feat gained at 8th level.

## Masterful Distraction (Ex) {#masterful-distraction}

At 20th level, a siegebreaker can [nauseate](ref/misc/nauseated) a foe he targets with his
disorienting blow instead of inflicting a penalty. This ability replaces weapon mastery.
