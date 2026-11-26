+++
id = "ref/arc-druid/boar-shaman"
kind = "archetype"
title = "Boar Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Boar%20Shaman"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "boar_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-combat"
page = "43"

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

A boar shaman chooses the stolid and ferocious boar as her totem. Content to be left alone, she
becomes one of the most dangerous creatures of the wild when provoked.

## Nature Bond {#nature-bond}

A boar shaman who chooses an animal companion must select a [boar](ref/companion/boar). If choosing
a domain, the boar shaman must choose from the [Animal](ref/domain/animal),
[Destruction](ref/domain/destruction) (Rage), [Protection](ref/domain/protection), and Strength
domains.

## Wild Empathy (Ex) {#wild-empathy}

A boar shaman can use wild empathy with porcine creatures as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a boar shaman may adopt an aspect of the boar while retaining her normal form. This
ability functions as the ape shaman ability, but the druid may select from the following sets of
bonuses and abilities: movement (+10 enhancement bonus to land speed), senses
([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent)),
[natural weapons](ref/umr/natural-attacks) (gore \[1d8 for a Medium druid\], +2 on combat maneuver
checks to overrun), or toughness (+2 natural armor bonus to AC, [Endurance](ref/feat/endurance)
feat). While using totem transformation, the boar shaman may speak normally and can cast
_[speak with animals](ref/spell/speak-with-animals)_ (boars and related animals only) at will. This
ability replaces woodland stride.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a boar shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning [boars](ref/monster/boar) or other porcine creatures, and these
summoned creatures gain [temporary hit points](ref/rule/temporary-hit-points) equal to her druid
level. This ability otherwise functions as the ape shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a boar shaman's wild shape ability functions at her druid level -2. If she takes on
the form of a boar, she instead uses her druid level +2.

## Bonus Feat {#bonus-feat}

At 9th level and every four levels thereafter, a boar shaman gains one of the following bonus feats:
[Bleeding Critical](ref/feat/bleeding-critical), [Blind-Fight](ref/feat/blind-fight),
[Diehard](ref/feat/diehard), or [Improved Overrun](ref/feat/improved-overrun). She must meet the
prerequisites for these bonus feats. This ability replaces venom immunity.
