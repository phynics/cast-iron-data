+++
id = "ref/spell/devil-snare"
kind = "spell"
title = "Devil Snare"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "devil_snare", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 full-round action"
components = "V, S, M (a pouch of silvered powder worth 25 gp)"
range = "touch"
effects = [
  { label = "Effect", value = "10-ft.-radius circle" },
]
duration = "1 round/level"
saving_throw = "Will negates, see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Cleric, Oracle, Warpriest\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 full-round action
Components: V, S, M (a pouch of silvered powder worth 25 gp)
Range: touch
Duration: 1 round/level
Saving throw: Will negates, see text
Spell resistance: yes, see text
Effect: 10-ft.-radius circle
Descriptors: good
:::

**Sources:** Agents of Evil pg 17

Your touch creates an invisible circle on a flat surface. Any outsider passing through this circle
must succeed at a Will save or be caught within. Once trapped, a creature must succeed at a Will
save as a standard action to physically exit the confines of the circle, teleport, or use any form
of extradimensional travel (as per dimensional anchor). Contained outsiders can still attack
adjacent creatures outside of the circle, or target others with ranged attacks, spells, and
[spell-like abilities](ref/umr/spell-like-abilities). Despite the spell's name, devil snare captures
outsiders of any type, not only devils.

As a standard action, you can dismiss the circle, expelling any outsiders still trapped within to
their planes of origin (as per dismissal). An outsider can resist this effect with a successful Will
save, enabling it to remain after the spell is dismissed.
