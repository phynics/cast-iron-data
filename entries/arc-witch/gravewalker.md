+++
id = "ref/arc-witch/gravewalker"
kind = "archetype"
title = "Gravewalker"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Gravewalker"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravewalker", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-magic"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "spell-poppet", level = 1 },
  { anchor = "deliver-touch-spells", level = 3 },
  { anchor = "aura-of-desecration", level = 1 },
  { anchor = "bonethrall", level = 1 },
  { anchor = "possess-undead", level = 8 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["spell-poppet"] },
  { replaces = "1st-level hex", feature = "hex", levels = [1], by = ["aura-of-desecration"] },
  { replaces = "Witch's hex gained at 4th level", feature = "hex", levels = [4], by = ["bonethrall"] },
  { replaces = "Witch's hex gained at 8th level", feature = "hex", levels = [8], by = ["possess-undead"] },
  { replaces = "Patron spells", feature = "patron-spells", by = ["spells"] },
]
+++

Having much in common with necromancers, the gravewalker is obsessed with the occult manipulations
of the dead, particularly mindless undead such as zombies. Unlike the creations of standard
necromancers, a gravewalker's creations remain forever tied to her will, and she can produce vile
apparitions of tremendous power.

## Spells {#spells}

A gravewalker replaces some of her patron spells with the following: 4th—_command undead_,
6th—_animate dead_, 12th—_create undead_, 14th—_control undead_, 16th—_create greater undead_. These
replace the patron spells

## Spell Poppet {#spell-poppet}

Each gravewalker carries around a gristly, inanimate poppet stitched from human skin and stuffed
with shards of bone, fingernails, and grave dirt. A gravewalker's spells come from the will of evil
spirits residing in the poppet, and its ability to hold spells functions in a manner identical to
the way a witch's spells are granted by her familiar. The gravewalker must commune with her poppet
each day to prepare her spells and cannot prepare spells that are not stored in the poppet. This
ability replaces familiar. The following familiar ability works differently for a gravewalker:

## Deliver Touch Spells (Su) {#deliver-touch-spells}

At 3rd level or higher, a gravewalker can use her poppet to deliver touch spells. After casting a
touch spell, as a full-round action, the witch can designate a target and stab a pin into her
poppet, delivering the spell as a ranged touch attack. The target must be within range of her aura
of desecration ability (see below).

## Aura of Desecration (Su) {#aura-of-desecration}

At 1st level, a gravewalker can create a 20-foot-radius aura of evil power. This aura increases the
DC of channeled negative energy by +1 and the turn resistance of undead by +1. At 3rd level and
every 2 levels thereafter, the radius of the aura increases by 5 feet, to a maximum of 70 feet at
20th level. This ability replaces the witch's 1st-level hex.

## Bonethrall (Su) {#bonethrall}

At 1st level, a gravewalker can take control of an undead creature within her aura of desecration by
forcing her will upon it (Will negates, using her hex DC). If it fails the save, the creature falls
under her control as if she had used _[command undead](ref/spell/command-undead)_ (once control is
established, the undead remain controlled even if outside the witch's aura). Intelligent undead
receive a new saving throw each day to resist her command. The witch can control up to 1 HD of
undead creatures per caster level. If an undead creature is under the control of another creature,
the witch must make an opposed Charisma check whenever her orders conflict with that creature's.
This replaces the witch's hex gained at 4th level.

## Possess Undead (Sp) {#possess-undead}

A gravewalker may take direct control of one of her undead minions within her aura of desecration,
as if using _[magic jar](ref/spell/magic-jar)_; the witch's poppet acts as the soul receptacle for
this ability. The minion gets no saving throw against this ability. This replaces the witch's hex
gained at 8th level.

## Hexes {#hexes}

The following witch hexes complement the gravewalker archetype: beast of ill-omen, evil eye,
misfortune.

## Major Hexes {#major-hexes}

The following major hexes complement the gravewalker archetype: ice tomb, infected wounds, waxen
image.

## Grand Hexes {#grand-hexes}

The following grand hexes complement the gravewalker archetype: death curse, summon spirit.
