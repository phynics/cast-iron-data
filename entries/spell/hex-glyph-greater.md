+++
id = "ref/spell/hex-glyph-greater"
kind = "spell"
title = "Greater Hex Glyph"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hex_glyph_greater", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Shaman", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered diamond worth 400 gp)"
range = "touch"
effects = [
  { label = "Target or Area", value = "object touched or up to 5 sq. ft./level" },
]
duration = "permanent until discharged (D)"
saving_throw = "see text"
spell_resistance = "no (object) and yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Shaman, Witch
Casting time: 10 minutes
Components: V, S, M (powdered diamond worth 400 gp)
Range: touch
Target or Area: object touched or up to 5 sq. ft./level
Duration: permanent until discharged (D)
Saving throw: see text
Spell resistance: no (object) and yes (see text)
:::

## Hex Glyph

**Sources:** Advanced Class Guide pg 184

This spell functions like the spell glyph version of [glyph of warding](ref/spell/glyph-of-warding),
except you can store a hex you know (but not a major hex or a grand hex) instead of a spell. If the
hex has a target, it targets the intruder. If the hex has an area or an amorphous effect, the area
or effect is centered on the intruder. The triggered hex uses this spell's caster level and DC.

[Read magic](ref/spell/read-magic) allows its caster to identify a hex glyph with a successful DC 13
Knowledge (arcana) check. Identifying the glyph does not discharge it and indicates that it stores a
hex, but does not indicate the effect of that hex.

### Greater Hex Glyph

**Sources:** Advanced Class Guide pg 184

This spell functions as hex glyph, except you can store a hex or a major hex (but not a grand hex).
You trace the glyph with incense, which must first be sprinkled with powdered diamond (as noted in
the material line).

[Read magic](ref/spell/read-magic) allows its caster to identify a greater hex glyph with a DC 16
Spellcraft check.
