+++
id = "ref/spell/curse-of-night"
kind = "spell"
title = "Curse of Night"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_night", path = "json/spells3.json" },
]
[[sources]]
publication = "horror-adventures"
page = "114"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["curse", "darkness"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, F (jet gemstones worth a total of 10,000 gp)"
range = "touch"
effects = [
  { label = "Area", value = "1-mile radius emanating from touched point)" },
]
duration = "permanent (D)"
saving_throw = "none (see curse text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 8: Arcanist, Cleric, Druid, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (jet gemstones worth a total of 10,000 gp)
Range: touch
Duration: permanent (D)
Saving throw: none (see curse text)
Spell resistance: no
Area: 1-mile radius emanating from touched point)
Descriptors: curse, darkness
:::

By touching the ground, you curse an area to remain in bleak darkness, as the endless night curse
(see below). The focus merges into the cursed area as part of the spell and can only be retrieved if
the curse is lifted.

### Endless Night

**Type** regional curse; **Area** 1-mile-radius emanation; **Save** Will DC 22 negates\
**Effect** Nonmagical light and magical light sources that produce normal light create only dim
light in the cursed area, and even direct sunlight leads to only an ambient dim light in the area
(similar to a full moon). Twilight and night are always dark. Creatures harmed or weakened by
daylight can move about during the day in this area and the only impairment they take from the
dimmed sunlight is that they become dazzled in its area. Plant growth in the area is stunted, as per
the stunt growth usage of diminish plants. Any spellcaster attempting to cast
[daylight](ref/spell/daylight) or a spell that creates true daylight or bright light in the area
fails unless she succeeds at a Will saving throw against the curse. Success leads to normal light,
rather than bright light.\
**Cure** An endless night can be lifted only by successfully casting
[remove curse](ref/spell/remove-curse) followed by [sunburst](ref/spell/sunburst) at noon on a clear
day.
