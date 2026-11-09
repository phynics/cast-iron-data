+++
id = "ref/spell/lament-of-summers-last-breath"
kind = "spell"
title = "Lament of Summer's Last Breath"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lament_of_summers_last_breath", path = "json/spells6.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "220"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["fire", "good"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft. radius spread centered on a creature, object, or point in space" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Bard, Hunter, Ranger, Skald
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: yes
Area: 30-ft. radius spread centered on a creature, object, or point in space
Descriptors: fire, good
:::

> _The following spell is available to the indicated race or ethnicity: Ulfen_

You wrap the target in a mantle of summery air, within which the ambient temperature never falls
below 70 degrees Fahrenheit. Creatures with the cold subtype that start their turns in the area take
an amount of fire damage equal to 1d4 points + 1 point per 2 caster levels (maximum 1d4+5) with no
saving throw. Each time an evil [dragon](ref/type/dragon), [fey](ref/type/fey), or
[giant](ref/subtype/giant) takes damage from the spell, it must succeed at a Will saving throw or
become [shaken](ref/misc/shaken) for 1 round. Creatures attempting to cast a cold spell in the area
must succeed at a Will save or the spell fails. Succeeding at one such save to cast a spell allows a
creature to continue casting cold spells in the area for the spell's remainder.
