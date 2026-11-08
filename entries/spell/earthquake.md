+++
id = "ref/spell/earthquake"
kind = "spell"
title = "Earthquake"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "earthquake", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["earth"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Shaman", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "80-ft.-radius spread (S)" },
]
duration = "1 round"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 8: Cleric, Druid, Oracle, Psychic, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 round
Saving throw: see text
Spell resistance: no
Area: 80-ft.-radius spread (S)
Descriptors: earth
:::

**Sources:** PRPG Core Rulebook pg 275

When you cast earthquake, an intense but highly localized tremor rips the ground. The powerful
shockwave created by this spell knocks creatures down, collapses structures, opens cracks in the
ground, and more. The effect lasts for 1 round, during which time creatures on the ground can't move
or attack. A spellcaster on the ground must make a [concentration](ref/rule/concentration) check (DC
20 + spell level) or lose any spell he or she tries to cast. The earthquake affects all terrain,
vegetation, structures, and creatures in the area. The specific effect of an earthquake spell
depends on the nature of the terrain where it is cast.

_Cave, Cavern, or Tunnel:_ The roof collapses, dealing 8d6 points of damage to any creature caught
under the cave-in (Reflex DC 15 half) and pinning that creature beneath the rubble (see below). An
earthquake cast on the roof of a very large cavern could also endanger those outside the actual area
but below the falling debris and rubble.

_Cliffs:_ Earthquake causes a cliff to crumble, creating a landslide that travels horizontally as
far as it falls vertically. Any creature in the path takes 8d6 points of bludgeoning damage (Reflex
DC 15 half) and is pinned beneath the rubble (see below).

_Open Ground:_ Each creature standing in the area must make a DC 15 Reflex save or fall down.
Fissures open in the earth, and every creature on the ground has a 25% chance to fall into one
(Reflex DC 20 to avoid a fissure). The fissures are 40 feet deep. At the end of the spell, all
fissures grind shut. Treat all trapped creatures as if they were in the
[bury zone of an avalanche](ref/rule/avalanches), trapped without air.

_Structure:_ Any structure standing on open ground takes 100 points of damage, enough to collapse a
typical wooden or masonry building, but not a structure built of stone or reinforced masonry.
[Hardness](ref/umr/hardness) does not reduce this damage, nor is it halved as damage dealt to
objects normally is. Any creature caught inside a collapsing structure takes 8d6 points of
bludgeoning damage (Reflex DC 15 half) and is pinned beneath the rubble (see below).

_River, Lake, or Marsh:_ Fissures open under the water, draining away the water from that area and
forming muddy ground. Soggy marsh or swampland becomes quicksand for the duration of the spell,
sucking down creatures and structures. Each creature in the area must make a DC 15 Reflex save or
sink down in the mud and quicksand. At the end of the spell, the rest of the body of water rushes in
to replace the drained water, possibly drowning those caught in the mud.

_Pinned Beneath Rubble:_ Any creature pinned beneath rubble takes 1d6 points of nonlethal damage per
minute while pinned. If a pinned character falls unconscious, he or she must make a DC 15
Constitution check or take 1d6 points of lethal damage each minute thereafter until freed or dead.
