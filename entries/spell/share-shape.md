+++
id = "ref/spell/share-shape"
kind = "spell"
title = "Share Shape"
aon = "SpellDisplay.aspx?ItemName=Share%20Shape"
source_ids = ["core-rulebook", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "share_shape", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/beast-shape-2" },
]
[[sources]]
publication = "animal-archive"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["polymorph"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Hunter, Ranger\
4: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: polymorph
:::

### Share Shape

This spell functions as [beast shape II](ref/spell/beast-shape-2), but you may only assume the form
of an animal of a type identical to your animal companion or familiar. If your familiar or companion
is not an animal, this spell has no effect.
