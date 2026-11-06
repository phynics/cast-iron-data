+++
id = "ref/spell/improve-trap"
kind = "spell"
title = "Improve Trap"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "improve_trap", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one trap" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Hunter, Ranger\
3: Arcanist, Druid, Inquisitor, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one trap
:::

**Sources:** Advanced Race Guide pg 137

> _[Kobolds](ref/race/kobold) have access to the following spell._

When this spell is cast upon a trap, it improves one specific element of the trap chosen at the time
of casting. The caster can improve the trap in any of the following ways (each one raises the trap's
CR by +1).

- Increase DC of the Perception check required to locate the trap by +5.
- Increase DC of the Disable Device check required to disarm trap by +5.
- Increase the trap's attack bonus or saving throw by +2.

To cast this on a trap, you must know that the trap exists and its precise location. A trap can only
have one improvement from this spell at a time. A second casting changes the improvement on the
trap, but does not add another improvement.
