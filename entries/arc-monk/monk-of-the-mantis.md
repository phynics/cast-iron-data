+++
id = "ref/arc-monk/monk-of-the-mantis"
kind = "archetype"
title = "Monk of the Mantis"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Mantis"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_mantis", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "pressuring-strikes", level = 2 },
  { anchor = "debilitating-blows", level = 7 },
  { anchor = "disabling-palm", level = 15 },
]
trades = [
  { replaces = "2nd-, 6th-, 10th-, 14th-, and 18th-level bonus feats", feature = "bonus-feat", levels = [2, 6, 10, 14, 18], by = ["pressuring-strikes"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["debilitating-blows"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["debilitating-blows"] },
  { replaces = "diamond soul", feature = "diamond-soul", by = ["debilitating-blows"] },
  { alters = "Quivering palm", feature = "quivering-palm", by = ["disabling-palm"] },
]
+++

A body contains many points where the flesh, mind, and spirit coincide. A monk of the mantis is
skilled at manipulating these points. With precise strikes, she temporarily disrupts a body's
connection with the rest of the self.

## Pressuring Strikes (Ex) {#pressuring-strikes}

At 2nd level, a monk of the mantis gains the [sneak attack](ref/ability/sneak-attack) ability. This
ability functions as the [rogue](ref/class/rogue) ability of the same name, except it can be used
only during a flurry of blows. The initial sneak attack damage is +1d6, and the damage increases by
1d6 every 4 levels beyond 2nd. This ability replaces the monk's 2nd-, 6th-, 10th-, 14th-, and
18th-level bonus feats.

## Debilitating Blows (Ex) {#debilitating-blows}

A monk of the mantis's knowledge of anatomy allows her to deal blows that both deal damage and
impose debilitating conditions. At 7th level, if a monk of the mantis stuns a target with
[Stunning Fist](ref/feat/stunning-fist), the target is also [entangled](ref/rule/entangled) for 1
round after the Stunning Fist effect ends. At 11th level, if the monk of the mantis stuns a target
with Stunning Fist, the target is also [exhausted](ref/misc/exhausted) for 1 round after the
Stunning Fist effect ends. At 13th level, the monk can spend 1 point from her ki pool as part of her
Stunning Fist attack to increase the duration of these additional effects to a number of rounds
equal to her Wisdom bonus (minimum 2 rounds). This ability replaces wholeness of body, diamond body,
and diamond soul. (For the unchained monk from _Pathfinder RPG Pathfinder Unchained_, this ability
is gained at 6th level, improves at 10th and 12th levels, and replaces the ki powers gained at those
levels.)

## Disabling Palm (Su) {#disabling-palm}

At 15th level, a monk of the mantis can render the target of her quivering palm
[unconscious](ref/misc/unconscious) instead of killing the creature. Upon failing its Fortitude
saving throw, the target either is knocked unconscious for a number of minutes equal to the monk of
the mantis's monk level or dies (the monk of the mantis's choice). This alters quivering palm. (For
the monk class from _Pathfinder Unchained_, this ability applies only if the monk selects the
quivering palm ki power.)
