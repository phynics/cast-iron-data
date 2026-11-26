+++
id = "ref/arc-paladin/forgefathers-seeker"
kind = "archetype"
title = "Forgefather's Seeker"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Forgefather%27s%20Seeker"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forgefathers_seeker", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "construct-handbook"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "torag-worshiper" },
  { anchor = "detect-construct", level = 1 },
  { anchor = "smite-construct", level = 1 },
  { anchor = "aura-of-destruction", level = 11 },
  { anchor = "aura-of-unmaking", level = 14 },
  { anchor = "forgefather-s-champion", level = 20 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["detect-construct"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["aura-of-unmaking"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["forgefather-s-champion"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["smite-construct"] },
  { alters = "Aura of justice", feature = "aura-of-justice", by = ["aura-of-destruction"] },
]
+++

[Torag](ref/faith/torag) constantly seeks those who would use the power of creation to threaten or
harm others. To this end, he sends his seekers to locate constructs that are used for evil or that
become uncontrollable. These paladins are adept at battling constructed foes and guarding those
threatened by such creations.

## Torag Worshiper {#torag-worshiper}

A Forgefather's seeker must select Torag as her patron deity.

## Detect Construct (Sp) {#detect-construct}

A Forgefather's seeker can detect the presence of constructs at will. This functions as the spell
_[aura sight](ref/spell/aura-sight)_, except the duration is 1 round and a Forgefather's seeker
learns the locations and power of all auras of all constructs, similar to
_[detect undead](ref/spell/detect-undead)._

This replaces detect evil.

## Smite Construct (Su) {#smite-construct}

This ability functions as the paladin's smite evil ability, but it functions only against
constructs. Smiting a construct automatically bypasses any DR or [hardness](ref/umr/hardness) a
construct might have. A Forgefather's seeker can still smite evil, but she adds only half her
Charisma bonus on attack rolls, adds only half of her level on damage rolls, and doesn't increase
her bonus damage against outsiders with the evil subtype, evil-aligned dragons, or undead. This
otherwise functions as smite evil for the purposes of feats, prerequisites, and other effects.

This alters smite evil.

## Aura of Destruction (Su) {#aura-of-destruction}

At 11th level, a Forgefather seeker grants her allies smite construct with her aura of justice
ability instead of smite evil.

This alters aura of justice.

## Aura of Unmaking (Su) {#aura-of-unmaking}

At 14th level, a Forgefather's seeker's weapons are treated as
[adamantine](ref/eq-material/adamantine) for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Any attack made against an enemy within 10 feet of
her is treated as adamantine for the purpose of overcoming damage reduction. This ability functions
only while a Forgefather's seeker is conscious, not if she is unconscious or dead.

This replaces aura of faith.

## Forgefather's Champion (Su) {#forgefather-s-champion}

At 20th level, a Forgefather's seeker becomes capable of completely dismantling constructs. Her DR
increases to 10/evil. Whenever she uses smite construct and hits a construct, she can immediately
attempt to destroy the construct. The construct is reduced to 0 hit points and destroyed unless it
succeeds at a Will save (DC = 10 + half the Forgefather's seeker's level + the Forgefather's
seeker's Charisma modifier). After this destruction effect and the damage from the attack is
resolved, the smite immediately ends. In addition, whenever a Forgefather's seeker channels positive
energy or uses lay on hands to heal a creature, she heals the maximum possible amount.

This replaces holy champion.
