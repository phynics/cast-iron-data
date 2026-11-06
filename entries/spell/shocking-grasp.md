+++
id = "ref/spell/shocking-grasp"
kind = "spell"
title = "Shocking Grasp"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shocking_grasp", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: creature or object touched
Descriptors: electricity
:::

**Sources:** PRPG Core Rulebook pg 343

Your successful melee touch attack deals 1d6 points of electricity damage per caster level (maximum
5d6). When delivering the jolt, you gain a +3 bonus on attack rolls if the opponent is wearing metal
armor (or is carrying a metal weapon or is made of metal).

### Mythic Shocking Grasp

**Sources:** Mythic Adventures pg 108\
The spell's damage increases to 1d8 points of electricity damage per caster level (maximum 5d8). If
the target is wearing metal armor or is made of metal, you may attempt a free grapple combat
maneuver against the target.

Alternatively, if the target is carrying a metal weapon, you may attempt a free disarm combat
maneuver against that weapon. This free combat maneuver doesn't provoke attacks of opportunity.

_Augmented:_ If you expend two uses of mythic power and the free grapple or disarm combat maneuver
is successful, the target is staggered until your next turn. This is an electricity effect.
