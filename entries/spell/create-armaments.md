+++
id = "ref/spell/create-armaments"
kind = "spell"
title = "Create Armaments"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_armaments", path = "json/spells12.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "7"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S, M (diamonds worth price of arms to be created)"
range = "0 ft."
effects = [
  { label = "Effect", value = "one nonmagical weapon, shield, or set of armor" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Spiritualist\
4: Arcanist, Bard, Medium, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S, M (diamonds worth price of arms to be created)
Range: 0 ft.
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one nonmagical weapon, shield, or set of armor
Subschool: Creation
:::

You create one nonmagical weapon, shield, or set of armor. To determine whether the item functions
as intended, you must attempt an appropriate Craft check with the DC required to create the item
normally. If you fail, the item is created with the broken condition. You can create items made of
rare or unusual materials if you include a bit of that material as an additional material component
when you cast the spell, but cannot create cold iron items with this spell.
