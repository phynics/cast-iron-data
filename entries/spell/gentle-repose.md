+++
id = "ref/spell/gentle-repose"
kind = "spell"
title = "Gentle Repose"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gentle_repose", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "289"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (salt and a copper piece for each of the corpse's eyes)"
range = "touch"
effects = [
  { label = "Target", value = "corpse touched" },
]
duration = "1 day/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Medium, Oracle, Shaman, Spiritualist, Warpriest, Witch\
3: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (salt and a copper piece for each of the corpse's eyes)
Range: touch
Duration: 1 day/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: corpse touched
:::

You preserve the remains of a dead creature so that they do not decay. Doing so effectively extends
the time limit on raising that creature from the dead (see [raise dead](ref/spell/raise-dead)). Days
spent under the influence of this spell don't count against the time limit. Additionally, this spell
makes transporting a slain (and thus decaying) comrade less unpleasant.

The spell also works on severed body parts and the like.
