+++
id = "ref/spell/martyrs-bargain"
kind = "spell"
title = "Martyr's Bargain"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martyrs_bargain", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: good
:::

**Sources:** Inner Sea Magic pg 58

Among the faithful followers of the gods of purity - whether they be the servants of Desna in Nidal,
zealous followers of Milani struggling against Cheliax's government, paladins of Iomedae fighting
against the horrors of the Worldwound, or simply those that fight evil the world over-martyr's
bargain represents true faith and true sacrifice.

You cast this spell as an immediate action when you are subject to a spell or
[spell-like ability](ref/umr/spell-like-abilities) that deals hit point damage, after attack rolls
and saving throws have been rolled but before the damage itself is determined. The damage dealt by
the spell and any related effects are then delayed for you (and you only) for a number of rounds
equal to your caster level.

At the end of that time (or immediately if martyr's bargain is dispelled), the delayed damage takes
effect on you as it would have at the time it was cast, but is maximized as if affected by the
[Maximize Spell](ref/feat/maximize-spell) metamagic feat. Spells and
[spell-like abilities](ref/umr/spell-like-abilities) that were already maximized gain no additional
benefit from this spell. Nothing can prevent this delayed damage from affecting you.

You can be affected by only one martyr's bargain spell at a time. If you cast this spell while you
are already under the effects of a previous martyr's bargain, the previous spell effect ends and you
immediately take the damage it had delayed.
