+++
id = "ref/carried/core-rulebook/spells/planar-binding/greater"
kind = "spell"
title = "Planar Binding, Greater"
aon = "SpellDisplay.aspx?ItemName=Planar%20Binding%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Planar Binding"]
tags = ["conjuration", "calling", "see text for lesser planar binding"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Planar Binding/Greater", path = "core_rulebook/spell/planar_binding_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["calling"]
descriptors = ["see text for lesser planar binding"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Elementalist Wizard", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
components = ": V, S"
effects = [
  { label = "Targets", value = "up to three elementals or outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear." },
]
+++

::: statblock
School: conjuration (calling) \[see text for lesser planar binding\]
Level: 6: Summoner\
8: Arcanist, Elementalist Wizard, Sorcerer, Wizard
Components: : V, S
Targets: up to three elementals or outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear.
:::

_As lesser planar binding, but up to 18 HD._

This spell functions like _[lesser planar binding](ref/spell/planar-binding-lesser)_, except that
you may call a single creature of 18 HD or less, or up to three creatures of the same kind whose Hit
Dice total no more than 18. Each creature gets a saving throw, makes an independent attempt to
escape, and must be individually persuaded to aid you.
