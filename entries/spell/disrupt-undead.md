+++
id = "ref/spell/disrupt-undead"
kind = "spell"
title = "Disrupt Undead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disrupt_undead", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Inquisitor", level = 0 },
  { class = "Magus", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 0: Arcanist, Inquisitor, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: ray
:::

**Sources:** PRPG Core Rulebook pg 273

You direct a ray of positive energy. You must make a ranged touch attack to hit, and if the ray hits
an undead creature, it deals 1d6 points of damage to it.
