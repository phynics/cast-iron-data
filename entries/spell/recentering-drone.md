+++
id = "ref/spell/recentering-drone"
kind = "spell"
title = "Recentering Drone"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "recentering_drone", path = "json/spells8.json" },
]
[[sources]]
publication = "champions-of-balance"
page = "27"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/2 levels (no two of which may be more than 30 ft. apart)" },
]
duration = "concentration"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature/2 levels (no two of which may be more than 30 ft. apart)
:::

You emit a calming subsonic drone that allows the targets to temporarily refocus and restore their
balance when they're suffering from debilitating conditions. A target with the dazzled, fatigued,
shaken, or sickened condition ignores the penalties of those conditions for the duration of this
spell. A target with one of the following conditions is treated as having the associated lesser
condition for the duration of the spell, as shown by the following table.

|Condition|Lesser Condition|
| --- | --- |
|Blinded|Dazzled|
|Exhausted|Fatigued|
|Frightened|Shaken|
|Nauseated|Sickened|

At the end of the spell's duration, the targets are again subject to the appropriate penalties if
the original conditions affecting the target are still in effect.
