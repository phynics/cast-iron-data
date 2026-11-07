+++
id = "ref/spell/demanding-message-mass"
kind = "spell"
title = "Mass Demanding Message"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demanding_message_mass", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["language-dependant"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of copper wire)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level" },
]
duration = "10 minutes/level, then 1 hour/level or until completed (D); see text"
saving_throw = "Will negates (see text)"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Bard, Mesmerist, Occultist, Psychic, Skald\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of copper wire)
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level
Duration: 10 minutes/level, then 1 hour/level or until completed (D); see text
Saving throw: Will negates (see text)
Spell resistance: yes; see text
Descriptors: language-dependant
:::

## Message

**Sources:** PRPG Core Rulebook pg 313

You can whisper messages and receive whispered replies. Those nearby can hear these messages with a
DC 25 Perception check. You point your finger at each creature you want to receive the message. When
you whisper, the whispered message is audible to all targeted creatures within range. Magical
silence, 1 foot of stone, 1 inch of common metal (or a thin sheet of lead), or 3 feet of wood or
dirt blocks the spell. The message does not have to travel in a straight line. It can circumvent a
barrier if there is an open path between you and the subject, and the path's entire length lies
within the spell's range. The creatures that receive the message can whisper a reply that you hear.
The spell transmits sound, not meaning; it doesn't transcend language barriers. To speak a message,
you must mouth the words and whisper.

### Demanding Message

**Sources:** Ultimate Intrigue pg 210

This spell initially functions as message (allowing no save or
[spell resistance](ref/rule/spell-resistance)). Once during the message effect, you can concentrate
as a standard action to issue a suggestion to one target as part of delivering a message. Spell
resistance and a Will save apply to the suggestion, and it lasts for 1 hour per level or until
completed.

### Mass Demanding Message

**Sources:** Ultimate Intrigue pg 210

This spell functions as demanding message, except that you can issue one suggestion to each of the
spell's targets instead of just one. Each time you do so, it takes a standard action. You can issue
a different suggestion to each target.
