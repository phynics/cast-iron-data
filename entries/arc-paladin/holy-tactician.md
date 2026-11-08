+++
id = "ref/arc-paladin/holy-tactician"
kind = "archetype"
title = "Holy Tactician"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_tactician", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Smite evil", "Divine health", "divine bond", "Aura of courage", "Aura of resolve", "Aura of justice", "Holy champion"]
+++

**Sources:** Ultimate Combat pg 64\
The holy tactician inspires her allies on the field of battle. Her place is at their side against
overwhelming odds, and her guidance brings out their true potential.

**Weal's Champion (Su)**

**Action:** Swift Action

**Gained:** At 1st Level

**Replaces:** Smite evil

**Special:** She can grant this bonus against more than one creature at a time. To gain this
benefit, the holy tactician's allies must be able to see or hear her, and she must be conscious.

**Usage:** 1 time/day + 1 per 3 paladin levels beyond 1st

A holy tactician can call on the powers of good to aid her against evil. Against evil targets, the
holy tactician gains her Charisma bonus (if any) on her attack rolls against evil creatures, and if
she hits, she adds 1/2 her paladin level on her weapon damage rolls as well. These bonuses last for
a number of rounds equal to [half](ref/misc/fractions-and-rounding) of her paladin level (minimum 1
round).

In addition, for 1 round after the holy tactician successfully strikes an evil creature, all
non-evil allies within 30 feet of her gain a competence bonus on attack rolls equal to 1/2 her
Charisma bonus against that creature as well as a competence bonus on damage rolls. The bonus on
damage rolls is equal to 1 + [one-fifth](ref/misc/fractions-and-rounding) of her paladin level.

**Tactical Acumen (Ex)**

**Ability:** A holy tactician gains a teamwork feat as a bonus feat.

**Gained:** At 3rd Level

**Repeat:** She gains an additional bonus teamwork feat., 7, 4

**Replaces:** Divine health, divine bond

**Special:** She must meet the prerequisites for these feats.

**Battlefield Presence (Su)**

**Gained:** At 3rd Level

**Replaces:** Aura of courage

**Special:** This ability does not function if the paladin is [flat-footed](ref/rule/flat-footed) or
unconscious. Allies must be able to see and hear the holy tactician in order to gain this benefit.

**Standard:** A tactician can direct her allies in battle, granting each ally within 30 feet one
teamwork feat she possesses as a bonus feat. All allies must receive the same feat, but do not need
to meet the prerequisites of this bonus feat.

**Swift:** She may change the bonus feat granted.

**Guide the Battle (Ex)**

**At 15th Level:** Her allies can make this 5-foot move and ignore
[difficult terrain](ref/rule/terrain-and-obstacles).

**Gained:** At 8th Level

**Move:** The paladin can direct her allies into an advantageous position once per round. Each ally
(if physically able to) can move 5 feet without expending an action. This movement does not provoke
attacks of opportunity. The allies must be able to see or hear the paladin in order to make this
movement and cannot be flat-footed.

**Replaces:** Aura of resolve

**Weal's Wrath (Su)**

**Ability:** A tactician can expend two uses of her _weal's champion_ ability at once to enhance its
effects. This functions as _weal's champion,_ except the bonus she provides to her allies lasts
until each creature she strikes is slain, her _weal's champion_ ability expires, or the paladin
herself is slain or knocked unconscious, whichever happens first.

**Gained:** At 11th Level

**Replaces:** Aura of justice

**Masterful Presence (Su)**

**Ability:** A tactician gains the ability to grant a different bonus feat to each ally affected by
her _battlefield presence._ In addition, all critical threats made by her and her allies against
creatures affected by her _weal's champion_ ability are automatically confirmed (no confirmation
roll is needed).

**Gained:** At 20th Level

**Replaces:** Holy champion
