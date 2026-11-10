+++
id = "ref/spell/deadly-juggernaut"
kind = "spell"
title = "Deadly Juggernaut"
aon = "SpellDisplay.aspx?ItemName=Deadly%20Juggernaut"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deadly_juggernaut", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "227"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: death
:::

With every enemy life you take, you become increasingly dangerous and difficult to stop. During the
duration of the spell, you gain a cumulative +1 luck bonus on melee attack rolls, melee weapon
damage rolls, Strength checks, and Strength-based skill checks as well as DR 2/- each time you
reduce a qualifying opponent to 0 or few hit points (maximum +5 bonus and DR 10/-) with a melee
attack. A qualifying opponent has a number of Hit Dice equal to or greater than your Hit Dice -4.
