+++
id = "ref/spell/spellscar"
kind = "spell"
title = "Spellscar"
aon = "SpellDisplay.aspx?ItemName=Spellscar"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellscar", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "61"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of sand from the Spellscar Desert)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "two 10-ft. cubes per level (S)" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of sand from the Spellscar Desert)
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Area: two 10-ft. cubes per level (S)
:::

This potent spell invokes the same sort of magical devastation that created the Mana Wastes so long
ago, albeit on a much more localized (and thankfully temporary) scale. Within the area you choose to
affect with spellscar, the terrain takes on a strange pale hue, as if colors were muted.
Periodically, ripples of vibrant color wriggle through the terrain. Within this area, any spell,
[spell-like ability](ref/umr/spell-like-abilities), or magic item activation automatically triggers
a [primal magic](ref/rule/primal-magic) event - a spellcaster can avoid triggering such an event by
making a [concentration](ref/rule/concentration) check (DC 15 + twice the spell's level), but
non-spellcasters who activate magic items have no such option.

You gain a +4 insight bonus on concentration checks made to avoid triggering primal magic events
while within a spellscar you have created, and if you do trigger a primal magic event, you may roll
d% twice and pick which of the two results you wish to have occur.
