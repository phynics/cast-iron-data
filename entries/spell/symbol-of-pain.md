+++
id = "ref/spell/symbol-of-pain"
kind = "spell"
title = "Symbol of Pain"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_pain", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "core-rulebook"
page = "356"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
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
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Occultist\
5: Arcanist, Cleric, Mesmerist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 1,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one symbol
Descriptors: evil, pain
:::

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that each creature
within the radius of a symbol of pain instead suffers wracking pains that impose a -4 penalty on
attack rolls, skill checks, and ability checks. These effects last for 1 hour after the creature
moves farther than 60 feet from the symbol.

Unlike symbol of death, symbol of pain has no hit point limit; once triggered, a symbol of pain
simply remains active for 10 minutes per caster level.

_Note:_ Magic traps such as symbol of pain are hard to detect and disable. A rogue (only) can use
the Perception skill to find a symbol of pain and Disable Device to thwart it. The DC in each case
is 25 + spell level, or 30 for symbol of pain.
