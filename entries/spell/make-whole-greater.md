+++
id = "ref/spell/make-whole-greater"
kind = "spell"
title = "Greater Make Whole"
source_ids = ["core-rulebook", "mythic-adventures", "technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "make_whole_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/make-whole" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "10 ft."
effects = [
  { label = "Target", value = "one object of up to 5 lb./level" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Cleric, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: 10 ft.
Target: one object of up to 5 lb./level
Duration: instantaneous
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
:::

### Mythic Make Whole

**Sources:** Mythic Adventures pg 100

The damage the spell repairs increases to 2d6 points of damage per caster level when cast on a
construct creature (maximum 10d6). A construct repaired with this spell gains a +2 enhancement bonus
on an ability score of your choice for the next 24 hours. To repair a magic item, your caster level
has to equal to only the caster level of the magic item, not double the caster level.

### Greater Make Whole

**Sources:** Technology Guide pg 10

This spell repairs 1d6 points of damage plus 1 point per level when cast on a construct creature
(maximum 10d6+10). Greater [make whole](ref/spell/make-whole) can fix destroyed magic items or
technological items (items at 0 hit points or fewer), and restores the magic properties of the item
if your caster level at least equal to that of the item. This spell otherwise functions as make
whole.
