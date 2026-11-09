+++
id = "ref/spell/healing-flames"
kind = "spell"
title = "Healing Flames"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "healing_flames", path = "json/spells5.json" },
]
[[sources]]
publication = "healers-handbook"
page = "8"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["fire", "good"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Area", value = "10-ft.-radius burst, centered on you" },
]
duration = "instantaneous"
saving_throw = "Reflex half; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: instantaneous
Saving throw: Reflex half; see text
Spell resistance: yes
Area: 10-ft.-radius burst, centered on you
Subschool: Healing
Descriptors: fire, good
:::

You unleash a blast of holy flames that washes over all creatures in the area in a glorious display
of divine power. This deals damage to evil creatures and heals good creatures in the area. The
amount of damage dealt and the number of hit points restored in each case is 1d8 points per 2 caster
levels (maximum 5d8).

Half of the damage this spell deals to evil creatures is fire damage, and half of the damage is pure
divine power that is therefore not subject to reduction by energy resistance to fire-based attacks.

Neutral enemies within the spell's area of effect also take the fire damage, but do not take the
divine damage. Neutral allies within the area are healed by half as much as good creatures. A
successful Reflex saving throw halves the damage taken in all cases.
