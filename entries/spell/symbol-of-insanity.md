+++
id = "ref/spell/symbol-of-insanity"
kind = "spell"
title = "Symbol of Insanity"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_insanity", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "core-rulebook"
page = "356"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
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
Level: 6: Occultist\
8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
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

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures
within the radius of the symbol of insanity instead become permanently insane (as the
[insanity](ref/spell/insanity) spell).

Unlike symbol of death, symbol of insanity has no hit point limit; once triggered, a symbol of
insanity simply remains active for 10 minutes per caster level.

_Note:_ Magic traps such as symbol of insanity are hard to detect and disable. A rogue (only) can
use the Perception skill to find a symbol of insanity and Disable Device to thwart it. The DC in
each case is 25 + spell level, or 33 for symbol of insanity.
