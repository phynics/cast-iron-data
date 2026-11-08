+++
id = "ref/spell/share-language-communal"
kind = "spell"
title = "Communal Share Language"
source_ids = ["advanced-players-guide", "black-markets", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "share_language_communal", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/share-language" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a page from a dictionary)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Medium, Mesmerist, Psychic, Skald\
2: Arcanist, Cleric, Druid, Hunter, Occultist, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a page from a dictionary)
Range: touch
Duration: 24 hours
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

## Share Language

**Sources:** Advanced Player's Guide pg 243

You can share your facility for one particular language with another creature. For 24 hours the
target can read, understand, and communicate to the best of its ability in any one language which
you already know. For every 5 levels you possess, you can grant the use of another language you
know, to a maximum of 5 languages at 20th level. The target must have the physical capacity to
articulate sounds, make gestures, or engage in whatever other method speakers of the language use to
communicate with each other in order to actually converse. If the target lacks the mental capacity
to grasp an actual language it still gains enough knowledge to respond to and carry out even
extremely complex commands or suggestions coached in the language (whether written or spoken).
However, since this spell does not endow the target with greater reasoning capacity, merely a
temporarily enhanced vocabulary, the person offering up instructions to non-sentient creatures must
take care to remove any ambiguity or guesswork.

Similarly, this spell does not affect the basic nature of the target, or its disposition toward you
or anyone else, so convincing it to actually carry out these instructions could require negotiation,
threats, or outright bribery.

### Compel Tongue

**Sources:** Black Markets pg 24

This spell functions as [share language](ref/spell/share-language), granting a creature the ability
to read, understand, and communicate to the best of its ability in any one language you know. For
the spell's entire duration, the target can speak and write only in the language imparted, but its
ability to understand other languages is unaffected.

### Communal Share Language

**Sources:** Ultimate Combat pg 243

This spell functions like share language, except you divide the duration in 1-hour increments among
the creatures touched.

### Mass Compel Tongue

**Sources:** Black Markets pg 24

This spell functions as compel tongue, except it affects multiple creatures. The same language
restriction applies to all creatures, and the same language must be imparted to all creatures
affected by the same casting on this spell.
