+++
id = "ref/spell/timely-inspiration"
kind = "spell"
title = "Timely Inspiration"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "timely_inspiration", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 immediate action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Skald
Casting time: 1 immediate action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

**Sources:** Advanced Player's Guide pg 249

A word of arcane-empowered inspiration can snatch victory from seeming defeat. Cast this spell when
a creature fails an attack roll or skill check. The target gains a +1 competence bonus per five
caster levels (maximum +3 bonus) on the attack roll or skill check retroactively. If the bonus is
enough to make the failure a success, the roll succeeds.
