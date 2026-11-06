+++
id = "ref/spell/light"
kind = "spell"
title = "Light"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "light", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Adept", level = 0 },
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 0 },
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Inquisitor", level = 0 },
  { class = "Magus", level = 0 },
  { class = "Medium", level = 0 },
  { class = "Mesmerist", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Shaman", level = 0 },
  { class = "Skald", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Spiritualist", level = 0 },
  { class = "Summoner", level = 0 },
  { class = "Unchained Summoner", level = 0 },
  { class = "Warpriest", level = 0 },
  { class = "Witch", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, M/DF (a firefly)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 0: Adept, Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Medium, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, M/DF (a firefly)
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: light
:::

**Sources:** PRPG Core Rulebook pg 304

This spell causes a touched object to glow like a torch, shedding normal light in a 20-foot radius,
and increasing the light level for an additional 20 feet by one step, up to normal light (darkness
becomes dim light, and dim light becomes normal light). In an area of normal or bright light, this
spell has no effect. The effect is immobile, but it can be cast on a movable object.

You can only have one light spell active at any one time. If you cast this spell while another
casting is still in effect, the previous casting is dispelled. If you make this spell permanent
(through [permanency](ref/spell/permanency) or a similar effect), it does not count against this
limit. Light can be used to counter or dispel any [darkness](ref/spelldef/darkness) spell of equal
or lower spell level.
