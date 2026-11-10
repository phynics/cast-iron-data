+++
id = "ref/spell/wing-bounty"
kind = "spell"
title = "Wing Bounty"
aon = "SpellDisplay.aspx?ItemName=Wing%20Bounty"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wing_bounty", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "14"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "0 ft."
effects = [
  { label = "Effect", value = "2d4 berries + 2 berries/level" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: 0 ft.
Duration: 1 day/level
Saving throw: none
Spell resistance: no
Effect: 2d4 berries + 2 berries/level
Subschool: Creation
:::

> _[Gathlains](ref/race/gathlain) have access to the following spell._

Your wings sprout a variety of colorful and flavorful berries. Each berry functions as if affected
by [goodberry](ref/spell/goodberry). You can choose for one affected berry to also be poisonous (as
striped toadstool); only you and druids of 5th level or higher can tell which is which without
magic.
