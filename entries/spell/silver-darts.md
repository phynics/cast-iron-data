+++
id = "ref/spell/silver-darts"
kind = "spell"
title = "Silver Darts"
aon = "SpellDisplay.aspx?ItemName=Silver%20Darts"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silver_darts", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "192"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a silver needle)"
range = "15 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a silver needle)
Range: 15 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cone-shaped burst
Subschool: Creation
:::

A cone of silver darts springs from your hand. These darts act as a silver weapon that deals 1d6
points of piercing damage per caster level (maximum 10d6). Any creature with an armor bonus greater
than +4 or a natural armor bonus greater than +4 takes 50% less damage.
