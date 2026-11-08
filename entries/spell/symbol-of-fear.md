+++
id = "ref/spell/symbol-of-fear"
kind = "spell"
title = "Symbol of Fear"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_fear", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 1,000 gp)"
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
School: necromancy
Level: 4: Occultist\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 1,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 356

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures
within 60 feet of the symbol of fear instead become panicked for 1 round per caster level.

_Note:_ Magic traps such as symbol of fear are hard to detect and disable. A rogue (only) can use
the Perception skill to find a symbol of fear and Disable Device to thwart it. The DC in each case
is 25 + spell level, or 31 for symbol of fear.
