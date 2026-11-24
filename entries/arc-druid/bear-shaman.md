+++
id = "ref/arc-druid/bear-shaman"
kind = "archetype"
title = "Bear Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Bear%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bear_shaman", path = "json/archetypes_druid.json" },
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
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["totemic-summons"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

A shaman with this focus calls upon the mighty bear, titan of the woodlands and mountains, a paragon
of strength and ferocity, and yet also a quiet protector rich in wisdom.

## Nature Bond {#nature-bond}

A [bear](ref/companion/bear) shaman who chooses an animal companion must select a bear. If choosing
a domain, the bear shaman must choose from the [Animal](ref/domain/animal),
[Earth](ref/domain/earth), [Protection](ref/domain/protection), and Strength domains.

## Wild Empathy (Ex) {#wild-empathy}

A bear shaman can use wild empathy with bears and wolverines as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a bear shaman may adopt an aspect of the bear while retaining her normal form. She
gains one of the following bonuses: movement (+10 enhancement bonus to land speed, +4 racial bonus
on Swim checks), senses ([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent)),
toughness (+2 natural armor bonus to AC, [Endurance](ref/feat/endurance) feat), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d6\] and 2 claws \[1d4\] for a Medium shaman, +2
to CMB on grapple checks). While using totem transformation, the bear shaman may speak normally and
can cast _[speak with animals](ref/spell/speak-with-animals)_ (mammals only) at will. Using this
ability is a standard action at 2nd level, a move action at 7th level, and a swift action at 12th
level. The bear shaman can use this ability for a number of minutes per day equal to her druid
level. These minutes do not need to be consecutive, but they must be used in 1-minute increments.
This is a polymorph effect and cannot be used while the druid is using another polymorph effect,
such as wild shape.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a bear shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning bears, and summoned bears gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. She can apply the
[young](ref/template/young) template to any bear to reduce the level of the summoning spell required
by one. She can also increase the level of summoning required by one in order to apply either the
[advanced](ref/template/advanced) or the [giant](ref/template/giant) template, or increase it by two
to apply both the advanced and giant templates. This ability replaces a thousand faces.

## Wild Shape (Su) {#wild-shape}

At 6th level, a bear shaman's wild shape ability functions at her druid level - 2. If she takes on
the form of a bear, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a bear shaman gains one of the following bonus feats:
[Diehard](ref/feat/diehard), Endurance, [Great Fortitude](ref/feat/great-fortitude),
[Improved Great Fortitude](ref/feat/improved-great-fortitude), [Toughness](ref/feat/toughness). She
must meet the prerequisites for these bonus feats. This ability replaces venom immunity.
