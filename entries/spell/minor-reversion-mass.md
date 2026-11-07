+++
id = "ref/spell/minor-reversion-mass"
kind = "spell"
title = "Mass Minor Reversion"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_reversion_mass", path = "json/spells14.json" },
]

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

## Minor Reversion

**Sources:** Plane-Hopper's Handbook pg 28

You create an imperfect replica of yourself within the Akashic Record at the time the spell is cast.
You must currently have a number of hit points equal to or greater than half your maximum hit points
to cast the spell. If at any time during the duration of the spell you are brought below half your
maximum hit points, you can end this spell as an immediate action to absorb strength from your
replica and immediately regain a number of hit points equal to 1d8 plus 1 point per caster level
(maximum +5).

### Greater Reversion

**Sources:** Plane-Hopper's Handbook pg 28

You create a fine-tuned replica of yourself within the [Akashic Record](ref/rule/akashic-record) at
the time the spell is cast. You must currently have a number of hit points equal to or greater than
half your maximum hit points to cast the spell. If at any time during the duration of the spell you
are brought below half your maximum hit points, you can end this spell as an immediate action to
absorb strength from your replica and immediately regain a number of hit points equal to 3d8 plus 1
point per caster level (maximum +15).

### Mass Minor Reversion

**Sources:** Plane-Hopper's Handbook pg 28

You create a replica within the Akashic Record of each target at the time the spell is cast. Each
targeted creature must currently have at least half its hit points. If at any time during the
duration of the spell a target is brought below half her maximum hit points, that target can end the
spell on herself as an immediate action to absorb strength from her replica and immediately regain a
number of hit points equal to 1d8 plus 1 point per caster level (maximum +25).
