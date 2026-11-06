+++
id = "ref/spell/demand-offering"
kind = "spell"
title = "Demand Offering"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demand_offering", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "5 ft."
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous or 1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Mesmerist\
2: Arcanist, Bard, Inquisitor, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 5 ft.
Duration: instantaneous or 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 164

A creature that fails its save uses an immediate action to hand you whatever object it's currently
wielding or holding. If the target doesn't have an immediate action available, it uses a move action
at the beginning of its next turn to hand you the object. If it's currently holding or wielding more
than one item, determine randomly which item it gives you. If you're no longer adjacent to the
creature when it has to give you the item, the spell ends with no effect. A creature that isn't
holding an item when you cast this spell is unaffected.
