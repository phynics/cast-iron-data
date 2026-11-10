+++
id = "ref/spell/contest-of-skill"
kind = "spell"
title = "Contest of Skill"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contest_of_skill", path = "json/spells12.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "27"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a tiny gong)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Magus, Paladin, Skald\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a tiny gong)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

The randomness of critical hits has long vexed certain duelists in the Aldori school who consider
luck to be an unwelcome addition to duels, which they view as contests of skill rather than chance.
The creature targeted by this spell is infused with magical power, altering the odds of combat to
weaken lucky strikes. Critical threats made by the affected creature automatically fail to confirm.
Critical threats that automatically confirm due to class features or feats, such as the fighter's
weapon mastery, are unaffected by this spell.

In addition, when the initial target of this spell fails its Will save to resist contest of skill,
it can select one additional creature within range of the spell to suffer the effects of the spell
as well (Will negates). If this secondary target negates this spell with a successful save, the
duration of contest of skill on the primary target is reduced to 1 round.
