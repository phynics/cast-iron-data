+++
id = "ref/spell/symbol-of-laughter"
kind = "spell"
title = "Symbol of Laughter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_laughter", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorus, plus powdered diamond and opal worth 1,000 gp each)"
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
Level: 3: Mesmerist, Occultist\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth 1,000 gp each)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Charm
Descriptors: mind-affecting
:::

**Sources:** Advanced Class Guide pg 196

This spell functions as [symbol of death](ref/spell/symbol-of-death), except that all creatures
within 60 feet are affected with uncontrollable laughter (as
[hideous laughter](ref/spell/hideous-laughter)) for 1 round per caster level.

Unlike symbol of death, symbol of laughter has no hit point limit; once it is triggered, a symbol of
laughter remains active for 1 minute per caster level.

Symbol of laughter can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 10th level or higher at a cost of 5,000 gp.
