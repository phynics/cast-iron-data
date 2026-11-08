+++
id = "ref/spell/celestial-healing-greater"
kind = "spell"
title = "Greater Celestial Healing"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "celestial_healing_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/celestial-healing" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (1 drop of blood from a good outsider or 1 dose of holy water)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/2 levels"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Bloodrager, Cleric, Magus, Oracle, Sorcerer, Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, M (1 drop of blood from a good outsider or 1 dose of holy water)
Range: touch
Duration: 1 round/2 levels
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
Descriptors: good
:::

**Sources:** Arcane Anthology pg 13

As per [celestial healing](ref/spell/celestial-healing), except the target gains
[fast healing](ref/umr/fast-healing) 4 and the target radiates the aura of a good cleric.
