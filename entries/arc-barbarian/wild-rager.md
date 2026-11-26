+++
id = "ref/arc-barbarian/wild-rager"
kind = "archetype"
title = "Wild Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Wild%20Rager"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "31"

[fields]
kind = "archetype"
features = [
  { anchor = "uncontrolled-rage" },
  { anchor = "wild-fighting", level = 2 },
  { anchor = "rage-conversion", level = 5 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["wild-fighting"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["rage-conversion"] },
]
+++

Rages are barely controlled, but there are those who wholly give in to their more savage side,
letting their rages take them to a confusing and uncontrolled place of terrible savagery. These
barbarians become beasts, consumed with absolute bloodlust to the point where they cannot tell
friend from foe.

## Uncontrolled Rage (Ex) {#uncontrolled-rage}

A wild rager's rage functions as normal, except that when she reduces a creature to 0 or fewer hit
points, she must attempt a Will save (DC 10 + 1/2 the barbarian's level + the barbarian's
Constitution modifier) or become confused. For the remainder of her current turn, she attacks the
nearest creature other than herself. On the following round, refer to the
_[confusion](ref/spell/confusion)_ spell (_Core Rulebook_ 258) to determine her actions. At the end
of this round, and each round thereafter, she can attempt a new saving throw to end the _confusion_
effect. The rounds during which she is confused do not count against the rounds she has spent raging
that day, but she cannot end her rage voluntarily, nor can she use rage powers while confused.

## Wild Fighting (Ex) {#wild-fighting}

At 2nd level, even when not raging, wild ragers often fight with reckless, savage abandon. A wild
rager using the [full-attack](ref/rule/full-attack) action can make one extra attack per round at
her highest base attack bonus. Until the beginning of her next turn, however, she takes a -2 penalty
on attack rolls and -4 penalty to AC. This ability replaces uncanny dodge.

## Rage Conversion (Ex) {#rage-conversion}

At 5th level, a wild rager who fails a saving throw against any mind-affecting effect can attempt a
new saving throw at the beginning of her next turn. If the save succeeds, that effect ends and she
instead rages and becomes confused as noted above. This ability replaces improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the wild rager archetype:
[animal fury](ref/ragepower/animal-fury), [bleeding blow](ref/ragepower/bleeding-blow),
[body bludgeon](ref/ragepower/body-bludgeon), [brawler](ref/ragepower/brawler),
[crippling blow](ref/ragepower/crippling-blow), [greater brawler](ref/ragepower/greater-brawler),
[intimidating glare](ref/ragepower/intimidating-glare), [mighty swing](ref/ragepower/mighty-swing),
[no escape](ref/ragepower/no-escape), [powerful blow](ref/ragepower/powerful-blow), and
[quick reflexes](ref/ragepower/quick-reflexes).
