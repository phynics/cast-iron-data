+++
id = "ref/spell/speak-with-haunt"
kind = "spell"
title = "Speak with Haunt"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_haunt", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["language-dependant"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 3 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "10 ft. (see text)"
effects = [
  { label = "Target", value = "one haunt" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Shaman\
4: Cleric, Oracle, Psychic, Spiritualist, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, DF
Range: 10 ft. (see text)
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: no
Target: one haunt
Descriptors: language-dependant
:::

**Sources:** Advanced Class Guide pg 193

You stir a haunt to a limited sense of awareness and consciousness, allowing it to answer questions.
The spell's range must reach any square within 10 feet of the haunt's area. You must be aware of the
haunt prior to casting the spell, and casting the spell does not trigger the haunt. You can ask one
question per 2 caster levels. The haunt's knowledge is limited to what its original creature knew
during life, including the languages it spoke. A haunt often remembers the circumstance that led to
its existence (though this recollection might be from the original victim's perspective and
therefore not objective), what triggers it, and how it can be laid to rest (destroyed). Answers are
brief, cryptic, or repetitive, especially if the haunt is angry and vindictive.

If the haunt's alignment is more than one step away from yours, the haunt can attempt a Will save to
resist the spell. A haunt's Will save modifier is equal to 3 + the haunt's CR. If the save is
successful, the haunt can refuse to answer your questions or attempt to deceive you (using Bluff). A
haunt's Bluff modifier equals its CR (minimum +0) or might be determined by the GM based upon the
original victim. The haunt can speak only about what it knew in life and the circumstances by which
it became a haunt. It cannot answer any questions that pertain to events that occurred after it was
created. A neutral or good haunt might cooperate with similarly aligned creatures in order to end
its suffering.

If a haunt has been subject to this spell within the past week, a new casting of this spell on it
fails. You can cast this on a haunt that has been deceased for any amount of time. Unlike a corpse
affected by [speak with dead](ref/spell/speak-with-dead), a haunt wants to express itself, if only
to share its pain or to cause mischief.
