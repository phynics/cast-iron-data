+++
id = "ref/spell/psychic-crush-1"
kind = "spell"
title = "Psychic Crush I"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_crush_1", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-adventures"
page = "182"

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

Using your psychic power, you invade the mind of the target and tear it asunder, causing massive
internal damage to both its mind and body. If the target succeeds at the initial Will save, it is
sickened for 1 round. If the target fails its Will save, it must attempt a Fortitude save (with a +4
circumstance bonus on this save if it has more than half its total hit points remaining). If it also
fails the Fortitude save, the target is reduced to -1 hit points and is dying. If the target
succeeds at its Fortitude save, it instead takes 3d6 points of damage + 1 point of damage per caster
level, which cannot reduce the target below -1 hit point, and the target is sickened for 1 round.
This attack has no effect on creatures without an Intelligence score.
