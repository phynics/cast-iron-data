+++
id = "ref/spell/lunar-veil"
kind = "spell"
title = "Lunar Veil"
aon = "SpellDisplay.aspx?ItemName=Lunar%20Veil"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lunar_veil", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "227"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["darkness", "shadow"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "120-ft.-radius emanation" },
]
duration = "10 minutes/level"
saving_throw = "Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level
Saving throw: Will negates, see text
Spell resistance: no
Area: 120-ft.-radius emanation
Subschool: Shadow
Descriptors: darkness, shadow
:::

You conjure a tremendous area of shadow to obscure moonlight within the area, creating something
akin to a lunar eclipse. The light level is lowered by two steps (though unlike
[deeper darkness](ref/spell/deeper-darkness), areas of normal light or dimmer become normal darkness
rather than supernaturally dark). Lycanthropes in the area must make a Will save every round or
revert to their humanoid forms. In addition, lycanthropes attempting to assume animal or hybrid form
within the affected area take a -5 penalty on Constitution checks to do so.
