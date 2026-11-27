+++
id = "ref/arc-sorcerer/dragon-drinker"
kind = "archetype"
title = "Dragon Drinker"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Dragon%20Drinker"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_drinker", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "bloodline" },
  { anchor = "bleeding-spells" },
  { anchor = "blood-drinking", level = 1 },
  { anchor = "energy-assimilation", level = 7 },
  { anchor = "breath-mimicry", level = 13 },
  { anchor = "blood-siphon", level = 19 },
]
trades = [
  { replaces = "Bloodline arcana", feature = "bloodline", power = "bloodline arcana", by = ["bleeding-spells"] },
  { replaces = "The claws bloodline power", feature = "bloodline", levels = [1], power = "bloodline power", by = ["blood-drinking"] },
  { replaces = "7th-level bloodline feat", feature = "bloodline", levels = [7], power = "bloodline feat", by = ["energy-assimilation"] },
  { replaces = "13th-level bloodline feat", feature = "bloodline", levels = [13], power = "bloodline feat", by = ["breath-mimicry"] },
  { replaces = "19th-level bloodline feat", feature = "bloodline", levels = [19], power = "bloodline feat", by = ["blood-siphon"] },
]
+++

The blood of dragons not only flows through a dragon drinker's veins, but also empowers her spells
and magical abilities when consumed. Dragon drinkers have the following class features.

## Bloodline {#bloodline}

A dragon drinker must belong to the draconic bloodline.

## Bleeding Spells (Su) {#bleeding-spells}

Whenever a dragon drinker casts a spell that deals damage, the spell deals 1 point of
[bleed](ref/rule/bleed) damage per spell level to any creatures of the dragon type damaged. This
ability replaces the bloodline arcana ability.

## Blood Drinking (Su) {#blood-drinking}

Starting at first level, a dragon drinker gains the ability to drink dragon blood to alter or
augment her spellcasting abilities. See page 18 for information on
[dragon's blood](ref/eq-misc/dragons-blood). For the purposes of harvesting dragon's blood, treat
the dragon drinker as though she has [Dragoncrafting](ref/feat/dragoncrafting) feat. At 5th level,
drinking a vial of dragon's blood is a standard action that provides the dragon drinker with the
normal benefits of the item, as well as a +1 bonus to her caster level for purposes of
level-dependent spell effects on a single spell cast within 1 minute. At 7th level, a consumed vial
of dragon blood also heals 1d8 points of damage instead of the standard 1d4. At 11th level, the
alchemical bonus on Fortitude and Reflex saves granted by the blood increases to +2.

In the absence of true dragon's blood, the dragon drinker may tap into the draconic blood flowing
through her veins to gain the temporary effects of having consumed dragon's blood. As a free action,
she can activate this ability, healing 1d4 points of damage and gaining a +1 resistance bonus on
Will and Fortitude saves for 1 round. This action may only be performed once per round, and can be
performed a number of times per day equal to 3 + her Charisma modifier. This ability replaces the
claws bloodline power.

## Energy Assimilation (Su) {#energy-assimilation}

At 7th level, when the dragon drinker drinks true dragon's blood from a dragon with a breath weapon
that deals a different type of energy damage than her chosen energy type, she may adopt the energy
resistance of the blood's source dragon as if it were her selected bloodline. This effect lasts for
1 minute per dose of dragon's blood, after which the dragon drinker's energy resistance reverts back
to her normal energy type. This ability replaces the 7th-level bloodline feat.

## Breath Mimicry (Su) {#breath-mimicry}

At 13th level, when the dragon drinker drinks true dragon's blood from a dragon with a breath weapon
of a shape or energy type different from her own, she may use the shape and energy type of the
blood's source dragon when she next uses her breath weapon. This ability replaces the 13th-level
bloodline feat.

## Blood Siphon (Su) {#blood-siphon}

At 19th level, when the dragon drinker is within 60 feet of a creature of the dragon type that is
suffering bleed damage, she can, as a swift action, draw a dose of its blood into herself as though
she had consumed it from a vial. Additionally, when she consumes dragon's blood, it heals 3d8 points
of damage and provides a +3 resistance bonus on Fortitude and Will saves for 1 minute in place of
its normal effects. This ability replaces the 19th-level bloodline feat.
