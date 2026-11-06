+++
id = "ref/spell/sotto-voce"
kind = "spell"
title = "Sotto Voce"
source_ids = ["faction-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sotto_voce", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["fear", "mind-affecting", "sonic"]
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 0 },
  { class = "Warpriest", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature of 4 HD or less" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 0: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard\
1: Bard, Skald
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid creature of 4 HD or less
Descriptors: fear, mind-affecting, sonic
:::

**Sources:** Faction Guide pg 61

Your dry, rasping whisper fills a living creature of 4 or fewer Hit Dice with unnatural dread. The
affected creature must make a Will save or be shaken for 1 round.

This spell originated among the followers of the [Whispering Way](ref/rule/f-gravepath), but
necromancers and other intimidating folk outside that group are known to use it.
