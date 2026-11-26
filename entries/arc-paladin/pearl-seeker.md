+++
id = "ref/arc-paladin/pearl-seeker"
kind = "archetype"
title = "Pearl Seeker"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Pearl%20Seeker"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pearl_seeker", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "aquatic-adventures"
page = "54"

[fields]
kind = "archetype"
features = [
  { anchor = "seek-impressions", level = 1 },
  { anchor = "aquatic-domain", level = 3 },
  { anchor = "vision-magic" },
  { anchor = "divine-hippocampus", level = 5 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["seek-impressions"] },
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["aquatic-domain"] },
  { replaces = "aura of resolve", feature = "aura-of-resolve", by = ["aquatic-domain"] },
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["divine-hippocampus"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Spells", feature = "spells", by = ["vision-magic"] },
  { alters = "Divine bond", feature = "divine-bond", by = ["divine-hippocampus"] },
  { alters = "Class skills" },
]
+++

Some paladins are called to their faith by strange empathic visions and dreams that beckon them to
the oceans and beyond, to right aquatic injustice and search for a glorious gasping and whispering
pearl they don't understand. Their contact with the strange but benevolent entity sending the dreams
grants them unusual powers compared to other paladins.

## Armor Proficiency and Class Skills {#armor-proficiency-and-class-skills}

A pearl seeker is proficient with light and medium armor but not with shields, and gains Swim as a
class skill.

This alters the paladin's armor proficiency and class skills.

## Seek Impressions (Ex, Sp) {#seek-impressions}

Pearl seekers gain their power from a rare resonant sensitivity to the vision-granting entity. A
pearl seeker gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus feat and can use
_[detect psychic significance](ref/spell/detect-psychic-significance)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities).

This ability replaces _detect evil_.

## Aquatic Domain (Su) {#aquatic-domain}

At 3rd level, a pearl seeker gains the 1st-level domain power of the
[Aquatic](ref/druiddomain/aquatic) terrain domain (see page 33 of _Ultimate Magic_), using her
paladin level as her effective druid level. At 8th level, she gains the 6th-level domain power of
the Aquatic terrain domain.

This ability replaces aura of courage and aura of resolve.

## Vision Magic {#vision-magic}

A pearl seeker casts divine spells spontaneously, using the spells known and spells per day from the
[bloodrager](ref/class/bloodrager) progression table. At 7th level, she gains
_[slipstream](ref/spell/slipstream)_ as a bonus 1st-level spell known; at 10th level, she gains
_[ride the waves](ref/spell/ride-the-waves)_ as a bonus 2nd-level spell known; at 13th level, she
gains _[fluid form](ref/spell/fluid-form)_ as a bonus 3rd-level spell known; and at 16th level, she
gains _[seamantle](ref/spell/seamantle)_ as a bonus 4th-level spell known. She also adds
_[hydraulic push](ref/spell/hydraulic-push)_ and _[hydraulic torrent](ref/spell/hydraulic-torrent)_
(as a 1st and 3rd level spells, respectively) to her paladin spell list (but must learn these spells
as normal).

This ability alters the paladin's spells.

## Divine Hippocampus {#divine-hippocampus}

At 5th level, a pearl seeker must choose a mount as her divine bond, gaining a
[hippocampus](ref/companion/hippocampus) mount with the following companion statistics.

**Size** Large; **Speed** 5 ft., swim 80 ft.; **AC** +4 natural armor; **Attack** bite (1d6), tail
slap (1d4; secondary attack); **Ability Scores** Str 18, Dex 13, Con 15, Int 2, Wis 12, Cha 11;
**Special Qualities** [darkvision](ref/rule/darkvision) 60 ft.,
[low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent),
[water dependency](ref/umr/water-dependency).

This ability alters divine bond and replaces channel positive energy.
