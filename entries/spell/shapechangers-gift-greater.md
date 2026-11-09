+++
id = "ref/spell/shapechangers-gift-greater"
kind = "spell"
title = "Greater Shapechanger's Gift"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shapechangers_gift_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shapechangers-gift" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "235"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "touch"
effects = [
  { label = "Target", value = "willing living creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: touch
Target: willing living creature touched
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Subschool: Polymorph
:::

### Greater Shapechanger's Gift

This spell functions as [shapechanger's gift](ref/spell/shapechangers-gift) except the chosen form
can be an animal (as per beast shape I), elemental (as per elemental body I), fey (as per fey form
I), humanoid (as per alter self), monstrous humanoid (as per monstrous physique I), or vermin (as
per vermin shape I) and the chosen form can have a fly speed.
