+++
id = "ref/arc-inquisitor/vigilant-defender"
kind = "archetype"
title = "Vigilant Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Vigilant%20Defender"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vigilant_defender", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "31"

[fields]
kind = "archetype"
replaces = ["Stern gaze", "Exploit weakness"]
alters = ["Judgment", "True judgment"]
+++

Some inquisitors focus more on protecting those who share their faiths and their ideals than on
actively hunting their enemies. These vigilant defenders often work alongside traveling clerics and
paladins.

**Shared Judgments (Su)**

**Alters:** Judgment

**Swift:** Whenever a vigilant defender has pronounced judgment on her foes, she can grant all of
her allies the bonus or special ability that the judgment bestows. If she has multiple active
judgments, they all affect her allies. When she does this, the judgments no longer affect her, and
their effects only last for 1 round, after which that daily use of judgment ends immediately, even
if the combat is not over. The vigilant defender cannot change any of these judgments to another
type during this round.

**Protect the Faithful (Ex)**

**Ability:** Affected allies receive a morale bonus equal to
[one-fourth](ref/misc/fractions-and-rounding) of the vigilant defender's inquisitor level (minimum
+1) on all Bluff, Disguise, Perception, and Stealth checks outside of combat made to avoid, deceive,
or notice other creatures. This bonus lasts for 10 minutes, and the vigilant defender can affect
herself and a number of allies equal to her Wisdom modifier (minimum 1).

**Info:** A vigilant defender can spend 1 minute coaching and teaching a group of allies how best to
avoid scrutiny from those who wish them harm. The vigilant defender and her allies cannot be in
combat or threatened during this coaching, and allies must be able to see and hear the vigilant
defender to benefit from this ability. This ability provides no benefits against enemies that have
heard or seen the coaching.

**Replaces:** Stern gaze

**Usage:** 1 time/day + 1 per 4 inquisitor levels

**Bolster the Wounded (Ex)**

**Flavor:** A vigilant defender can preternaturally sense when her allies are in grave peril and can
form a mystical conduit to protect them from the full effects of grievous wounds.

**Immediate:** Whenever an enemy confirms a critical hit against an ally within 30 feet, the
vigilant defender can choose to accept half the damage. If she does so, similar to the
[shield other](ref/spell/shield-other) spell, any of her
[damage reduction](ref/rule/damage-reduction), resistances, or immunities do not apply to the damage
she takes.

**Gained:** At 14th Level

**Replaces:** Exploit weakness

**True Vengeance (Su)**

**Alters:** True judgment

**Gained:** At 20th Level

**Passive:** When a vigilant defender calls _true judgment_ down upon a foe, if the foe has killed
one of the vigilant defender's allies (permanent sentient allies, such as fellow party members or
cohorts, not summoned monsters, animal companions, pets, or the like), the DC of the target's
Fortitude save to avoid death is 2 higher. If the foe has not damaged any of the vigilant defender's
allies, the DC to avoid death is instead 2 lower.
