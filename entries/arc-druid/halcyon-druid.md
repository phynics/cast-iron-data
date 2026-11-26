+++
id = "ref/arc-druid/halcyon-druid"
kind = "archetype"
title = "Halcyon Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Halcyon%20Druid"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "halcyon_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "adventurers-guide"
page = "121"

[fields]
kind = "archetype"
features = [
  { anchor = "bonded-mask", level = 1 },
  { anchor = "magaambya-trained", level = 1 },
  { anchor = "peacekeeper", level = 1 },
  { anchor = "spontaneous-casting", level = 1 },
  { anchor = "natural-arcana", level = 4 },
  { anchor = "resist-fiendish-influence", level = 4 },
  { anchor = "embody-mask", level = 13 },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["bonded-mask"] },
  { replaces = "Nature sense", feature = "nature-sense", by = ["magaambya-trained"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["peacekeeper"] },
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["spontaneous-casting"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["natural-arcana"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-fiendish-influence"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["embody-mask"] },
  { alters = "Class skills", by = ["magaambya-trained"] },
]
+++

Druids of the Halcyon Circle embrace [the teachings of Old- Mage Jatembe](ref/rule/aff-i-school),
combining them with traditional druidic practices. Though they revere the natural world, halcyon
druids are less focused on emulating its inhabitants. Instead, like Old-Mage Jatembe, they treat
with beings from the Outer Sphere. As a sign of their allegiance, these druids wear fantastical
masks depicting celestials, fiends, and—most often—the bestial agathions.

Halcyon druids are peacekeepers, mediating between people and nature, people and the spirit world,
and different groups of people. Yet when necessary, they use their magic to fight enemies of peace,
especially demons and demon cultists.

Most halcyon druids serve Nantambu and the surrounding villages—making, memorizing, and arbitrating
the unwritten pacts between them. Some halcyon druids, however, are drawn farther afield. They may
do so to forge new connections between tribes and villages, to spread the message of peace, or to
fight demonic outbreaks.

## Bonded Mask (Su) {#bonded-mask}

A halcyon druid forms a powerful bond with a mask, which functions identically to a
[wizard's](ref/class/wizard) bonded object except that it can be used to cast druid spells
(including those gained from class abilities) instead of wizard spells. A bonded mask must be worn
to have an effect, and it occupies the [head slot](ref/rule/magic-items-on-the-body). A halcyon
druid can enhance her mask with abilities appropriate for a head slot item, and can designate an
existing head slot item as her bonded mask (but only if it covers her face).

This ability replaces nature bond.

## Magaambya-Trained (Ex) {#magaambya-trained}

A halcyon druid adds [Diplomacy](ref/skill/diplomacy) and all [Knowledge](ref/skill/knowledge-all)
skills to her list of class skills.

This ability replaces nature sense and alters the druid's class skills.

## Peacekeeper (Ex) {#peacekeeper}

A halcyon druid adds [half](ref/misc/fractions-and-rounding) her class level (minimum 1) to
Diplomacy and Knowledge (local) checks.

This ability replaces wild empathy.

## Spontaneous Casting {#spontaneous-casting}

A halcyon druid adds all spells from the Good cleric domain to her druid spell list, and she can
focus stored spell energy into spells from the Good domain that she hasn't prepared ahead of time.
She can lose a prepared spell to cast any spell of the same level or lower from the Good domain.

This ability replaces spontaneous casting.

## Natural Arcana (Su) {#natural-arcana}

At 4th level and every 2 levels thereafter, a halcyon druid chooses two spells from the
wizard/sorcerer spell list and adds them to her druid spell list. The chosen spells must be at least
1 level lower than the highest level spell she can currently cast. At 20th level, the halcyon druid
can choose wizard/sorcerer spells of any level.

This ability replaces wild shape.

## Resist Fiendish Influence (Ex) {#resist-fiendish-influence}

At 4th level, a halcyon druid gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of outsiders with the evil subtype and spells with the evil descriptor.

This ability replaces resist nature's lure.

## Embody Mask (Sp) {#embody-mask}

At 13th level, a halcyon druid wearing her bonded mask can embody the spirit it represents, which
can be any Tiny to Large [agathion](ref/family/agathion), [angel](ref/family/angel),
[archon](ref/family/archon), or [azata](ref/family/azata). This ability requires a standard action
to activate and functions as per _[beast shape IV](ref/spell/beast-shape-4)_ (using the adjustments
for magical beasts), but adds the following abilities if the assumed form has them: aura of menace,
protective aura, speak with animals, telepathy, and truespeech. If the assumed form has
[immunity](ref/umr/immunity) to a condition, the druid gains a +4 bonus on saving throws against
effects that cause that condition. A halcyon druid can use this ability for a number of minutes per
day equal to her druid level. The duration does not need to be consecutive, but must be used in
1-minute increments.

This ability replaces a thousand faces.
