+++
id = "ref/arc-rogue/dreamthief"
kind = "archetype"
title = "Dreamthief"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Dreamthief"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dreamthief", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "planar-adventures"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "dreamshard-focus", level = 1 },
  { anchor = "lucid-dreamer", level = 3 },
  { anchor = "soothe-dreaming", level = 4 },
  { anchor = "dream-infiltrator", level = 8 },
]
trades = [
  { replaces = "Sneak attack", feature = "sneak-attack", by = ["dreamshard-focus"] },
  { replaces = "master strike", feature = "master-strike", by = ["dreamshard-focus"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["lucid-dreamer"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["soothe-dreaming"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["dream-infiltrator"] },
  { replaces = "rogue talent gained at 12th level", feature = "rogue-talents", levels = [12], by = ["dream-infiltrator"] },
  { alters = "Class skills" },
]
+++

The dreamthief is master of both waking and dreaming worlds. Each dreamthief bears a focused
fragment of emotion, known as a dreamshard, within her soul. Some are born with such fragments,
while others gain their dreamshards during traumatic moments, especially those involving nightmares,
attacks by ethereal beings, or incidents that take place in the Dimension of Dreams. Whether a
dreamshard is shaped from the dreamer's aggregated emotions or manifested from a repressed aspect of
herself, this metaphysical crystal grants a dreamthief supernatural powers, which she supplements
with skill and grace.

Dreamthieves' powers grant them enhanced access to [dreamscapes](ref/rule/dimension-of-dreams).
Using the unique power of her dreamshard, a knowledgeable dreamthief can crystallize and steal
dreamers' deepest emotions. Such theft can alter dreamers in profound ways, whether for better or
worse.

## Skills {#skills}

Knowledge (arcana) and Knowledge (planes) are class skills for a dreamthief.

This alters the rogue's class skills.

## Dreamshard Focus (Su) {#dreamshard-focus}

At 1st level, a dreamthief selects an [emotional focus](ref/ability/emotional-focus) from among
those available to a spiritualist's phantom (_Pathfinder RPG Occult Adventures_ 80). She gains the
abilities granted by that emotional focus (with the exception of the focus determining her good
saving throws—she retains the typical rogue saves). For each of the two skills associated with that
emotional focus, a dreamthief gains ranks in that skill equal to her rogue level; this does not
allow her ranks in these skills to exceed her Hit Dice.

A dreamthief is considered to be both a phantom and a spiritualist for the purpose of emotional
focus abilities whose effect references both a phantom and a spiritualist, such as dutiful strike,
and she treats her rogue level as both her spiritualist level and her phantom Hit Dice when
determining abilities and save DCs.

Once per round when a dreamthief makes a melee attack, she can declare that attack to be a
dreamstrike. This does not require an action, but a dreamthief must declare a dreamstrike before
making the attack roll. A dreamstrike is treated as a slam attack for the purpose of emotional focus
abilities that apply to a phantom's slam attacks, such as miserable strike. At 20th level, any melee
attack a dreamthief makes automatically gains this benefit.

This replaces sneak attack and master strike.

## Lucid Dreamer (Ex) {#lucid-dreamer}

At 3rd level, a dreamthief can control her dreams, and gains [Lucid Dreamer](ref/feat/lucid-dreamer)
as a bonus feat.

This replaces trap sense.

## Soothe Dreaming (Su) {#soothe-dreaming}

At 4th level, a dreamthief can steal negative emotions, freeing allies from harmful conditions. This
acts as the [mesmerist's](ref/class/mesmerist) touch treatment ability (_Occult Adventures_ 43),
treating her rogue level as her mesmerist level; a dreamthief can use this ability once per day for
every 3 rogue levels she has.

This replaces uncanny dodge.

## Dream Infiltrator (Sp) {#dream-infiltrator}

A dreamthief can enter dreams, whether to learn secrets or meddle more directly. At 8th level, a
dreamthief can cast _[dream scan](ref/spell/dream-scan)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities). At 12th level, once per day she can cast either
_[dream scan](ref/spell/dream-scan)_ or _[dream travel](ref/spell/dream-travel)_ as a
[spell-like ability](ref/umr/spell-like-abilities). The caster level of these
[spell-like abilities](ref/umr/spell-like-abilities) is equal to her rogue level.

This replaces improved uncanny dodge and the rogue talent gained at 12th level.
