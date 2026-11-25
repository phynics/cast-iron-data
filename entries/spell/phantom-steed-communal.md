+++
id = "ref/spell/phantom-steed-communal"
kind = "spell"
title = "Communal Phantom Steed"
aon = "SpellDisplay.aspx?ItemName=Phantom%20Steed%2C%20Communal"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_steed_communal", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/phantom-steed" },
]
[[sources]]
publication = "ultimate-combat"
page = "239"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to six quasi-real, horse-like creatures" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Summoner, Unchained Summoner\
4: Arcanist, Bard, Occultist, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: up to six quasi-real, horse-like creatures
Subschool: creation
:::

### Communal Phantom Steed

This spell functions like [phantom steed](ref/spell/phantom-steed), except you can summon up to six
steeds, and you divide the duration in 1-hour intervals among the steeds summoned.
