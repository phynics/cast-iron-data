+++
id = "ref/arc-inquisitor/kinslayer"
kind = "archetype"
title = "Kinslayer"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Kinslayer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kinslayer", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-race-guide"
page = "98"

[fields]
kind = "archetype"
replaces = ["Destruction judgment", "Detect alignment"]
alters = ["Teamwork feats"]
replaces_features = ["detect-alignment"]
+++

Appalled and guilt-ridden by the horrific circumstances of her birth, a kinslayer dedicates herself
to eradicating the very creatures whose blood flows within her veins. She spends her life hunting
and slaying those vampiric monsters for whom humans have become prey. A kinslayer has the following
class features.

**Prerequisites:** Dhampir

**Judgment (Su)**

**Info:** A kinslayer gains the following judgment.

**Gained:** At 1st Level

**Replaces:** _[Destruction](ref/spell/destruction)_ judgment

**Slayer's Brand (Su)**

**Ability:** When using this judgment, the kinslayer gains the ability to brand undead creatures
with positive energy. To do so, she must make a successful melee touch attack against the undead
creature. This attack deals an amount of positive energy damage equal to 1d6 + the kinslayer's
Charisma modifier, and burns her personal symbol into the undead creature's flesh, bone, or even its
incorporeal form. From that point onward, the kinslayer can sense the existence of the branded
creature as if it were the target of a [locate creature](ref/spell/locate-creature) spell (caster
level equal to 1/2 the kinslayer's inquisitor level).

**Special:** A _slayer's brand_ lasts until the undead creature is destroyed or until the kinslayer
uses this ability on another creature.

**Greater Brand (Su)**

**Ability:** Whenever she gains the ability to learn a teamwork feat, she can instead opt to learn
one of the following modifications to her _slayer's brand_ judgment.

**Alters:** Teamwork feats

**Flavor:** A kinslayer learns to modify her _slayer's brand_ judgment as she gains levels.

**Gained:** At 1st Level

**Special:** Each time the kinslayer opts to take a greater brand, it replaces her ability to gain a
teamwork feat at that level.

**Branding Ray**

**Ability:** The _slayer's brand_ judgment can be used as a ranged touch attack with a range of 20
feet.

**Special:** A kinslayer can take this modification more than once. Whenever she does, she increases
the range of her _[brand](ref/spell/brand)_ by 20 feet.

**Debilitating Brand**

**Passive:** A creature currently affected by the _slayer's brand_ judgment takes a -2 penalty on
attack rolls against the kinslayer who placed the _[brand](ref/spell/brand)._

**Devastating Brand**

**Ability:** When the kinslayer attacks a creature that she has branded with her _slayer's brand,_
she threatens a critical hit on a roll of 19-20. If the kinslayer is good, she also gains a +2
sacred bonus on all rolls to confirm critical hits on a branded creature.

**Dual Brand**

**Ability:** The kinslayer can have up to two creatures branded at a time.

**Holy Brand**

**Ability:** The kinslayer can use her _[brand](ref/spell/brand)_ on creatures with the evil subtype
as well as undead.

**Searing Brand**

**Ability:** The kinslayer's _slayer's brand_ deals an additional 1d6 points of damage for every
five inquisitor levels she has. If the creature hit with the _slayer's brand_ is particularly
vulnerable to bright light, the damage dice of her _slayer's brand_ increases to d8s.

**Prereq:** 6th-Level Inquisitor

**Silver Brand**

**Ability:** The kinslayer can use her _[brand](ref/spell/brand)_ on lycanthropes and creatures with
vulnerability to silver as well as undead.

**Undead Sense (Sp)**

**Ability:** A kinslayer gains the ability to use [detect undead](ref/spell/detect-undead) as a
[spell-like ability](ref/umr/spell-like-abilities) (caster level equal to the kinslayer's inquisitor
level) at will. If she detects the presence of undead, she can use her _monster lore_ ability to
attempt to determine the type of undead detected as well as to reveal any strengths or weaknesses
the undead might have. If any of the detected undead are vampires, she gains a bonus on the check
equal to her inquisitor level to immediately identify them as such.

**Gained:** At 2nd Level

**Replaces:** Detect alignment
