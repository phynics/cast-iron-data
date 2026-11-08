+++
id = "ref/spell/symbol-of-distraction"
kind = "spell"
title = "Symbol of Distraction"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_distraction", path = "json/spells10.json" },
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
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (mercuty and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)"
range = "0 feet; see text"
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
6: Arcanist, Bard, Cleric, Mesmerist, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercuty and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)
Range: 0 feet; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Magic Tactics Toolbox pg 26

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures
within the radius of a symbol of distraction instead become fascinated by the symbol for 10 minutes
per caster level. Unlike symbol of death, symbol of distraction has no hit point limit; once
triggered, a symbol of distraction simply remains active for a duration of 10 minutes × your caster
level. All fascinated creatures move toward the symbol of distraction, trying to remain within the
symbol's area of effect. If the symbol leads affected creatures into a dangerous area, each
fascinated creature can attempt an additional Will saving throw, with success indicating it is no
longer fascinated. If a creature's view of the symbol is completely blocked, it is immediately freed
of the symbol's effect.
