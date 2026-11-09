+++
id = "ref/spell/catatonia"
kind = "spell"
title = "Catatonia"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "catatonia", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "161"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "willing creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Alchemist, Bard, Investigator, Medium, Mesmerist, Skald, Spiritualist\
3: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: touch
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: yes
Target: willing creature touched
:::

You touch the target and place it into a deathlike state that persists for the duration. The target
appears to be dead, and any creature that interacts with the target must succeed at a DC 20 Heal
check to recognize it is actually alive.

Until the spell ends, the target counts as if it were dead for the purpose of resolving any effects
that target or affect only living creatures, but it doesn't count as undead. The subject is
helpless, and can still be killed normally.

Any effect that would bring the creature back to life or animate it as an undead fails, but ends the
catatonia. The target can be affected by spells that affect only objects, including animate objects
(if the creature is Small) and teleport object. However, anything that would cause the body to
change form (such as shrink item) fails and ends the catatonia. This doesn't prevent the effects of
spells that simply deal damage or otherwise destroy objects.
