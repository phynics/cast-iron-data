+++
id = "ref/spell/darkvault"
kind = "spell"
title = "Darkvault"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darkvault", path = "json/spells3.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "15"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a stone that has never seen sunlight)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft.-radius emanation" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Alchemist, Investigator\
5: Arcanist, Cleric, Druid, Hunter, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a stone that has never seen sunlight)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 24 hours
Saving throw: none
Spell resistance: no
Area: 30-ft.-radius emanation
:::

You ward an area's shadows such that light cannot penetrate them. The illumination level in the
affected area no longer changes when nonmagical light enters it. Any magical effect must succeed at
a caster level check (DC = 10 + your caster level) in order to change the light level within the
spell's radius. Darkvault has no effect on spells or effects that would make the spell's area
darker.

The spell must be cast on an area, such as a cave or room. A spellcaster of 11th level or higher can
make darkvault permanent with a [permanency](ref/spell/permanency) spell, at a cost of 7,500 gp.
