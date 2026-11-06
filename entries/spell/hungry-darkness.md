+++
id = "ref/spell/hungry-darkness"
kind = "spell"
title = "Hungry Darkness"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hungry_darkness", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness", "force"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a bat's tooth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "60-ft.-radius spread" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a bat's tooth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes (see text)
Area: 60-ft.-radius spread
Descriptors: darkness, force
:::

**Sources:** Inner Sea Magic pg 56

This spell creates an area of intense blackness, as deeper darkness, but filled with unseen chewing
teeth and ravenous maws. Any creatures beginning its turn within the hungry darkness is gnawed and
slashed by these unseen fangs of force, dealing 3d6 points of force damage and 2 points of
Constitution damage per round. Once a creature leaves the cloud, it continues to take 1d6 points of
bleed damage each round until it receives magical healing or enters an area of bright light.
[Spell resistance](ref/rule/spell-resistance) can prevent damage from the hungry darkness but not
against the darkness it creates.
