+++
id = "ref/arc-ranger/blightwarden"
kind = "archetype"
title = "Blightwarden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Blightwarden"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightwarden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "hunt-the-blighted" },
  { anchor = "emulate-taint-ex-su-or-sp", level = 1 },
  { anchor = "blightwalker", level = 3 },
  { anchor = "resist-corruption", level = 3 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["emulate-taint-ex-su-or-sp"] },
  { replaces = "1st favored terrain", feature = "favored-terrain", levels = [3], by = ["blightwalker"] },
  { replaces = "Endurance", feature = "endurance", by = ["resist-corruption"] },
  { alters = "Favored enemy", feature = "favored-enemy", by = ["hunt-the-blighted"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["blightwalker"] },
]
+++

Some rangers feel so closely connected to their homelands that they stand as guardians against
pervasive corruptions that pervert those lands beyond the point of recognition.

## Hunt the Blighted (Ex) {#hunt-the-blighted}

A blightwarden's first favored enemy is always a special type of creature: blighted. His bonuses
from his first favored enemy apply to creatures with one or more of the following templates:
[blighted fey](ref/template/blighted-fey), [fungal creature](ref/template/fungal-creature),
[fungoid](ref/template/fungoid), [Mana Wastes mutant](ref/template/mana-wastes-mutant),
[mutant](ref/template/mutant), [mutant goblin](ref/template/mutant-goblin), and
[plagued beast](ref/template/plagued-beast). Additionally, the bonuses apply against creatures with
the [blight](ref/subtype/blight) subtype.

Each time the blightwarden gains a new favored enemy, his additional +2 bonus always applies to this
first favored enemy.

This alters favored enemy.

## Emulate Taint (Ex, Su, or Sp) {#emulate-taint-ex-su-or-sp}

Once per day as a standard action, a blightwarden can examine visible evidence of a creature that
has been affected by a natural or supernatural [blight](ref/spell/blight). This might include
visible tracks left by a creature with the fungal creature template, or a dead creature with the
blighted fey template, or any similar evidence left by any creature as described in the hunt the
blighted fey ability.

When the blightwarden does this, for the next 24 hours, he can use any one extraordinary,
supernatural, or [spell-like ability](ref/umr/spell-like-abilities) granted by the template (or the
blight subtype) for a number of minutes equal to his ranger level. This duration need not be used
all at once, but they must be spent in 1-minute increments. Saving throw DCs for this ability are
calculated as if the blightwarden had the relevant template (for example, the DC of an ability from
the blighted fey template would be equal to 10 + half the blightwarden's Hit Dice + his Constitution
modifier). He cannot use abilities that would create a permanent effect beyond this ability's
duration, and can never use more than one ability from a template or subtype in this way during a
single 24-hour period.

For example, the blightwarden cannot use a blighted ooze's cursed domain ability to create a domain
of evil. However, the blightwarden could gain a blighted fey's thorn throw ability for a number of
minutes equal to his ranger level (in this case, the blightwarden would gain a thorn attack for that
duration).

This replaces wild empathy.

## Blightwalker (Ex) {#blightwalker}

At 3rd level, a blightwarden gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks when in areas afflicted by a natural or supernatural
blight. Blighted areas include [cursed lands](ref/rule/cursed-land),
[domains of evil](ref/rule/domains-of-evil), regions negatively affected by a spell or ability that
affects at least a 300-square-foot area, or regions where a specific
[affliction](ref/rule/afflictions) is prevalent. In addition, the blightwarden adds this bonus to
ability checks, saving throws, and skill checks to avoid natural and supernatural hazards in
blighted areas. He can choose to improve this bonus in place of improving a favored terrain bonus. A
blightwarden traveling through blighted areas leaves no trail and cannot be tracked (though he can
leave a trail if he chooses).

This alters favored terrain and replaces the blightwarden's first favored terrain.

## Resist Corruption (Ex) {#resist-corruption}

At 3rd level, a blightwarden gains a +2 bonus on saving throws against curses, diseases,
mind-affecting effects, poisons, and transmutation effects.

This replaces endurance.
