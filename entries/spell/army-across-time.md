+++
id = "ref/spell/army-across-time"
kind = "spell"
title = "Army Across Time"
aon = "SpellDisplay.aspx?ItemName=Army%20Across%20Time"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "army_across_time", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ally-across-time" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "30"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "five 5-ft. cubes of temporal possibility plus one additional cube/level" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Hunter, Medium, Ranger\
4: Bard, Inquisitor, Skald\
5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: five 5-ft. cubes of temporal possibility plus one additional cube/level
Subschool: summoning
:::

### Army Across Time

This spell functions as [ally across time as noted above](ref/spell/ally-across-time) with two
exceptions. First, you can summon one duplicate per caster level before the spell ends. Second, you
can have up to one duplicate in existence at a time for every 3 caster levels you have.
