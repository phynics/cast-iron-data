+++
id = "ref/spell/rune-of-durability"
kind = "spell"
title = "Rune of Durability"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rune_of_durability", path = "json/spells8.json" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute"
components = "V, S, M (iron fillings)"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (iron fillings)
Range: touch
Duration: permanent
Saving throw: none
Spell resistance: no
Target: weapon touched
:::

You inscribe an angular rune upon the surface of a weapon, increasing its hit points. A weapon that
bears this rune multiplies its hit points by 2, as if it were one size category larger than it
actually is. Placing more than one rune of this type on a weapon has no effect.
