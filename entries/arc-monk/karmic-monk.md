+++
id = "ref/arc-monk/karmic-monk"
kind = "archetype"
title = "Karmic Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Karmic%20Monk"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "karmic_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "occult-adventures"
page = "122"

[fields]
kind = "archetype"
features = [
  { anchor = "karmic-strike", level = 1 },
  { anchor = "balanced-mind", level = 3 },
  { anchor = "ki-pool", level = 7 },
  { anchor = "harmony", level = 9 },
  { anchor = "karmic-disruption", level = 16 },
  { anchor = "harmonic-self", level = 20 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["karmic-strike"] },
  { replaces = "Still mind", feature = "still-mind", by = ["balanced-mind"] },
  { replaces = "7th- and 10th-level ki pool abilities", feature = "ki-pool", levels = [7, 10], by = ["ki-pool"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["harmony"] },
  { replaces = "Slow fall 80 feet", feature = "slow-fall", levels = [16], by = ["karmic-disruption"] },
  { alters = "Alignment requirement" },
  { alters = "Slow fall at 19th level to become slow fall 80 feet", feature = "slow-fall", by = ["karmic-disruption"] },
  { alters = "Perfect self", feature = "perfect-self", by = ["harmonic-self"] },
  { alters = "Class skills" },
]
+++

A karmic monk contemplates the myriad harmonies that guide existence. He learns to use the
disharmony in others against them, and to alter his own inner harmonies to exploit weaknesses in his
opponents' defenses.

## Alignment {#alignment}

A karmic monk must be true neutral or of any lawful alignment. This alters the monk's alignment
requirement.

## Class Skills {#class-skills}

The karmic monk gains Diplomacy (Cha) as a class skill instead of Intimidate. This alters the monk's
class skills.

## Karmic Strike (Su) {#karmic-strike}

At 1st level, a karmic monk gains bonuses against creatures that attack him first. If a creature the
karmic monk has not attacked within the past 24 hours makes an attack roll against the karmic monk
or casts an offensive spell that affects the karmic monk, the karmic monk receives a +2 bonus on
attack rolls and damage rolls against that creature. If the karmic monk hits such a target, this
bonus lasts until the end of the karmic monk's turn (or until the beginning of the karmic monk's
next turn, if it isn't his turn). Otherwise, the bonus against a particular creature lasts for 1
minute after the creature's last attack against the karmic monk. This ability replaces stunning
fist.

## Balanced Mind (Su) {#balanced-mind}

At 3rd level, a karmic monk receives a +2 bonus on saving throws against effects with the chaos,
evil, good, or law subtype. He also receives this bonus against the abilities and effects of
creatures of the listed subtypes. This ability replaces still mind.

## Ki Pool (Su) {#ki-pool}

At 7th level, when a karmic monk makes unarmed strikes, they're treated as chaotic, evil, good, and
lawful. This ability replaces the 7th- and 10th-level ki pool abilities.

## Harmony (Su) {#harmony}

At 9th level, as an immediate action, a karmic monk can shift his alignment by one step for the
purpose of all effects dependent on alignment until the beginning of his next turn. This does not
actually alter the karmic monk's alignment. This ability replaces improved evasion.

## Karmic Disruption (Su) {#karmic-disruption}

At 16th level, a karmic monk can spend 1 point from his ki pool as a swift action to add 1d6 points
of damage to his unarmed strikes against creatures of either chaotic, evil, good, or lawful
alignment for 1 round. This stacks with other abilities that deal damage based on alignment. He
cannot alter his alignment choice until the next time he uses this ability.

Creatures that are of the appropriate alignment and are struck by this attack must succeed at a Will
save (DC = 10 + 1/2 the karmic monk's class level + the karmic monk's Wisdom modifier) or lose any
[damage reduction](ref/rule/damage-reduction) based on alignment for a number of rounds equal to the
karmic monk's Wisdom modifier (minimum 1 round). A creature that succeeds at this save is immune to
having its [damage reduction](ref/rule/damage-reduction) disrupted by that karmic monk for 24 hours.
This attack disrupts only alignment components of damage reduction, not any other components; for
example, DR/cold iron and good becomes DR/cold iron.

This ability replaces slow fall 80 feet, and alters slow fall at 19th level to become slow fall 80
feet.

## Harmonic Self {#harmonic-self}

At 20th level, a karmic monk is truly in tune with the harmonic balance of the universe. He gains
the abilities of perfect self, except that instead of DR 10/chaotic, he gains DR 10 that is overcome
only by attacks that do not count as chaotic, evil, good, or lawful. This ability alters perfect
self.
