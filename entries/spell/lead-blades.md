+++
id = "ref/spell/lead-blades"
kind = "spell"
title = "Lead Blades"
aon = "SpellDisplay.aspx?ItemName=Lead%20Blades"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lead_blades", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "230"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Hunter", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "touch" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Hunter, Occultist, Ranger
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: touch
:::

Lead blades increases the momentum and density of your melee weapons just as they strike a foe. All
melee weapons you are carrying when the spell is cast deal damage as if
[one size category larger](ref/misc/damage-die-adjustments) than they actually are. For instance, a
Medium longsword normally deals 1d8 points of damage, but it would instead deal 2d6 points of damage
if benefiting from lead blades. Only you can benefit from this spell. If anyone else uses one of
your weapons to make an attack it deals damage as normal for its size.
