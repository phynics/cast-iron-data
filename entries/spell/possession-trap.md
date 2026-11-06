+++
id = "ref/spell/possession-trap"
kind = "spell"
title = "Possession Trap"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "possession_trap", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a gem or crystal worth at least 500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "24 hours or until activated (see text); 1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a gem or crystal worth at least 500 gp)
Range: personal
Duration: 24 hours or until activated (see text); 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Undead Slayer's Handbook pg 19

You place a protective ward over your spirit that ensnares creatures attempting to possess you.
Should a creature attempt to possess you (such as via magic jar or a similar effect) while you are
under the effects of possession trap, that creature must first succeed at a Will save or its
possession attempt is ruined and its spirit is shunted into this spell's focus gem. The trapped
creature is contained within the focus gem for 1 round per caster level, acting as though it were
trapped in a magic jar for the duration of this effect. This effect fails if you are not carrying
the focus gem during the time of the possession attempt.

If the possessor's Will save is successful, you are affected by its possession attempt as normal,
and may attempt a saving throw against this possession attempt if one is normally allowed.
Regardless of whether the possessor fails or succeeds at its save against possession trap, you
immediately become aware of the possession attempt and whether or not a creature is trapped in the
focus gem. If the focus gem is destroyed while it contains a creature, the creature is immediately
released. Once this spell is triggered, it offers no further protection, and a trapped creature can
attempt to possess you again once it's free of the focus gem.
