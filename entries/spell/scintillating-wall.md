+++
id = "ref/spell/scintillating-wall"
kind = "spell"
title = "Scintillating Wall"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scintillating_wall", path = "json/spells8.json" },
]
[[sources]]
publication = "distant-realms"
page = "42"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Pattern"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of crushed d'ziriak chitin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "wall with an area of up to one 10-ft. square/level" },
]
duration = "1 round/level (D)"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Bard, Skald\
5: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of crushed d'ziriak chitin)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: see text
Spell resistance: no
Effect: wall with an area of up to one 10-ft. square/level
Subschool: Pattern
Descriptors: mind-affecting
:::

You create a vibrant wall of hypnotic light and color. The wall does not impede movement or line of
sight in any way. Creatures moving through the wall must succeed at a Will save or become
fascinated. Each round, on its turn, a fascinated creature can attempt a new saving throw to end the
effect as a full-round action that does not provoke attacks of opportunity. A creature that succeeds
at the save against the fascination effect is no longer affected if it remains within the wall, but
it must attempt a new saving throw if it leaves the area and later moves through the wall again.
Creatures adjacent to the wall and creatures moving through the wall that succeed at their save
against fascination are dazzled.

If you create the wall so that it appears in the same space as one or more creatures, each affected
creature must succeed at a Fortitude save or become blinded. Creatures that successfully save
against the blindness are subject to the fascination effect unless they leave the wall within 1
round of casting the spell.

Scintillating wall can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 13th level or higher, at a cost of 12,500 gp.
