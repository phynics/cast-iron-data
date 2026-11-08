+++
id = "ref/spell/infernal-healing-greater"
kind = "spell"
title = "Greater Infernal Healing"
source_ids = ["hells-vengeance-players-guide", "pathfinder-29-mother-of-flies", "gods-and-magic", "inner-sea-world-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infernal_healing_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/infernal-healing" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (1 drop of devil blood or 1 dose of unholy water)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Cleric, Magus, Oracle, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, M (1 drop of devil blood or 1 dose of unholy water)
Range: touch
Target: creature touched
Duration: 1 minute
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
Descriptors: evil
:::

### Greater Infernal Healing

**Sources:** Hell's Vengeance Player's Guide pg 11

As per [infernal healing](ref/spell/infernal-healing), except the target gains
[fast healing](ref/umr/fast-healing) 4 and the target detects as an evil cleric.
