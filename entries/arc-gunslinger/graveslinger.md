+++
id = "ref/arc-gunslinger/graveslinger"
kind = "archetype"
title = "Graveslinger"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Graveslinger"
source_ids = ["pathfinder-139-the-dead-road"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "graveslinger", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "pathfinder-139-the-dead-road"
page = "65"

[fields]
kind = "archetype"
features = [
  { anchor = "ghostbane-shot", level = 1 },
  { anchor = "ectoplasmic-anchor", level = 7 },
  { anchor = "undead-hunter", level = 11 },
  { anchor = "staggering-shot", level = 15 },
  { anchor = "supernatural-awareness", level = 4 },
]
trades = [
  { replaces = "Deadeye deed", feature = "deeds", power = "deadeye", by = ["ghostbane-shot"] },
  { replaces = "Startling shot deed", feature = "deeds", power = "startling shot", by = ["ectoplasmic-anchor"] },
  { replaces = "Bleeding wound deed", feature = "deeds", power = "bleeding wound", by = ["undead-hunter"] },
  { replaces = "Menacing shot deed", feature = "deeds", power = "menacing shot", by = ["staggering-shot"] },
  { replaces = "The bonus feat gained at 4th level", feature = "bonus-feats", levels = [4], by = ["supernatural-awareness"] },
]
+++

Graveslingers craft signature bullets to hunt down wandering undead. With this infused ammunition,
they can take on the most resilient spectral foes with ease.

## Deeds {#deeds}

A graveslinger gains the following deeds.

## Ghostbane Shot (Ex) {#ghostbane-shot}

At 1st level, once per day by spending 10 minutes to combine mundane ammunition with a mixture of
grave dirt and powdered bone, the graveslinger can prepare a number of special bullets equal to her
graveslinger level plus her Wisdom modifier (minimum 1). When attacking incorporeal undead, these
bullets are treated as if they had the _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ special
ability. These bullets function only for the graveslinger, and if not fired within 24 hours, the
bullets become inert, losing their _ghost touch_ special ability.

This deed replaces the deadeye deed.

## Ectoplasmic Anchor (Su) {#ectoplasmic-anchor}

At 7th level, an incorporeal undead creature hit by one of the graveslinger's ghostbane shots
becomes infused with ectoplasm, interfering with its defenses and mobility. The creature must
succeed at a Will save (DC = 10 + half the graveslinger's level + the graveslinger's Wisdom
modifier) or become semicorporeal for 1 round. A semicorporeal creature takes half damage (50%) from
nonmagical attack forms, and it takes full damage from magic weapons, spells, spell-like effects,
and supernatural effects. During this time, it cannot enter or pass through solid objects.

This deed replaces the startling shot deed.

## Undead Hunter (Ex) {#undead-hunter}

At 11th level, the graveslinger's ghostbane shots are treated as if they also had the
_[undead bane](ref/magic-enh/bane)_ special ability.

This deed replaces the bleeding wound deed.

## Staggering Shot (Ex) {#staggering-shot}

At 15th level, when a graveslinger confirms a critical hit against an undead creature with one of
her ghostbane shots, the creature is [staggered](ref/misc/staggered) for 1 round.

This deed replaces the menacing shot deed.

## Supernatural Awareness (Ex) {#supernatural-awareness}

At 4th level, the graveslinger gains [Blind-Fight](ref/feat/blind-fight) as a bonus feat.
Additionally, as long as she has 1 grit point, she can always act in surprise rounds that are
triggered by haunts and incorporeal undead, even if she fails to notice them.

This replaces the bonus feat gained at 4th level.
