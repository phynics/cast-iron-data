+++
id = "ref/spell/animal-trance"
kind = "spell"
title = "Animal Trance"
aon = "SpellDisplay.aspx?ItemName=Animal%20Trance"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_trance", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "241"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "animals or magical beasts with Intelligence 1 or 2" },
]
duration = "concentration"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Adept, Bard, Druid, Hunter, Mesmerist, Psychic, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration
Saving throw: Will negates
Spell resistance: yes
Targets: animals or magical beasts with Intelligence 1 or 2
Subschool: Compulsion
Descriptors: mind-affecting, sonic
:::

Your swaying motions and music (or singing, or chanting) compel animals and magical beasts to do
nothing but watch you. Only a creature with an Intelligence score of 1 or 2 can be fascinated by
this spell. Roll 2d6 to determine the total number of HD worth of creatures that you fascinate. The
closest targets are selected first until no more targets within range can be affected.
