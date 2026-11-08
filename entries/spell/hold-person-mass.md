+++
id = "ref/spell/hold-person-mass"
kind = "spell"
title = "Mass Hold Person"
source_ids = ["core-rulebook", "the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_person_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hold-person" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small, straight piece of iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more humanoid creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Mesmerist\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a small, straight piece of iron)
Range: medium (100 ft. + 10 ft./level)
Targets: one or more humanoid creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Hold Person

**Sources:** PRPG Core Rulebook pg 296

The subject becomes paralyzed and freezes in place. It is aware and breathes normally but cannot
take any actions, even speech. Each round on its turn, the subject may attempt a new saving throw to
end the effect. This is a full-round action that does not provoke attacks of opportunity. A winged
creature who is paralyzed cannot flap its wings and falls. A swimmer can't swim and may drown.

### Hold Fey

**Sources:** The First World, Realm of the Fey pg 12

This spell functions as per [hold person](ref/spell/hold-person), except it affects a fey instead of
a humanoid.

### Mass Hold Person

**Sources:** PRPG Core Rulebook pg 296

This spell functions like hold person, except as noted above.
