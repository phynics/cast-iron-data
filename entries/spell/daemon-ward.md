+++
id = "ref/spell/daemon-ward"
kind = "spell"
title = "Daemon Ward"
source_ids = ["book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daemon_ward", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/death-ward" },
]
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "38"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (50 gp worth of powdered silver)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Cleric, Oracle, Paladin, Sorcerer, Warpriest, Witch, Wizard\
5: Druid, Hunter
Casting time: 1 standard action
Components: V, S, M (50 gp worth of powdered silver)
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

This spell functions like [death ward](ref/spell/death-ward), except as noted above and it only
protects against these attacks from daemons.
