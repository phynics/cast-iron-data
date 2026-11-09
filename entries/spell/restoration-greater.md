+++
id = "ref/spell/restoration-greater"
kind = "spell"
title = "Greater Restoration"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restoration_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/restoration-lesser" },
]
[[sources]]
publication = "core-rulebook"
page = "334"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
]
casting_time = "3 rounds"
components = "V, S, M (diamond dust worth 5,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Cleric, Oracle, Shaman
Casting time: 3 rounds
Components: V, S, M (diamond dust worth 5,000 gp)
Range: touch
Target: creature touched
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
:::

### Greater Restoration

This spell functions like [lesser restoration](ref/spell/restoration-lesser), except that it dispels
all permanent and temporary negative levels afflicting the healed creature. Greater restoration also
dispels all magical effects penalizing the creature's abilities, cures all temporary ability damage,
and restores all points permanently drained from all ability scores. It also eliminates fatigue and
exhaustion, and removes all forms of insanity, confusion, and similar mental effects.
