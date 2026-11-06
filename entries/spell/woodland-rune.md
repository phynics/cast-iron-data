+++
id = "ref/spell/woodland-rune"
kind = "spell"
title = "Woodland Rune"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "woodland_rune", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "10 minutes"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one rune" },
]
duration = "permanent until discharged (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Druid, Hunter, Ranger, Shaman, Witch
Casting time: 10 minutes
Components: V, S
Range: 0 ft.
Duration: permanent until discharged (D)
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one rune
:::

**Sources:** Wilderness Origins pg 13

Created by Ghorus as a safety measure to limit his enemies' movements, this spell allows you to
inscribe a powerful rune on any surface. Woodland rune triggers when any non-plant creature (apart
from the caster) moves within 30 feet of the rune. When it's triggered, roots and branches sprout
from the ground, catching all creatures within a 30-foot burst of the rune and hindering their
movement as if they were moving through heavy undergrowth, though it does not provide concealment.
Plant creatures and creatures under the effect of woodland stride or
[freedom of movement](ref/spell/freedom-of-movement) are not affected by this spell. In all other
respects, this spell functions as [symbol of death](ref/spell/symbol-of-death).
