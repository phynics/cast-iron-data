+++
id = "ref/spell/entrap-spirit"
kind = "spell"
title = "Entrap Spirit"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entrap_spirit", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Spiritualist", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a small silver mirror)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "incorporeal creature or haunt" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Medium, Spiritualist\
5: Occultist, Psychic
Casting time: 1 standard action
Components: V, S, F (a small silver mirror)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: incorporeal creature or haunt
:::

**Sources:** Occult Adventures pg 170

You trap the target in the mirror used as the spell's focus. The target cannot be affected by any
means while inside the mirror. If the mirror is destroyed, any incorporeal creature within is
immediately freed and any haunt within returns to its original location. Creatures that assumed
incorporeal form through a spell or other means remain incorporeal while trapped, even if the
duration of the effect that rendered them incorporeal expires. If your focus mirror belonged to the
target, the target takes a -2 penalty on its saving throw.
