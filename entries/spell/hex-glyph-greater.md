+++
id = "ref/spell/hex-glyph-greater"
kind = "spell"
title = "Greater Hex Glyph"
aon = "SpellDisplay.aspx?ItemName=Hex%20Glyph%2C%20Greater"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hex_glyph_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hex-glyph" },
]
[[sources]]
publication = "advanced-class-guide"
page = "184"

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

### Greater Hex Glyph

This spell functions as [hex glyph](ref/spell/hex-glyph), except you can store a hex or a major hex
(but not a grand hex). You trace the glyph with incense, which must first be sprinkled with powdered
diamond (as noted in the material line).

[Read magic](ref/spell/read-magic) allows its caster to identify a greater hex glyph with a DC 16
Spellcraft check.
