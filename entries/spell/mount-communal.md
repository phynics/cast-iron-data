+++
id = "ref/spell/mount-communal"
kind = "spell"
title = "Communal Mount"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mount_communal", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mount" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, M (a bit of horse hair)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one mount" },
]
duration = "2 hours/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bloodrager, Magus, Occultist, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a bit of horse hair)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level (D)
Saving throw: none
Spell resistance: no
Effect: one mount
Subschool: Summoning
:::

### Communal Mount

**Sources:** Ultimate Combat pg 237

This spell functions like [mount](ref/spell/mount), except you can summon up to six light horses or
ponies, and you divide the duration in 2-hour increments among the steeds summoned.
