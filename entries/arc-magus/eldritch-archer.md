+++
id = "ref/arc-magus/eldritch-archer"
kind = "archetype"
title = "Eldritch Archer"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Eldritch%20Archer"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_archer", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-pool", level = 5 },
  { anchor = "ranged-weapon-bond", level = 1 },
  { anchor = "ranged-spell-combat", level = 1 },
  { anchor = "ranged-spellstrike", level = 2 },
  { anchor = "focusing-spellstrike", level = 16 },
  { anchor = "distant-spellstrike" },
  { anchor = "reach-spellstrike" },
]
trades = [
  { replaces = "Counterstrike", feature = "counterstrike", by = ["focusing-spellstrike"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["arcane-pool"] },
  { alters = "Spell combat", feature = "spell-combat", by = ["ranged-spell-combat"] },
  { alters = "Spellstrike", feature = "spellstrike", by = ["ranged-spellstrike"] },
]
+++

The eldritch archer rains magical attacks down on her foes from the city walls.

## Class Skills {#class-skills}

An eldritch archer gains Perception as a class skill, but does not gain Use Magic Device as a class
skill. This ability modifies the magus's class skills.

## Arcane Pool (Su) {#arcane-pool}

An eldritch archer's choices of weapon special abilities to apply with arcane pool at 5th level
include _[distance](ref/magic-enh/distance)_, _[nimble shot](ref/magic-enh/nimble-shot)_, and
_[returning](ref/magic-enh/returning)_ but not _dancing_, _keen_, or _vorpal_. This ability modifies
the magus's arcane pool.

## Ranged Weapon Bond (Ex) {#ranged-weapon-bond}

At 1st level, an eldritch archer gains a bonded object as per the [wizard's](ref/class/wizard)
arcane bonded object; it must be a ranged weapon, and it can't be used to cast a spell once per day.
Holding her bonded item does not prevent the eldritch archer from providing somatic components for
her spells.

## Ranged Spell Combat (Ex) {#ranged-spell-combat}

Instead of a light or one-handed melee weapon, an eldritch archer must use a ranged weapon for spell
combat. She doesn't need a free hand for ranged spell combat. The eldritch archer cannot accept an
attack penalty to gain a bonus on [concentration](ref/rule/concentration) checks to cast a spell
defensively. This ability modifies spell combat.

## Ranged Spellstrike (Su) {#ranged-spellstrike}

At 2nd level, whenever an eldritch archer casts a spell that calls for a ranged attack, she can
deliver the spell through a ranged weapon she wields as part of a ranged attack. Instead of the free
ranged attack normally allowed to deliver the spell, an eldritch archer can make one free ranged
attack with a ranged weapon (at her highest base attack bonus) as part of casting this spell. The
attack does not increase the spell's range.

If the spell can normally affect multiple targets, only a single missile, ray, or effect accompanies
each attack; if the spell allows multiple attacks and the eldritch archer can make additional ranged
attacks as part of a full-round action with spell combat, one additional ray, missile, or effect
from the spell accompanies each subsequent ranged attack the eldritch archer makes in the same round
until all attacks allowed by the spell are made. Unused missiles, rays, or effects remaining at the
end of the eldritch archer's turn are wasted. This ability alters spellstrike.

## Focusing Spellstrike (Su) {#focusing-spellstrike}

At 16th level, an eldritch archer can use ranged spellstrike to deliver a cone- or line-shaped spell
as a ray, affecting only the creature or object struck. This ability replaces counterstrike.

## Magus Arcana {#magus-arcana}

The following magus arcana can be selected by any magus who meets their prerequisites.

## Distant Spellstrike (Su) {#distant-spellstrike}

The range of any spell the magus delivers through a ranged weapon attack increases to the maximum
range of the weapon if that is greater than the spell's range. The magus must be at least 12th level
and must have ranged spellstrike to select this arcana.

## Reach Spellstrike (Su) {#reach-spellstrike}

The magus can deliver spells with a range of touch with ranged spellstrike up to a maximum range of
close (25 feet + 5 feet per 2 caster levels). The magus must be at least 9th level and must have
ranged spellstrike to select this arcana.
