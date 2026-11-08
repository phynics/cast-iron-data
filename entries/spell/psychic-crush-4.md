+++
id = "ref/spell/psychic-crush-4"
kind = "spell"
title = "Psychic Crush IV"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_crush_4", path = "json/spells15.json" },
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

## Psychic Crush I

**Sources:** Occult Adventures pg 182

Using your psychic power, you invade the mind of the target and tear it asunder, causing massive
internal damage to both its mind and body. If the target succeeds at the initial Will save, it is
sickened for 1 round. If the target fails its Will save, it must attempt a Fortitude save (with a +4
circumstance bonus on this save if it has more than half its total hit points remaining). If it also
fails the Fortitude save, the target is reduced to -1 hit points and is dying. If the target
succeeds at its Fortitude save, it instead takes 3d6 points of damage + 1 point of damage per caster
level, which cannot reduce the target below -1 hit point, and the target is sickened for 1 round.
This attack has no effect on creatures without an Intelligence score.

### Psychic Crush II

**Sources:** Occult Adventures pg 182

This functions as [psychic crush I](ref/spell/psychic-crush-1), but on a successful Fortitude save,
the target takes 5d6 points of damage + 1 point of damage per caster level. In addition, the target
receives a +4 circumstance bonus on the Fortitude save only if it is at full hit points; otherwise,
it gains a +2 bonus if it has more than half its total hit points remaining. This spell can be
undercast.

### Psychic Crush III

**Sources:** Occult Adventures pg 183

This functions as psychic crush I, but the target takes 7d6 points of damage + 1 point of damage per
caster level on a successful Fortitude save and 1 point of damage per caster level on a successful
Will save. The target receives a +2 circumstance bonus on the Fortitude save if it is at full hit
points, and no bonus if it has taken any damage. This spell can be undercast.

### Psychic Crush IV

**Sources:** Occult Adventures pg 183

This functions as psychic crush I, but the target takes 9d6 points of damage + 1 point of damage per
caster level on a successful Fortitude or Will save. The target does not receive any saving throw
bonus because of its hit points. If it is at fewer than half its total hit points, it doesn't gain a
Fortitude save to resist this spell but instead proceeds as if it had automatically failed its
Fortitude save. This spell can be undercast.

### Psychic Crush V

**Sources:** Occult Adventures pg 183

This functions as psychic crush IV, but on a successful Fortitude or Will save, the target takes
11d6 points of damage + 1 point of damage per caster level. If it is at fewer than half its total
hit points, the target takes a -2 penalty on the Will save to resist this spell. This spell can be
undercast.
