+++
id = "ref/spell/inflict-moderate-wounds-mass"
kind = "spell"
title = "Mass Inflict Moderate Wounds"
aon = "SpellDisplay.aspx?ItemName=Inflict%20Moderate%20Wounds%2C%20Mass"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_moderate_wounds_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inflict-light-wounds-mass" },
]
[[sources]]
publication = "core-rulebook"
page = "300"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest\
7: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
:::

### Mass Inflict Moderate Wounds

This spell functions like [mass inflict light wounds](ref/spell/inflict-light-wounds-mass), except
that it deals 2d8 points of damage + 1 point per caster level (maximum +30).
