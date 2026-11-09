+++
id = "ref/spell/touch-of-slumber"
kind = "spell"
title = "Touch of Slumber"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_slumber", path = "json/spells10.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "26"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a bit of seaweed)"
range = "touch"
effects = [
  { label = "Target", value = "non-hostile creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Arcanist, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Warpriest, Wizard\
6: Bard, Psychic, Skald, Witch
Casting time: 1 standard action
Components: V, S, M (a bit of seaweed)
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: non-hostile creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions only against a creature with an attitude toward you of indifferent or better,
and only if the target is not hostile toward you or your visible allies. A target touched by you
(this touch usually requires a successful melee touch attack) must succeed at a Will saving throw or
fall asleep for 2d6 hours. While asleep, the creature is helpless. For 1 minute after the creature
is affected, any loud noise or rough contact causes it to awaken immediately. Thereafter, slapping
or wounding an affected creature awakens it, but normal noise does not. Awakening a creature is a
standard action (this is an application of the aid another action).
