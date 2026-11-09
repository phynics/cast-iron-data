+++
id = "ref/spell/natural-rhythm"
kind = "spell"
title = "Natural Rhythm"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natural_rhythm", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "233"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of pebbles dropped one by one onto the ground)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter
Casting time: 1 standard action
Components: V, S, M (a handful of pebbles dropped one by one onto the ground)
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You enhance a creature's ability to harm an opponent based on the number of times it has already
injured that opponent with a natural attack. Each time the creature successfully strikes an opponent
with a natural attack, the subject gains a cumulative +1 bonus on damage rolls made against that
opponent when making natural attacks (maximum +5 bonus). If an attack misses, the bonus to damage
for all attacks resets to +0.
