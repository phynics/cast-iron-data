+++
id = "ref/spell/psychic-crush-2"
kind = "spell"
title = "Psychic Crush II"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_crush_2", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/psychic-crush-1" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will partial and Fortitude partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will partial and Fortitude partial, see text
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

### Psychic Crush II

**Sources:** Occult Adventures pg 182

This functions as [psychic crush I](ref/spell/psychic-crush-1), but on a successful Fortitude save,
the target takes 5d6 points of damage + 1 point of damage per caster level. In addition, the target
receives a +4 circumstance bonus on the Fortitude save only if it is at full hit points; otherwise,
it gains a +2 bonus if it has more than half its total hit points remaining. This spell can be
undercast.
