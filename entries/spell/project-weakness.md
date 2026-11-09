+++
id = "ref/spell/project-weakness"
kind = "spell"
title = "Project Weakness"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "project_weakness", path = "json/spells15.json" },
]
[[sources]]
publication = "blood-of-the-night"
page = "30"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Cleric, Oracle, Warpriest, Witch\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: living creature touched
Descriptors: curse, evil
:::

> _[Vampires](ref/template/vampire) have access to the following spell._

You curse the target with the weaknesses of your kind of vampirism. The creature reacts to garlic,
mirrors, ringing bells, sunlight, and so on as if it were a vampire of the same type as you. This
cannot kill the target; anything that would kill it (such as a lengthy exposure to sunlight if you
are a moroi vampire) renders it helpless until the curse or the harmful effect is removed. The
target gains none of the benefits of being a vampire (such as [fast healing](ref/umr/fast-healing)
or requiring special ways to be permanently killed), only the penalties.
