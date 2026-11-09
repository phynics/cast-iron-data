+++
id = "ref/carried/core-rulebook/spells/inflict-light-wounds/mass"
kind = "spell"
title = "Inflict Light Wounds, Mass"
aon = "SpellDisplay.aspx?ItemName=Inflict%20Light%20Wounds%2C%20Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Inflict Light Wounds"]
tags = ["necromancy"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Inflict Light Wounds/Mass", path = "core_rulebook/spell/inflict_light_wounds_mass.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
School: necromancy
Level: 5: Cleric, Inquisitor, Oracle, Shaman, Warpriest\
6: Witch
Casting Time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving Throw: Will half
Spell Resistance: yes
:::

_Deals 1d8 damage + 1/level, affects 1 subject/level._

Negative energy spreads out in all directions from the point of origin, dealing 1d8 points of
damage + 1 point per caster level (maximum +25) to nearby living enemies.

Like other _inflict_ spells, _[mass inflict light wounds](ref/spell/inflict-light-wounds-mass)_
cures undead in its area rather than damaging them. A cleric capable of spontaneously casting
_inflict_ spells can also spontaneously cast _mass inflict_ spells.
