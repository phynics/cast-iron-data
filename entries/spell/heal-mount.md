+++
id = "ref/spell/heal-mount"
kind = "spell"
title = "Heal Mount"
aon = "SpellDisplay.aspx?ItemName=Heal%20Mount"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heal_mount", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heal" },
]
[[sources]]
publication = "core-rulebook"
page = "294"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your mount touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: your mount touched
Subschool: Healing
:::

This spell functions like [heal](ref/spell/heal), but it affects only the paladin's special mount
(typically a horse).
