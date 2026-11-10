+++
id = "ref/spell/ether-step"
kind = "spell"
title = "Ether Step"
aon = "SpellDisplay.aspx?ItemName=Ether%20Step"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ether_step", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ethereal-jaunt" },
]
[[sources]]
publication = "planar-adventures"
page = "40"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 immediate action"
components = "S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Magus\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 immediate action
Components: S
Range: personal
Duration: see text
Saving throw: none
Spell resistance: no
Target: you
:::

You step into the Ethereal Plane long enough to dodge a blow or confound a spell; you must cast
ether step after you are targeted by an attack or effect but before you learn the results of the
attack or effect. This spell functions as [ethereal jaunt](ref/spell/ethereal-jaunt), except that
you become ethereal until the beginning of your next turn. On the turn after you cast this spell and
return to your starting point, you can take only move actions or free actions.
