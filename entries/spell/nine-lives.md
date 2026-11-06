+++
id = "ref/spell/nine-lives"
kind = "spell"
title = "Nine Lives"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nine_lives", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a cat's whisker)"
range = "touch"
effects = [
  { label = "Target", value = "one creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Cleric, Oracle, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a cat's whisker)
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature touched
:::

**Sources:** Advanced Race Guide pg 95

> _[Catfolk](ref/race/catfolk) have access to the following spell._

Despite its name, this powerful ward does not grant the target multiple lives, but rather gives the
target the ability to get out of trouble and relieves harmful effects and conditions. For the
spell's duration, the target can use any of the following abilities as an immediate action, but only
up to a total of nine times, at which point the spell ends.

_Cat's Luck:_ The target can use this ability when it fails a saving throw. The target can reroll
the failed saving throw, but must take the new result even if it is worse.

_Fortitude:_ The target uses this ability when a critical hit or sneak attack is scored against it.
The critical hit or sneak attack is negated and the damage is instead rolled normally.

_Rejuvenate:_ The target uses this ability when it is reduced to 0 or fewer hit points. The target
is instantly healed 3d6 points of damage. If enough hit points are regained to bring the target to
positive hit points, it does not fall unconscious. If it is not enough to leave the target with
positive hit points, the target automatically stabilizes. Both of these effects work even if the
damage was originally enough to kill the target.

_Shake Off:_ The target uses this ability when it is under the effects of any of the following
conditions: blinded, confused, cowering, dazed, dazzled, entangled, exhausted, fatigued, frightened,
nauseated, panicked, shaken, sickened, or staggered. Using this ability ends one of those
conditions.

_Shimmy Out:_ The target uses this ability when it is grappled or pinned. The target automatically
escapes the grapple as if it had succeeded at an Escape Artist check to escape the grapple.

_Stay Up:_ The target uses this ability when it is tripped or otherwise knocked prone. The target
steadies itself and stays upright.
