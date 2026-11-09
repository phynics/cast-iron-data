+++
id = "ref/spell/resize-item"
kind = "spell"
title = "Resize Item"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resize_item", path = "json/spells8.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "33"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (silver calipers worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one weapon or suit of armor weighing up to 25 lbs./level" },
]
duration = "24 hours (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (silver calipers worth 25 gp)
Range: touch
Duration: 24 hours (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one weapon or suit of armor weighing up to 25 lbs./level
:::

You alter a magic weapon or suit of armor to be up to two size categories larger or smaller. If the
spell on a resized suit of armor ends while the armor is being worn, the armor falls off harmlessly.
If the spell would cause an item to grow too large for the area containing it, its growth halts just
before that point.

Resize item can be made permanent with a [permanency](ref/spell/permanency) spell for 7,500 gp, in
which case the affected object is set at one specific new size within two steps of its original
size.
