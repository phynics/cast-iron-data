+++
id = "ref/spell/cloak-of-chaos"
kind = "spell"
title = "Cloak of Chaos"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloak_of_chaos", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["chaotic"]
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
Descriptors: chaotic
:::

**Sources:** PRPG Core Rulebook pg 255

A random pattern of color surrounds the subjects, protecting them from attacks, granting them
resistance to spells cast by lawful creatures, and causing lawful creatures that strike the subjects
to become confused. This abjuration has four effects.

First, each warded creature gains a +4 deflection bonus to AC and a +4 resistance bonus on saves.
Unlike [protection from law](ref/spell/protection-from-law), the benefit of this spell applies
against all attacks, not just against attacks by lawful creatures.

Second, each warded creature gains [spell resistance](ref/rule/spell-resistance) 25 against lawful
spells and spells cast by lawful creatures.

Third, the abjuration protects from possession and mental influence, just as protection from law
does.

Finally, if a lawful creature succeeds on a melee attack against a warded creature, the offending
attacker is confused for 1 round (Will save negates, as with the confusion spell, but against the
save DC of cloak of chaos).
