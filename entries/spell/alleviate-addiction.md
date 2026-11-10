+++
id = "ref/spell/alleviate-addiction"
kind = "spell"
title = "Alleviate Addiction"
aon = "SpellDisplay.aspx?ItemName=Alleviate%20Addiction"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alleviate_addiction", path = "json/spells.json" },
]
[[sources]]
publication = "black-markets"
page = "19"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Alchemist, Cleric, Druid, Hunter, Investigator, Oracle, Paladin, Ranger, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

The subject ignores the effects of addictions. The subject can naturally recover from damage dealt
by the drug if she is under the effects of this spell for the entire duration of her rest.
