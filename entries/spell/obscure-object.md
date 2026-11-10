+++
id = "ref/spell/obscure-object"
kind = "spell"
title = "Obscure Object"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "obscure_object", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "317"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (chameleon skin)"
range = "touch"
effects = [
  { label = "Target", value = "one object touched of up to 100 lbs./level" },
]
duration = "8 hours (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Bard, Mesmerist, Skald\
2: Arcanist, Occultist, Psychic, Sorcerer, Wizard\
3: Cleric, Inquisitor, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (chameleon skin)
Range: touch
Duration: 8 hours (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one object touched of up to 100 lbs./level
:::

This spell hides an object from location by divination (scrying) effects, such as the
[scrying](ref/spell/scrying) spell or a [crystal ball](ref/magic-wondrous/crystal-ball). Such an
attempt automatically fails (if the divination is targeted on the object) or fails to perceive the
object (if the divination is targeted on a nearby location, object, or person).
