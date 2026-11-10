+++
id = "ref/spell/rune-of-warding"
kind = "spell"
title = "Rune of Warding"
aon = "SpellDisplay.aspx?ItemName=Rune%20of%20Warding"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rune_of_warding", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/glyph-of-warding" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "25"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 hour"
components = "V, S, M (powdered adamantine, diamond, or mithral worth 200 gp)"
range = "touch"
effects = [
  { label = "Target", value = "doorway or portal touched" },
]
duration = "permanent until discharged (D)"
saving_throw = "Reflex half"
spell_resistance = "no (object) and yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 hour
Components: V, S, M (powdered adamantine, diamond, or mithral worth 200 gp)
Range: touch
Duration: permanent until discharged (D)
Saving throw: Reflex half
Spell resistance: no (object) and yes (see text)
Target: doorway or portal touched
:::

You inscribe a series of runes upon the surface of a door or around the border of an entryway. They
function as a [glyph of warding](ref/spell/glyph-of-warding) (blast glyph), though unlike a glyph of
warding, these runes are always visible. The runes count as a glyph of warding for the purpose of
what spells can defeat it, placing multiple glyphs in the same area, and so on.
