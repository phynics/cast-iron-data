+++
id = "ref/spell/heros-defiance"
kind = "spell"
title = "Hero's Defiance"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heros_defiance", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "226"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Paladin", level = 1 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Paladin
Casting time: 1 immediate action
Components: V
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

The instant before you are reduced to 0 or fewer hit points, you can expend a use of your lay on
hands ability to heal yourself as if you had used lay on hands, plus an additional 1d6 hit points.
If this healing brings your hit point total above 0 hit points, you do not fall, and may continue to
act. If you have no more uses of lay on hands this spell has no effect.
