+++
id = "ref/spell/hex-glyph"
kind = "spell"
title = "Hex Glyph"
aon = "SpellDisplay.aspx?ItemName=Hex%20Glyph"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hex_glyph", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/glyph-of-warding" },
]
[[sources]]
publication = "advanced-class-guide"
page = "184"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Shaman", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered diamond worth 200 gp)"
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
Level: 3: Shaman, Witch
Casting time: 10 minutes
Components: V, S, M (powdered diamond worth 200 gp)
Range: touch
Duration: permanent until discharged (D)
Saving throw: see text
Spell resistance: no (object) and yes (see text)
Target or Area: object touched or up to 5 sq. ft./level
:::

This spell functions like the spell glyph version of [glyph of warding](ref/spell/glyph-of-warding),
except you can store a hex you know (but not a major hex or a grand hex) instead of a spell. If the
hex has a target, it targets the intruder. If the hex has an area or an amorphous effect, the area
or effect is centered on the intruder. The triggered hex uses this spell's caster level and DC.

[Read magic](ref/spell/read-magic) allows its caster to identify a hex glyph with a successful DC 13
Knowledge (arcana) check. Identifying the glyph does not discharge it and indicates that it stores a
hex, but does not indicate the effect of that hex.
