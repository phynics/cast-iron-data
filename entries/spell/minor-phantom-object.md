+++
id = "ref/spell/minor-phantom-object"
kind = "spell"
title = "Minor Phantom Object"
aon = "SpellDisplay.aspx?ItemName=Minor%20Phantom%20Object"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_phantom_object", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/minor-creation" },
]
[[sources]]
publication = "advanced-race-guide"
page = "39"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "illusory, unattended, nonmagical object of nonliving plant matter, up to 1 cu. ft./level" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Mesmerist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: 0 ft.
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Effect: illusory, unattended, nonmagical object of nonliving plant matter, up to 1 cu. ft./level
Subschool: Shadow
Descriptors: shadow
:::

> _[Gnomes](ref/race/gnome) have access to the following spell._

This spell functions as the [minor creation](ref/spell/minor-creation) spell, except the object
created is a semi-real illusion. Any creature that interacts with the object may make a Will save,
with success causing the object to cease to exist. A gnome casting this spell may make a Spellcraft
check in place of any Craft check required to make a complex item.
