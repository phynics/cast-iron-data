+++
id = "ref/spell/gallant-inspiration"
kind = "spell"
title = "Gallant Inspiration"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gallant_inspiration", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bard, Skald
Casting time: 1 immediate action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one living creature
:::

**Sources:** Advanced Player's Guide pg 225

This word of arcane-empowered inspiration often ensures success of a crucial endeavor. Cast this
spell when a creature fails an attack roll or skill check. The creature gains a +2d4 competence
bonus to the attack roll or skill check retroactively. If the bonus is enough to turn the failure
into a success, the roll succeeds.
