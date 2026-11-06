+++
id = "ref/spell/open-arms"
kind = "spell"
title = "Open Arms"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "open_arms", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 immediate action"
components = "V, S, F (a magical or masterwork melee weapon)"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Sorcerer, Wizard
Casting time: 1 immediate action
Components: V, S, F (a magical or masterwork melee weapon)
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: melee weapon touched
:::

**Sources:** Arcane Anthology pg 21

You cast this spell in response to a specific cavalier's challenge, inquisitor's judgment, or smite
(such as a paladin's smite evil) declared against you by an enemy creature. It can also be cast if a
creature uses a spell that causes you to qualify as the creature's
[favored enemy](ref/ability/favored-enemy) when you normally wouldn't, such as
[instant enemy](ref/spell/instant-enemy).

You imbue your weapon with a powerful ability to ward off attacks made against you by the creature
that challenged you. You gain a +5 insight bonus to your AC and CMD against the attacks of the
initiating creature as long as you hold the weapon. If you release the weapon for any reason, the
spell ends. You can cast this spell only in response to one of the conditions listed above. The
spell fails if you attempt to cast it when you were not subject to a challenge or similar effect
since your last turn.
