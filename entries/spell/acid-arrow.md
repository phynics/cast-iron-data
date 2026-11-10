+++
id = "ref/spell/acid-arrow"
kind = "spell"
title = "Acid Arrow"
aon = "SpellDisplay.aspx?ItemName=Acid%20Arrow"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acid_arrow", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "239"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (rhubarb leaf and an adder's stomach), F (a dart)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "one arrow of acid" },
]
duration = "1 round + 1 round per three levels"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Bloodrager, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (rhubarb leaf and an adder's stomach), F (a dart)
Range: long (400 ft. + 40 ft./level)
Duration: 1 round + 1 round per three levels
Saving throw: none
Spell resistance: no
Effect: one arrow of acid
Subschool: Creation
Descriptors: acid
:::

An arrow of acid springs from your hand and speeds to its target. You must succeed on a ranged touch
attack to hit your target. The arrow deals 2d4 points of acid damage with no splash damage. For
every three caster levels you possess, the acid, unless neutralized, lasts for another round (to a
maximum of 6 additional rounds at 18th level), dealing another 2d4 points of damage in each round.
