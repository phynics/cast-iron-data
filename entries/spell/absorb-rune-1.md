+++
id = "ref/spell/absorb-rune-1"
kind = "spell"
title = "Absorb Rune I"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorb_rune_1", path = "json/spells.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "60"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a white silk glove worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one spell effect" },
]
duration = "instantaneous plus 1 minute/level (see text)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Bard, Cleric, Magus, Occultist, Oracle, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a white silk glove worth 25 gp)
Range: touch
Duration: instantaneous plus 1 minute/level (see text)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one spell effect
:::

This spell allows you to lay your hand upon a magical glyph, symbol, or other magical spell effect
(referred to in this spell description as a "rune") and attempt to absorb the essence of its effect.
To absorb a rune, you must be aware of the rune's existence (but need not know the details of what
it actually does) and then succeed at a caster level check (DC = 10 + the caster level of the spell
affect being absorbed) as you touch the rune in question. If you fail this caster level check, the
magical rune is not triggered unless you fail the roll by 5 or more.

If you succeed at the caster level check, the rune is removed from the surface it was originally
placed upon and duplicated on the cloth of a silk glove worn on your hand. The rune remains located
on the glove's palm in an inert state for up to 1 minute per caster level. As a standard action
taken at any time during that duration, you can transfer the rune to another surface similar to the
one it was originally placed upon, at which point the rune's function either returns to normal or
dissipates harmlessly as if successfully dispelled (your choice). If the spell's duration expires
before you place the rune on a new surface, the absorbed rune dissipates harmlessly.

Absorb rune I affects only runes whose effects are equivalent to a spell of 3rd level or lower. An
attempt to use absorb rune I on a more powerful effect automatically triggers the rune when you
touch it.
