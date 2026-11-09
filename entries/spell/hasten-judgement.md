+++
id = "ref/spell/hasten-judgement"
kind = "spell"
title = "Hasten Judgement"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hasten_judgement", path = "json/spells5.json" },
]
[[sources]]
publication = "planar-adventures"
page = "40"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (2 silver pieces)"
range = "touch"
effects = [
  { label = "Target", value = "one living or corporeal undead creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Inquisitor, Spiritualist\
5: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (2 silver pieces)
Range: touch
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one living or corporeal undead creature
Descriptors: curse
:::

This potent curse weighs upon the target's soul, hastening a living creature's journey to the
Boneyard upon death or weakening an undead creature's animating force. A living creature that dies
during the spell's duration cannot be affected by breath of life or similar effects, and the period
during which attempts to restore the target to life can succeed is reduced to 1 hour/level (for
[raise dead](ref/spell/raise-dead)), 1 day/level (for [resurrection](ref/spell/resurrection)), or 10
days/level (for [true resurrection](ref/spell/true-resurrection)). Reincarnate and similar effects
work normally on a creature killed under this spell's effects.

An undead creature affected by this spell cannot gain temporary hit points, and any existing
[channel resistance](ref/rule/channel-resistance) the undead may have is reduced by half as long as
the curse persists.

Creatures whose souls are separate from their bodies (such as liches) or are merged with their
bodies (such as non-native outsiders) are unaffected by hasten judgment.
