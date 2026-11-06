+++
id = "ref/carried/ultimate-combat/spells/protection-from-energy/communal"
kind = "spell"
title = "Protection From Energy, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Protection From Energy"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Protection From Energy/Communal", path = "ultimate_combat/spell/protection_from_energy_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level or until discharged"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 3: Hunter, Hunter, Hunter, Hunter, Hunter, Ranger\
4: Arcanist, Cleric, Druid, Inquisitor, Oracle, Sorcerer, Summoner, Warpriest, Wizard
Casting Time: 1 standard action
Components: V, S, DF
Range: touch
Target: creatures touched
Duration: 10 min./level or until discharged
Saving Throw: Fortitude negates (harmless)
Spell Resistance: yes (harmless)
:::

_As protection from energy, but you may divide the duration among creatures touched._

This spell functions like _[protection from energy](ref/spell/protection-from-energy)_, except you
divide the duration in 10-minute intervals among the creatures touched. Once the spell absorbs 12
points of energy damage per caster level (maximum 120 points) for a subject, the spell's effects end
for that subject.
