+++
id = "ref/spell/celestial-healing"
kind = "spell"
title = "Celestial Healing"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "celestial_healing", path = "json/spells2.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "13"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
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
Level: 1: Arcanist, Bloodrager, Cleric, Magus, Oracle, Sorcerer, Summoner, Warpriest, Witch, Wizard
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

You anoint a wounded creature with the blood of an outsider with the good subtype (such as an angel)
or holy water, giving it [fast healing](ref/umr/fast-healing) 1. The target radiates the aura of a
good creature for the duration of the spell and can sense the righteousness of the magic, though
this has no long-term effect on the target's alignment. If the target has its own evil aura, this is
not suppressed by celestial healing, and can also be detected normally.
