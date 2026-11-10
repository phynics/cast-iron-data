+++
id = "ref/spell/eldritch-conduit-greater"
kind = "spell"
title = "Greater Eldritch Conduit"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_conduit_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/eldritch-conduit" },
]
[[sources]]
publication = "inner-sea-magic"
page = "54"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a small mirror)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a small mirror)
Range: medium (100 ft. + 10 ft./level)
Area: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
:::

### Greater Eldritch Conduit

This spell functions like [eldritch conduit](ref/spell/eldritch-conduit) save for the differences
listed above and that the target must be within medium range (100 ft. + 10 ft./level) in order for
you to use the conduit. Using a creature as a conduit for a spell ends the greater eldritch conduit
effect on that creature, but does not end the effect for other eldritch conduits.
