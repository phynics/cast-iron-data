+++
id = "ref/arc-druid/bat-shaman"
kind = "archetype"
title = "Bat Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Bat%20Shaman"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bat_shaman", path = "json/archetypes_druid.json" },
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
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["bonus-feat"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["wild-empathy"] },
]
+++

The bat shaman's totem is the agile bat, flitting and turning with incredible speed through even the
most convoluted mazes. Her enemies do not know when she will appear, and when she does, she strikes
fast and hard before disappearing into the night.

## Nature Bond {#nature-bond}

A [bat](ref/companion/dire-bat) shaman who chooses an animal companion must select a bat. If
choosing a domain, the bat shaman must choose from [Air](ref/domain/air),
[Animal](ref/domain/animal), Darkness (Night subdomain), and Trickery (Deception subdomain).

## Wild Empathy (Ex) {#wild-empathy}

A bat shaman can use wild empathy with bats as a full-round action with a +4 bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a bat shaman may adopt an aspect of the bat while retaining her normal form. This
ability functions as the ape shaman ability, but the druid may select from the following sets of
bonuses and abilities: movement (fly speed 30 ft. \[average\]; the druid must be at least 5th level
to select this bonus), [natural weapons](ref/umr/natural-attacks) (bite \[1d4 for a Medium
shaman\]), or senses ([blindsense](ref/umr/blindsense) 20 ft.).

While using totem transformation, the bat shaman may speak normally and can cast
_[speak with animals](ref/spell/speak-with-animals)_ (bats only) at will. This ability replaces
woodland stride.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a bat shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning bats, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the ape shaman ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a bat shaman's wild shape ability functions at her druid level -2. If she takes on the
form of a bat, she instead uses her druid level + 2.

## Bonus Feat {#bonus-feat}

At 9th level and every four levels thereafter, a bat shaman gains one of the following bonus feats:
[Acrobatic](ref/feat/acrobatic), [Agile Maneuvers](ref/feat/agile-maneuvers),
[Improved Initiative](ref/feat/improved-initiative),
[Lightning Reflexes](ref/feat/lightning-reflexes), or [Skill Focus](ref/feat/skill-focus)
(Perception). She must meet the prerequisites for these bonus feats. This ability replaces venom
immunity.
