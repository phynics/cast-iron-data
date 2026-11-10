+++
id = "ref/spell/remove-disease"
kind = "spell"
title = "Remove Disease"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_disease", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "332"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Alchemist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Adept, Alchemist, Cleric, Druid, Hunter, Inquisitor, Investigator, Oracle, Ranger, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

Remove disease can cure all diseases from which the subject is suffering. You must make a caster
level check (1d20 + caster level) against the DC of each disease affecting the target. Success means
that the disease is cured. The spell also kills some hazards and parasites, including green slime
and others.

Since the spell's duration is instantaneous, it does not prevent reinfection after a new exposure to
the same disease at a later date.
