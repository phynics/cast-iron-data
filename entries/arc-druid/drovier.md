+++
id = "ref/arc-druid/drovier"
kind = "archetype"
title = "Drovier"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Drovier"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drovier", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-s-bond", level = 1 },
  { anchor = "communal-aspect", level = 4 },
]
trades = [
  { replaces = "Wild shape", feature = "wild-shape", by = ["communal-aspect"] },
  { alters = "Nature's bond", feature = "nature-bond", by = ["nature-s-bond"] },
]
+++

Droviers view their allies and adventuring companions as a herd or pack to be protected and
directed, with variations on that theme ranging from culture to culture. The orcs of Belkzen see
droviers as alpha predators, offering tribal warriors totemic power in exchange for obedience in
combat. The elves of the Mwangi Expanse regard them as spokespeople for the jungle, adopting aspects
that help preserve and defend the land.

## Nature's Bond (Ex) {#nature-s-bond}

A drovier must take the [Animal](ref/domain/animal) domain with this ability, or the
[Eagle](ref/druiddomain/eagle) or [Wolf](ref/druiddomain/wolf) animal domains from pages 34 and 36
respectively of _Pathfinder RPG Ultimate Magic_.

This ability modifies nature's bond.

## Communal Aspect (Su) {#communal-aspect}

At 4th level, a drovier can imbue her allies (including herself) with an aspect of a wild animal. As
a standard action, she chooses an animal totem and grants the abilities of that totem to every ally
within 30 feet. This otherwise functions like the spell _[animal aspect](ref/spell/animal-aspect)_.
She can use this ability for 10 minutes per druid level each day. This duration does not need to be
consecutive, but it must be used in 10-minute increments. If she uses the ability to grant a new
aspect, any previous aspect immediately ends. At 20th level, the drovier can use this ability at
will.

At 6th level, the drovier's communal aspect ability grants the benefits of the spell
_[greater animal aspect](ref/spell/animal-aspect-greater)_. The drovier can still choose only one
aspect to grant her allies. At 8th level, the drovier can choose to grant her allies the benefits of
the spell _[aspect of the falcon](ref/spell/aspect-of-the-falcon)_ instead of an animal aspect. At
10th level, the drovier can choose to grant her allies the benefits of the spell
_[aspect of the bear](ref/spell/aspect-of-the-bear)_ instead of an animal aspect. At 12th level, the
drovier can choose to grant her allies the benefits of the spell
_[aspect of the stag](ref/spell/aspect-of-the-stag)_ instead of an animal aspect. At 14th level, the
drovier can choose to grant her allies the benefits of the spell
_[aspect of the wolf](ref/spell/aspect-of-the-wolf)_ rather than an animal aspect.

This replaces wild shape.
