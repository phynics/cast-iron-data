+++
id = "ref/spell/curse-item"
kind = "spell"
title = "Curse Item"
source_ids = ["pathfinder-64-beyond-the-doomsday-door"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_item", path = "json/spells3.json" },
]
[[sources]]
publication = "pathfinder-64-beyond-the-doomsday-door"
page = "73"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 minute"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 minute
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: object touched
Descriptors: curse
:::

> _Clerics of [Groetus](ref/faith/groetus) have access to the following spell._

The object becomes flawed and prone to failure. The effects of this spell depend on the nature of
the object.

_Magic Item:_ The item functions intermittently, gaining either an unreliable curse or a random
dependent curse.

_Nonmagical Armor or Shield:_ The item gains the fragile armor quality.

_Nonmagical Weapon:_ The item gains the fragile weapon quality.

_Tool:_ The item gains the broken condition if a creature rolls a natural 1 while making a skill
check with the tool.

_Other Item:_ Each day it is used, the item has a 5% chance of gaining the broken condition.

This spell does not affect artifacts. The item can be sold or discarded as normal (the bearer is not
compelled to keep it). If a cleric of Groetus is using an item that is affected by this spell, he or
she may make a DC 20 Will saving throw to override the item's curse for 1 day (using it as if the
item were not cursed).
