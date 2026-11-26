+++
id = "ref/arc-druid/wolf-shaman"
kind = "archetype"
title = "Wolf Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Wolf%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wolf_shaman", path = "json/archetypes_druid2.json" },
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
  { anchor = "nature-bond", level = 1 },
  { anchor = "wild-empathy", level = 1 },
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

A shaman with this totem calls upon the clever wolf, capable of roaming alone yet wise enough to run
with a pack when facing dangers too great for one alone.

## Nature Bond {#nature-bond}

A [wolf](ref/companion/wolf) shaman who chooses an animal companion must select a wolf. If choosing
a domain, the wolf shaman must choose from the [Animal](ref/domain/animal), Community, Liberation,
and [Travel](ref/domain/travel) domains.

## Wild Empathy (Ex) {#wild-empathy}

A wolf shaman can use wild empathy with canines as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a wolf shaman may adopt an aspect of the wolf while retaining her normal form. This
ability functions as the bear shaman ability, but the druid may select from the following bonuses:
movement (+20 enhancement bonus to land speed), senses
([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent), +4 racial bonus to Survival
when tracking by scent), or [natural weapons](ref/umr/natural-attacks) (bite \[1d4 plus trip\] for a
Medium druid, +2 CMB to trip). While using totem transformation, the wolf shaman may speak normally
and can cast _[speak with animals](ref/spell/speak-with-animals)_ (canines only) at will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a wolf shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning canines, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the bear shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a wolf shaman's wild shape ability functions at her druid level - 2. If she takes on
the form of a canine, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a wolf shaman gains one of the following bonus feats:
[Greater Trip](ref/feat/greater-trip), [Improved Trip](ref/feat/improved-trip),
[Mobility](ref/feat/mobility), [Skill Focus](ref/feat/skill-focus) (Stealth), or
[Spring Attack](ref/feat/spring-attack). She must meet the prerequisites for these bonus feats. This
ability replaces venom immunity.
