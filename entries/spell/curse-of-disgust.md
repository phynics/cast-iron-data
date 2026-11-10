+++
id = "ref/spell/curse-of-disgust"
kind = "spell"
title = "Curse of Disgust"
aon = "SpellDisplay.aspx?ItemName=Curse%20of%20Disgust"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_disgust", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "215"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald\
4: Occultist\
5: Arcanist, Sorcerer, Witch, Wizard\
6: Psychic
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, emotion, mind-affecting
:::

You place a curse upon a creature, causing it to avoid the sight of a specific trigger, which is a
kind of creature, object, or condition designated by you. When the target is within 30 feet of a
trigger and is aware of the trigger, it gains the sickened condition and feels an urge to leave. A
successful Will save negates the urge to leave, but the sickened condition persists as long as the
target is within 30 feet of a trigger and aware of it. Example triggers include beggars, filthy
clothing, diseased creatures, the king, blood, spiders, rats, corpses, and sewage.
