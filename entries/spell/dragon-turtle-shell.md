+++
id = "ref/spell/dragon-turtle-shell"
kind = "spell"
title = "Dragon Turtle Shell"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_turtle_shell", path = "json/spells13.json" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "28"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of turtle shell)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Druid, Hunter\
3: Alchemist, Arcanist, Cleric, Investigator, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of turtle shell)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

When you are struck by an opponent's natural attacks, the damage is resolved as if the attack came
from a creature one size smaller per 5 caster levels (maximum of four size categories smaller at CL
20th). Refer to [Table 3-1](ref/umr/natural-attacks) to determine an attack's altered base damage.
If the creature's natural attack deals non-standard damage, refer instead to the
[Improved Natural Attack](ref/feat/improved-natural-attack) feat. It is not possible to reduce the
base damage of a creature's natural attack below 1d2 with this spell.
