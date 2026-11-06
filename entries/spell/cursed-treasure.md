+++
id = "ref/spell/cursed-treasure"
kind = "spell"
title = "Cursed Treasure"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cursed_treasure", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S, M (a platinum piece)"
range = "touch"
effects = [
  { label = "Target", value = "unattended object touched" },
]
duration = "permanent until discharged, then permanent (see text)"
saving_throw = "Fortitude negates (object), then Will negates (see text)"
spell_resistance = "yes (object), then yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Cleric, Oracle, Shaman, Spiritualist, Warpriest, Witch\
4: Arcanist, Bloodrager, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (a platinum piece)
Range: touch
Duration: permanent until discharged, then permanent (see text)
Saving throw: Fortitude negates (object), then Will negates (see text)
Spell resistance: yes (object), then yes (see text)
Target: unattended object touched
Descriptors: curse
:::

**Sources:** Villain Codex pg 188

You touch a piece of treasure or container filled with treasure and place a terrible curse upon it,
choosing from any option available with bestow curse. The next creature to take the treasure or
remove items from the container is affected by the curse, unless it succeeds at a Will save
([spell resistance](ref/rule/spell-resistance) applies). If you are the next creature to take the
treasure or get objects from the container, though, the spell discharges harmlessly instead.
