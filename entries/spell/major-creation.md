+++
id = "ref/spell/major-creation"
kind = "spell"
title = "Major Creation"
aon = "SpellDisplay.aspx?ItemName=Major%20Creation"
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
subschools = ["creation"]
levels = [
  { class = "Adept", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (a tiny piece of matter of the same sort of item you plan to create with major creation)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "unattended, nonmagical object of nonliving matter, up to 1 cu. ft./level" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Occultist, Summoner, Unchained Summoner\
5: Adept, Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (a tiny piece of matter of the same sort of item you plan to create with major creation)
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: no
Effect: unattended, nonmagical object of nonliving matter, up to 1 cu. ft./level
Subschool: creation
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
