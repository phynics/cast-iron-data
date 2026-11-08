+++
id = "ref/spell/false-resurrection"
kind = "spell"
title = "False Resurrection"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_resurrection", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/resurrection" },
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

## Resurrection

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

### False Resurrection

**Sources:** Ultimate Intrigue pg 214

This spell functions as [resurrection](ref/spell/resurrection) except that instead of recalling the
dead soul to life, the spell calls a shadow demon with the advanced simple template to possess the
body. If you fail to overcome the subject's [spell resistance](ref/rule/spell-resistance), the
subject's soul can negate the calling and gain the option to return to life (as resurrection) in the
restored body. The possession otherwise functions (as possession) except that the subject's soul is
not present to resist. When false resurrection ends or the demon is removed from the subject, the
demon returns to the Abyss, leaving the body alive but soulless (like that created by clone). If the
soul hasn't been returned to life already, it has the option to return in the now-empty body if it
still lives (as resurrection). If the body was killed, the demon is sent back to the Abyss but the
subject remains dead.

Attempts to identify false resurrection with a skill check incorrectly identify it as resurrection
(see the [ruse](ref/spelldef/ruse) descriptor). A fooled viewer mistakes false resurrection's aura
as the lingering aura of an instantaneous conjuration effect.

### Greater False Resurrection

**Sources:** Ultimate Intrigue pg 214

This spell functions as false resurrection except that it calls a belier devil with the young simple
template to possess the body and all parts of false resurrection that function like resurrection
instead function like [true resurrection](ref/spell/true-resurrection).

Attempts to identify greater false resurrection with a skill check incorrectly identify it as true
resurrection (see the [ruse](ref/spelldef/ruse) descriptor). A fooled viewer mistakes greater false
resurrection's aura as the lingering aura of an instantaneous conjuration effect.
