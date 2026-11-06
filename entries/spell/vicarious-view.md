+++
id = "ref/spell/vicarious-view"
kind = "spell"
title = "Vicarious View"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vicarious_view", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Effect: magical sensor
Subschool: Scrying
:::

**Sources:** Ultimate Intrigue pg 229

You plant a scrying sensor on a touched creature, object, or point in space, allowing you to see and
hear the creature, object, or point and its surroundings (approximately 10 feet in all directions).
If the creature or object on moves, the sensor moves with it. Unlike other scrying spells, vicarious
view doesn't allow magically or supernaturally enhanced senses to work through it.
