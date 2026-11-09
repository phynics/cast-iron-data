+++
id = "ref/carried/core-rulebook/spells/shout/greater"
kind = "spell"
title = "Shout, Greater"
aon = "SpellDisplay.aspx?ItemName=Shout%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Shout"]
tags = ["evocation", "sonic"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Shout/Greater", path = "core_rulebook/spell/shout_greater.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Elementalist Wizard", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = ": V, S, F (a metal or ivory horn)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial or Reflex negates (object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
School: evocation \[sonic\]
Level: 6: Bard, Skald\
8: Arcanist, Elementalist Wizard, Sorcerer, Wizard
Casting Time: 1 standard action
Components: : V, S, F (a metal or ivory horn)
Range: 60 ft.
Area: cone-shaped burst
Duration: instantaneous
Saving Throw: Fortitude partial or Reflex negates (object); see text
Spell Resistance: yes (object)
:::

_Devastating yell deals 10d6 sonic damage; stuns creatures._

This spell functions like _[shout](ref/spell/shout)_, except that the cone deals 10d6 points of
sonic damage (or 1d6 points of sonic damage per caster level, maximum 20d6, against exposed brittle
or crystalline objects or crystalline creatures). It also causes creatures to be stunned for 1 round
and deafened for 4d6 rounds. A creature in the area of the cone can negate the stunning and halve
both the damage and the duration of the deafness with a successful Fortitude save. A creature
holding vulnerable objects can attempt a Reflex save to negate the damage to those objects.
