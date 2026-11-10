+++
id = "ref/spell/gravity-bow"
kind = "spell"
title = "Gravity Bow"
aon = "SpellDisplay.aspx?ItemName=Gravity%20Bow"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravity_bow", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "226"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Hunter, Occultist, Ranger, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

Gravity bow significantly increases the weight and density of arrows or bolts fired from your bow or
crossbow the instant before they strike their target and then return them to normal a few moments
later. Any arrow fired from a bow or crossbow you are carrying when the spell is cast deals damage
as if [one size category larger](ref/misc/damage-die-adjustments) than it actually is. For instance,
an arrow fired from a Medium longbow normally deals 1d8 points of damage, but it would instead deal
2d6 points of damage if fired from a gravity bow. Only you can benefit from this spell. If anyone
else uses your bow to make an attack the arrows deal damage as normal for their size.
