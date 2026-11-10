+++
id = "ref/spell/unbreakable-construct"
kind = "spell"
title = "Unbreakable Construct"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unbreakable_construct", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "244"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered adamantine worth 100 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one construct" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Occultist\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered adamantine worth 100 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: one construct
:::

This spell increases the target's DR/adamantine by 5 or its [hardness](ref/umr/hardness) by 5. If
the target does not have DR/adamantine or hardness, this spell has no effect.
