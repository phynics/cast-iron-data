+++
id = "ref/spell/haunting-choir"
kind = "spell"
title = "Haunting Choir"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "haunting_choir", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft.-radius emanation" },
]
duration = "concentration+ 2 rounds"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Bard, Mesmerist, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 2 rounds
Saving throw: Will negates
Spell resistance: yes
Area: 30-ft.-radius emanation
Descriptors: mind-affecting, pain
:::

**Sources:** Ultimate Magic pg 222

You create a spectral choir and conduct its tortured, ghostly moans, deluding listeners into
believing they are suffering the torments of the dead. The transparent singers occupy a 10-foot
cube, but they are intangible and do not interfere with creatures in any physical way, nor can they
be attacked. Creatures within 30 feet of the choir experience wracking pain that causes them to take
a -2 penalty on attack rolls, skill checks, and ability checks. Individuals who exit the area of
effect take these penalties for an additional 2 rounds before the delusion wears off.
