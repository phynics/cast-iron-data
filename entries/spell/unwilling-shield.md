+++
id = "ref/spell/unwilling-shield"
kind = "spell"
title = "Unwilling Shield"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unwilling_shield", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (ruby dust worth 250 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Bard, Inquisitor, Mesmerist, Occultist, Skald\
6: Arcanist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (ruby dust worth 250 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
:::

**Sources:** Advanced Player's Guide pg 253

Like [shield other](ref/spell/shield-other), unwilling shield creates a mystic connection between
you and the target, but unlike _[shield other](ref/spell/shield-other),_ the target shares the
wounds that you receive. In addition, the link draws upon the target's life force to supplement your
own defenses. You gain a +1 luck bonus to AC and on saving throws. You take only half damage from
all wounds and attacks (including those dealt by special abilities) that deal hit point damage. The
amount of damage not taken by you is taken by the target. Forms of harm that do not involve hit
points, such as charm effects, ability damage, level draining, and death effects are not affected.
If you take a reduction in hit points from a lowered Constitution score, the reduction is not split
with the target because it is not hit point damage. When the spell ends, subsequent damage is no
longer divided between you and the subject, but damage already split is not assigned to you.

If you and the target of the spell move out of range of each other, the spell remains active, but
damage is no longer shared until you are once again within range of each other.
