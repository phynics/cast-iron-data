+++
id = "ref/spell/glyph-of-warding-greater"
kind = "spell"
title = "Greater Glyph of Warding"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "glyph_of_warding_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/glyph-of-warding" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered diamond worth 200 gp)"
range = "touch"
effects = [
  { label = "Target or Area", value = "object touched or up to 5 sq. ft./level" },
]
duration = "permanent until discharged (D)"
saving_throw = "see text"
spell_resistance = "no (object) and yes; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 10 minutes
Components: V, S, M (powdered diamond worth 200 gp)
Range: touch
Target or Area: object touched or up to 5 sq. ft./level
Duration: permanent until discharged (D)
Saving throw: see text
Spell resistance: no (object) and yes; see text
:::

### Greater Glyph of Warding

**Sources:** PRPG Core Rulebook pg 291

This spell functions like [glyph of warding](ref/spell/glyph-of-warding), except that a greater
blast glyph deals up to 10d8 points of damage, and a greater spell glyph can store a spell of 6th
level or lower.

[Read magic](ref/spell/read-magic) allows you to identify a greater glyph of warding with a DC 16
Spellcraft check.

_Material Component:_ You trace the glyph with incense, which must first be sprinkled with powdered
diamond worth at least 400 gp.
