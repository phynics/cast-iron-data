+++
id = "ref/spell/major-phantom-object"
kind = "spell"
title = "Major Phantom Object"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "major_phantom_object", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/major-creation" },
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
  { class = "Arcanist", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (a tiny piece of matter of the same sort of item you plan to create with major phantom object)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "illusory, unattended, nonmagical object, up to 1 cu. ft./level" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Arcanist, Mesmerist, Psychic, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, M (a tiny piece of matter of the same sort of item you plan to create with major phantom object)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Effect: illusory, unattended, nonmagical object, up to 1 cu. ft./level
Subschool: Shadow
Descriptors: shadow
:::

> _[Gnomes](ref/race/gnome) have access to the following spell._

This spell functions as the [major creation](ref/spell/major-creation) spell, except as noted above
and the object created is a semi-real illusion. Any creature that interacts with the object may make
a Will save, with success causing the object to cease to exist. A gnome casting this spell may make
a Spellcraft check in place of any Craft check required to make a complex item.
