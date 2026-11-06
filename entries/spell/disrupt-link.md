+++
id = "ref/spell/disrupt-link"
kind = "spell"
title = "Disrupt Link"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disrupt_link", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature and her animal companion, familiar, or other bonded creature (which may be no more than 30 ft. apart)" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Antipaladin, Arcanist, Sorcerer, Witch, Wizard\
3: Bard, Inquisitor, Skald
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: one creature and her animal companion, familiar, or other bonded creature (which may be no more than 30 ft. apart)
:::

**Sources:** Familiar Folio pg 22

The target has her link with her bonded creature temporarily severed. If the subject has a familiar,
she loses the benefits of the alertness, deliver touch spells, empathic link, scry on familiar,
share spells, and speak with master abilities. If the target has an animal companion, she loses the
benefits of the link, share spells, and devotion abilities. The target and her familiar or animal
companion also lose any other abilities (such as those from archetypes or feats) that rely on the
two having a connection.
