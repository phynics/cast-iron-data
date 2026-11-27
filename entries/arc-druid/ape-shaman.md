+++
id = "ref/arc-druid/ape-shaman"
kind = "archetype"
title = "Ape Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Ape%20Shaman"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ape_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-combat"
page = "42"

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
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["totemic-summons"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

A shaman with this totem calls upon the mighty ape, a peaceful but powerful simian whose strength is
beyond compare. An ape shaman is a friendly protector of the forest, but will crush those enemies
who rouse her anger.

## Nature Bond {#nature-bond}

An ape shaman who chooses an animal companion must select an [ape](ref/companion/ape) or related
primate. If choosing a domain, the ape shaman must choose from the [Animal](ref/domain/animal),
Community (Family subdomain), [Destruction](ref/domain/destruction) (Rage subdomain), and Strength
domains.

## Wild Empathy (Ex) {#wild-empathy}

An ape shaman can use wild empathy with apes and other primates as a full-round action with a +4
bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, an ape shaman may adopt an aspect of the ape while retaining her normal form. The
druid gains one of the following sets of bonuses and abilities: movement (climb speed 20 ft., +4
racial bonus on Climb checks), senses ([low-light vision](ref/rule/low-light-vision),
[scent](ref/umr/scent)), [natural weapons](ref/umr/natural-attacks) (2 slams \[1d6 for a Medium
shaman\], +2 on combat maneuver checks to [grapple](ref/rule/grapple)), or toughness (+2 natural
armor bonus to AC, [Endurance](ref/feat/endurance) feat).

While using totem transformation, the ape shaman may speak normally and can cast
_[speak with animals](ref/spell/speak-with-animals)_ (primates only) at will. Using this ability is
a standard action at 2nd level, a move action at 7th level, and a swift action at 12th level. The
ape shaman can use this ability for a number of minutes per day equal to her druid level. These
minutes do not need to be consecutive, but they must be used in 1-minute increments. This is a
polymorph effect and cannot be used while the druid is using another polymorph effect, such as wild
shape. This ability replaces woodland stride.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, an ape shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning primates, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. She can apply the
[young](ref/template/young) template to any primate to reduce the level of the summoning spell
required by one. She can also increase the level of summoning required by one in order to apply
either the [advanced](ref/template/advanced) or the [giant](ref/template/giant) template, or
increase it by two to apply both the advanced and giant templates. This ability replaces a thousand
faces.

## Wild Shape (Su) {#wild-shape}

At 6th level, an ape shaman's wild shape ability functions at her druid level -2. If she takes on
the form of an ape, she instead uses her druid level +2.

## Bonus Feat {#bonus-feat}

At 9th level and every four levels thereafter, an ape shaman gains one of the following bonus feats:
[Diehard](ref/feat/diehard), [Endurance](ref/feat/endurance),
[Great Fortitude](ref/feat/great-fortitude), [Improved Bull Rush](ref/feat/improved-bull-rush), and
[Toughness](ref/feat/toughness). She must meet the prerequisites for these bonus feats. This ability
replaces venom immunity.
