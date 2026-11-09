+++
id = "ref/spell/remove-blindness-deafness"
kind = "spell"
title = "Remove Blindness/Deafness"
aon = "SpellDisplay.aspx?ItemName=Remove%20Blindness%2FDeafness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_blindness_deafness", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "332"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
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
Level: 3: Alchemist, Cleric, Investigator, Mesmerist, Oracle, Paladin, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

Remove blindness/deafness cures blindness or deafness (your choice), whether the effect is normal or
magical in nature. The spell does not restore ears or eyes that have been lost, but it repairs them
if they are damaged.

Remove blindness/deafness counters and dispels [blindness/deafness](ref/spell/blindness-deafness).
