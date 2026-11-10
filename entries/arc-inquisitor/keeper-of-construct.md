+++
id = "ref/arc-inquisitor/keeper-of-construct"
kind = "archetype"
title = "Keeper of Construct"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Keeper%20of%20Construct"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "keeper_of_construct", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "27"

[fields]
kind = "archetype"
replaces = ["Domain", "Stern gaze", "Monster lore", "Exploit weakness"]
replaces_features = ["domain", "stern-gaze", "monster-lore", "exploit-weakness"]
+++

Some of Brigh's inquisitors, and occasionally those who follow Torag, track down malicious construct
crafters and fight renegade constructs with unrivaled expertise.

**Penetrating Blows (Ex)**

**Flavor:** A keeper of constructs' attacks are divinely guided to pierce the defenses of
constructs.

**At 16th Level:** She ignores the first 10 points of DR or [hardness](ref/umr/hardness) when
attacking constructs.

**At 8th Level:** She ignores the first 5 points of DR or [hardness](ref/umr/hardness) when
attacking constructs.

**Passive:** The keeper of constructs treats her weapons as [adamantine](ref/eq-material/adamantine)
for the purpose of overcoming [damage reduction](ref/rule/damage-reduction) when attacking
constructs.

**Replaces:** Domain

**Construct Influence (Ex)**

**Ability:** She can use the [Intimidate](ref/skill/intimidate) skill to demoralize constructs, and
when she attempts to do so, she gains a bonus on the check equal to half her inquisitor level
(minimum 1).

**Flavor:** A keeper of constructs' knowledge of constructs' inner workings allows her to gain an
upper hand over constructs.

**Replaces:** Stern gaze

**Construct Lore (Ex)**

**Passive:** A keeper of constructs adds twice her Wisdom modifier plus her Intelligence modifier as
a bonus when attempting Knowledge checks to identify the abilities and weaknesses of constructs.

**Replaces:** Monster lore

**Wrest Control (Sp)**

**Gained:** At 14th Level

**Replaces:** Exploit weakness

**Special:** If an affected construct was being controlled by a creature, that individual can regain
control of the construct with a successful Charisma check (attempting this check requires a standard
action) opposed by the inquisitor's Charisma check. On a success, the original creature regains full
control of the construct and this effect ends.

**Standard:** The keeper of constructs can issue a command to a construct. This functions as a
[suggestion](ref/spell/suggestion) spell that is [dismissible](ref/misc/dismissible), affects the
construct despite its normal immunity to mind-affecting effects, and has a caster level equal to the
keeper of constructs' inquisitor level. The construct can resist the command with a successful Will
saving throw (DC = 10 + half the keeper of constructs' inquisitor level + her Wisdom modifier). A
construct that successfully saves is immune to this ability for the following 24 hours. This effect
immediately ends if the construct is attacked while under its influence.

**Usage:** Three times per day

**Usage:** Three times per day
