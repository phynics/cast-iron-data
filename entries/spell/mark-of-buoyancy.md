+++
id = "ref/spell/mark-of-buoyancy"
kind = "spell"
title = "Mark of Buoyancy"
aon = "SpellDisplay.aspx?ItemName=Mark%20of%20Buoyancy"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mark_of_buoyancy", path = "json/spells6.json" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "28"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "touched object weighing up to 10 lbs./level" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Bard, Cleric, Magus, Occultist, Oracle, Psychic, Skald, Sorcerer, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: touched object weighing up to 10 lbs./level
:::

You cause the touched object to become lighter than air, such that it floats if not weighted down.
The object is effectively weightless and, if left unattended, will rise to a number of feet off the
ground equal to twice your caster level, and then remain floating at that height. The object can be
pushed, dragged, carried, or otherwise moved normally, and it can be carried by the wind if not held
or secured. The object is buoyant enough that it can carry an additional weight of up to 10 pounds
per caster level with it, potentially allowing it to be used to carry small objects or creatures.

Mark of buoyancy can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 11th level or higher at the cost of 7,500 gp.
