+++
id = "ref/spell/path-of-glory"
kind = "spell"
title = "Path of Glory"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "path_of_glory", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch (see text)"
effects = [
  { label = "Area", value = "four 5-ft. squares/level (see text)" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Bard, Cleric, Oracle, Skald, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch (see text)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: four 5-ft. squares/level (see text)
Subschool: Healing
:::

**Sources:** Advanced Class Guide pg 189

You cause four 5-foot squares (one of which must be your space) to glow with dim illumination.
Starting on your next turn, as a swift action you can extend the glowing area by an additional four
5-foot squares; each new square must be adjacent to a square that was previously glowing. Allies
that end their turns on a glowing square (including one who falls unconscious in the square) are
healed of 1 point of damage.

### Greater Path of Glory

**Sources:** Advanced Class Guide pg 189

This spell functions as path of glory, except as noted above, and a square provides 5 points of
healing instead of 1.
