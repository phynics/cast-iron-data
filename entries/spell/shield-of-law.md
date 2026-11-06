+++
id = "ref/spell/shield-of-law"
kind = "spell"
title = "Shield of Law"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_law", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["lawful"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a reliquary worth 500 gp)"
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
Components: V, S, F (a reliquary worth 500 gp)
Range: 20 ft.
Duration: 1 round/level (D)
Saving throw: see text
Spell resistance: yes
Targets: one creature/level in a 20-ft.-radius burst centered on you
Descriptors: lawful
:::

**Sources:** PRPG Core Rulebook pg 342

A dim, blue glow surrounds the subjects, protecting them from attacks, granting them resistance to
spells cast by chaotic creatures, and slowing chaotic creatures when they strike the subjects. This
abjuration has four effects.

First, each warded creature gains a +4 deflection bonus to AC and a +4 resistance bonus on saves.
Unlike [protection from chaos](ref/spell/protection-from-chaos), this benefit applies against all
attacks, not just against attacks by chaotic creatures.

Second, a warded creature gains [spell resistance](ref/rule/spell-resistance) 25 against chaotic
spells and spells cast by chaotic creatures.

Third, the abjuration protects you from possession and mental influence, just as protection from
chaos does.

Finally, if a chaotic creature succeeds on a melee attack against a warded creature, the attacker is
slowed (Will save negates, as the [slow](ref/spell/slow) spell, but against shield of law's save
DC).
