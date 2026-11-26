+++
id = "ref/arc-skald/war-painter"
kind = "archetype"
title = "War Painter"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20War%20Painter"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "war_painter", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "furious-paint", level = 1 },
  { anchor = "thousand-totems", level = 5 },
  { anchor = "arcane-flourish", level = 7 },
]
trades = [
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["thousand-totems"] },
  { replaces = "Lore master", feature = "lore-master", by = ["arcane-flourish"] },
  { alters = "Raging song", feature = "raging-song", by = ["furious-paint"] },
]
+++

The gripplis of the Valashmai Jungle exhibit savage strength for their size—attributed in part to
the frightful magical pigments applied to their skin by the tribes' mystical lore keepers.

## Furious Paint (Su) {#furious-paint}

By spending 10 minutes preparing and applying special paints to his or an ally's skin, a war painter
can create patterns that store the effects of one of his raging songs. The war painter must expend 1
or more rounds of his raging song class ability while anointing the ally, and the paint retains its
potency until the war painter recovers his daily uses of raging song. The ally can activate the
paint as a move action, gaining the benefits of the raging song, including any rage powers as
appropriate. This effect lasts a number of rounds equal to the rounds of raging song the war painter
expended + the war painter's ranks in [Craft](ref/skill/craft-any) (calligraphy, paintings, or
tattoos)—but no more than double the number of rounds of raging song expended. By halving the
remaining number of rounds of raging song, an ally can suspend the paint's effects as a free action
and activate the paint again later as a move action.

A war painter can apply the effects of any feats that affect bardic performance to his furious
paint, except effects that extend the effects of performances, such as the Lingering Song feat. A
creature can be subject to only one application of furious paint at a time.

This ability modifies the raging song class feature and does not prevent a war painter from
performing other raging songs.

## Thousand Totems (Su) {#thousand-totems}

At 5th level, a war painter can channel a powerful totem into his furious paints while applying the
pigments on an ally. This grants the painted ally the benefits of one additional rage power when the
ally activates the furious paints. The war painter does not need to know the rage power, but it must
be one for which he qualifies. Furthermore, the war painter can select only a blood rage power
(_Pathfinder RPG Advanced Class Guide_ 80) or a totem rage power (_Pathfinder RPG Advanced Player's
Guide_ 74). If the war painter already has a different blood rage or totem rage power that would be
applied to the painted ally, this new rage power replaces it and any other rage powers that require
it as a prerequisite.

A war painter can use this ability once per day at 5th level, and he gains one additional use at
11th and 17th levels. He can apply this ability multiple times to the same creature, though only to
give it rage powers that use the granted rage power as a prerequisite (such as
[beast totem](ref/ragepower/beast-totem) and
[greater beast totem](ref/ragepower/greater-beast-totem)).

This ability replaces spell kenning.

## Arcane Flourish (Su) {#arcane-flourish}

At 7th level, once per day as he finishes applying his furious paint to a creature, a war painter
can cast one skald spell with a casting time of no more than 1 standard action and infuse the spell
into the paint. Once while benefiting from the paint's raging song, the painted ally can use a
standard action to cast the infused spell on herself as if the war painter had cast it. The spell
ends when the paint's other effects end.

A war painter can infuse only a skald spell whose level is at least 2 levels lower than the
highest-level skald spell he can cast. He can infuse any targeted spell in a painted ally, even if
its range is personal. The war painter can use this ability twice per day at 13th level and three
times per day at 19th level.

This ability replaces lore master.
