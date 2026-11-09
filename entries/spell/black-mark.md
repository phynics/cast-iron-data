+++
id = "ref/spell/black-mark"
kind = "spell"
title = "Black Mark"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "black_mark", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mark-of-justice" },
]
[[sources]]
publication = "advanced-race-guide"
page = "79"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "fear"]
levels = [
  { class = "Druid", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a flask of seawater)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Druid, Witch
Casting time: 1 standard action
Components: V, S, M (a flask of seawater)
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse, fear
:::

> _[Humans](ref/race/human) have access to the following spells._

You mark the target with a black marking on its skin; the mark's exact appearance determined by you,
but can be no larger than your hand. The black mark functions as a
[mark of justice](ref/spell/mark-of-justice), and when the mark is activated, the target becomes
shaken anytime it is on or in the water more than a 5 feet from shore. In addition, as long as the
black mark is active, the target is affected as if subject to nature's exile, but all creatures with
the aquatic or water subtype or with a swim speed are made hostile, even those not of the animal
type, though non-aquatic animals are not.
