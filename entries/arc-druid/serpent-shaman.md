+++
id = "ref/arc-druid/serpent-shaman"
kind = "archetype"
title = "Serpent Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Serpent%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serpent_shaman", path = "json/archetypes_druid2.json" },
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

A shaman with this totem calls upon the cunning serpent, the stealthy deceiver who draws the weak
minded in and strikes while they are unaware. Some hate its treacherous nature, while others praise
its thoughtful pragmatism.

## Nature Bond {#nature-bond}

A serpent shaman who chooses an animal companion must select a snake. If choosing a domain, the
serpent shaman must choose from the [Animal](ref/domain/animal), [Charm](ref/domain/charm),
Trickery, and [Water](ref/domain/water) domains.

## Wild Empathy (Ex) {#wild-empathy}

A serpent shaman can use wild empathy with reptiles as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a serpent shaman may adopt an aspect of the snake while retaining her normal form.
This ability functions as the bear shaman ability, but the druid may select from the following
bonuses: movement (climb speed 20 feet, swim speed 20 feet), scales (+2 natural armor bonus to AC),
senses ([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent)), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d4\], poison \[_frequency_ 1 round (6), _effect_
1 Con damage, _Cure_ 1 save, Con-based DC\] for a Medium druid, +2 CMB to grapple). While using
totem transformation, the serpent shaman may speak normally and can cast
_[speak with animals](ref/spell/speak-with-animals)_ (reptiles only) at will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a serpent shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning snakes, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the bear shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a serpent shaman's wild shape ability functions at her druid level - 2. If she takes
on the form of a snake, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a serpent shaman gains one of the following bonus feats:
[Combat Expertise](ref/feat/combat-expertise), [Improved Feint](ref/feat/improved-feint),
[Skill Focus](ref/feat/skill-focus) (Bluff), [Stealthy](ref/feat/stealthy), or
[Strike Back](ref/feat/strike-back). She must meet the prerequisites for these bonus feats. This
ability replaces venom immunity.
