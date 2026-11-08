+++
id = "ref/spell/symbol-of-sleep"
kind = "spell"
title = "Symbol of Sleep"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_sleep", path = "json/spells10.json" },
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
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
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
School: enchantment
Level: 4: Occultist\
5: Arcanist, Cleric, Mesmerist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 1,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 356

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures of
10 HD or less within 60 feet of the symbol of sleep instead fall into a catatonic slumber for 3d6 ×
10 minutes. Unlike with the [sleep](ref/spell/sleep) spell, sleeping creatures cannot be awakened by
nonmagical means before this time expires.

Unlike symbol of death, symbol of sleep has no hit point limit; once triggered, a symbol of sleep
simply remains active for 10 minutes per caster level.

_Note:_ Magic traps such as symbol of sleep are hard to detect and disable. A rogue (only) can use
the Perception skill to find a symbol of sleep and Disable Device to thwart it. The DC in each case
is 25 + spell level, or 30 for symbol of sleep.
