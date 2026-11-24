+++
id = "ref/arc-ranger/wild-stalker"
kind = "archetype"
title = "Wild Stalker"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wild%20Stalker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_stalker", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "68"

[fields]
kind = "archetype"
trades = [
  { replaces = "1st favored enemy", feature = "favored-enemy", levels = [1] },
  { replaces = "2nd-level combat style feat", feature = "combat-style-feat", levels = [2] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond" },
  { replaces = "2nd, 3rd, 4th, and 5th favored enemy", feature = "favored-enemy", levels = [5, 10, 15, 20] },
  { replaces = "6th-, 10th-, 14th-, and 18th-level combat style feat", feature = "combat-style-feat", levels = [6, 10, 14, 18] },
]
+++

Civilization grows stronger and more decadent with each passing year. It tears into unclaimed
wilderness and destroys the fragile ecology in its constant push for expansion and exploitation. The
wild stalker forsakes the bonds of community and lives in the trackless wilds far from others of his
kind, or perhaps grew up there, never knowing of civilization as anything more than his enemy. He
drives pioneers back to civilization and strives to keep the land unspoiled.

**Strong Senses (Ex)**

**Ability:** He gains [low-light vision](ref/rule/low-light-vision) and a bonus on Perception checks
equal to 1 + [one-fourth](ref/misc/fractions-and-rounding) of his ranger level. If he already has
low-light vision, the bonus becomes 2 + one-fourth of his ranger level.

**Flavor:** A wild stalker's life among the wild has sharpened his senses.

**Gained:** At 1st Level

**Replaces:** 1st favored enemy

**Uncanny Dodge (Ex)**

**Ability:** A wild stalker gains [uncanny dodge](ref/ability/uncanny-dodge) as the barbarian class
feature.

**Gained:** At 2nd Level

**Replaces:** 2nd-level combat style feat

**Rage of the Wild (Ex)**

**Ability:** A wild stalker gains the _rage_ ability as the [barbarian](ref/class/barbarian) class
feature, but its barbarian level is considered to be his ranger level - 3.

**Gained:** At 4th Level

**Replaces:** Hunter's bond

**Rage (Ex)**

**Flavor:** Text from the barbarian class.

**Free:** You can enter (or end) a _rage._ You gain a +4 morale bonus to your Strength and
Constitution, as well as a +2 morale bonus on Will saves. The increase to Constitution grants you 2
hit points per Hit Dice, but these disappear when the _rage_ ends and are not lost first like
[temporary hit points](ref/rule/temporary-hit-points).

**Passive:** While in _rage,_ you take a -2 penalty to Armor Class, and you cannot use any
Charisma-, Dexterity-, or Intelligence-based skills (except Acrobatics, Fly, Intimidate, and Ride)
or any ability that requires patience or concentration. You are [fatigued](ref/misc/fatigued) after
_rage_ for a number of rounds equal to 2 times the number of rounds spent in the _rage._ You cannot
enter a new _rage_ while fatigued or [exhausted](ref/misc/exhausted) but can otherwise enter _rage_
multiple times during a single encounter or combat. If you fall unconscious, your _rage_ immediately
ends, placing you in peril of death.

**Special:** Temporary increases to Constitution, such as those gained from _rage_ and spells like
[bear's endurance](ref/spell/bears-endurance), do not increase the total number of rounds that a
barbarian can _rage_ per day. The total number of rounds of _rage_ per day is renewed after resting
for 8 hours, although these hours do not need to be consecutive.

**Usage:** 2 rounds/day + double your barbarian level + your Constitution modifier

**Usage:** 2 rounds/day + double your barbarian level + your Constitution modifier

**Rage Powers**

**Ability:** A wild stalker ranger gains a single rage power, as the barbarian class feature.

**Gained:** At 5th Level

**Repeat:** He gains another rage power., 10, 5

**Replaces:** 2nd, 3rd, 4th, and 5th favored enemy

**Wild Talents (Ex)**

**Choice:** A wild stalker can either take a rage power, or gain a +2 insight bonus into any one of
the following skills: Acrobatics, Climb, Perception, Stealth, Survival, or Swim.

**Gained:** At 6th Level

**Repeat:** The wild stalker can gain one of these two benefits again., 10, 4

**Replaces:** 6th-, 10th-, 14th-, and 18th-level combat style feat
