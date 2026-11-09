+++
id = "ref/spell/stabilize"
kind = "spell"
title = "Stabilize"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stabilize", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "348"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 0 },
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Inquisitor", level = 0 },
  { class = "Medium", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Shaman", level = 0 },
  { class = "Spiritualist", level = 0 },
  { class = "Warpriest", level = 0 },
  { class = "Witch", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 0: Adept, Cleric, Druid, Hunter, Inquisitor, Medium, Occultist, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one living creature
Subschool: Healing
:::

Upon casting this spell, you target a living creature that has -1 or fewer hit points. That creature
is automatically stabilized and does not lose any further hit points. If the creature later takes
damage, it continues dying normally.
