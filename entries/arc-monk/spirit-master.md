+++
id = "ref/arc-monk/spirit-master"
kind = "archetype"
title = "Spirit Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Spirit%20Master"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_master", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "resilient-soul", level = 3 },
  { anchor = "spirit-combat", level = 3 },
  { anchor = "diamond-spirit", level = 5 },
  { anchor = "spirit-burst", level = 7 },
  { anchor = "purifying-palm", level = 15 },
  { anchor = "spirit-flow", level = 19 },
  { anchor = "spirit-mastery", level = 20 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["resilient-soul"] },
  { replaces = "Maneuver training", feature = "maneuver-training", by = ["spirit-combat"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["diamond-spirit"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["spirit-burst"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["purifying-palm"] },
  { replaces = "Empty body", feature = "empty-body", by = ["spirit-flow"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["spirit-mastery"] },
]
+++

Spirit masters are monks who specialize in combating the undead, laying their corpses to rest, and
sending their souls to final judgment.

## Resilient Soul (Ex) {#resilient-soul}

At 3rd level, a spirit master gains a +2 bonus on saving throws against necromancy spells and
effects. This ability replaces still mind.

## Spirit Combat (Su) {#spirit-combat}

At 3rd level, a spirit master can charge his unarmed strike so it affects incorporeal creatures. The
spirit master's unarmed strike deals half damage to incorporeal creatures, or full damage if it's a
magic weapon (such as via an [amulet of mighty fists](ref/magic-wondrous/amulet-of-mighty-fists)).
This benefit lasts for a number of rounds equal to the spirit master's class level. A spirit master
can use this ability a number of times per day equal to 3 + his Wisdom modifier. This ability
replaces maneuver training.

## Diamond Spirit (Ex) {#diamond-spirit}

At 5th level, a spirit master becomes fortified against the effects of
[energy drain](ref/rule/energy-drain-and-negative-levels). When the spirit master gains a negative
level, he does not take any penalties, his total hit points remain unchanged, and he is not
considered lower level for the purpose of level-dependent variables. Once per day when attempting a
Fortitude save to remove a temporary negative level, the spirit master may choose to automatically
succeed. The spirit master still dies if his number of negative levels equals or exceeds his number
of Hit Dice. This ability replaces purity of body.

## Spirit Burst (Su) {#spirit-burst}

At 7th level, whenever a spirit master destroys an undead creature with a melee attack, he may as a
free action expend 2 points from his ki pool to release an 15-foot-radius [burst](ref/misc/burst) of
positive energy centered on the destroyed creature. Undead creatures in the affected area each take
a number of points of damage equal the number of Hit Dice of the destroyed creature. Living
creatures in the area are healed by the same amount. This ability replaces wholeness of body.

## Purifying Palm (Su) {#purifying-palm}

At 15th level, the spirit master gains the ability to alter the balance of positive and negative
energy within an opponent's body. The spirit master can make a purifying palm attack once per day,
and must announce his intention before making a melee attack roll. If his attack deals damage, the
target must attempt a Will save (DC = 10 + 1/2 the spirit master's class level + the spirit master's
Wisdom modifier). On a failed save, the target cannot [channel energy](ref/ability/channel-energy),
nor can it be healed by positive or negative energy. This effect lasts for 1 round per class level.
If the target is an undead creature, it must succeed at its Will save or be instantly destroyed.
This ability replaces quivering palm.

## Spirit Flow (Su) {#spirit-flow}

At 19th level, a spirit master can dramatically alter the flow of his own ki. As an immediate
action, the spirit master can expend 3 ki points to alter his ki for a number of rounds equal to his
class level. During this time, he is healed by negative energy as if he were an undead creature. The
spirit master is still healed by positive energy as normal. This ability replaces empty body.

## Spirit Mastery (Su) {#spirit-mastery}

At 20th level, a spirit master gains DR 10/evil and becomes immune to
[ability drain and ability damage](ref/rule/ability-damage-drain). Additionally, once per week, the
spirit master may bring a dead creature back to life. This ability functions as
[true resurrection](ref/spell/true-resurrection), except the spirit master may not resurrect a
creature that has been dead for longer than 1 day per class level. This ability replaces perfect
self.
