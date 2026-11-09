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
[[sources]]
publication = "occult-adventures"
page = "183"

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

### Psychic Crush IV

This functions as [psychic crush I](ref/spell/psychic-crush-1), but the target takes 9d6 points of
damage + 1 point of damage per caster level on a successful Fortitude or Will save. The target does
not receive any saving throw bonus because of its hit points. If it is at fewer than half its total
hit points, it doesn't gain a Fortitude save to resist this spell but instead proceeds as if it had
automatically failed its Fortitude save. This spell can be undercast.
