+++
id = "ref/spell/trial-by-fire"
kind = "spell"
title = "Trial by Fire"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trial_by_fire", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Antipaladin, Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: fire
:::

**Sources:** Spymaster's Handbook pg 22

You test a creature's purity of convictions by exposing it to a sheet of divine fire. Unless the
target's alignment is within one step of your deity's, the spell deals 1d6 points of damage per 2
caster levels (maximum 5d6 points of damage). Half the damage is fire damage, but the other half
results directly from divine power and is therefore not subject to being reduced by resistance to
fire-based attacks. Additionally, if the target has an element of its alignment that is in direct
opposition to your (chaos opposes law and evil opposes good), you can also attempt an Intimidate
check to demoralize the target as a free action.
