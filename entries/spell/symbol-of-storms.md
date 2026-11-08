+++
id = "ref/spell/symbol-of-storms"
kind = "spell"
title = "Symbol of Storms"
source_ids = ["core-rulebook", "blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_storms", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
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
components = "V, S, M (mercury and phosphorus, plus powdered diamond and opal worth 5,000 gp each)"
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
Level: 6: Occultist\
8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorus, plus powdered diamond and opal worth 5,000 gp each)
Range: 0 ft.; see text
Duration: see text
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one symbol
Descriptors: death
:::

### Symbol of Storms

**Sources:** Blood of the Ancients pg 28

This spell functions as [symbol of death](ref/spell/symbol-of-death), except that when triggered, a
30-foot-radius centered on the symbol fills with hurricane-force winds (75 mph). Each round, a bolt
of lightning that deals 10d6 points of electricity damage strikes a random creature within the area.
A successful Reflex save halves this damage. Unlike symbol of death, symbol of storms has no hit
point limit. Regardless of the trigger method or methods chosen, a creature more than 30 feet from a
symbol of storms can't trigger it (even if it meets one or more of the triggering conditions, such
as reading the rune). Once triggered, a symbol of storms remains active for 1 minute per caster
level.
