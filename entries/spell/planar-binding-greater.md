+++
id = "ref/spell/planar-binding-greater"
kind = "spell"
title = "Greater Planar Binding"
aon = "SpellDisplay.aspx?ItemName=Planar%20Binding%2C%20Greater"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_binding_greater", path = "json/spells7.json" },
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
  { class = "Arcanist", level = 8 },
  { class = "Elementalist Wizard", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to three elementals or outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear." },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "no and yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text for lesser planar binding\]
Level: 6: Summoner\
8: Arcanist, Elementalist Wizard, Psychic, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Targets: up to three elementals or outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear.
Duration: instantaneous
Saving throw: Will negates
Spell resistance: no and yes; see text
Subschool: Calling
:::

### Greater Planar Binding

This spell functions like [lesser planar binding](ref/spell/planar-binding-lesser), except that you
may call a single creature of 18 HD or less, or up to three creatures of the same kind whose Hit
Dice total no more than 18. Each creature gets a saving throw, makes an independent attempt to
escape, and must be individually persuaded to aid you.
