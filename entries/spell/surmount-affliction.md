+++
id = "ref/spell/surmount-affliction"
kind = "spell"
title = "Surmount Affliction"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "surmount_affliction", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Inquisitor, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Magic pg 241

You temporarily overcome one harmful condition. This does not end the effect causing the condition;
it just suspends that condition's effect for the duration of the spell. You can surmount any one of
the following conditions: blinded, confused, dazed, dazzled, deafened, fatigued, frightened,
paralyzed, shaken, or sickened.

### Mythic Surmount Affliction

**Sources:** Mythic Adventures pg 110\
You can cast this spell with no verbal or somatic component, and even if you're helpless (but not
unconscious). You temporarily overcome a number of additional harmful conditions equal to half your
tier.

_Augmented (7th):_ If you expend three uses of mythic power, you become immune to all afflictions
the spell can normally overcome. In addition, you overcome (but do not become immune to) one of the
following conditions: exhausted, nauseated, panicked, petrified, staggered, and stunned.
