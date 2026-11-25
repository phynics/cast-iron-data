+++
id = "ref/arc-fighter/aldori-defender"
kind = "archetype"
title = "Aldori Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Aldori%20Defender"
source_ids = ["adventurers-guide", "inner-sea-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aldori_defender", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "adventurers-guide"
page = "22"
[[sources]]
publication = "inner-sea-primer"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "defensive-parry", level = 3 },
  { anchor = "disarming-strike", level = 6 },
  { anchor = "steel-net", level = 8 },
  { anchor = "counterattack", level = 10 },
]
trades = [
  { replaces = "Armor training", feature = "armor-training", by = ["defensive-parry"] },
  { replaces = "Bonus feat the fighter would normally gain at 6th level", feature = "bonus-feats", levels = [6], by = ["disarming-strike"] },
  { replaces = "Bonus feat the fighter would normally gain at 8th level", feature = "bonus-feats", levels = [8], by = ["steel-net"] },
  { replaces = "Bonus feat the fighter would normally gain at 10th level", feature = "bonus-feats", levels = [10], by = ["counterattack"] },
]
+++

The Aldori swordlords of Brevoy are among the deadliest and most feared fighters of the Inner Sea.
They have spent long years mastering the [Aldori dueling sword](ref/eq-weapon/aldori-dueling-sword),
pitting themselves against other dueling swords and all manner of weaponry besides. Their speed and
reflexes weave a net of impenetrable steel around them, from which they strike and harry their
unfortunate opponents. The most common form of Aldori dueling (and arguably the easiest of the
techniques to master) focuses on avoiding damage and disarming foes; these swordlords prefer to wear
light or no armor, trusting their skill for protection. This archetype focuses on such
techniques—characters seeking a more offensive method of focusing training on the Aldori dueling
sword should consider the [Aldori swordlord](ref/pclass/aldori-swordlord) prestige class on page 20.
However, this archetype also synergizes well with the powers and skills the prestige class offers.

The following benefits apply only when an Aldori defender is wielding an
[Aldori dueling sword](ref/eq-weapon/aldori-dueling-sword) (see page 24) and carrying nothing in his
other hand. An Aldori defender fights with his sword wielded with both hands only in moments of
desperation.

## Suggested Feats {#suggested-feats}

Although this archetype replaces some of the bonus feats that a fighter would normally have access
to, Aldori defenders still have several opportunities to gain feats. The following feats are the
most thematically appropriate for an Aldori defender, but the archetype does not require any of
them: [Aldori Dueling Mastery](ref/feat/aldori-dueling-mastery) (see page 24),
[Combat Expertise](ref/feat/combat-expertise), [Dazzling Display](ref/feat/dazzling-display),
[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency) (Aldori dueling sword),
[Improved Disarm](ref/feat/improved-disarm), [Improved Feint](ref/feat/improved-feint),
[Improved Initiative](ref/feat/improved-initiative), [Lunge](ref/feat/lunge),
[Quick Draw](ref/feat/quick-draw), [Weapon Finesse](ref/feat/weapon-finesse),
[Weapon Focus](ref/feat/weapon-focus) (Aldori dueling sword),
[Weapon Specialization](ref/feat/weapon-specialization) (Aldori dueling sword).

## Defensive Parry (Ex) {#defensive-parry}

At 3rd level, when an Aldori defender makes a [full attack](ref/rule/full-attack) with an Aldori
dueling sword, he gains a +1 shield bonus to his AC against melee attacks until the beginning of his
next turn. This bonus increases to +2 at 7th level, +3 at 11th level, and +4 at 15th level.

This ability replaces armor training.

## Disarming Strike (Ex) {#disarming-strike}

At 6th level, when an Aldori defender successfully [disarms](ref/rule/disarm) an opponent using an
Aldori dueling sword, he also deals normal damage to the target, but without the normal Strength
bonus to damage.

This ability replaces the bonus feat the fighter would normally gain at 6th level.

## Steel Net (Ex) {#steel-net}

At 8th level, an Aldori defender can create a blazing wall of steel to defend himself. When
[fighting defensively](ref/misc/fighting-defensively) as a full-round action with an Aldori dueling
sword, the Aldori defender's penalties on all attacks in a round are reduced by 2, and his dodge
bonus to AC increases by 2 for the same round.

This ability replaces the bonus feat the fighter would normally gain at 8th level.

## Counterattack (Ex) {#counterattack}

At 10th level, once per round, an Aldori defender can make an attack of opportunity against an
opponent who hits him with a melee attack (regardless of how many attacks of opportunity the Aldori
defender can otherwise make), so long as the attacking creature is within the his reach.

This ability replaces the bonus feat the fighter would normally gain at 10th level.
