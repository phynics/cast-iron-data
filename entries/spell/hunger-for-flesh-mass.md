+++
id = "ref/spell/hunger-for-flesh-mass"
kind = "spell"
title = "Mass Hunger for Flesh"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunger_for_flesh_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hunger-for-flesh" },
]
[[sources]]
publication = "horror-adventures"
page = "121"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a ghoul fang)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid, magical beast, or monstrous humanoid/level, no two of which can be more than 30 feet apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Spiritualist\
7: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a ghoul fang)
Range: close (25 ft. + 5 ft./2 levels)
Target: one humanoid, magical beast, or monstrous humanoid/level, no two of which can be more than 30 feet apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Descriptors: evil, mind-affecting
:::

### Mass Hunger for Flesh

This spell functions like [hunger for flesh](ref/spell/hunger-for-flesh), except that it affects
multiple targets. When forced to feed by the spell, affected creatures attack creatures not affected
by this spell if there are any such appropriate creatures nearby, but otherwise they attack other
affected creatures.
