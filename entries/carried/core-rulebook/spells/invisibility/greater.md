+++
id = "ref/carried/core-rulebook/spells/invisibility/greater"
kind = "spell"
title = "Invisibility, Greater"
aon = "SpellDisplay.aspx?ItemName=Invisibility%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Invisibility"]
tags = ["illusion", "glamer"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Invisibility/Greater", path = "core_rulebook/spell/invisibility_greater.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["glamer"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = ": V, S"
range = "personal or touch"
effects = [
  { label = "Target", value = "you or creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless) or yes (harmless, object)"
+++

::: statblock
School: illusion (glamer)
Level: 3: Summoner\
4: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Magus, Skald, Sorcerer, Wizard
Casting Time: 1 standard action
Components: : V, S
Range: personal or touch
Target: you or creature touched
Duration: 1 round/level (D)
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless) or yes (harmless, object)
:::

_As invisibility, but subject can attack and stay invisible._

This spell functions like _invisibility_, except that it doesn't end if the subject attacks.
