+++
id = "ref/spell/unleash-pandemonium"
kind = "spell"
title = "Unleash Pandemonium"
source_ids = ["pathfinder-74-sword-of-valor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unleash_pandemonium", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["chaotic"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-foot-radius spread" },
]
duration = "concentration (maximum 1 round/level) +1 round (D)"
saving_throw = "Will partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Cleric, Oracle, Summoner, Unchained Summoner, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration (maximum 1 round/level) +1 round (D)
Saving throw: Will partial, see text
Spell resistance: no
Area: 30-foot-radius spread
Descriptors: chaotic
:::

**Sources:** Pathfinder \#74: Sword of Valor pg 75

You call upon the wild winds of the Abyssal atmosphere, howling with the screams of damned and
demented souls in torment. The area is filled with winds of windstorm strength, blowing in a random
direction each round. Creatures within the area of effect are deafened as long as they remain within
the area and for 1d4 rounds thereafter; however, they continue to hear the sounds of screams in
their minds with painful intensity, causing them to become shaken for as long as they remain
deafened. A successful Will save negates the shaken condition but not the deafness.
