+++
id = "ref/spell/incendiary-cloud"
kind = "spell"
title = "Incendiary Cloud"
aon = "SpellDisplay.aspx?ItemName=Incendiary%20Cloud"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "incendiary_cloud", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level (D)"
saving_throw = "Reflex half, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Summoner\
8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Reflex half, see text
Spell resistance: no
Area: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
Descriptors: fire
:::

An incendiary cloud spell creates a cloud of roiling smoke shot through with white-hot embers. The
smoke obscures all sight as a fog cloud does. In addition, the white-hot embers within the cloud
deal 6d6 points of fire damage to everything within the cloud on your turn each round. All targets
can make Reflex saves each round to take half damage.

As with a cloudkill spell, the smoke moves away from you at 10 feet per round. Figure out the
smoke's new spread each round based on its new point of origin, which is 10 feet farther away from
where you were when you cast the spell. By concentrating, you can make the cloud move as much as 60
feet each round. Any portion of the cloud that would extend beyond your maximum range dissipates
harmlessly, reducing the remainder's spread thereafter.

As with fog cloud, wind disperses the smoke, and the spell can't be cast underwater.
