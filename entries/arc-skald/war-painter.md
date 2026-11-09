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
replaces = ["Spell kenning", "Lore master"]
alters = ["Raging song"]
+++

The gripplis of the Valashmai Jungle exhibit savage strength for their size - attributed in part to
the frightful magical pigments applied to their skin by the tribes' mystical lore keepers.

**Prerequisites:** Grippli

**Furious Paint (Su)**

**Ability:** By spending 10 minutes preparing and applying special paints to his or an ally's skin,
a war painter can create patterns that store the effects of one of his _raging songs._ The war
painter must expend 1 or more rounds of his _raging song_ class ability while anointing the ally,
and the paint retains its potency until the war painter recovers his daily uses of _raging song._
The ally can activate the paint as a **move action**, gaining the benefits of the _raging song,_
including any rage powers as appropriate. This effect lasts a number of rounds equal to the rounds
of _raging song_ the war painter expended + the war painter's ranks in [Craft](ref/skill/craft-any)
(calligraphy, paintings, or tattoos) - but no more than double the number of rounds of _raging song_
expended.

**Alters:** Raging song

**Free:** By halving the remaining number of rounds of _raging song,_ an ally can suspend the
paint's effects and activate the paint again later as a **move action**.

**Special:** A war painter can apply the effects of any feats that affect bardic performance to his
furious paint, except effects that extend the effects of performances, such as the
[Lingering Performance](ref/feat/lingering-performance) feat. A creature can be subject to only one
application of furious paint at a time. The war painter can still use his _raging song_ ability in
the normal way.

**Thousand Totems (Su)**

**Ability:** A war painter can channel a powerful totem into his furious paints while applying the
pigments on an ally. This grants the painted ally the benefits of one additional rage power when the
ally activates the furious paints. The war painter does not need to know the rage power, but it must
be one for which he qualifies. Furthermore, the war painter can select only a blood rage power or a
totem rage power. If the war painter already has a different blood rage or totem rage power that
would be applied to the painted ally, this new rage power replaces it and any other rage powers that
require it as a prerequisite.

**Gained:** At 5th Level

**Replaces:** Spell kenning

**Special:** He can apply this ability multiple times to the same creature, though only to give it
rage powers that use the granted rage power as a prerequisite (such as
[beast totem](ref/ragepower/beast-totem) and
[greater beast totem](ref/ragepower/greater-beast-totem)).

**Usage:** Once per day

**Usage:** Once per day

**Arcane Flourish (Su)**

**Ability:** Once per day as he finishes applying his _furious paint_ to a creature, a war painter
can cast one skald spell with a casting time of no more than 1 standard action and infuse the spell
into the paint. Once while benefiting from the paint's _raging song,_ the painted ally can use a
**standard action** to cast the infused spell on herself as if the war painter had cast it. The
spell ends when the paint's other effects end.

**Gained:** At 7th Level

**Replaces:** Lore master

**Special:** A war painter can infuse only a skald spell whose level is at least 2 levels lower than
the highest-level skald spell he can cast. He can infuse any targeted spell in a painted ally, even
if its range is personal.
