+++
id = "ref/spell/pocketful-of-vipers"
kind = "spell"
title = "Pocketful of Vipers"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pocketful_of_vipers", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "222"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (a snake scale and fang)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 hour/level or until discharged (D)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Druid, Hunter, Occultist, Shaman, Witch
Casting time: 1 round
Components: V, S, M (a snake scale and fang)
Range: touch
Duration: 1 hour/level or until discharged (D)
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: object touched
Subschool: Summoning
:::

You set a magical ward upon the object touched, which must be a container such as a pouch, bag,
backpack, or pocket. If any creature opens the container without first speaking a command word, 1d3
summoned venomous snakes appear, slithering out of the container and attacking that creature for 1
round/level before disappearing. They attack other creatures only if they themselves are attacked.
