+++
id = "ref/arc-ranger/toxic-herbalist"
kind = "archetype"
title = "Toxic Herbalist"
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
replaces = ["Wild empathy", "Endurance", "Hunter's bond", "Swift tracker", "Quarry", "Improved quarry"]
replaces_features = ["wild-empathy", "endurance", "hunter-s-bond", "swift-tracker", "quarry", "improved-quarry"]
+++

Saviors and destroyers in equal measure, toxic herbalists use nature's bounty to craft remedies and
poisons.

**Toxic Touch (Ex)**

**Passive:** A toxic herbalist studies the safe handling of deadly substances. He cannot
accidentally poison himself when he applies poison to a weapon.

**Replaces:** Wild empathy

**Nature's Mercy (Ex and Su)**

**Ability:** Once per day, he can spend 1 hour in a wilderness area gathering herbs and other
natural materials and combine them into a medicinal poultice - this hour can be integrated with the
hour required for the ranger to prepare spells.

**Ability2:** Placing the poultice on a wound or ingesting it is a **standard action**; the creature
receiving the poultice heals a number of hit points equal to 1d6 + the ranger's Wisdom modifier.

**Flavor:** A toxic herbalist's knowledge of the natural world offers respite from wounds and
illness.

**At 13th Level:** A poultice also attempts to cure one disease affecting the recipient, as per
[remove disease](ref/spell/remove-disease).

**At 8th Level:** A poultice neutralizes one poison affecting the recipient, as per
[neutralize poison](ref/spell/neutralize-poison).

**Gained:** At 3rd Level

**Replaces:** Endurance

**Special:** The caster level of the neutralizing/curing effects is equal to the toxic herbalist's
level. These additional effects are supernatural effects.

At 11th level: The ranger can now create 2 poultices per day.

At 19th level: The ranger can now create 3 poultices per day.

**Sudden Onset (Ex)**

**Info:** Additionally, the toxic herbalist adds the following spells to the ranger spell list at
the indicated spell levels.

**Gained:** At 4th Level

**Replaces:** Hunter's bond

**Spells:** Nauseating dart, ray of sickening

**Spells:** Pernicious poison, pox pustules

**Spells:** Poison, toxic gift

**Spells:** Absorb toxicity, cloudkill

**Swift:** A toxic herbalist can administer a poultice he created via _nature's mercy_ or poison a
weapon as a swift action.

**Grim Harvest (Ex)**

**Ability:** A toxic herbalist can spend 1 hour foraging for poisonous substances to create a dose
of poison (this hour can be integrated with the hour required to prepare spells or poultices). The
toxic herbalist rolls 1d20 and adds his ranger level and his Intelligence modifier. The DC of this
check is equal to the Craft DC of the poison he wishes to create. If he succeeds at this check, the
ranger creates 1 dose of the chosen poison. The poison remains potent for a number of hours equal to
the toxic herbalist's level, regardless of the means used in attempts to preserve it, and it can't
be sold.

**Gained:** At 8th Level

**Replaces:** Swift tracker

**Special:** This ability functions only while the toxic herbalist is within one of his _favored
terrains._

**Potent Venom (Ex)**

**Ability:** When he poisons a _favored enemy,_ the DC of the poison's saving throw increases by
half the toxic herbalist's _favored enemy_ bonus against that target.

**Flavor:** A toxic herbalist's poisons become even deadlier.

**Gained:** At 11th Level

**Replaces:** Quarry

**Poisonous Reaper (Ex)**

**Gained:** At 19th Level

**Passive:** A single dose of poison on a toxic herbalist's weapon remains potent for the entirety
of a full attack, instead of for a single strike.

**Replaces:** Improved quarry
