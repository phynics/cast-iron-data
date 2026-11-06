+++
id = "ref/spell/true-resurrection"
kind = "spell"
title = "True Resurrection"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_resurrection", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (diamond worth 25,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Cleric, Oracle
Casting time: 10 minutes
Components: V, S, DF, M (diamond worth 25,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 362

This spell functions like [raise dead](ref/spell/raise-dead), except that you can resurrect a
creature that has been dead for as long as 10 years per caster level. This spell can even bring back
creatures whose bodies have been destroyed, provided that you unambiguously identify the deceased in
some fashion (reciting the deceased's time and place of birth or death is the most common method).

Upon completion of the spell, the creature is immediately restored to full hit points, vigor, and
health, with no negative levels (or Constitution points) and all of the prepared spells possessed by
the creature when it died.

You can revive someone killed by a death effect or someone who has been turned into an undead
creature and then destroyed. This spell can also resurrect elementals or outsiders, but it can't
resurrect constructs or undead creatures.

Even [true resurrection](ref/spell/true-resurrection) can't restore to life a creature who has died
of old age.
