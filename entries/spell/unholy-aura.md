+++
id = "ref/spell/unholy-aura"
kind = "spell"
title = "Unholy Aura"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unholy_aura", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["evil"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a tiny reliquary worth 500 gp)"
range = "20 ft."
effects = [
  { label = "Targets", value = "one creature/level in a 20-ft.-radius burst centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, F (a tiny reliquary worth 500 gp)
Range: 20 ft.
Duration: 1 round/level (D)
Saving throw: see text
Spell resistance: yes
Targets: one creature/level in a 20-ft.-radius burst centered on you
Descriptors: evil
:::

**Sources:** PRPG Core Rulebook pg 364

A malevolent darkness surrounds the subjects, protecting them from attacks, granting them resistance
to spells cast by good creatures, and weakening good creatures when they strike the subjects. This
abjuration has four effects.

First, each warded creature gains a +4 deflection bonus to AC and a +4 resistance bonus on saves.
Unlike the effect of [protection from good](ref/spell/protection-from-good), this benefit applies
against all attacks, not just against attacks by good creatures.

Second, a warded creature gains SR 25 against good spells and spells cast by good creatures.

Third, the abjuration protects the subjects from possession and mental influence, just as protection
from good does.

Finally, if a good creature succeeds on a melee attack against a warded creature, the offending
attacker takes 1d6 points of Strength damage (Fortitude negates).
