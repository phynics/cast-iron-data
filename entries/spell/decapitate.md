+++
id = "ref/spell/decapitate"
kind = "spell"
title = "Decapitate"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "decapitate", path = "json/spells3.json" },
]
[[sources]]
publication = "horror-adventures"
page = "115"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Magus", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 immediate action"
components = "V, S, F (a sliver from a guillotine blade)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature (see text)" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Inquisitor\
6: Arcanist, Magus, Psychic, Sorcerer, Wizard
Casting time: 1 immediate action
Components: V, S, F (a sliver from a guillotine blade)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one creature (see text)
:::

You can cast this spell only as a response to a confirmed critical hit against the target that would
deal slashing damage. If the target fails the saving throw and has a discernible head, the attack
deals an extra 4d6 points of damage and the critical multiplier of the critical hit increases by 1.
If the critical hit then brings the target to 0 hit points or fewer, the target is instantly
decapitated and dies unless it can survive decapitation. Even on a successful saving throw, the
critical hit deals an extra 4d6 points of damage.
