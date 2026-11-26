+++
id = "ref/arc-fighter/high-guardian"
kind = "archetype"
title = "High Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20High%20Guardian"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "high_guardian", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "obligation", level = 1 },
  { anchor = "right-hand", level = 1 },
  { anchor = "defender-s-reflexes", level = 2 },
  { anchor = "unassailable-allegiance", level = 2 },
  { anchor = "royal-protector", level = 4 },
]
trades = [
  { replaces = "The bonus feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["right-hand"] },
  { replaces = "The bonus feat gained at 2nd level", feature = "bonus-feats", levels = [2], by = ["defender-s-reflexes"] },
  { replaces = "Bravery", feature = "bravery", by = ["unassailable-allegiance"] },
  { replaces = "The bonus feat gained at 4th level", feature = "bonus-feats", levels = [4], by = ["royal-protector"] },
  { alters = "Class skills" },
]
+++

As the shield that protects his lord from the myriad dangers around every corner, the high guardian
pledges his life to keep his charge safe. High guardians epitomize personal devotion, making them
especially popular among Taldan nobles envious of the emperor's [Ulfen Guard](ref/rule/f-imperial),
as well as in the courts of the Lands of the Linnorm Kings, the war councils of Molthune and
Lastwall, and the refined chambers of Osirion.

## Class Skills {#class-skills}

A high guardian adds Knowledge (local) and Knowledge (nobility) to his list of class skills, instead
of Knowledge (dungeoneering) and Knowledge (engineering).

This alters the fighter's class skills.

## Obligation (Ex) {#obligation}

At 1st level, a high guardian can spend 1 minute of focused concentration each day to select a
single ally as his obligation, vowing to keep that person alive for that day. Once he has chosen, he
can't change his obligation until the following day. If his obligation dies, the high guardian must
atone for 1 week before he can select another obligation.

## Right Hand (Ex) {#right-hand}

At 1st level, a high guardian can take [a 5-foot step](ref/rule/take-5-foot-step) as an immediate
action, as long as he ends this movement adjacent to his obligation. If he takes this step, he
cannot take a 5-foot step during his next turn and his total movement is reduced by 5 feet during
his next turn.

This ability replaces the bonus feat gained at 1st level.

## Defender's Reflexes (Ex) {#defender-s-reflexes}

At 2nd level, a high guardian gains [Combat Reflexes](ref/feat/combat-reflexes) as a bonus feat, and
he can use his Strength modifier instead of his Dexterity modifier to determine the number of
additional attacks of opportunity he can make per round. If he already has Combat Reflexes, he
instead gains [Stand Still](ref/feat/stand-still) as a bonus feat.

This ability replaces the bonus feat gained at 2nd level.

## Unassailable Allegiance (Ex) {#unassailable-allegiance}

At 2nd level, a high guardian gains a +1 bonus on Will saves against compulsion spells and effects.
This bonus increases by 1 for every 4 fighter levels beyond 2nd.

This ability replaces bravery.

## Royal Protector (Ex) {#royal-protector}

At 4th level, a high guardian gains [Bodyguard](ref/feat/bodyguard) and
[In Harm's Way](ref/feat/in-harms-way) as bonus feats, though he can use them only to improve his
obligation's AC or intercept a successful attack against his obligation.

This ability replaces the bonus feat gained at 4th level.
