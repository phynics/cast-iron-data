+++
id = "ref/spell/false-future"
kind = "spell"
title = "False Future"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_future", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (crushed jade worth 100 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates or Will disbelief (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Medium, Mesmerist, Skald\
4: Cleric, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (crushed jade worth 100 gp)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates or Will disbelief (see text)
Spell resistance: yes
Target: creature or object touched
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Ultimate Intrigue pg 214

You interfere with attempts to predict the target's future by preventing divinations from revealing
what the target will do and what will befall the target while under the spell's effects. Instead of
the target's true actions or experiences, divinations resolve as if the target will experience some
different future you describe as you cast false future. The target creature can attempt a Will save
to avoid the initial effect, and creatures using divinations get a Will save to disbelieve the
illusion. This spell doesn't prevent divinations cast after the duration's end from determining what
the subject actually did during the time you obscured using false future.

False future can't be detected by [detect magic](ref/spell/detect-magic) or
[identify](ref/spell/identify), but [greater detect magic](ref/spell/detect-magic-greater) can
detect it.
