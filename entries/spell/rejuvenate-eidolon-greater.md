+++
id = "ref/spell/rejuvenate-eidolon-greater"
kind = "spell"
title = "Greater Rejuvenate Eidolon"
aon = "SpellDisplay.aspx?ItemName=Rejuvenate%20Eidolon%2C%20Greater"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rejuvenate_eidolon_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/rejuvenate-eidolon-lesser" },
]
[[sources]]
publication = "advanced-players-guide"
page = "238"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
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
Level: 5: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a drop of your blood)
Range: touch
Target: eidolon touched
Duration: instantaneous
Saving throw: none
Spell resistance: no
Subschool: Healing
:::

### Greater Rejuvenate Eidolon

This spell functions as [lesser rejuvenate eidolon](ref/spell/rejuvenate-eidolon-lesser), except
that it cures 5d10 points of damage +1 point per caster level (maximum +20).
