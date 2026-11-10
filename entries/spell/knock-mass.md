+++
id = "ref/spell/knock-mass"
kind = "spell"
title = "Mass Knock"
aon = "SpellDisplay.aspx?ItemName=Knock%2C%20Mass"
source_ids = ["core-rulebook", "inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knock_mass", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/knock" },
]
[[sources]]
publication = "inner-sea-temples"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one means of closure/level, no two of which can be more than 30 feet apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Cleric, Inquisitor, Mesmerist, Occultist, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Target: one means of closure/level, no two of which can be more than 30 feet apart
Duration: instantaneous
Saving throw: none
Spell resistance: no
:::

### Mass Knock

Also known as "unshackle," this spell functions as [knock](ref/spell/knock), but works on multiple
means of closure at once.
