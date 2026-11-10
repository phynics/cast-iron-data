+++
id = "ref/spell/reinforce-armaments"
kind = "spell"
title = "Reinforce Armaments"
aon = "SpellDisplay.aspx?ItemName=Reinforce%20Armaments"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reinforce_armaments", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "241"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a metal pin)"
range = "touch"
effects = [
  { label = "Target", value = "one armor suit or weapon touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Cleric, Magus, Occultist, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a metal pin)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one armor suit or weapon touched
:::

You reinforce a weapon or armor suit to give it a temporarily upgrade or mitigate the
[fragile](ref/misc/fragile) quality. A suit of armor or weapon touched that has the fragile quality
is not considered to have the fragile quality for the spell's duration. Normal armor suits or
weapons subjected to this spell instead gain the masterwork quality for the spell's duration and
their [hardness](ref/umr/hardness) is doubled. If this spell is cast on masterwork or magical armor
or weapons, their hardness is doubled for the duration of the spell.
