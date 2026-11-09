+++
id = "ref/spell/repair-undead"
kind = "spell"
title = "Repair Undead"
aon = "SpellDisplay.aspx?ItemName=Repair%20Undead"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "repair_undead", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "191"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one undead creature touched (see text)" },
]
duration = "instantaneous"
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless)
Target: one undead creature touched (see text)
:::

When you touch an undead creature, you channel negative energy that heals 1d8 points of damage + 1
point per caster level (maximum +5). This spell has no effect on living creatures, except those that
are healed by negative energy are also healed by the spell.
