+++
id = "ref/carried/ultimate-magic/spells/animate-dead/lesser"
kind = "spell"
title = "Animate Dead, Lesser"
source_ids = ["ultimate-magic"]
section = ["Spells", "Animate Dead"]
tags = ["necromancy", "evil"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Animate Dead/Lesser", path = "ultimate_magic/spell/animate_dead_lesser.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)"
range = "touch"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
School: necromancy \[evil\]
Level: 2: Cleric, Oracle, Shaman, Warpriest\
3: Arcanist, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)
Range: touch
Target: one corpse
Duration: instantaneous
Saving Throw: none
Spell Resistance: no
:::

_Create one skeleton or zombie._

This spell functions as _[animate dead](ref/spell/animate-dead)_, except you can only create a
single Small or Medium skeleton or zombie. You cannot create variant skeletons or zombies with this
spell.
