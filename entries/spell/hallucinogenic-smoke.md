+++
id = "ref/spell/hallucinogenic-smoke"
kind = "spell"
title = "Hallucinogenic Smoke"
source_ids = ["faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hallucinogenic_smoke", path = "json/spells5.json" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["poison"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "S, M (tobacco leaves, ingested)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "3 rounds/level or until discharged; see text"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Cleric, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: S, M (tobacco leaves, ingested)
Range: personal
Duration: 3 rounds/level or until discharged; see text
Saving throw: Fortitude partial
Spell resistance: yes
Target: you
Descriptors: poison
:::

Dark gray smoke seeps from your eyes, ears, and mouth for the spell's duration, though the smoke
doesn't significantly hamper your vision. Upon casting the spell, you may immediately exhale the
smoke in a 30-foot cone or do so in a later round as a standard action, ending the spell. Each
living creature caught within the cone must succeed at a Fortitude save or be nauseated for 1 round
per caster level as it is wracked with waves of nausea and disorienting visions. If it succeeds at
its Fortitude save, the creature is instead sickened for 1d4 rounds.

If you don't expel the smoke by the end of the spell's duration, you suffer the spell's effects
instead.

If you cast augury during the duration of hallucinogenic smoke, treat your caster level as 5 higher
when determining the chance for a meaningful reply. Additionally, you know whether a result of
"nothing" resulted from a failed or successful augury.
