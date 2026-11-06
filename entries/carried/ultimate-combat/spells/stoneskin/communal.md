+++
id = "ref/carried/ultimate-combat/spells/stoneskin/communal"
kind = "spell"
title = "Stoneskin, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Stoneskin"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Stoneskin/Communal", path = "ultimate_combat/spell/stoneskin_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (granite and diamond dust worth 100 gp per creature affected)"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "10 min./level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 4: Summoner\
5: Alchemist, Arcanist, Inquisitor, Investigator, Sorcerer, Wizard\
6: Druid, Hunter, Hunter, Hunter, Hunter
Casting Time: 1 standard action
Components: V, S, M (granite and diamond dust worth 100 gp per creature affected)
Range: touch
Target: creatures touched
Duration: 10 min./level or until discharged
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As stoneskin, but you may divide the duration among creatures touched._

This spell functions like _[stoneskin](ref/spell/stoneskin)_, except you divide the duration in 10
minute intervals among the creatures touched. Once the spell has prevented 10 points of damage per
caster level (maximum 150 points) for a subject, the spell's effects end for that subject.
