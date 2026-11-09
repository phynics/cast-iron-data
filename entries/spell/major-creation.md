+++
id = "ref/spell/major-creation"
kind = "spell"
title = "Major Creation"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "major_creation", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/minor-creation" },
]
[[sources]]
publication = "core-rulebook"
page = "311"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Adept", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S, M (a tiny piece of matter of the same sort of item you plan to create with minor creation)"
range = "0 ft."
effects = [
  { label = "Effect", value = "unattended, nonmagical object of nonliving plant matter, up to 1 cu. ft./level" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Occultist, Spiritualist, Summoner, Unchained Summoner\
4: Adept, Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S, M (a tiny piece of matter of the same sort of item you plan to create with minor creation)
Range: 0 ft.
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: unattended, nonmagical object of nonliving plant matter, up to 1 cu. ft./level
Subschool: Creation
:::

### Major Creation

This spell functions like [minor creation](ref/spell/minor-creation), except that you can also
create an object of mineral nature: stone, crystal, metal, or the like. The duration of the created
item varies with its relative [hardness](ref/umr/hardness) and rarity, as indicated on the following
table.

|Hardness and Rarity Examples|Duration|
| --- | --- |
|Vegetable matter|2 hr./level|
|Stone, crystal, base metals|1 hr./level|
|Precious metals|20 min./level|
|Gems|10 min./level|
|Rare metal^[1](ref/spell/major-creation#footnote-r)^|1 round/level|

###### ^1^ {#footnote-r}

Includes adamantine, alchemical silver, and mithral. You can't use major creation to create a cold
iron item.
