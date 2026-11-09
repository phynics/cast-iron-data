+++
id = "ref/spell/unshakeable-zeal"
kind = "spell"
title = "Unshakeable Zeal"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unshakeable_zeal", path = "json/spells11.json" },
]
[[sources]]
publication = "occult-adventures"
page = "190"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Inquisitor", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
  { class = "Spiritualist", level = 6 },
]
casting_time = "1 standard action"
components = "S, F (a silver circlet)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Skald\
6: Inquisitor, Spiritualist\
7: Psychic
Casting time: 1 standard action
Components: S, F (a silver circlet)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill the target with boundless enthusiasm and faith in its ultimate triumph. Whenever the target
fails an attack roll, a save, a skill check, a [concentration](ref/rule/concentration) check, or an
ability check, the target receives a +4 morale bonus on its next attempt at the failed check within
1 round (this includes attack rolls against the same foe, saving throws against the same ability
from the same foe, and so on). In addition, when the target would be affected by a fear or emotion
effect, it can instead dismiss unshakeable zeal without spending an action to negate the effect on
itself.
