+++
id = "ref/spell/heretics-tongue"
kind = "spell"
title = "Heretic's Tongue"
source_ids = ["pathfinder-107-scourge-of-the-godclaw"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heretics_tongue", path = "json/spells5.json" },
]
[[sources]]
publication = "pathfinder-107-scourge-of-the-godclaw"
page = "72"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Mesmerist", level = 6 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Cleric, Inquisitor, Oracle, Warpriest\
6: Mesmerist
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: living creature
Descriptors: mind-affecting
:::

> _Priests of [Geryon](ref/faith/geryon) have access to the following spell._

You fill your target's mind with blasphemous knowledge. If the target fails its saving throw, it
cannot cast spells or use [spell-like abilities](ref/umr/spell-like-abilities) for the duration of
the spell. Divine spellcasters whose power derives from the worship of a single deity (most clerics,
paladins, and warpriests) have the potential to suffer worse. When targeting a divine spellcaster,
you can designate an alignment. If the named alignment coincides with either the spellcaster's
alignment or that of her deity, the divine spellcaster loses access to all supernatural and
spell-like class abilities granted by the associated class for the spell's duration-blessings,
domain powers, channel energy, smite evil, etc.

Those affected by this spell can end the effect early by choosing to release the blasphemies in a
litany of screamed curses and heretical decadences. The creature is effectively paralyzed for half
the spell's duration, and each ally within 50 feet must succeed at a Will saving throw (equal to
this spell's save DC) or be shaken until the litany ends. If the creature chooses to do this, it
cannot end the litany of blasphemies early. A creature that succeeds at its saving throw to avoid
being shaken by its ally's blasphemous litany is immune to the litany's effects and need not attempt
additional saves on subsequent rounds.
