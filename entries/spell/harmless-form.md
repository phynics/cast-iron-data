+++
id = "ref/spell/harmless-form"
kind = "spell"
title = "Harmless Form"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harmless_form", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one willing animal companion, familiar, or spirit animal" },
]
duration = "8 hours (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Druid, Hunter, Ranger, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 8 hours (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: one willing animal companion, familiar, or spirit animal
Subschool: Polymorph
:::

**Sources:** Heroes of the Streets pg 23

You transform the target into a harmless animal of the same approximate body type. The form assumed
must be one considered unobtrusive by local communities, such as a cat, a dog, a hunting hawk, a
horse, or a rat. This transformation can reduce the target by up to two size categories, but cannot
make an animal smaller than Tiny. It cannot increase the size of the target or give it new natural
attacks or new forms of movement. The spell otherwise functions as
[beast shape II](ref/spell/beast-shape-2).
