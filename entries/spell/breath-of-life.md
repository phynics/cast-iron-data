+++
id = "ref/spell/breath-of-life"
kind = "spell"
title = "Breath of Life"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "breath_of_life", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless) or Will half, see text"
spell_resistance = "yes (harmless) or yes, see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Cleric, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless) or Will half, see text
Spell resistance: yes (harmless) or yes, see text
Target: creature touched
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 251

This spell cures 5d8 points of damage + 1 point per caster level (maximum +25).

Unlike other spells that heal damage, breath of life can bring recently slain creatures back to
life. If cast upon a creature that has died within 1 round, apply the healing from this spell to the
creature. If the healed creature's hit point total is at a negative amount less than its
Constitution score, it comes back to life and stabilizes at its new hit point total. If the
creature's hit point total is at a negative amount equal to or greater than its Constitution score,
the creature remains dead. Creatures brought back to life through breath of life gain a temporary
negative level that lasts for 1 day.

Creatures slain by death effects cannot be saved by breath of life.

Like cure spells, breath of life deals damage to undead creatures rather than curing them, and
cannot bring them back to life.

### Mythic Breath of Life

**Sources:** Mythic Adventures pg 87\
The spell heals 5d12 points of damage + 1 point per caster level (maximum +25). It can revive a
creature that died of hp damage within the past 2 rounds. If the target was slain by a death effect
that allows a saving throw, this spell allows the creature to attempt another save against that
effect. If this save is successful, the creature is revived with -10 hp plus the amount healed by
this spell.

_Augmented (9th):_ If you expend two uses of mythic power, you can target up to one creature per
caster level within 30 feet of you. Alternatively, you can target one creature that has been dead
for a number of rounds up to your caster level.
