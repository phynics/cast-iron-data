+++
id = "ref/arc-oracle/river-soul"
kind = "archetype"
title = "River Soul"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20River%20Soul"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "river_soul", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "68"

[fields]
kind = "archetype"
features = [
  { anchor = "river-bound-curse", level = 1 },
  { anchor = "revelations", level = 1 },
  { anchor = "river-flow", level = 1 },
  { anchor = "river-form", level = 11 },
  { anchor = "river-soul-revelation", level = 20 },
]
trades = [
  { replaces = "The class skills granted by the oracle's mystery", feature = "mystery", power = "class skills" },
  { replaces = "The oracle's mystery bonus spells at these levels", feature = "mystery", levels = [2, 6, 8, 10, 18], power = "bonus spells" },
  { replaces = "Oracle's curse", feature = "oracle-s-curse", by = ["river-bound-curse"] },
  { replaces = "Revelations gained at 1st and 11th levels", feature = "revelation", levels = [1, 11], by = ["revelations"] },
  { replaces = "Final revelation", feature = "final-revelation", by = ["river-soul-revelation"] },
]
+++

River soul oracles derive their powers from their bonds with rivers, whether these waterways are
rapid cascades or lazy channels plied by boats. The powerful bond formed with a river is also the
river soul oracle's curse, as he must always carry water from the river with him, and his fate is
bound to it. River soul oracles can be gentle and still when calm, but they're raging torrents when
angered.

## Class Skills {#class-skills}

A river soul oracle adds Escape Artist, Knowledge (nature), Survival, and Swim to his list of class
skills.

This replaces the class skills granted by the oracle's mystery and alters the oracle's class skills.

## Recommended Mysteries {#recommended-mysteries}

Life, nature, stone, waves.

## Bonus Spells {#bonus-spells}

_Hydraulic push_ (2nd), _hydraulic torrent_ (6th), _control water_ (8th), _cone of cold_ (10th),
_world wave_ (18th). These bonus spells replace the oracle's mystery bonus spells at these levels.

## River Bound Curse (Su) {#river-bound-curse}

You bind your power to one particular river, which is the source of your spells and class abilities.
You must carry a small vessel containing water from the river you are bound to at all times. If the
vessel is destroyed or travels more than 10 feet away from you, you are unable to cast oracle spells
or use your supernatural or spell-like class abilities until you recover the vessel or fill a new
one with water from the river to which you are bound. Once per month, you can bond with a different
river in a ceremony at that river that takes 12 hours to complete. You lose your bond with the
previous river in the process.

This replaces oracle's curse.

## Revelations {#revelations}

A river soul oracle must take the following revelations at the listed levels.

## River Flow (Su) {#river-flow}

At 1st level, as a free action while you are underwater, you can negate the
[penalties you take](ref/rule/underwater-combat) for making bludgeoning, piercing, and slashing
melee attacks underwater. You can use this ability a number of rounds per day equal to 1 + your
Charisma modifier (minimum 1). The rounds do not have to be used consecutively.

## River Form (Su) {#river-form}

At 11th level, you can become one with a river. Once a day as a standard action, while immersed in a
river, you can completely merge with it. Your body and all your gear meld into the water, as per
_[meld into stone](ref/spell/meld-into-stone)_, except abilities that control or shape water expel
you and deal you 5d6 damage rather than abilities that control or shape stone. You travel along with
the river at the rate it is currently moving. You can remain in this form a number of hours equal to
3 + your Charisma modifier (minimum 1). Transforming back to your normal form is a swift action.

## River Soul Revelation (Su) {#river-soul-revelation}

At 20th level, you strengthen your ties to the river with which you bonded. While traveling on or
immersed in the river, you gain [fast healing](ref/umr/fast-healing) 10 and immunity to bleed, death
attacks, exhaustion, fatigue, nausea effects, negative levels, and sickened effects. Additionally,
if you are slain and your body or some part of your body (including your ashes, if applicable) is
floated down the river in a specially prepared vessel costing 5,000 gp, you return to life as per
_[resurrection](ref/spell/resurrection)_ once you reach the mouth of the river, as long as the trip
has taken 24 hours or longer.

This replaces final revelation.
