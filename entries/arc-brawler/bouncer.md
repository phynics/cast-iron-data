+++
id = "ref/arc-brawler/bouncer"
kind = "archetype"
title = "Bouncer"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Bouncer"
source_ids = ["inner-sea-taverns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bouncer", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "inner-sea-taverns"
page = "58"

[fields]
kind = "archetype"
features = [
  { anchor = "crowd-control" },
  { anchor = "lesser-flexibility", level = 1 },
  { anchor = "drunk-handler", level = 2 },
  { anchor = "drunk-knockout", level = 4 },
  { anchor = "bar-fight-mastery", level = 5 },
]
trades = [
  { replaces = "The bonus feat gained at 2nd level", feature = "bonus-combat-feats", levels = [2], by = ["drunk-handler"] },
  { alters = "Martial flexibility", feature = "martial-flexibility", by = ["lesser-flexibility"] },
  { alters = "Close weapon mastery", feature = "close-weapon-mastery", by = ["bar-fight-mastery"] },
]
+++

Some taverns employ bouncers to keep out undesirables or for when their customers get too rowdy.

## Crowd Control (Ex) {#crowd-control}

When in a bar fight, a bouncer has her tenacity reduced by the crowd at the end of a round by the
minimum possible amount. In addition, when she takes the mix it up action, she reduces the tenacity
of the crowd by an additional amount equal to her brawler level.

## Lesser Flexibility (Ex) {#lesser-flexibility}

A bouncer can use her martial flexibility only a number of times per day equal to 2 +
[half](ref/misc/fractions-and-rounding) her brawler level (minimum 3 times per day).

This alters martial flexibility.

## Drunk Handler (Ex) {#drunk-handler}

At 2nd level, a bouncer gains a +2 circumstance bonus on Intimidate and Sense Motive checks against
foes that are tipsy or worse. In addition, when in a bar fight, she ignores
[damage reduction](ref/rule/damage-reduction) against nonlethal damage her targets have from being
drunk or worse.

This replaces the bonus feat gained at 2nd level.

## Drunk Knockout (Ex) {#drunk-knockout}

At 4th level, a bouncer can use one use of her knockout ability to attempt a similar maneuver in a
bar fight against a major participant who is drunk or worse. She must declare her intent before
attempting her brawling check, and if she hits and reduces the target's tenacity, that target must
succeed at a Fortitude saving throw (DC = 10 + half the bouncer's brawler level + the higher of the
bouncer's Strength or Dexterity modifiers) or immediately be reduced to 0 tenacity.

## Bar Fight Mastery (Ex) {#bar-fight-mastery}

At 5th level, in addition to the benefits of close weapon mastery, when a bouncer confirms a
critical hit against a major participant in a bar fight, she also reduces the tenacity of the crowd
by her normal brawling damage amount (this amount isn't doubled).

This alters close weapon mastery.
