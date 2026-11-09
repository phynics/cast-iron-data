+++
id = "ref/spell/phantasmal-asphixiation"
kind = "spell"
title = "Phantasmal Asphixiation"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantasmal_asphixiation", path = "json/spells7.json" },
]
[[sources]]
publication = "horror-adventures"
page = "123"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (an empty vial)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief, then Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium\
4: Arcanist, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (an empty vial)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will disbelief, then Fortitude partial (see text)
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

Your target must succeed at a Will save or believe it can no longer breathe. An affected target must
attempt a Fortitude save each round at the beginning of its turn. The first time it fails the
Fortitude save, it is staggered until the next time it attempts a save against the spell. If the
target fails a second Fortitude save in a row, it falls unconscious for the spell's remaining
duration. The target breathes normally while unconscious, but is shaken for 1 minute upon awakening.
If the target succeeds at two Fortitude saves in a row, it shakes off the spell's effects entirely.
Otherwise, the target continues to attempt a save each round until it falls unconscious or the spell
ends. This spell has no effect on creatures that don't need to breathe.
