+++
id = "ref/spell/planar-binding"
kind = "spell"
title = "Planar Binding"
aon = "SpellDisplay.aspx?ItemName=Planar%20Binding"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_binding", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-binding-lesser" },
]
[[sources]]
publication = "core-rulebook"
page = "321"

[fields]
kind = "spell"
school = "conjuration [see text for lesser planar binding]"
subschools = ["Calling"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to three elementals or outsiders, totaling no more than 12 HD, no two of which can be more than 30 ft. apart when they appear" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "no and yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text for lesser planar binding\]
Level: 5: Summoner\
6: Arcanist, Occultist, Psychic, Sorcerer, Unchained Summoner, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: no and yes; see text
Targets: up to three elementals or outsiders, totaling no more than 12 HD, no two of which can be more than 30 ft. apart when they appear
Subschool: Calling
:::

This spell functions like [lesser planar binding](ref/spell/planar-binding-lesser), except that you
may call a single creature of 12 HD or less, or up to three creatures of the same kind whose Hit
Dice total no more than 12. Each creature gets a saving throw, makes an independent attempt to
escape, and must be individually persuaded to aid you.
