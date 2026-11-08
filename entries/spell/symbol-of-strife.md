+++
id = "ref/spell/symbol-of-strife"
kind = "spell"
title = "Symbol of Strife"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_strife", path = "json/spells10.json" },
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
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond opal worth a total of 15,000 gp)"
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
9: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond opal worth a total of 15,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Ultimate Magic pg 242

This spell functions as [symbol of death](ref/spell/symbol-of-death), except all creatures within
the radius of a symbol of strife are compelled to attack the nearest conscious creature for 1 round
per caster level (similar to the "attack nearest creature" result of the
[confusion](ref/spell/confusion) spell), even after leaving the symbol's area of effect. If no other
creatures are visible, an affected creature can act normally. Once triggered, the symbol remains
active for 10 minutes per caster level.

Symbol of strife can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 18th level or higher for the cost of 25,000 gp.
