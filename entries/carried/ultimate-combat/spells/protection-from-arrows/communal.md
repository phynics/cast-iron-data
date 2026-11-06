+++
id = "ref/carried/ultimate-combat/spells/protection-from-arrows/communal"
kind = "spell"
title = "Protection From Arrows, Communal"
source_ids = ["ultimate-combat"]
section = ["Spells", "Protection From Arrows"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Protection From Arrows/Communal", path = "ultimate_combat/spell/protection_from_arrows_communal.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of tortoiseshell or turtle shell)"
range = "touch"
effects = [
  { label = "Target", value = "creatures touched" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: abjuration
Level: 3: Alchemist, Arcanist, Investigator, Sorcerer, Summoner, Wizard
Casting Time: 1 standard action
Components: V, S, F (a piece of tortoiseshell or turtle shell)
Range: touch
Target: creatures touched
Duration: 1 hour/level or until discharged
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As protection from arrows, but you may divide the duration among creatures touched._

This spell functions like _[protection from arrows](ref/spell/protection-from-arrows)_, except you
divide the duration in 1-hour intervals among the creatures touched. Once the spell absorbs 10
points of damage per caster level (maximum 100 points) for a subject, the spell's effects end for
that subject.
