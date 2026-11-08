+++
id = "ref/spell/symbol-of-weakness"
kind = "spell"
title = "Symbol of Weakness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_weakness", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "necromancy"
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
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Occultist\
7: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one symbol
:::

**Sources:** PRPG Core Rulebook pg 357

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that every creature
within 60 feet of a symbol of weakness instead suffers crippling weakness that deals 3d6 points of
Strength damage.

Unlike symbol of death, symbol of weakness has no hit point limit; once triggered, a symbol of
weakness simply remains active for 10 minutes per caster level. A creature can only be affected by
this symbol once.

_Note:_ Magic traps such as symbol of weakness are hard to detect and disable. A rogue (only) can
use the Perception skill to find a symbol of weakness and Disable Device to thwart it. The DC in
each case is 25 + spell level, or 32 for symbol of weakness.
