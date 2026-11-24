+++
id = "ref/arc-druid/lion-shaman"
kind = "archetype"
title = "Lion Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Lion%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lion_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "103"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-bond" },
  { anchor = "wild-empathy" },
  { anchor = "totem-transformation", level = 2 },
  { anchor = "totemic-summons", level = 5 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "bonus-feat", level = 9 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["totem-transformation"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

A shaman with this totem calls upon the proud lion, imposing and majestic, the mighty leader of
deadly hunters.

## Nature Bond {#nature-bond}

A [lion](ref/companion/cat-big) shaman who chooses an animal companion must select a lion. If
choosing a domain, the lion shaman must choose from the [Animal](ref/domain/animal), Glory,
Nobility, and [Sun](ref/domain/sun) domains.

## Wild Empathy (Ex) {#wild-empathy}

A lion shaman can use wild empathy with felines as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a lion shaman may adopt an aspect of the lion while retaining her normal form. This
ability functions as the bear shaman ability, but the druid may select from the following bonuses:
movement (+20 enhancement bonus to land speed), senses
([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent)), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d4\], 2 claws \[1d4\] for a Medium druid, rake,
+2 CMB to grapple). While using totem transformation, the lion shaman may speak normally and can
cast _[speak with animals](ref/spell/speak-with-animals)_ (felines only) at will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a lion shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning felines, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the bear shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a lion shaman's wild shape ability functions at her druid level - 2. If she takes on
the form of a feline, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a lion shaman gains one of the following bonus feats:
[Dodge](ref/feat/dodge), [Lunge](ref/feat/lunge), [Improved Iron Will](ref/feat/improved-iron-will),
[Iron Will](ref/feat/iron-will), or [Skill Focus](ref/feat/skill-focus) (Acrobatics). She must meet
the prerequisites for these bonus feats. This ability replaces venom immunity.
