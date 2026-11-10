+++
id = "ref/spell/ban-corruption"
kind = "spell"
title = "Ban Corruption"
aon = "SpellDisplay.aspx?ItemName=Ban%20Corruption"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ban_corruption", path = "json/spells12.json" },
]
[[sources]]
publication = "horror-adventures"
page = "109"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a ceremonial dagger)"
range = "personal"
effects = [
  { label = "Area", value = "30 ft.-radius emanation centered on you" },
]
duration = "concentrationplus 1 round/level, up to 1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Medium\
4: Inquisitor, Occultist, Paladin\
5: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, F (a ceremonial dagger)
Range: personal
Duration: concentrationplus 1 round/level, up to 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Area: 30 ft.-radius emanation centered on you
Descriptors: good
:::

You strip all creatures within the emanation of any gifts associated with
[corruptions](ref/rule/corruption). Abilities associated with corruptions cease to function, as if
they were magically dispelled. The corruption stains still fully affect creatures. A creature that
enters the emanation and fails its saving throw loses its gifts until the spell's duration ends,
even if it leaves the emanation, but a successful saving throw renders a creature immune to the
spell, even if it enters and exits the emanation several times.
