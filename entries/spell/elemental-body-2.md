+++
id = "ref/spell/elemental-body-2"
kind = "spell"
title = "Elemental Body II"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_body_2", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/elemental-body-1" },
]
[[sources]]
publication = "core-rulebook"
page = "276"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (the element you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (the element you plan to assume)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Elemental Body II

This spell functions as [elemental body I](ref/spell/elemental-body-1), except that it also allows
you to assume the form of a Medium air, earth, fire, or water elemental. The abilities you gain
depend upon the elemental.

_Air elemental:_ As elemental body I except that you gain a +4 size bonus to your Dexterity and a +3
natural armor bonus.

_Earth elemental:_ As elemental body I except that you gain a +4 size bonus to your Strength and a
+5 natural armor bonus.

_Fire elemental:_ As elemental body I except that you gain a +4 size bonus to your Dexterity and a
+3 natural armor bonus.

_Water elemental:_ As elemental body I except that you gain a +4 size bonus to your Constitution and
a +5 natural armor bonus.
