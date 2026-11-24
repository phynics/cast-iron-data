+++
id = "ref/arc-monk/tetori"
kind = "archetype"
title = "Tetori"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Tetori"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tetori", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "61"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat" },
  { anchor = "graceful-grappler" },
  { anchor = "counter-grapple", level = 4 },
  { anchor = "break-free", level = 5 },
  { anchor = "inescapable-grasp", level = 9 },
  { anchor = "form-lock", level = 13 },
  { anchor = "iron-body", level = 19 },
]
trades = [
  { replaces = "Bonus feats", feature = "bonus-feat", by = ["bonus-feat"] },
  { replaces = "Flurry of blows", feature = "flurry-of-blows", by = ["graceful-grappler"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["counter-grapple"] },
  { replaces = "High jump", feature = "high-jump", by = ["break-free"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["inescapable-grasp"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["inescapable-grasp"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["inescapable-grasp"] },
  { replaces = "tongue of sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["inescapable-grasp"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["form-lock"] },
  { replaces = "Empty body", feature = "empty-body", by = ["iron-body"] },
]
+++

The style of the tetori is that of the majestic wrestler - a warrior with a dizzying array of grabs,
holds, and locks with which to bewilder and incapacitate his foes.

## Bonus Feat {#bonus-feat}

A tetori gains the following bonus feats: 1st level—[Improved Grapple](ref/feat/improved-grapple),
2nd level—[Stunning Pin](ref/feat/stunning-pin), 6th
level—[Greater Grapple](ref/feat/greater-grapple), 10th level—Pinning Knockout, 14th
level—[Chokehold](ref/feat/chokehold), 18th level—[Neckbreaker](ref/feat/neckbreaker). These feats
replace a monk's normal bonus feats.

## Graceful Grappler (Ex) {#graceful-grappler}

A tetori uses his monk level in place of his base attack bonus to determine CMB and CMD for
grappling. At 4th level, he suffers no penalties on attack rolls, can make attacks of opportunity
while grappling, and retains his Dexterity bonus to AC when pinning an opponent or when
[grappled](ref/rule/grapple-conditions). At 8th level, a tetori gains the [grab](ref/umr/grab)
special attack when using unarmed strikes, and can use this ability against creatures his own size
or smaller by spending 1 point from his ki pool, or against larger creatures by spending 2 points
from his ki pool. At 15th level, a tetori gains the [constrict](ref/umr/constrict) special attack,
inflicting his unarmed strike damage on any successful [grapple](ref/rule/grapple) check. This
ability replaces flurry of blows.

## Counter-Grapple (Ex) {#counter-grapple}

At 4th level, a tetori wrestler may make an attack of opportunity against a creature attempting to
grapple him. This ability does not allow the tetori to make an attack of opportunity against a
creature with the Greater Grapple feat. At 6th level, he may use counter-grapple even if his
attacker has [concealment](ref/rule/concealment) or total concealment, at 8th level even if he is
flat-footed, and at 10th level even if his attacker has exceptional reach. This ability replaces
slow fall.

## Break Free (Ex) {#break-free}

At 5th level, a tetori adds his monk level on combat maneuver or Escape Artist checks made to escape
a grapple. If a tetori fails a save against an effect that causes him to become
[entangled](ref/rule/entangled), [paralyzed](ref/rule/paralyzed), [slowed](ref/spell/slow), or
[staggered](ref/misc/staggered), he may spend 1 point from his ki pool as an immediate action to
attempt a new save. This ability replaces high jump.

## Inescapable Grasp (Su) {#inescapable-grasp}

At 9th level, a tetori can spend 1 point from his ki pool to suppress his opponents'
_[freedom of movement](ref/spell/freedom-of-movement)_ and magical bonuses to Escape Artist or on
checks to escape a grapple. At 13th level, this ability also duplicates the effect of
_[dimensional anchor](ref/spell/dimensional-anchor)_. At 17th level, the tetori's unarmed strike
gains the _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ special ability, and an
[incorporeal](ref/subtype/incorporeal) creature that he strikes gains the grappled condition (Reflex
negates, DC 10 + 1/2 the wrestler's level + his Wisdom modifier). Inescapable grasp is a swift
action and lasts until the beginning of the wrestler's next turn. This ability replaces abundant
step, improved evasion, timeless body, and tongue of the sun and moon.

## Form Lock (Su) {#form-lock}

At 13th level, a tetori can negate a polymorph effect by touch with a Wisdom check, adding a bonus
equal to his monk level, against a DC of 11 + the caster level of the effect (or HD of the creature,
for supernatural polymorph effects). This is a standard action requiring 2 points from the tetori's
ki pool, or an immediate action if a creature the tetori is grappling attempts to use a polymorph
effect. This ability replaces diamond soul.

## Iron Body (Su) {#iron-body}

At 19th level, as a move action, a tetori can make his tissues ultra-dense for 1 minute as the
_[iron body](ref/spell/iron-body)_ spell by spending 3 points from his ki pool. This ability
replaces empty body.
