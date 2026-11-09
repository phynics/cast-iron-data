+++
id = "ref/spell/healing-leak"
kind = "spell"
title = "Healing Leak"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "healing_leak", path = "json/spells5.json" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "13"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a piece of muslin)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Paladin\
3: Arcanist, Cleric, Oracle, Shaman, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a piece of muslin)
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

Whenever the target is affected by a spell or effect that heals hit point damage through the use of
positive or negative energy, it regains only half the number of hit points it normally would
recover. If the target employs a spell or effect that heals itself or other creatures through the
use of positive or negative energy, the target must succeed at a
[concentration](ref/rule/concentration) check (DC = this spell's save DC) or the effect restores
only half of the normal number of hit points. Other forms of healing (such as from the Heal skill)
are not affected by this spell.
