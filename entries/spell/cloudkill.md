+++
id = "ref/spell/cloudkill"
kind = "spell"
title = "Cloudkill"
aon = "SpellDisplay.aspx?ItemName=Cloudkill"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloudkill", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "256"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 minute/level"
saving_throw = "Fortitude partial; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Magus, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Fortitude partial; see text
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
Descriptors: poison
:::

This spell generates a bank of fog, similar to a [fog cloud](ref/spell/fog-cloud), except that its
vapors are yellowish green and poisonous. These vapors automatically kill any living creature with 3
or fewer HD (no save). A living creature with 4 to 6 HD is slain unless it succeeds on a Fortitude
save (in which case it takes 1d4 points of Constitution damage on your turn each round while in the
cloud).

A living creature with 6 or more HD takes 1d4 points of Constitution damage on your turn each round
while in the cloud (a successful Fortitude save halves this damage). Holding one's breath doesn't
help, but creatures immune to poison are unaffected by the spell.

Unlike a [fog cloud](ref/spell/fog-cloud), the cloudkill moves away from you at 10 feet per round,
rolling along the surface of the ground.

Figure out the cloud's new spread each round based on its new point of origin, which is 10 feet
farther away from the point of origin where you cast the spell.

Because the vapors are heavier than air, they sink to the lowest level of the land, even pouring
down den or sinkhole openings. It cannot penetrate liquids, nor can it be cast underwater.
