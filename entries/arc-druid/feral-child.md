+++
id = "ref/arc-druid/feral-child"
kind = "archetype"
title = "Feral Child"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Feral%20Child"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_child", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-race-guide"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "illiteracy", level = 1 },
  { anchor = "improved-unarmed-strike", level = 1 },
  { anchor = "beast-family", level = 1 },
  { anchor = "nature-bond", level = 1 },
  { anchor = "favored-terrain", level = 3 },
  { anchor = "native-cunning", level = 3 },
  { anchor = "native-fortitude", level = 4 },
  { anchor = "native-call", level = 9 },
]
trades = [
  { replaces = "Trackless step", feature = "trackless-step", by = ["favored-terrain"] },
  { replaces = "a thousand faces", feature = "a-thousand-faces", by = ["favored-terrain"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["native-cunning"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["native-fortitude"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["native-call"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["native-call"] },
]
+++

Some youths, abandoned in the wilderness and then raised by animals, are so connected with their
adoptive home and family that they become feral. Suspicious of civilized society, these foundlings
often choose allegiance to the wild over their human forebears. A feral child has the following
class features.

**Prerequisites:** Human

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A feral child loses proficiency with the scimitar, scythe, and sickle and with shields.

## Class Skills {#class-skills}

A feral child adds Acrobatics to her list of class skills and removes Fly and Profession from her
list of class skills.

## Illiteracy {#illiteracy}

At 1st level, a feral child is unable to read and write, though she may learn by taking 1 rank of
Linguistics. She does not gain Druidic as a free language and cannot select Sylvan as a bonus
language.

## Improved Unarmed Strike {#improved-unarmed-strike}

At 1st level, a feral child gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat.

## Beast Family (Ex) {#beast-family}

At 1st level, a feral child may choose one specific type of animal as the type that raised her. She
gains a +2 circumstance bonus on Handle Animal and wild empathy checks with animals of that type,
and she can communicate with them as if using a continual
_[speak with animals](ref/spell/speak-with-animals)_
[spell-like ability](ref/umr/spell-like-abilities), but this ability is nonmagical.

## Nature Bond (Ex) {#nature-bond}

At 1st level, a feral child must select an animal companion as her nature bond.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a feral child gains the [favored terrain](ref/ability/favored-terrain) ability as a
[ranger](ref/class/ranger) of her class level. A feral child may not choose urban as a favored
terrain. This ability replaces trackless step and a thousand faces.

## Native Cunning (Ex) {#native-cunning}

At 3rd level, a feral child gains [trap sense](ref/ability/trap-sense) as a
[barbarian](ref/class/barbarian) of equal level, and in her favored terrain, she immediately
receives a Perception check to notice traps within 10 feet, as the trap spotter rogue talent. In
addition, at 3rd level and every three levels thereafter, she may choose one combat maneuver, and
gains a bonus equal to her trap sense bonus to her CMD against that maneuver. This ability replaces
wild shape.

## Native Fortitude (Ex) {#native-fortitude}

At 4th level, a feral child gains a +1 bonus on saving throws against disease,
[exhaustion](ref/misc/exhausted), [fatigue](ref/misc/fatigued), fear, and poison. When she is in her
favored terrain, she instead applies her favored terrain bonus on such saving throws. She also
recovers from [ability damage](ref/rule/ability-damage-drain), exhaustion, and fatigue at twice the
normal rate. This ability replaces resist nature's lure.

## Native Call (Su) {#native-call}

At 9th level, when in her favored terrain, for any
_[summon nature's ally](ref/spell/summon-natures-ally)_ spells a feral child uses to summon animals
that are native to that terrain, she treats the duration of the spell as if she were 2 levels
higher.

At 17th level, when the feral child uses _[summon nature's ally](ref/spell/summon-natures-ally)_
spells to summon such animals, those animals gain a +2 bonus to both their Strength and Constitution
ability scores. This stacks with the effects of the Augmented Summoning feat.

This ability replaces venom immunity and timeless body.
