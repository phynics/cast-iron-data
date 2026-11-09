+++
id = "ref/spell/false-resurrection-greater"
kind = "spell"
title = "Greater False Resurrection"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_resurrection_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/false-resurrection" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "214"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
]
casting_time = "1 minute"
components = "V, S, DF, M (diamond worth 25,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Cleric, Oracle
Casting time: 1 minute
Components: V, S, DF, M (diamond worth 25,000 gp)
Range: touch
Target: dead creature touched
Duration: permanent
Saving throw: none
Spell resistance: yes (harmless)
Subschool: Healing
:::

### Greater False Resurrection

This spell functions as [false resurrection](ref/spell/false-resurrection) except that it calls a
belier devil with the young simple template to possess the body and all parts of false resurrection
that function like resurrection instead function like
[true resurrection](ref/spell/true-resurrection).

Attempts to identify greater false resurrection with a skill check incorrectly identify it as true
resurrection (see the [ruse](ref/spelldef/ruse) descriptor). A fooled viewer mistakes greater false
resurrection's aura as the lingering aura of an instantaneous conjuration effect.
