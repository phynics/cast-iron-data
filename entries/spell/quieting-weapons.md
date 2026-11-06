+++
id = "ref/spell/quieting-weapons"
kind = "spell"
title = "Quieting Weapons"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quieting_weapons", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to one natural or manufactured weapon per 3 caster levels" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Hunter, Ranger\
4: Arcanist, Bard, Cleric, Inquisitor, Magus, Occultist, Oracle, Psychic, Skald, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: up to one natural or manufactured weapon per 3 caster levels
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Ultimate Intrigue pg 223

The target weapons and any ammunition they fire make no sound as part of their normal functions as a
weapon. For instance, a firearm's firing would not make an explosive sound, but if you cast this
spell on a creature's bite attack, it would not prevent it from vocalizing from its mouth. The first
time a creature is struck by a weapon affected by this spell, it must succeed at a Will save (SR
applies to this effect) or it becomes unable to make noise louder than a whisper (Perception DC 10
to hear) whether vocally or by other means for the duration of the effect. Because the creature can
still whisper, this doesn't interfere with verbal spell components. Whether it succeeds or fails its
saving throw, the creature is immune to further effects from this casting of quieting weapons.
