+++
id = "ref/spell/spider-climb-communal"
kind = "spell"
title = "Communal Spider Climb"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spider_climb_communal", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spider-climb" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a live spider)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Bloodrager, Druid, Hunter, Investigator, Magus, Medium, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a live spider)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Mythic Spider Climb

**Sources:** Mythic Adventures pg 109

The target gains a climb speed equal to its base land speed or 30 feet, whichever is higher. The
target can take the run action while climbing and needs only one hand free to climb.

The target can move freely across spider webs (including giant spider webs), web spells, and similar
adhesives of 2nd level or less (including tanglefoot bags) as if it were using freedom of movement.

### Communal Spider Climb

**Sources:** Ultimate Combat pg 245

This spell functions like [spider climb](ref/spell/spider-climb), except you divide the duration in
10-minute intervals among the creatures touched.
