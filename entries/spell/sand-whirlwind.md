+++
id = "ref/spell/sand-whirlwind"
kind = "spell"
title = "Sand Whirlwind"
aon = "SpellDisplay.aspx?ItemName=Sand%20Whirlwind"
source_ids = ["taldor-echoes-of-glory"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sand_whirlwind", path = "json/spells8.json" },
]
[[sources]]
publication = "taldor-echoes-of-glory"
page = "25"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of sand, dust, or fine powder)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates (blinding only)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a handful of sand, dust, or fine powder)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates (blinding only)
Spell resistance: no
Target: one creature
Subschool: Creation
:::

A whirling cloud of sand strikes the target, blinding it and hampering its ability to speak. To
speak while affected by the spell, the target must make a [concentration](ref/rule/concentration)
check (DC equal to the DC of this spell). If the target tries to cast a spell, the Concentration DC
increases by the level of the spell being cast. A successful Will save negates the blindness but not
the speechhampering effect.
