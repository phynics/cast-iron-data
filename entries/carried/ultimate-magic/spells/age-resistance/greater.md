+++
id = "ref/carried/ultimate-magic/spells/age-resistance/greater"
kind = "spell"
title = "Age Resistance, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Age Resistance"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Age Resistance/Greater", path = "ultimate_magic/spell/age_resistance_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Investigator", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "24 hours"
+++

::: statblock
School: transmutation
Level: 5: Alchemist, Investigator\
7: Arcanist, Druid, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 24 hours
:::

_Ignore penalties from venerable age._

This spell functions as _[lesser age resistance](ref/spell/age-resistance-lesser)_, except you
ignore all Strength, Dexterity, and Constitution penalties gained from middle age, old age, and
venerable age.
