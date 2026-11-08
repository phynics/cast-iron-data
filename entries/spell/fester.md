+++
id = "ref/spell/fester"
kind = "spell"
title = "Fester"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fester", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Inquisitor", level = 3 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (rotted meat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level or 1 round; see text"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Witch\
3: Inquisitor
Casting time: 1 standard action
Components: V, S, M (rotted meat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or 1 round; see text
Saving throw: Fortitude partial
Spell resistance: yes
Target: one living creature
:::

**Sources:** Advanced Player's Guide pg 221

Necrotic energy permeates the target, blocking healing abilities. The subject gains
[spell resistance](ref/rule/spell-resistance) equal to 12 + your caster level against effects that
restore hit points or grant temporary hit points. In addition, any healing provided by effects that
ignore spell resistance (such as [fast healing](ref/umr/fast-healing), regeneration, and some
spells) are halved. If the target succeeds on a Fortitude saving throw, fester lasts only a single
round.
