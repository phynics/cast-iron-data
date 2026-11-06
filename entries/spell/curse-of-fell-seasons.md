+++
id = "ref/spell/curse-of-fell-seasons"
kind = "spell"
title = "Curse of Fell Seasons"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_fell_seasons", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse", "darkness"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Druid", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, F (darkwood carving of a tree worth 15,000 gp)"
range = "touch"
effects = [
  { label = "Area", value = "2-mile radius emanating from the touched point" },
]
duration = "permanent (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 9: Arcanist, Druid, Shaman, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (darkwood carving of a tree worth 15,000 gp)
Range: touch
Duration: permanent (D)
Saving throw: none
Spell resistance: no
Area: 2-mile radius emanating from the touched point
Descriptors: curse, darkness
:::

**Sources:** Horror Adventures pg 114

By touching the ground, you drastically change the weather in the area, as the unseasonable weather
curse (see below). The focus merges into the cursed area as part of the spell and can only be
retrieved if the curse is lifted.

### Unseasonable Weather

**Type** regional curse; **Area** 2-mile-radius emanation; **Save** Will DC 23 to remove\
**Effect** The weather in the cursed region changes drastically, even bringing snow to a blazing
desert. The area is plagued by your choice of cold weather conditions, very hot conditions, or
frequent powerful storms. The weather remains unpredictable, and can change over time (as determined
by the GM), but the baseline weather is altered as long as the curse remains.\
**Cure** The cursed weather can be returned to normal only by casting
[remove curse](ref/spell/remove-curse) at the center of the affected area, followed by a casting of
control weather.
