+++
id = "ref/spell/erase"
kind = "spell"
title = "Erase"
aon = "SpellDisplay.aspx?ItemName=Erase"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "erase", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "279"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one scroll or two pages" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bard, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Target: one scroll or two pages
:::

Erase removes writings of either magical or mundane nature from a scroll or from one or two pages of
paper, parchment, or similar surfaces. With this spell, you can remove explosive runes, a glyph of
warding, a sepia snake sigil, or an arcane mark, but not illusory script or a symbol spell.
Nonmagical writing is automatically erased if you touch it and no one else is holding it. Otherwise,
the chance of erasing nonmagical writing is 90%.

Magic writing must be touched to be erased, and you also must succeed on a caster level check
(1d20 + caster level) against DC 15. A natural 1 is always a failure on this check. If you fail to
erase explosive runes, a glyph of warding, or a sepia snake sigil, you accidentally activate that
writing instead.
