+++
id = "ref/spell/demanding-message-mass"
kind = "spell"
title = "Mass Demanding Message"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demanding_message_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/demanding-message" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "210"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["language-dependant"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of copper wire)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level" },
]
duration = "10 minutes/level, then 1 hour/level or until completed (D); see text"
saving_throw = "Will negates (see text)"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Bard, Mesmerist, Occultist, Psychic, Skald\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of copper wire)
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level
Duration: 10 minutes/level, then 1 hour/level or until completed (D); see text
Saving throw: Will negates (see text)
Spell resistance: yes; see text
Descriptors: language-dependant
:::

### Mass Demanding Message

This spell functions as [demanding message](ref/spell/demanding-message), except that you can issue
one suggestion to each of the spell's targets instead of just one. Each time you do so, it takes a
standard action. You can issue a different suggestion to each target.
