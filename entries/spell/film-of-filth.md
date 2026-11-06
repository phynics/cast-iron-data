+++
id = "ref/spell/film-of-filth"
kind = "spell"
title = "Film of Filth"
source_ids = ["pathfinder-74-sword-of-valor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "film_of_filth", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Hunter, Ranger\
4: Arcanist, Cleric, Druid, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: poison
:::

**Sources:** Pathfinder \#74: Sword of Valor pg 74

You cause the target's flesh to exude a layer of putrescent slime so foul that the target is
sickened (Fortitude negates) for the duration of the spell and for 1d4 rounds thereafter. All
creatures within 20 feet also become sickened (Fortitude negates), and remain sickened for as long
as they remain within 20 feet of the target and for 1d4 rounds thereafter. A creature that strikes
the target with a bite attack must succeed at an additional save or become nauseated for 1d4 rounds.
Creatures immune to poison are unaffected.
