+++
id = "ref/spell/web-cloud"
kind = "spell"
title = "Web Cloud"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "web_cloud", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/web" },
]
[[sources]]
publication = "advanced-race-guide"
page = "107"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 minute/level"
saving_throw = "Reflex partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Reflex partial, see text
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
:::

> _[Drow](ref/race/drow) have access to the following spell._

You create a cloud of flame-resistant strands of adhesive webbing that billows and flows much like a
[cloudkill](ref/spell/cloudkill) spell. The cloud moves away from you at a rate of 10 feet per
round, rolling along the surface of the ground.

Figure out the cloud's new spread each round based on its new point of origin, which is 10 feet
farther away from the point of origin where the caster cast the spell. Creatures trapped in the
webbing remain trapped even after the cloud passes, but the area the cloud leaves behind does not
count as difficult terrain.

Because the webbing is heavier than air, it sinks to the lowest level of the land, even pouring down
den or sinkhole openings. The cloud of webbing cannot penetrate liquids, nor can it be cast
underwater.

The cloud otherwise acts like a [web](ref/spell/web) spell. A creature in the cloud at the start of
its turn must save against the cloud or be affected. The webbing of this spell is flammable (as the
web spell), but has fire resistance 5.
