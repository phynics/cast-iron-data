+++
id = "ref/spell/symbol-of-persuasion"
kind = "spell"
title = "Symbol of Persuasion"
aon = "SpellDisplay.aspx?ItemName=Symbol%20of%20Persuasion"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_persuasion", path = "json/spells10.json" },
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
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
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
Level: 4: Occultist\
6: Arcanist, Cleric, Mesmerist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth a total of 5,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Charm
Descriptors: mind-affecting
:::

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that all creatures
within the radius of a symbol of persuasion instead become charmed by the caster (as the
[charm monster](ref/spell/charm-monster) spell) for 1 hour per caster level.

Unlike symbol of death, symbol of persuasion has no hit point limit; once triggered, a symbol of
persuasion simply remains active for 10 minutes per caster level.

_Note:_ Magic traps such as symbol of persuasion are hard to detect and disable. A rogue (only) can
use the Perception skill to find a symbol of persuasion and Disable Device to thwart it. The DC in
each case is 25 + spell level, or 31 for symbol of persuasion.
