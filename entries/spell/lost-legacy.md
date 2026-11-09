+++
id = "ref/spell/lost-legacy"
kind = "spell"
title = "Lost Legacy"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lost_legacy", path = "json/spells6.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "22"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a holy symbol of a dead or forgotten deity, or flag of a fallen or forgotten nation)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Inquisitor, Occultist, Skald, Witch\
7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a holy symbol of a dead or forgotten deity, or flag of a fallen or forgotten nation)
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse, mind-affecting
:::

You inflict a powerful curse on a touched creature that causes others to quickly forget positive
aspects of their interactions with the target. The target cannot attempt a Diplomacy (or
[wild empathy](ref/ability/wild-empathy) or similar ability) check to improve the attitude of other
creatures. Any creature that normally has an attitude of friendly or helpful toward the target must
succeed at a Will save at the spell's normal saving throw DC each time it interacts with the target,
or its attitude becomes indifferent. Once this curse is removed, creatures coming back into contact
with the target regain their pleasant memories of it. If their attitudes toward the target have not
been reduced from indifferent, their original attitudes are restored.
