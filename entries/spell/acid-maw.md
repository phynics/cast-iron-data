+++
id = "ref/spell/acid-maw"
kind = "spell"
title = "Acid Maw"
aon = "SpellDisplay.aspx?ItemName=Acid%20Maw"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acid_maw", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-class-origins"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["acid"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "your animal companion" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: your animal companion
Descriptors: acid
:::

Your animal companion's bite attack deals an additional 1d4 points of acid damage, and the acid
deals another 1d4 points of acid damage to the target on the next round. The acid continues to deal
damage for 1 additional round per 4 caster levels (to a maximum of 6 total rounds at caster level
20th). This ongoing acid damage doesn't stack from multiple attacks, but the duration resets if a
newer bite would cause the ongoing damage to last longer than the duration remaining from a previous
one. The acid does not harm the animal companion.
