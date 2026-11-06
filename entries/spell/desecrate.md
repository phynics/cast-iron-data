+++
id = "ref/spell/desecrate"
kind = "spell"
title = "Desecrate"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "desecrate", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a vial of unholy water and 25 gp worth [5 pounds] of silver dust, all of which must be sprinkled around the area)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation" },
]
duration = "2 hours/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Antipaladin, Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (a vial of unholy water and 25 gp worth \[5 pounds\] of silver dust, all of which must be sprinkled around the area)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level
Saving throw: none
Spell resistance: yes
Area: 20-ft.-radius emanation
Descriptors: evil
:::

**Sources:** PRPG Core Rulebook pg 265

This spell imbues an area with negative energy. The DC to resist negative channeled energy within
this area gains a +3 profane bonus. Every undead creature entering a desecrated area gains a +1
profane bonus on all attack rolls, damage rolls, and saving throws. An undead creature created
within or summoned into such an area gains +1 hit points per HD.

If the desecrated area contains an altar, shrine, or other permanent fixture dedicated to your deity
or aligned higher power, the modifiers given above are doubled (+6 profane bonus to negative
channeled energy DCs, +2 profane bonus and +2 hit points per HD for undead created in the area).

Furthermore, anyone who casts [animate dead](ref/spell/animate-dead) within this area may create as
many as double the normal amount of undead (that is, 4 HD per caster level rather than 2 HD per
caster level).

If the area contains an altar, shrine, or other permanent fixture of a deity, pantheon, or higher
power other than your patron, the desecrate spell instead curses the area, cutting off its
connection with the associated deity or power. This secondary function, if used, does not also grant
the bonuses and penalties relating to undead, as given above.

Desecrate counters and dispels [consecrate](ref/spell/consecrate).

### Mythic Desecrate

**Sources:** Mythic Adventures pg 90\
Select one alignment component that you have (chaotic, evil, or lawful). Outsiders with the opposite
alignment subtype of the chosen alignment component take a -1 penalty on attack rolls, damage rolls,
and saves in the area.
