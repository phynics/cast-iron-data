+++
id = "ref/spell/sacred-space"
kind = "spell"
title = "Sacred Space"
aon = "SpellDisplay.aspx?ItemName=Sacred%20Space"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_space", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "89"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a vial of ambrosia)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation" },
]
duration = "2 hours/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, M (a vial of ambrosia)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius emanation
Descriptors: good
:::

> _[Aasimars](ref/race/aasimar) have access to the following spell._

This spell sanctifies an area with heavenly power. The DC to resist spells or
[spell-like abilities](ref/umr/spell-like-abilities) with the good descriptor or channeled energy
that damages evil outsiders (as when using [Alignment Channel](ref/feat/alignment-channel))
increases by +2. In addition, evil outsiders take a -1 penalty on attack rolls, damage rolls, and
saving throws, and they cannot be called or summoned into a sacred space. If the sacred space
contains an altar, shrine, or other permanent fixture dedicated to your deity, pantheon, or
good-aligned higher power, the modifiers given above are doubled. You cannot cast sacred space in an
area with a permanent fixture dedicated to a deity other than yours.
