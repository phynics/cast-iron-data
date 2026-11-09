+++
id = "ref/spell/align-weapon-communal"
kind = "spell"
title = "Communal Align Weapon"
source_ids = ["core-rulebook", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "align_weapon_communal", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/align-weapon" },
]
[[sources]]
publication = "advanced-class-guide"
page = "173"

[fields]
kind = "spell"
school = "transmutation [see text]"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched or 50 projectiles (all of which must be together at the time of casting)" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[see text\]
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: weapon touched or 50 projectiles (all of which must be together at the time of casting)
:::

### Communal Align Weapon

This spell functions as [align weapon](ref/spell/align-weapon), except you divide the duration in
1-minute increments between any number of touched weapons. Every group of up to 50 projectiles
(which must be together at the time of casting) counts as one weapon for the purpose of dividing the
spell's duration.
