+++
id = "ref/spell/gloomblind-bolts"
kind = "spell"
title = "Gloomblind Bolts"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gloomblind_bolts", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "113"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one or more bolts of energy" },
]
duration = "instantaneous"
saving_throw = "Reflex negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Reflex negates, see text
Spell resistance: yes
Effect: one or more bolts of energy
Subschool: Creation
Descriptors: shadow
:::

> _[Fetchlings](ref/race/fetchling) have access to the following spell._

You create one or more bolts of negative energy infused with shadow pulled from the Shadow Plane.
You can fire one bolt, plus one for every four levels beyond 5th (to a maximum of three bolts at
13th level) at the same or different targets, but all bolts must be aimed at targets within 30 feet
of each other and require a ranged touch attack to hit. Each bolt deals 4d6 points of damage to a
living creature or heals 4d6 points of damage to an undead creature. Furthermore, the bolt's energy
spreads over the skin of creature, possibly blinding it for a short time. Any creature struck by a
bolt must succeed at a Reflex saving throw or become blinded for 1 round.
