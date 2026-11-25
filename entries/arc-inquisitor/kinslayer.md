+++
id = "ref/arc-inquisitor/kinslayer"
kind = "archetype"
title = "Kinslayer"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Kinslayer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kinslayer", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-race-guide"
page = "98"

[fields]
kind = "archetype"
features = [
  { anchor = "judgment", level = 1 },
  { anchor = "slayer-s-brand" },
  { anchor = "greater-brand", level = 1 },
  { anchor = "undead-sense", level = 2 },
]
trades = [
  { replaces = "Destruction judgment", feature = "judgment", power = "destruction", by = ["slayer-s-brand"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["undead-sense"] },
  { alters = "Teamwork feats", feature = "teamwork-feat", by = ["greater-brand"] },
]
+++

Appalled and guilt-ridden by the horrific circumstances of her birth, a kinslayer dedicates herself
to eradicating the very creatures whose blood flows within her veins. She spends her life hunting
and slaying those vampiric monsters for whom humans have become prey. A kinslayer has the following
class features.

## Judgment (Su) {#judgment}

At 1st level, a kinslayer gains the following judgment.

## Slayer's Brand (Su) {#slayer-s-brand}

When using this judgment, the kinslayer gains the ability to brand undead creatures with positive
energy. To do so, she must make a successful melee touch attack against the undead creature. This
attack deals an amount of positive energy damage equal to 1d6 + the kinslayer's Charisma modifier,
and burns her personal symbol into the undead creature's flesh, bone, or even its incorporeal form.
From that point onward, the kinslayer can sense the existence of the branded creature as if it were
the target of a _[locate creature](ref/spell/locate-creature)_ spell (caster level equal to 1/2 the
kinslayer's inquisitor level). A slayer's brand lasts until the undead creature is destroyed or
until the kinslayer uses this ability on another creature. This ability replaces the
[destruction](ref/spell/destruction) judgment.

## Greater Brand (Su) {#greater-brand}

At 1st level, a kinslayer learns to modify her slayer's brand judgment as she gains levels. Whenever
she gains the ability to learn a teamwork feat, she can instead opt to learn one of the following
modifications to her slayer's brand judgment.

### Branding Ray {#branding-ray}

The slayer's [brand](ref/spell/brand) judgment can be used as a ranged touch attack with a range of
20 feet. A kinslayer can take this modification more than once. Whenever she does, she increases the
range of her brand by 20 feet.

### Debilitating Brand {#debilitating-brand}

A creature currently affected by the slayer's [brand](ref/spell/brand) judgment takes a -2 penalty
on attack rolls against the kinslayer who placed the brand.

### Devastating Brand {#devastating-brand}

When the kinslayer attacks a creature that she has branded with her slayer's brand, she threatens a
critical hit on a roll of 19–20. If the kinslayer is good, she also gains a +2 sacred bonus on all
rolls to confirm critical hits on a branded creature.

### Dual Brand {#dual-brand}

The kinslayer can have up to two creatures branded at a time.

### Holy Brand {#holy-brand}

The kinslayer can use her [brand](ref/spell/brand) on creatures with the evil subtype as well as
undead.

### Searing Brand {#searing-brand}

The kinslayer's slayer's brand deals an additional 1d6 points of damage for every five inquisitor
levels she has. If the creature hit with the slayer's brand is particularly vulnerable to bright
light, the damage dice of her slayer's brand increases to d8s. A kinslayer must be at least 6th
level to take this modification.

### Silver Brand {#silver-brand}

The kinslayer can use her [brand](ref/spell/brand) on lycanthropes and creatures with vulnerability
to silver as well as undead.

Each time the kinslayer opts to take a greater brand, it replaces her ability to gain a teamwork
feat at that level.

## Undead Sense (Sp) {#undead-sense}

At 2nd level, a kinslayer gains the ability to use _[detect undead](ref/spell/detect-undead)_ as a
[spell-like ability](ref/umr/spell-like-abilities) (caster level equal to the kinslayer's inquisitor
level) at will. If she detects the presence of undead, she can use her monster lore ability to
attempt to determine the type of undead detected as well as to reveal any strengths or weaknesses
the undead might have. If any of the detected undead are vampires, she gains a bonus on the check
equal to her inquisitor level to immediately identify them as such.

This ability replaces _detect alignment_.
