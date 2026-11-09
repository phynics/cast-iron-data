+++
id = "ref/spell/advanced-scurvy"
kind = "spell"
title = "Advanced Scurvy"
source_ids = ["pathfinder-55-the-wormwood-mutiny"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "advanced_scurvy", path = "json/spells.json" },
]
[[sources]]
publication = "pathfinder-55-the-wormwood-mutiny"
page = "73"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
Descriptors: disease, evil
:::

> _This spell is associated with [Besmara](ref/faith/besmara), but there are no restrictions on its
> use by others._

The subject contracts an advanced form of scurvy. He becomes constantly fatigued, suffers from bone
pain (-1 penalty on Strength- and Dexterity-based checks), wounds easily (add +1 point of damage to
any bleed effects affecting the target), experiences loose teeth, and is slow to heal (natural
healing occurs at half the normal rate). Scurvy can be treated magically or can be overcome with
proper nutrition; eating the right foods ends the fatigue and bone pain within 1-2 days and provides
a full cure 2d6 days after that.
