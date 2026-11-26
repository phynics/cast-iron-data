+++
id = "ref/arc-fighter/sensate"
kind = "archetype"
title = "Sensate"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Sensate"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sensate", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "occult-adventures"
page = "118"

[fields]
kind = "archetype"
features = [
  { anchor = "guarded-senses", level = 2 },
  { anchor = "uncanny-dodge", level = 3 },
  { anchor = "centered-senses", level = 5 },
  { anchor = "improved-uncanny-dodge", level = 7 },
  { anchor = "evasion", level = 11 },
  { anchor = "steady", level = 15 },
  { anchor = "perfect-senses", level = 19 },
  { anchor = "precision", level = 20 },
]
trades = [
  { replaces = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Bravery", feature = "bravery", by = ["guarded-senses"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["uncanny-dodge"] },
  { replaces = "Weapon training 2, 3, and 4", feature = "weapon-training", levels = [9, 13, 17], by = ["centered-senses"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["improved-uncanny-dodge"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["evasion"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["steady"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["perfect-senses"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["precision"] },
  { replaces = "Class skills" },
]
+++

A sensate perceives battle through senses beyond mortal ken, anticipating his opponents' movements
before they even begin to act. As long as he keeps his focus about him, he fights with a skill
rivaling that of the finest masters-at-arms.

## Skills {#skills}

The sensate's class skills are Acrobatics (Dex), Climb (Str), Craft (Int), Perception (Wis),
Profession (Wis), Ride (Dex), Sense Motive (Wis), Survival (Wis), and Swim (Str). This replaces the
fighter's class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Sensates are proficient with all simple and martial weapons, light armor, medium armor, and shields
(except tower shields). This replaces the fighter's weapon and armor proficiency.

## Guarded Senses (Su) {#guarded-senses}

At 2nd level, a sensate gains a +1 bonus on saves against sonic effects, figments, glamers,
patterns, [gaze](ref/umr/gaze) attacks, and scent-based attacks. This bonus increases by 1 for every
4 levels the sensate possesses beyond 2nd. This ability replaces bravery.

## Uncanny Dodge (Su) {#uncanny-dodge}

At 3rd level, a sensate gains [uncanny dodge](ref/ability/uncanny-dodge) as the
[barbarian](ref/class/barbarian) ability of the same name, except supernatural in nature. This
ability replaces armor training 1.

## Centered Senses (Su) {#centered-senses}

At 5th level, a sensate can center his senses as a move action. While centered, a sensate gains a +1
insight bonus on attack rolls, weapon damage rolls, and Will saves. This bonus increases by 1 at 9th
level and every 4 levels thereafter. A sensate loses his centered state if he gains the confused,
dazed, fascinated, staggered, or stunned condition; falls unconscious; or fails a Will save. This
ability replaces weapon training 2, 3, and 4.

## Improved Uncanny Dodge (Su) {#improved-uncanny-dodge}

At 7th level, a sensate gains [improved uncanny dodge](ref/ability/improved-uncanny-dodge) as the
barbarian ability of the same name, except supernatural in nature. This ability replaces armor
training 2.

## Evasion (Su) {#evasion}

At 11th level, a sensate gains [evasion](ref/ability/evasion) while using centered senses. This
functions as the rogue ability of the same name, except that it is supernatural in nature and works
regardless of the sensate's armor and encumbrance. This ability replaces armor training 3.

## Steady (Su) {#steady}

At 15th level, a sensate can center himself as a swift action. This ability replaces armor
training 4.

## Perfect Senses (Su) {#perfect-senses}

At 19th level, a sensate's senses reach perfection, and he can easily notice illusions and unseen
foes by combining his senses. While centered, he gains the effects of
_[true seeing](ref/spell/true-seeing)_ as well as [blindsense](ref/umr/blindsense) 60 feet. An
unseen creature that makes no sound and leaves no scent (such as a creature under the effects of
_[invisibility](ref/spell/invisibility)_, _[silence](ref/spell/silence)_, and
_[negate aroma](ref/spell/negate-aroma)_) can still avoid both the
_[true seeing](ref/spell/true-seeing)_ and the [blindsense](ref/rule/blindsight-and-blindsense).

This ability replaces armor mastery.

## Precision (Su) {#precision}

At 20th level, a sensate rolls twice to confirm critical hits while centered, taking the more
favorable result. Opponents must roll twice to confirm critical hits against him, taking the less
favorable result. The latter ability does not function when the sensate is denied his Dexterity
bonus. This ability replaces weapon mastery.
