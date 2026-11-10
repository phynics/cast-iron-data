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
replaces = ["Proficiency with medium armor", "heavy armor", "and shields", "Aura of good", "Detect evil", "Smite evil", "Aura of courage", "Channel positive energy", "Divine bond", "Aura of justice"]
replaces_features = ["aura-of-good", "detect-evil", "smite-evil", "aura-of-courage", "channel-positive-energy", "divine-bond", "aura-of-justice"]
+++

Iroran paladins meditate on self-perfection and train relentlessly, knowing that their example can
inspire others to excel. [Irori](ref/faith/irori) offers no universal paladin code; each paladin in
his service creates his own code as part of his spiritual journey, seeing the adherence to such a
self-formulated creed as one of the many tests one must face to reach perfection.

**Gained class skills:** acro, climb, swim

**Confident Defense (Ex)**

**Gained:** At 1st Level

**Passive:** When wearing light or no armor and not using a shield, an Iroran paladin adds 1 point
of his Charisma bonus (if any) per class level to his Dexterity bonus to his Armor Class. If he is
caught [flat-footed](ref/rule/flat-footed) or otherwise denied his Dexterity bonus, he also loses
this bonus.

**Replaces:** Proficiency with medium armor, heavy armor, and shields

**Unarmed Strike**

**Ability:** An Iroran paladin gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as
a bonus feat. In addition, he gains the unarmed strike [monk](ref/class/monk) ability, treating his
monk level as half his paladin level (minimum 1) for calculating his unarmed strike damage.

**Gained:** At 1st Level

**Unarmed Strike**

**Flavor:** Relevant text from the monk class ability.

**At 4th Level:** Your unarmed strike now deals 1d6 (Small), 1d8 (Medium), or 2d6 (Large) damage.

**At 8th Level:** Your unarmed strike now deals 1d8 (Small), 1d10 (Medium), or 2d8 (Large) damage.

**At 1st Level:** Your unarmed strike deals 1d4 (Small), 1d6 (Medium), or 1d8 (Large) damage.

**Aura of Law (Su)**

**Info:** The power of an Iroran paladin's _aura of law_ is equal to his class level.

**Replaces:** Aura of good

**Sense Perfection (Su)**

**Ability:** At will, an Iroran paladin can detect life forces as if he were using a paladin's
_[detect evil](ref/spell/detect-evil)_ class ability; however, instead of sensing evil creatures, he
senses creatures that have a ki pool. Each such creature has an aura like a cleric of an aligned
deity, and treats its current number of ki points as its Hit Dice for the purposes of this ability.

**Gained:** At 1st Level

**Replaces:** Detect evil

**Personal Trial (Su)**

**Replaces:** Smite evil

**Special:** The _personal trial_ effect remains until the target of the trial is dead or the next
time the paladin rests and regains daily uses of this ability.

**Swift:** An Iroran paladin can declare one target within line of sight as his _personal trial._
The Iroran paladin gains an insight bonus on attack rolls and damage rolls against that creature, to
his AC against attacks made by the target, and on saving throws against the target's spells and
special abilities. This bonus is equal to 1 + one-fourth of his paladin level.

**Usage:** 1 time/day + 1 per 3 paladin levels beyond 1st

**Aura of Excellence (Su)**

**Gained:** At 3rd Level

**Passive:** An Iroran paladin is immune to any effect that would force him to reroll a die against
his will or roll twice and take the lower result. Whenever an ally within 10 feet of him would
reroll a die against her will, she can roll twice and take the higher result. Whenever an ally
within 10 feet would be forced to roll twice and take the lower result, she can instead roll three
times and take the second-lowest result. This ability functions only while the Iroran paladin is
conscious.

**Replaces:** Aura of courage

**Ki Pool (Su)**

**Ability:** An Iroran paladin gains a ki pool with an effective monk level equal to his class
level. The number of points in an Iroran paladin's ki pool is equal to 1/2 his class level + his
Charisma modifier.

**Gained:** At 4th Level

**Replaces:** Channel positive energy

**Special:** By spending 1 point from his ki pool, he can ignore any
[damage reduction](ref/rule/damage-reduction) possessed by the target of his _personal trial_
ability for 1 round. This ability otherwise functions as the monk ability of the same name.

**Divine Body (Su)**

**Info:** An Iroran paladin must form a bond with a weapon, except he can only choose to enhance his
unarmed strike. This ability otherwise functions as _divine bond._

**Gained:** At 5th Level

**Replaces:** Divine bond

**Aura of Perfection (Su)**

**Gained:** At 11th Level

**Passive:** Whenever an Iroran paladin or ally within 10 feet would reroll a die and take the
second result even if it is lower (via the good fortune ability of the [Luck](ref/domain/luck)
domain, for example), he can roll an additional die as part of the reroll and use the higher of the
two as the result of the reroll.

**Replaces:** Aura of justice

**Special:** This ability functions only while the Iroran paladin is conscious.
