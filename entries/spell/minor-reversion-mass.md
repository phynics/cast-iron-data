+++
id = "ref/spell/minor-reversion-mass"
kind = "spell"
title = "Mass Minor Reversion"
aon = "SpellDisplay.aspx?ItemName=Minor%20Reversion%2C%20Mass"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_reversion_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/minor-reversion" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "30 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Psychic\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 30 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 24 hours
Saving throw: none
Spell resistance: no
Subschool: Healing
:::

### Mass Minor Reversion

You create a replica within the Akashic Record of each target at the time the spell is cast. Each
targeted creature must currently have at least half its hit points. If at any time during the
duration of the spell a target is brought below half her maximum hit points, that target can end the
spell on herself as an immediate action to absorb strength from her replica and immediately regain a
number of hit points equal to 1d8 plus 1 point per caster level (maximum +25).
