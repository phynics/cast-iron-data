+++
id = "ref/arc-witch/flood-walker"
kind = "archetype"
title = "Flood Walker"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Flood%20Walker"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flood_walker", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "89"

[fields]
kind = "archetype"
features = [
  { anchor = "patron-spells" },
  { anchor = "gasping-breath-aura", level = 1 },
  { anchor = "river-stride", level = 6 },
  { anchor = "breath-siphon", level = 10 },
]
trades = [
  { replaces = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["gasping-breath-aura"] },
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["river-stride"] },
  { replaces = "Hex gained at 10th level", feature = "hex", levels = [10], by = ["breath-siphon"] },
  { alters = "Patron spells", feature = "patron-spells", by = ["patron-spells"] },
  { alters = "Class skills" },
]
+++

Witches who dwell in floodplains or along the banks of predictably dangerous rivers can tap into the
underlying potential of surging waters in order to enhance their eerie powers.

## Alignment {#alignment}

Flood walkers exult in the final gasp for air of a drowning victim and must be evil in alignment. A
flood walker who becomes nonevil loses access to all abilities granted by this archetype but does
not regain any abilities this archetype replaced.

## Class Skills {#class-skills}

A flood walker gains Survival and Swim as class skills but does not gain Fly and Heal as class
skills.

This alters the witch's class skills.

## Patron Spells {#patron-spells}

Regardless of which patron a flood walker selects, he replaces some of his patron spells with the
following: 4th—_aboleth's lung_, 10th—_suffocation_, 16th—_seamantle_, 18th—_mass suffocation_.

This alters the witch's patron spells.

## Gasping Breath Aura (Su) {#gasping-breath-aura}

A creature attempting to [hold its breath](ref/misc/hold-your-breath) within 30 feet of a flood
walker is treated as having taken a standard or full-round action when determining how long it can
hold its breath, regardless of the number and type of actions it takes in a round. At 5th level,
increase the DC of Swim checks attempted within 30 feet of the flood walker by 5, and creatures
actively engaged in combat or a similarly strenuous activity use air twice as quickly within the
aura. The flood walker can exempt creatures within this aura from these increased penalties.

This replaces the hex gained at 1st level.

## River Stride (Su) {#river-stride}

At 6th level, a flood walker and his familiar can walk on the surface of water and other liquids as
if under the effects of a _[water walk](ref/spell/water-walk)_ spell. The flood walker chooses at
the beginning of his turn each round whether this ability is active or suppressed (for himself and
his familiar separately), allowing him to walk on water or swim.

This replaces the hex gained at 6th level.

## Breath Siphon (Su) {#breath-siphon}

At 10th level, a flood walker gains strength from his patron when creatures suffocate or drown.
Whenever a creature with an Intelligence of 3 or higher asphyxiates or drowns within 30 feet of him,
the flood walker gains the benefit of a _[death knell](ref/spell/death-knell)_ spell for 1 hour. If
a flood walker drowns such a victim himself (such as by holding a grappled or helpless creature
under water until it dies or by killing it with a _[suffocation](ref/spell/suffocation)_ spell), the
duration is doubled, and the flood walker gains 4d8
[temporary hit points](ref/rule/temporary-hit-points) and a +6 enhancement bonus to Strength instead
of the usual temporary hit points and enhancement bonus to Strength from
_[death knell](ref/spell/death-knell)_. Like _[death knell](ref/spell/death-knell)_ itself, this is
an evil act.

This replaces the hex gained at 10th level.

## Hexes {#hexes}

The following witch hexes complement the flood walker archetype: blight, prehensile hair, swamp hag,
water lung.

## Major Hexes {#major-hexes}

The following major hex complements the flood walker archetype: weather control.

## Grand Hexes {#grand-hexes}

The following grand hex complements the flood walker archetype: natural disaster.
