+++
id = "ref/spell/unbearable-brightness"
kind = "spell"
title = "Unbearable Brightness"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unbearable_brightness", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal and 30 ft. (see text)"
effects = [
  { label = "Area", value = "30-ft.-radius emanation centered on you" },
]
duration = "1 round/level"
saving_throw = "none and Reflex partial (see text)"
spell_resistance = "no and yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Alchemist, Arcanist, Investigator, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal and 30 ft. (see text)
Duration: 1 round/level
Saving throw: none and Reflex partial (see text)
Spell resistance: no and yes (see text)
Area: 30-ft.-radius emanation centered on you
Descriptors: light
:::

**Sources:** Advanced Class Guide pg 197

Your body glows with a terrible light. Creatures within 30 feet of you that can see you are dazzled
(no saving throw). Creatures with light sensitivity must succeed at a Reflex saving throw or be
blinded. This light counts as [daylight](ref/spell/daylight) for the purpose of affecting darkness
effects (and vice versa). If the emanation enters an area under the effect of magical darkness (or
vice versa), both effects are temporarily negated so that the otherwise prevailing light conditions
exist in the overlapping areas of effect. Dazzled and blinded conditions from your light end when
the spell ends or when the creature is out of line of sight.
