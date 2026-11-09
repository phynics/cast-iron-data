+++
id = "ref/spell/pillow-talk"
kind = "spell"
title = "Pillow Talk"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pillow_talk", path = "json/spells7.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "63"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "sleeping, living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates; see text
Spell resistance: yes
Target: sleeping, living creature touched
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

This spell can be cast only on a sleeping creature, which must be present for the full duration of
the casting time. You grant the semblance of wakefulness to the target, allowing it to answer
questions. You can ask one question per 2 caster levels. The target's knowledge is limited to what
it normally knows, including the languages it speaks. Answers are brief, cryptic, or repetitive,
especially if the creature would have opposed you when awake. If the target succeeds at a Will save,
it awakens (unless some force is preventing it from being awake, such as magic or drugs), and it
remains aware of the first question you asked. If the target has been subject to pillow talk within
the past week, the new spell fails. While your questions don't otherwise wake the target, this spell
does nothing to prevent other sounds or stimulus from waking the target. A target who sleeps through
the spellcasting and duration of the spell has no memory of it taking place, but a target who
awakens before the spell ends remembers every question asked and what answers it gave.
