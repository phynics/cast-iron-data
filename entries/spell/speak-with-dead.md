+++
id = "ref/spell/speak-with-dead"
kind = "spell"
title = "Speak with Dead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_dead", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "346"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["language-dependant"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "10 ft."
effects = [
  { label = "Target", value = "one dead creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Cleric, Inquisitor, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, DF
Range: 10 ft.
Duration: 1 minute/level
Saving throw: Will negates; see text
Spell resistance: no
Target: one dead creature
Descriptors: language-dependant
:::

You grant the semblance of life to a corpse, allowing it to answer questions. You may ask one
question per two caster levels. The corpse's knowledge is limited to what it knew during life,
including the languages it spoke. Answers are brief, cryptic, or repetitive, especially if the
creature would have opposed you in life.

If the dead creature's alignment was different from yours, the corpse gets a Will save to resist the
spell as if it were alive. If successful, the corpse can refuse to answer your questions or attempt
to deceive you, using Bluff. The soul can only speak about what it knew in life. It cannot answer
any questions that pertain to events that occurred after its death.

If the corpse has been subject to [speak with dead](ref/spell/speak-with-dead) within the past week,
the new spell fails. You can cast this spell on a corpse that has been deceased for any amount of
time, but the body must be mostly intact to be able to respond. A damaged corpse may be able to give
partial answers or partially correct answers, but it must at least have a mouth in order to speak at
all. This spell does not affect a corpse that has been turned into an undead creature.
