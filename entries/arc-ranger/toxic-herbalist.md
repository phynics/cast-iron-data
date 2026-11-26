+++
id = "ref/arc-ranger/toxic-herbalist"
kind = "archetype"
title = "Toxic Herbalist"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Toxic%20Herbalist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_herbalist", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "74"

[fields]
kind = "archetype"
features = [
  { anchor = "toxic-touch", level = 1 },
  { anchor = "nature-s-mercy", level = 3 },
  { anchor = "sudden-onset", level = 4 },
  { anchor = "grim-harvest", level = 8 },
  { anchor = "potent-venom", level = 11 },
  { anchor = "poisonous-reaper", level = 19 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["toxic-touch"] },
  { replaces = "Endurance", feature = "endurance", by = ["nature-s-mercy"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["sudden-onset"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["grim-harvest"] },
  { replaces = "Quarry", feature = "quarry", by = ["potent-venom"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["poisonous-reaper"] },
]
+++

Saviors and destroyers in equal measure, toxic herbalists use nature's bounty to craft remedies and
poisons.

## Toxic Touch (Ex) {#toxic-touch}

A toxic herbalist studies the safe handling of deadly substances. He cannot accidentally poison
himself when he applies poison to a weapon.

This replaces wild empathy.

## Nature's Mercy (Ex and Su) {#nature-s-mercy}

At 3rd level, a toxic herbalist's knowledge of the natural world offers respite from wounds and
illness. Once per day, he can spend 1 hour in a wilderness area gathering herbs and other natural
materials and combine them into a medicinal poultice—this hour can be integrated with the hour
required for the ranger to prepare spells. Placing the poultice on a wound or ingesting it is a
standard action; the creature receiving the poultice heals a number of hit points equal to 1d6 + the
ranger's Wisdom modifier.

At 8th level and every 5 levels thereafter, the ranger creates one additional poultice when using
this ability, to a maximum of four at 18th level. Poultices remain potent for 1 hour.

Additionally, at 8th level, the poultice neutralizes one poison affecting the recipient, as per
_[neutralize poison](ref/spell/neutralize-poison)_. At 13th level, it also attempts to cure one
disease affecting the recipient, as per _[remove disease](ref/spell/remove-disease)_. The caster
level of both of these effects is equal to the toxic herbalist's level. These additional effects are
supernatural effects.

This replaces endurance.

## Sudden Onset (Ex) {#sudden-onset}

At 4th level, a toxic herbalist can administer a poultice he created via nature's mercy or poison a
weapon as a swift action. Additionally, the toxic herbalist adds the following spells to the ranger
spell list at the indicated spell levels: 1st—_nauseating dart_, _ray of sickening_; 2nd—_pernicious
poison_, _pox pustules_; 3rd—_poison_, _toxic gift_; 4th—_absorb toxicity_, _cloudkill_.

This replaces hunter's bond.

## Grim Harvest (Ex) {#grim-harvest}

At 8th level, a toxic herbalist can spend 1 hour foraging for poisonous substances to create a dose
of poison (this hour can be integrated with the hour required to prepare spells or poultices). The
toxic herbalist rolls 1d20 and adds his ranger level and his Intelligence modifier. The DC of this
check is equal to the Craft DC of the poison he wishes to create. If he succeeds at this check, the
ranger creates 1 dose of the chosen poison. The poison remains potent for a number of hours equal to
the toxic herbalist's level, regardless of the means used in attempts to preserve it, and it can't
be sold. This ability functions only while the toxic herbalist is within one of his favored
terrains.

This replaces swift tracker.

## Potent Venom (Ex) {#potent-venom}

At 11th level, a toxic herbalist's poisons become even deadlier. When he poisons a favored enemy,
the DC of the poison's saving throw increases by half the toxic herbalist's favored enemy bonus
against that target.

This replaces quarry.

## Poisonous Reaper (Ex) {#poisonous-reaper}

At 19th level, a single dose of poison on a toxic herbalist's weapon remains potent for the entirety
of a full attack, instead of for a single strike.

This replaces improved quarry.
