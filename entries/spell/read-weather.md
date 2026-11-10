+++
id = "ref/spell/read-weather"
kind = "spell"
title = "Read Weather"
aon = "SpellDisplay.aspx?ItemName=Read%20Weather"
source_ids = ["inner-sea-gods", "faiths-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "read_weather", path = "json/spells8.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "238"
[[sources]]
publication = "faiths-of-balance"
page = "28"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 minute"
components = "V, S, F (a set of marked sticks or bones worth at least 25 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Cleric, Druid, Hunter, Oracle, Ranger, Shaman, Skald, Warpriest, Witch
Casting time: 1 minute
Components: V, S, F (a set of marked sticks or bones worth at least 25 gp)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

This spell allows you to forecast the weather at your location for the next 48 hours, providing you
with advance warning of storms, tornadoes, and so on. This forecast reveals only the weather that
would arise naturally, and does not take into account any magical occurrences that might change the
weather.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
