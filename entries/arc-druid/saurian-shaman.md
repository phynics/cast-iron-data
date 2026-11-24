+++
id = "ref/arc-druid/saurian-shaman"
kind = "archetype"
title = "Saurian Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Saurian%20Shaman"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "saurian_shaman", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "39"

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

A shaman with this focus calls upon the primeval dinosaur, the archaic terror that lingers as a
hungering, atavistic stranger at the fringes of the ecosystem, a destroyer and despoiler whose
coming other animals dread.

## Nature Bond {#nature-bond}

A saurian shaman who chooses

an animal companion must select a dinosaur.

If choosing a domain, a saurian shaman

must choose from the [Animal](ref/domain/animal), [Destruction](ref/domain/destruction),

Strength, and [War](ref/domain/war) domains.

## Wild Empathy (Ex) {#wild-empathy}

A saurian shaman can use wild empathy with dinosaurs and reptiles as a full-round action with a +4
bonus.

## Totem Transformation (Su) {#totem-transformation}

At 2nd level, a saurian shaman may adopt an aspect of the saurian while retaining her normal form.
This ability functions as the dragon shaman's totem transformation ability, but the druid may select
from the following bonuses: movement (+10 enhancement bonus to land speed), scales (+2 natural armor
bonus to AC), senses ([low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent)), or
[natural weapons](ref/umr/natural-attacks) (bite \[1d6\], 2 claws \[1d4\] for a Medium druid, rake,
+2 CMB to grapple). While using totem transformation, a saurian shaman may speak normally and can
cast _[speak with animals](ref/spell/speak-with-animals)_ (reptiles and dinosaurs only) at will.

## Totemic Summons (Su) {#totemic-summons}

At 5th level, a saurian shaman may cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
standard action when summoning reptiles and dinosaurs, and these summoned creatures gain
[temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. This ability
otherwise functions as the dragon shaman's totemic summons ability.

## Wild Shape (Su) {#wild-shape}

At 6th level, a saurian shaman's wild shape ability functions at her druid level -2. If she takes on
the form of a reptile or a dinosaur, she instead uses her druid level +2.

## Bonus Feat {#bonus-feat}

At 9th level and every 4 levels thereafter, a saurian shaman gains one of the following bonus feats:
[Improved Overrun](ref/feat/improved-overrun), [Nimble Moves](ref/feat/nimble-moves),
[Power Attack](ref/feat/power-attack), [Skill Focus](ref/feat/skill-focus) (Intimidate), or
[Vital Strike](ref/feat/vital-strike). She must meet the prerequisites for these bonus feats. This
ability replaces venom immunity.
