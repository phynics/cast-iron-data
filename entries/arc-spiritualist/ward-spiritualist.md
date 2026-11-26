+++
id = "ref/arc-spiritualist/ward-spiritualist"
kind = "archetype"
title = "Ward Spiritualist"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Ward%20Spiritualist"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ward_spiritualist", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "wilderness-origins"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "kami-phantom", level = 1 },
  { anchor = "ward-implement", level = 2 },
  { anchor = "merged-manifestation", level = 3 },
]
trades = [
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["ward-implement"] },
  { replaces = "phantom recall", feature = "phantom-recall", by = ["ward-implement"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["ward-implement"] },
  { alters = "Phantom", feature = "phantom", by = ["kami-phantom"] },
  { alters = "Spellcasting", feature = "spells", by = ["ward-implement"] },
]
+++

While many spiritualists are bound to a departed spirit, a condition more likely to be the result of
chance or tragedy than a career choice, there are some individuals who seek out this life. A ward
spiritualist ventures into the wilderness and petitions a [kami](ref/family/kami) to help her in her
travels, either taking an existing ward with her or becoming the kami's new ward.

## Kami Phantom (Su) {#kami-phantom}

The ward spiritualist's [phantom](ref/sidekick/phantom) is less powerful than most, but it has an
innate connection to its ward. The ward spiritualist's phantom is a kami phantom, functioning as
normal for a phantom, except that its base attack bonus is equal to three-quarters its Hit Dice (as
a [rogue](ref/class/rogue)) and its Hit Dice are d8s instead of d10s. Additionally, a kami phantom
cannot manifest as incorporeal, only ectoplasmic.

This alters phantom.

## Ward Implement (Su) {#ward-implement}

The ward spiritualist gains a single implement school of her choice, as an
[occultist](ref/class/occultist), along with its resonant focus power and base focus power. The ward
spiritualist does not gain additional spells from her ward implement, and it always starts each day
with mental focus invested equal to half her class level (minimum 1).

When she gains her ward implement, the ward spiritualist must choose either to have a physical
implement or to be the implement herself. If she chooses to have a physical implement, her
spiritualist spells include it as a focus component, and she can change what item is her implement
when she regains her spells at the start of each day. Her implement must be an item that can be held
in one hand, and it cannot be a manufactured weapon. If the ward spiritualist chooses to be her own
ward implement, her spiritualist spells always have a somatic component in addition to their other
components; this component does not become an emotion component.

She can remove the focus or somatic component of her spells, but this requires a
[concentration](ref/rule/concentration) check with a DC equal to 15 + twice the spell level, which
is increased for a thought component as normal.

She gains a focus power for her implement school at 2nd level, and again at 6th level and 12th
level. She must meet the prerequisites of these focus powers, treating her spiritualist level as her
occultist level for focus power prerequisites. She also treats her spiritualist level as her
occultist level for feat prerequisites.

This alters spellcasting and replaces bonded senses, phantom recall, and greater spiritual
interference.

## Merged Manifestation (Su) {#merged-manifestation}

At 3rd level, the ward spiritualist learns how to merge her kami phantom with her ward implement.
This functions as bonded manifestation, except that she does not choose ectoplasmic or incorporeal.
Instead, she gains different benefits depending on whether she has a physical implement or is her
own implement.

If she has a physical implement, when using her merged manifestation, her implement functions as a
one-handed [improvised weapon](ref/misc/improvised-weapons) of appropriate size, and she does not
take the usual penalties associated with wielding an improvised weapon. Additionally, it is
considered to have a +1 enhancement bonus for the duration of the merged manifestation. This
enhancement bonus increases by 1 at 8th level, and again at 13th level and 18th level. At 8th level,
and again at 18th level, it deals damage as a weapon
[one size category larger](ref/misc/damage-die-adjustments). At 13th level, her implement also gains
the benefits of _[spirit-bound blade](ref/spell/spirit-bound-blade)_ for the duration of the merged
manifestation.

If she is her own implement, when using her merged manifestation, she gains the unarmed strike class
feature as a 1st level [unchained monk](ref/class/unchained-monk). At 8th level, her unarmed strike
damage is that of a 4th-level unchained monk, and she gains flurry of blows as a 1st-level unchained
monk. At 13th level, her unarmed damage is that of an 8th-level unchained monk, and her unarmed
strikes gain the benefits of _spirit-bound blade_ for the duration of the merged manifestation. At
18th level, her unarmed damage is that of a 12th level unchained monk, and she can use flurry of
blows as an 11th-level unchained monk.
