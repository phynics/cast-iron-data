+++
id = "ref/spell/source-severance"
kind = "spell"
title = "Source Severance"
aon = "SpellDisplay.aspx?ItemName=Source%20Severance"
source_ids = ["core-rulebook", "faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "source_severance", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/antimagic-field" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (pinch of powdered iron or iron fillings)"
range = "10 ft."
effects = [
  { label = "Area", value = "10-ft.-radius emanation, centered on you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Arcanist, Occultist, Sorcerer, Wizard\
7: Psychic\
8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, M/DF (pinch of powdered iron or iron fillings)
Range: 10 ft.
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: see text
Area: 10-ft.-radius emanation, centered on you
:::

### Source Severance

You create an invisible barrier that surrounds you and moves with you, inhibiting one category of
magic. When you cast this spell, choose either arcane or divine magic. This spell functions like
[antimagic field](ref/spell/antimagic-field), but it suppresses only spells of the chosen type and
supernatural and spell-like class abilities from classes that grant spellcasting of the selected
type. Magic items, other [spell-like abilities](ref/umr/spell-like-abilities), and other
supernatural abilities are unaffected.

While this spell is in effect, you must succeed at a [concentration](ref/rule/concentration) check
(DC 20 + twice the spell level) to cast any spell, whether arcane or divine. If you fail at the
check, you lose the spell as if you had cast it to no effect.
