+++
id = "ref/spell/bladed-dash-greater"
kind = "spell"
title = "Greater Bladed Dash"
aon = "SpellDisplay.aspx?ItemName=Bladed%20Dash%2C%20Greater"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bladed_dash_greater", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bladed-dash" },
]
[[sources]]
publication = "inner-sea-magic"
page = "52"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Bard, Magus, Skald
Casting time: 1 standard action
Components: V
Range: personal
Target: you
Duration: instantaneous
Saving throw: none
Spell resistance: no
:::

### Greater Bladed Dash

This spell functions like [bladed dash](ref/spell/bladed-dash), save that you can make a single
melee attack against every creature you pass during the 30 feet of your dash. You cannot attack an
individual creature more than once with spell.
