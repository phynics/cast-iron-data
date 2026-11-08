+++
id = "ref/spell/rejuvenate-eidolon"
kind = "spell"
title = "Rejuvenate Eidolon"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rejuvenate_eidolon", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rejuvenate-eidolon-lesser" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of your blood)"
range = "touch"
effects = [
  { label = "Target", value = "eidolon touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a drop of your blood)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: eidolon touched
Subschool: Healing
:::

### Rejuvenate Eidolon

**Sources:** Advanced Player's Guide pg 238

This spell functions as [lesser rejuvenate eidolon](ref/spell/rejuvenate-eidolon-lesser), except
that it cures 3d10 points of damage +1 point per caster level (maximum +10).
