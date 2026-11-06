+++
id = "ref/spell/free-swim"
kind = "spell"
title = "Free Swim"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "free_swim", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF, M (a strip of kelp bound to the target)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Alchemist, Bard, Cleric, Druid, Hunter, Inquisitor, Investigator, Medium, Mesmerist, Occultist, Oracle, Psychic, Ranger, Skald, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF, M (a strip of kelp bound to the target)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Aquatic Adventures pg 59

The target can move and attack underwater normally without the usual penalties involved with
underwater combat, as if under the effects of freedom of movement. However, the target doesn't gain
any protections against grapple, paralysis, and magical effects that impede movement (such as solid
fog, slow, and web).
