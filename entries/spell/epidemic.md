+++
id = "ref/spell/epidemic"
kind = "spell"
title = "Epidemic"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "epidemic", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature
Descriptors: disease, evil
:::

**Sources:** Ultimate Magic pg 218

_The target contracts one of the following diseases:_ blinding sickness, bubonic plague, cackle
fever, filth fever, leprosy, mindfire, red ache, shakes, or slimy doom, as the spell
[contagion](ref/spell/contagion). However, the disease is highly contagious, and any creature that
touches the infected target, is touched by the target, or spends more than an hour in a confined
space with the target must make a save against the disease's normal DC (not the spell DC) or
contract the disease. If the initial target overcomes the disease by making the required number of
saving throws, it remains a carrier of the disease for a length of time equal to the disease's
frequency, and can continue to infect others during this time.
