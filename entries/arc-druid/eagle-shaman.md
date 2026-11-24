+++
id = "ref/arc-druid/eagle-shaman"
kind = "archetype"
title = "Eagle Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Eagle%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eagle_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "102"

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
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
]
+++

A shaman with this totem calls upon the noble eagle, stern and proud, soaring high above the world
with keen and pitiless eyes that miss nothing.

## Nature Bond {#nature-bond}

An eagle shaman who chooses an [animal](ref/domain/animal) companion must select a
[bird (eagle)](ref/companion/bird). If choosing a domain, the eagle shaman must choose from the
[Air](ref/domain/air), Animal, Nobility, and [Weather](ref/domain/weather) domains.

## Wild Empathy (Ex) {#wild-empathy}

An eagle shaman can use wild empathy with birds as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, an eagle shaman may adopt an aspect of the eagle while retaining her normal form. This
ability functions as the bear shaman ability, but the druid may select from the following bonuses:
movement (fly speed 30 feet \[average\], the druid must be 5th level to select this bonus), senses
([low-light vision](ref/rule/low-light-vision), +4 racial bonus to Perception), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d4\], 2 talons \[1d4\] for a Medium shaman).
While using totem transformation, the eagle shaman may speak normally and can cast
_[speak with animals](ref/spell/speak-with-animals)_ (birds only) at will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, an eagle shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning [eagles](ref/monster/eagle), [rocs](ref/monster/roc), and
[giant eagles](ref/monster/eagle-giant-eagle) (added to the 4th- level list), and these summoned
creatures gain [temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This
ability otherwise functions as the bear shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, an eagle shaman's wild shape ability functions at her druid level - 2. If she takes on
the form of an eagle or roc, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, an eagle shaman gains one of the following bonus feats:
Flyby Attack, Improved Lightning Reflexes, Lightning Reflexes, Skill Focus (Perception), or Wind
Stance. She must meet the prerequisites for these bonus feats. This ability replaces venom immunity.
