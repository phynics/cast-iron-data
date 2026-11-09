+++
id = "ref/spell/restoration"
kind = "spell"
title = "Restoration"
aon = "SpellDisplay.aspx?ItemName=Restoration"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restoration", path = "json/spells8.json" },
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
  { class = "Adept", level = 4 },
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "3 rounds"
components = "V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)"
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
Level: 4: Adept, Alchemist, Cleric, Inquisitor, Investigator, Mesmerist, Oracle, Paladin, Shaman, Spiritualist, Warpriest
Casting time: 3 rounds
Components: V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

This spell functions like [lesser restoration](ref/spell/restoration-lesser), except that it also
dispels temporary negative levels or one permanent negative level. If this spell is used to dispel a
permanent negative level, it has a material component of diamond dust worth 1,000 gp. This spell
cannot be used to dispel more than one permanent negative level possessed by a target in a 1-week
period.

Restoration cures all temporary ability damage, and it restores all points permanently drained from
a single ability score (your choice if more than one is drained). It also eliminates any fatigue or
exhaustion suffered by the target.
