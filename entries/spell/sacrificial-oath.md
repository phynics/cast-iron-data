+++
id = "ref/spell/sacrificial-oath"
kind = "spell"
title = "Sacrificial Oath"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacrificial_oath", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "240"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Paladin", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You create a powerful bond between yourself and a single creature. Until the end of the spell's
duration, each time the target is hit with an attack or fails a saving throw, you can take the full
damage of that attack and any other effects that creature suffers. If you choose not to take on the
damage and effects, you instead take a number of points of damage equal to your Constitution score
as backlash. Any resistances or immunities you have are applied normally, but you cannot otherwise
reduce or negate the damage or effects of either the transfer or the backlash. If you or the subject
of the spell move out of line of sight, the spell ends.
