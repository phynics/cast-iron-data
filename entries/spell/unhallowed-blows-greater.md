+++
id = "ref/spell/unhallowed-blows-greater"
kind = "spell"
title = "Greater Unhallowed Blows"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unhallowed_blows_greater", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/unhallowed-blows" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of dust from a destroyed undead creature)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one undead creature/level, no two of which can be more than 30 ft. apart, or one undead creature; see text" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Antipaladin, Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of dust from a destroyed undead creature)
Range: medium (100 ft. + 10 ft./level)
Target: one undead creature/level, no two of which can be more than 30 ft. apart, or one undead creature; see text
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Descriptors: evil
:::

### Greater Unhallowed Blows

This spell functions as [unhallowed blows](ref/spell/unhallowed-blows), except the enhancement bonus
is +1 per 4 caster levels (maximum +5). Alternatively, you can imbue all of a creature's natural
weapons with a +1 enhancement bonus (regardless of your caster level).

Greater unhallowed blows can be made permanent with a [permanency](ref/spell/permanency) spell. In
this case, the caster must be at least 11th level and must expend 7,500 gp worth of diamond dust as
a material component.
