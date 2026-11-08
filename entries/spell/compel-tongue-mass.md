+++
id = "ref/spell/compel-tongue-mass"
kind = "spell"
title = "Mass Compel Tongue"
source_ids = ["advanced-players-guide", "black-markets", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compel_tongue_mass", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/compel-tongue" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a wooden block carved with a letter)"
range = "touch"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Bard, Skald\
5: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a wooden block carved with a letter)
Range: touch
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
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

This spell functions as share language, granting a creature the ability to read, understand, and
communicate to the best of its ability in any one language you know. For the spell's entire
duration, the target can speak and write only in the language imparted, but its ability to
understand other languages is unaffected.

### Communal Share Language

**Sources:** Ultimate Combat pg 243

This spell functions like share language, except you divide the duration in 1-hour increments among
the creatures touched.

### Mass Compel Tongue

**Sources:** Black Markets pg 24

This spell functions as [compel tongue](ref/spell/compel-tongue), except it affects multiple
creatures. The same language restriction applies to all creatures, and the same language must be
imparted to all creatures affected by the same casting on this spell.
