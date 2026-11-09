+++
id = "ref/arc-brawler/bouncer"
kind = "archetype"
title = "Bouncer"
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
replaces = ["The bonus feat gained at 2nd level"]
alters = ["Martial flexibility", "Close weapon mastery"]
+++

Some taverns employ bouncers to keep out undesirables or for when their customers get too rowdy.

> **Note:** This archetype extensively uses the optional [Bar Fights](ref/rule/bar-fights) rules.

**Crowd Control (Ex)**

**Passive:** When in a bar fight, a bouncer has her tenacity reduced by the crowd at the end of a
round by the minimum possible amount. In addition, when she takes the mix it up action, she reduces
the tenacity of the crowd by an additional amount equal to her brawler level.

**Lesser Flexibility (Ex)**

**Ability:** A bouncer can use her martial flexibility only a number of times per day equal to 2 +
[half](ref/misc/fractions-and-rounding) her brawler level (minimum 3 times per day).

**Alters:** Martial flexibility

**Drunk Handler (Ex)**

**Gained:** At 2nd Level

**Passive:** A bouncer gains a +2 circumstance bonus on Intimidate and Sense Motive checks against
foes that are tipsy or worse. In addition, when in a bar fight, she ignores
[damage reduction](ref/rule/damage-reduction) against nonlethal damage her targets have from being
drunk or worse.

**Replaces:** The bonus feat gained at 2nd level

**Drunk Knockout (Ex)**

**Ability:** A bouncer can use one use of her _knockout_ ability to attempt a similar maneuver in a
bar fight against a major participant who is drunk or worse. She must declare her intent before
attempting her brawling check, and if she hits and reduces the target's tenacity, that target must
succeed at a Fortitude saving throw (DC = 10 + half the bouncer's brawler level + the higher of the
bouncer's Strength or Dexterity modifiers) or immediately be reduced to 0 tenacity.

**Gained:** At 4th Level

**Bar Fight Mastery (Ex)**

**Alters:** Close weapon mastery

**Gained:** At 5th Level

**Passive:** In addition to the benefits of _close weapon mastery,_ when a bouncer confirms a
critical hit against a major participant in a bar fight, she also reduces the tenacity of the crowd
by her normal brawling damage amount (this amount isn't doubled).
