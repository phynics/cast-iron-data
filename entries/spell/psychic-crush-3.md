+++
id = "ref/spell/psychic-crush-3"
kind = "spell"
title = "Psychic Crush III"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_crush_3", path = "json/spells15.json" },
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

### Psychic Crush III

**Sources:** Occult Adventures pg 183

This functions as [psychic crush I](ref/spell/psychic-crush-1), but the target takes 7d6 points of
damage + 1 point of damage per caster level on a successful Fortitude save and 1 point of damage per
caster level on a successful Will save. The target receives a +2 circumstance bonus on the Fortitude
save if it is at full hit points, and no bonus if it has taken any damage. This spell can be
undercast.
