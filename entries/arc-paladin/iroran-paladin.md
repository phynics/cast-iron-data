+++
id = "ref/arc-paladin/iroran-paladin"
kind = "archetype"
title = "Iroran Paladin"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Iroran%20Paladin"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iroran_paladin", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "inner-sea-combat"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "confident-defense", level = 1 },
  { anchor = "unarmed-strike", level = 1 },
  { anchor = "aura-of-law", level = 1 },
  { anchor = "sense-perfection", level = 1 },
  { anchor = "personal-trial", level = 1 },
  { anchor = "aura-of-excellence", level = 3 },
  { anchor = "ki-pool", level = 4 },
  { anchor = "divine-body", level = 5 },
  { anchor = "aura-of-perfection", level = 11 },
]
trades = [
  { replaces = "Proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["confident-defense"] },
  { replaces = "heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["confident-defense"] },
  { replaces = "and shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["confident-defense"] },
  { replaces = "Aura of good", feature = "aura-of-good", by = ["aura-of-law"] },
  { replaces = "Detect evil", feature = "detect-evil", by = ["sense-perfection"] },
  { replaces = "Smite evil", feature = "smite-evil", by = ["personal-trial"] },
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["aura-of-excellence"] },
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["ki-pool"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["divine-body"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["aura-of-perfection"] },
]
+++

Iroran paladins meditate on self-perfection and train relentlessly, knowing that their example can
inspire others to excel. [Irori](ref/faith/irori) offers no universal paladin code—each paladin in
his service creates his own code as part of his spiritual journey, seeing the adherence to such a
self-formulated creed as one of the many tests one must face to reach perfection.

## Skills {#skills}

An Iroran paladin gains Acrobatics, Climb, and Swim as class skills.

## Confident Defense (Ex) {#confident-defense}

At 1st level, when wearing light or no armor and not using a shield, an Iroran paladin adds 1 point
of his Charisma bonus (if any) per class level to his Dexterity bonus to his Armor Class. If he is
caught [flat-footed](ref/rule/flat-footed) or otherwise denied his Dexterity bonus, he also loses
this bonus. This ability replaces his proficiency with medium armor, heavy armor, and shields.

## Unarmed Strike {#unarmed-strike}

At 1st level, an Iroran paladin gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as
a bonus feat. In addition, he gains the unarmed strike [monk](ref/class/monk) ability, treating his
monk level as half his paladin level (minimum 1) for calculating his unarmed strike damage.

## Aura of Law (Su) {#aura-of-law}

The power of an Iroran paladin's aura of law is equal to his class level. This ability replaces aura
of good.

## Sense Perfection (Su) {#sense-perfection}

At 1st level, at will, an Iroran paladin can detect life forces as if he were using a paladin's
[detect evil](ref/spell/detect-evil) class ability; however, instead of sensing evil creatures, he
senses creatures that have a ki pool. Each such creature has an aura like a cleric of an aligned
deity, and treats its current number of ki points as its Hit Dice for the purposes of this ability.
This ability replaces detect evil.

## Personal Trial (Su) {#personal-trial}

Once per day, an Iroran paladin can as a swift action declare one target within line of sight as his
personal trial. The Iroran paladin gains a +1 insight bonus on attack rolls and damage rolls against
that creature, to his AC against attacks made by the target, and on saving throws against the
target's spells and special abilities. This bonus increases by 1 at 4th level and every 4 levels
thereafter, to a maximum bonus of +6 at 20th level. The personal trial effect remains until the
target of the trial is dead or the next time the paladin rests and regains daily uses of this
ability. At 4th level and every three levels thereafter, the Iroran paladin can use personal trial
one additional time per day. This ability replaces smite evil.

## Aura of Excellence (Su) {#aura-of-excellence}

At 3rd level, an Iroran paladin is immune to any effect that would force him to reroll a die against
his will or roll twice and take the lower result. Whenever an ally within 10 feet of him would
reroll a die against her will, she can roll twice and take the higher result. Whenever an ally
within 10 feet would be forced to roll twice and take the lower result, she can instead roll three
times and take the second-lowest result. This ability functions only while the Iroran paladin is
conscious, and replaces aura of courage.

## Ki Pool (Su) {#ki-pool}

At 4th level, an Iroran paladin gains a ki pool with an effective monk level equal to his class
level. The number of points in an Iroran paladin's ki pool is equal to 1/2 his class level + his
Charisma modifier. By spending 1 point from his ki pool, he can ignore any
[damage reduction](ref/rule/damage-reduction) possessed by the target of his personal trial ability
for 1 round. This ability otherwise functions as the monk ability of the same name and replaces
channel positive energy.

## Divine Body (Su) {#divine-body}

Upon reaching 5th level, an Iroran paladin must form a bond with a weapon, except he can only choose
to enhance his unarmed strike. This ability otherwise functions as and replaces divine bond.

## Aura of Perfection (Su) {#aura-of-perfection}

At 11th level, whenever an Iroran paladin or ally within 10 feet would reroll a die and take the
second result even if it is lower (via the good fortune ability of the [Luck](ref/domain/luck)
domain, for example), he can roll an additional die as part of the reroll and use the higher of the
two as the result of the reroll. This ability functions only while the Iroran paladin is conscious,
and replaces aura of justice.
