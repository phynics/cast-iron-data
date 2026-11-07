+++
id = "ref/spell/simulacrum-lesser"
kind = "spell"
title = "Lesser Simulacrum"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "simulacrum_lesser", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 hour"
components = "V, S, M (an ice sculpture of the target plus powdered rubies worth 50 gp per HD of the simulacrum)"
range = "0 ft."
effects = [
  { label = "Effect", value = "one duplicate creature" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 hour
Components: V, S, M (an ice sculpture of the target plus powdered rubies worth 50 gp per HD of the simulacrum)
Range: 0 ft.
Effect: one duplicate creature
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Subschool: Shadow
:::

## Simulacrum

**Sources:** PRPG Core Rulebook pg 343

Simulacrum creates an illusory duplicate of any creature. The duplicate creature is partially real
and formed from ice or snow. It appears to be the same as the original, but it has only half of the
real creature's levels or HD (and the appropriate hit points, feats, skill ranks, and special
abilities for a creature of that level or HD). You can't create a simulacrum of a creature whose HD
or levels exceed twice your caster level. You must make a Disguise check when you cast the spell to
determine how good the likeness is. A creature familiar with the original might detect the ruse with
a successful Perception check (opposed by the caster's Disguise check) or a DC 20 Sense Motive
check.

At all times, the simulacrum remains under your absolute command. No special telepathic link exists,
so command must be exercised in some other manner. A simulacrum has no ability to become more
powerful. It cannot increase its level or abilities. If reduced to 0 hit points or otherwise
destroyed, it reverts to snow and melts instantly into nothingness. A complex process requiring at
least 24 hours, 100 gp per hit point, and a fully equipped magical laboratory can repair damage to a
simulacrum.

### Lesser Simulacrum

**Sources:** Ultimate Magic pg 238

This spell functions as simulacrum, except you can't create a simulacrum of a creature whose HD or
levels exceed your caster level, and it has no magical abilities. The creature is not under your
control, though it recognizes you are its creator.
