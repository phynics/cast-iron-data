+++
id = "ref/spell/minor-reversion"
kind = "spell"
title = "Minor Reversion"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_reversion", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "self" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Psychic\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S
Range: personal
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: self
Subschool: Healing
:::

**Sources:** Plane-Hopper's Handbook pg 28

You create an imperfect replica of yourself within the Akashic Record at the time the spell is cast.
You must currently have a number of hit points equal to or greater than half your maximum hit points
to cast the spell. If at any time during the duration of the spell you are brought below half your
maximum hit points, you can end this spell as an immediate action to absorb strength from your
replica and immediately regain a number of hit points equal to 1d8 plus 1 point per caster level
(maximum +5).
