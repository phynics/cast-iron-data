+++
id = "ref/arc-druid/shark-shaman"
kind = "archetype"
title = "Shark Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Shark%20Shaman"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shark_shaman", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-bond", level = 1 },
  { anchor = "wild-empathy", level = 1 },
  { anchor = "totem-transformation", level = 2 },
  { anchor = "totemic-summons", level = 5 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "bonus-feat", level = 9 },
]
trades = [
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

Some druids emulate the deadly shark, a remorseless hunter that marine dwellers dread. Like a true
shark, a shark shaman leaves blood and fear in her wake.

## Nature Bond {#nature-bond}

A shark shaman who chooses an animal companion must select a [shark](ref/companion/shark). If
choosing a domain, a shark shaman may choose the [Animal](ref/domain/animal), Death,
[War](ref/domain/war), or [Water](ref/domain/water) domain.

## Wild Empathy (Ex) {#wild-empathy}

A shark shaman can use wild empathy with fish as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a shark shaman may adopt an aspect of the shark while retaining her normal form. This
ability functions as the dragon shaman's totem transformation ability, but the druid may select from
the following bonuses: movement (can breathe water, swim speed 30 feet), senses
([scent](ref/umr/scent) 30 feet, scent 90 feet in water), [natural weapons](ref/umr/natural-attacks)
(bite 1d6 for a Medium shaman), or shark skin (+2 natural armor, creatures grappling the shaman take
1 point of slashing damage per round of grapple). While using totem transformation, the shark shaman
may speak normally and can cast _[speak with animals](ref/spell/speak-with-animals)_ (fish only) at
will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a shark shaman may use _[summon nature's ally I](ref/spell/summon-natures-ally-1)_ to
summon a [stingray](ref/monster/ray-stingray) (_Bestiary 2_) and
_[summon nature's ally II](ref/spell/summon-natures-ally-2)_ to summon a
[manta ray](ref/monster/ray-manta-ray) (_Bestiary 2_). She may cast _summon nature's ally_ as a
standard action when summoning rays and sharks, and summoned rays and sharks gain a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the dragon shaman's totemic summons ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a shark shaman's wild shape ability functions at her druid level -2. If she takes on
the form of a shark, she instead uses her druid level +2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a shark shaman gains one of the following bonus feats:
[Bleeding Critical](ref/feat/bleeding-critical),
[Improved Initiative](ref/feat/improved-initiative),
[Lightning Reflexes](ref/feat/lightning-reflexes), [Self-Sufficient](ref/feat/self-sufficient), or
[Skill Focus](ref/feat/skill-focus) (Swim). She must meet prerequisites for these bonus feats. This
ability replaces venom immunity.
