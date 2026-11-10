+++
id = "ref/spell/overwhelming-poison"
kind = "spell"
title = "Overwhelming Poison"
aon = "SpellDisplay.aspx?ItemName=Overwhelming%20Poison"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overwhelming_poison", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "221"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (an adder's fang)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or one dose of poison; see text" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Hunter, Ranger\
6: Cleric, Druid, Oracle, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (an adder's fang)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: one creature or one dose of poison; see text
Descriptors: poison
:::

This spell increases the virulence of the targeted dose of poison, making the poison more difficult
to resist. The poison is unaffected by delay poison, and the DC to remove it with neutralize poison
is increased by 5. Additionally, the poison uses its own saving throw DC or overwhelming poison's
DC, whichever is higher.

If cast on a creature that is currently suffering from exposure to one or more doses of poison, the
spell applies to one of the doses of your choice, or a random dose of poison affecting the target if
you don't know what poisons are afflicting the target.

If cast on a creature that is venomous, this spell affects the first dose of poison that creature
delivers before the end of the spell's duration.
