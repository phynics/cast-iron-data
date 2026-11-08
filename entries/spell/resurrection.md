+++
id = "ref/spell/resurrection"
kind = "spell"
title = "Resurrection"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resurrection", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 minute"
components = "V, S, DF, M (diamond worth 10,000 gp)"
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
Level: 7: Cleric, Oracle\
8: Shaman, Witch
Casting time: 1 minute
Components: V, S, DF, M (diamond worth 10,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 334

This spell functions like [raise dead](ref/spell/raise-dead), except that you are able to restore
life and complete strength to any deceased creature.

The condition of the remains is not a factor. So long as some small portion of the creature's body
still exists, it can be resurrected, but the portion receiving the spell must have been part of the
creature's body at the time of death. (The remains of a creature hit by a disintegrate spell count
as a small portion of its body.) The creature can have been dead no longer than 10 years per caster
level.

Upon completion of the spell, the creature is immediately restored to full hit points, vigor, and
health, with no loss of prepared spells. The subject of the spell gains one permanent negative level
when it is raised, just as if it had been hit by an energy-draining creature. If the subject is 1st
level, it takes 2 points of Constitution drain instead (if this would reduce its Con to 0 or less,
it can't be resurrected).

You can resurrect someone killed by a death effect or someone who has been turned into an undead
creature and then destroyed. You cannot resurrect someone who has died of old age. Constructs,
elementals, outsiders, and undead creatures can't be resurrected.
