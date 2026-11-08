+++
id = "ref/arc-barbarian/wild-rager"
kind = "archetype"
title = "Wild Rager"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]

[fields]
kind = "archetype"
replaces = ["Uncanny dodge", "Improved uncanny dodge"]
+++

**Sources:** Ultimate Combat pg 31\
Rages are barely controlled, but there are those who wholly give in to their more savage side,
letting their rages take them to a confusing and uncontrolled place of terrible savagery. These
barbarians become beasts, consumed with absolute bloodlust to the point where they cannot tell
friend from foe.

**Uncontrolled Rage (Ex)**

**Passive:** A wild rager's _rage_ functions as normal, except that when she reduces a creature to 0
or fewer hit points, she must attempt a Will save (DC 10 + [half](ref/misc/fractions-and-rounding)
the barbarian's level + the barbarian's Constitution modifier) or become _confused._ For the
remainder of her current turn, she attacks the nearest creature other than herself. On the following
round, refer to the [confusion](ref/spell/confusion) spell to determine her actions. At the end of
this round, and each round thereafter, she can attempt a new saving throw to end the confusion
effect.

**Special:** The rounds during which she is confused do not count against the rounds she has spent
_raging_ that day, but she cannot end her _rage_ voluntarily, nor can she use rage powers while
confused.

**Wild Fighting (Ex)**

**Ability:** A wild rager using the [full-attack](ref/rule/full-attack) action can make one extra
attack per round at her highest base attack bonus. Until the beginning of her next turn, however,
she takes a -2 penalty on attack rolls and -4 penalty to AC.

**Flavor:** Even when not _raging,_ wild ragers often fight with reckless, savage abandon.

**Gained:** At 2nd Level

**Replaces:** Uncanny dodge

**Rage Conversion (Ex)**

**Gained:** At 5th Level

**Passive:** A wild rager who fails a saving throw against any mind-affecting effect can attempt a
new saving throw at the beginning of her next turn. If the save succeeds, that effect ends and she
instead rages and becomes confused as noted above.

**Replaces:** Improved uncanny dodge

**Rage Powers:** The following rage powers complement the wild rager archetype:
[animal fury](ref/ragepower/animal-fury), [bleeding blow](ref/ragepower/bleeding-blow),
[body bludgeon](ref/ragepower/body-bludgeon), [brawler](ref/ragepower/brawler),
[crippling blow](ref/ragepower/crippling-blow), [greater brawler](ref/ragepower/greater-brawler),
[intimidating glare](ref/ragepower/intimidating-glare), [mighty swing](ref/ragepower/mighty-swing),
[no escape](ref/ragepower/no-escape), [powerful blow](ref/ragepower/powerful-blow),
[quick reflexes](ref/ragepower/quick-reflexes).
