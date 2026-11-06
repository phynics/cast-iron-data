+++
id = "ref/spell/reflexive-barrier"
kind = "spell"
title = "Reflexive Barrier"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reflexive_barrier", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Magus", level = 3 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round (see text)"
saving_throw = "none"
spell_resistance = "no (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Magus, Psychic
Casting time: 1 immediate action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round (see text)
Saving throw: none
Spell resistance: no (harmless)
Target: one creature
Descriptors: force
:::

**Sources:** Psychic Anthology pg 10

In the blink of an eye, you erect a deflective barrier of force to protect one target. The target
gains a deflection bonus to its AC equal to half your caster level. This bonus lasts until the
beginning of your next turn. You can cast this spell as a reaction to an attack, but you must do so
before the result of the attack is revealed.
