+++
id = "ref/spell/symbol-of-dispelling"
kind = "spell"
title = "Symbol of Dispelling"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_dispelling", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "inner-sea-gods"
page = "243"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, M (pure grain alcohol and powdered diamond worth 5,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (pure grain alcohol and powdered diamond worth 5,000 gp)
Range: 0 ft.; see text
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one symbol
:::

This spell functions as [symbol of death](ref/spell/symbol-of-death), except that all creatures
within 40 feet of the symbol of dispelling are instead affected as if by the area dispel function of
[greater dispel magic](ref/spell/dispel-magic-greater). Attempt a dispel check when casting symbol
of dispelling. Once the symbol is triggered, apply the result of that check to each creature in the
area, as well as each object that is the target of one or more spells. Unlike symbol of death,
symbol of dispelling grants no saving throws, and it is not subject to
[spell resistance](ref/rule/spell-resistance).
