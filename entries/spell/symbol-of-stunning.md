+++
id = "ref/spell/symbol-of-stunning"
kind = "spell"
title = "Symbol of Stunning"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_stunning", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Occultist\
7: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 356

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures
within 60 feet of a symbol of stunning instead become stunned for 1d6 rounds.

_Note:_ Magic traps such as symbol of stunning are hard to detect and disable. A rogue (only) can
use the Perception skill to find a symbol of stunning and Disable Device to thwart it. The DC in
each case is 25 + spell level, or 32 for symbol of stunning.
