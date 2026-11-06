+++
id = "ref/spell/itching-curse"
kind = "spell"
title = "Itching Curse"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "itching_curse", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 5 HD or fewer" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Arcanist, Bard, Druid, Hunter, Inquisitor, Occultist, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one living creature with 5 HD or fewer
Descriptors: curse
:::

**Sources:** Magic Tactics Toolbox pg 22

You curse the target with a distracting, unbearable itch. Unless the target scratches as a move
action, it takes a -1 penalty on attack rolls, saving throws, skill checks, and ability checks.
