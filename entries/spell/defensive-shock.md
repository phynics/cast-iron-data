+++
id = "ref/spell/defensive-shock"
kind = "spell"
title = "Defensive Shock"
aon = "SpellDisplay.aspx?ItemName=Defensive%20Shock"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "defensive_shock", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "216"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a hollow metal sphere)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a hollow metal sphere)
Range: personal
Duration: 1 minute/level or until discharged
Saving throw: none
Spell resistance: no
Target: you
Descriptors: electricity
:::

Electrical energy floods your body, shocking the next creature that touches you. Any creature
striking you with its body or a handheld weapon takes 1d6 points of electricity damage per two
caster levels (maximum 6d6). If the attacker has [spell resistance](ref/rule/spell-resistance), it
applies against this damage. Each time the spell discharges, the number of damage dice it deals is
halved (rounded down); when the spell's damage dice reach 0, the spell ends.
