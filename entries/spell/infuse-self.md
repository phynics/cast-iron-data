+++
id = "ref/spell/infuse-self"
kind = "spell"
title = "Infuse Self"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infuse_self", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bloodrager, Bard, Investigator, Magus, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

**Sources:** Planar Adventures pg 41

When you cast this spell, you assume the form of a native outsider from the following list: aasimar,
aphorite, duskwalker, fetchling, ganzi, ifrit, oread, shabti, suli, sylph, tiefling, or undine. You
gain a +2 size bonus to one physical ability score of your choice. If the race has resistance to one
or more energy types, you gain energy resistance 5 to your choice of one of those types. If the race
gains a racial bonus on saving throws or skills, you gain those bonuses. If the race has
[darkvision](ref/rule/darkvision) or [low-light vision](ref/rule/low-light-vision), you gain those
qualities.
