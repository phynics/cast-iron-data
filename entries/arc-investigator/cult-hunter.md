+++
id = "ref/arc-investigator/cult-hunter"
kind = "archetype"
title = "Cult Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Cult%20Hunter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cult_hunter", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "horror-adventures"
page = "54"

[fields]
kind = "archetype"
features = [
  { anchor = "sense-madness", level = 1 },
  { anchor = "purify-body-and-mind", level = 2 },
  { anchor = "student-of-the-beyond", level = 2 },
  { anchor = "ambush-defenses", level = 3 },
  { anchor = "cultic-study" },
  { anchor = "cult-combat" },
  { anchor = "cult-strike" },
  { anchor = "summoning-sense", level = 7 },
  { anchor = "extraplanar-expulsion", level = 13 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["sense-madness"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["purify-body-and-mind"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["purify-body-and-mind"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["student-of-the-beyond"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["ambush-defenses"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["cultic-study"] },
  { replaces = "The 7th-level investigator talent", feature = "investigator-talent", levels = [7], by = ["summoning-sense"] },
  { replaces = "The 13th-level investigator talent", feature = "investigator-talent", levels = [13], by = ["extraplanar-expulsion"] },
  { alters = "Studied combat", feature = "studied-combat", by = ["cult-combat"] },
  { alters = "Studied strike", feature = "studied-strike", by = ["cult-strike"] },
]
+++

Cult hunters seek out heretical secret societies, purging their ideological taint and banishing
summoned servants.

## Sense Madness (Ex) {#sense-madness}

A cult hunter adds a bonus equal to 1/2 his class level (minimum +1) on Sense Motive checks, or
double that bonus to determine whether a creature suffers from natural or magical insanity.

This ability replaces trapfinding.

## Purify Body and Mind (Ex) {#purify-body-and-mind}

At 2nd level, a cult hunter gains a +1 bonus on saving throws against compulsions and poisons. This
bonus increases to +2 at 5th level and +3 at 8th level. At 11th level, a cult hunter who fails a
saving throw against a compulsion or poison can expend 1 use of his inspiration to reroll the saving
throw (and his inspiration die, if added to the save). He must accept the result of this second
roll, even if it is worse.

This ability replaces poison resistance and poison immunity.

## Student of the Beyond (Ex) {#student-of-the-beyond}

At 2nd level, a cult hunter gains a bonus equal to 1/2 his class level on Knowledge and Spellcraft
checks made to recognize any calling and summoning spells, portals, rifts, and planar travel.

This ability replaces poison lore.

## Ambush Defenses (Ex) {#ambush-defenses}

At 3rd level, a cult hunter gains a +1 insight bonus during a surprise round triggered by his
enemies on Reflex saves and to his AC. This bonus increases by 1 for every 3 investigator levels
beyond 3rd.

This ability replaces trap sense.

## Cultic Study (Ex) {#cultic-study}

A cult hunter can spend 8 hours studying a specific deity or religion to gain a +1 bonus on Bluff,
Intimidate, Knowledge, Perception, and Sense Motive checks against followers of that deity or
religion and against extraplanar creatures. These bonuses increase by 1 for every 4 investigator
levels beyond 4th. If he studies a new deity or religion, the bonuses replace the former bonuses.

This ability replaces swift alchemy.

## Cult Combat (Ex) {#cult-combat}

A cult hunter's bonuses on attack and damage rolls when using studied combat increase by 1 against
followers of the cult he chose with his cultic study ability and decrease by 1 against other
targets.

This ability alters studied combat.

## Cult Strike (Ex) {#cult-strike}

A cult hunter's studied strike uses d8s for the bonus damage against targets that belong to the cult
he's studied. Against other targets, his studied strike uses d4s for the bonus damage.

This ability alters studied strike.

## Summoning Sense (Su) {#summoning-sense}

At 7th level, a cult hunter gains the benefits of [uncanny dodge](ref/ability/uncanny-dodge) and
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) against summoned creatures.

This ability replaces the 7th-level investigator talent.

## Extraplanar Expulsion (Sp) {#extraplanar-expulsion}

At 13th level, a cult hunter can grant himself the ability to use _dispel chaos_, _dispel evil_,
_dispel good_, or _dispel law_ as a [spell-like ability](ref/umr/spell-like-abilities) (using his
investigator level as his caster level and his Intelligence to determine the DCs) by sacrificing an
unused 5th- or 6th-level extract for the day. He is able to use this ability as many times as he
likes, but only so long as he continues to have unused 5th- or 6th-level extract slots to expend.

This replaces the 13th-level investigator talent.
