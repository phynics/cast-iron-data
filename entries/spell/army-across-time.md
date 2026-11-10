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
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one 5-ft. cube of temporal possibility/2 levels" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Hunter, Medium, Ranger\
2: Arcanist, Bard, Cleric, Inquisitor, Oracle, Psychic, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: one 5-ft. cube of temporal possibility/2 levels
Subschool: Summoning
:::

### Army Across Time

This spell functions as [ally across time as noted above](ref/spell/ally-across-time) with two
exceptions. First, you can summon one duplicate per caster level before the spell ends. Second, you
can have up to one duplicate in existence at a time for every 3 caster levels you have.
