+++
id = "ref/spell/force-punch"
kind = "spell"
title = "Force Punch"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "force_punch", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Magus, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: creature touched
Descriptors: force
:::

**Sources:** Ultimate Magic pg 221

This spell charges your hand with telekinetic force. Your successful melee touch attack deals 1d4
points of force damage per level (maximum 10d4) and causes the target to be pushed away from you in
a straight line up to 5 feet per two caster levels. For every size category of the target above
Medium, reduce the distance pushed by 5 feet (-5 feet for Large, -10 feet for Huge, -15 for
Gargantuan, and -20 feet for Colossal) to a minimum of 0 feet. A successful Fortitude save negates
the movement but not the damage.

### Mythic Force Punch

**Sources:** Mythic Adventures pg 96\
The damage dealt increases to 1d6 points of force damage per caster level (maximum 10d6). If moving
the target would push it into another creature's space and it has at least 10 feet of distance
remaining, you can attempt to overrun the other creature, adding your tier on the combat maneuver
check. For each creature you overrun with the target, reduce the distance the target moves by 5
feet. If moving the target would push it into a solid obstacle (such as a wall or tree), the target
takes damage as if it had fallen the distance pushed.

_Augmented (3rd):_ If you expend two uses of mythic power, you can cast this spell as a ranged touch
attack with a range of close (25 feet + 5 feet per 2 caster levels), and the target is treated as
two size categories smaller for the purpose of determining the total distance pushed.
