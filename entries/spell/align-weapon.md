+++
id = "ref/spell/align-weapon"
kind = "spell"
title = "Align Weapon"
source_ids = ["core-rulebook", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "align_weapon", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation [see text]"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched or 50 projectiles (all of which must be together at the time of casting)" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[see text\]
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: weapon touched or 50 projectiles (all of which must be together at the time of casting)
:::

**Sources:** PRPG Core Rulebook pg 240

Align weapon makes a weapon chaotic, evil, good, or lawful, as you choose. A weapon that is aligned
can bypass the [damage reduction](ref/rule/damage-reduction) of certain creatures. This spell has no
effect on a weapon that already has an alignment.

You can't cast this spell on a natural weapon, such as an unarmed strike. When you make a weapon
chaotic, evil, good, or lawful, align weapon is a chaotic, evil, good, or lawful spell,
respectively.
