+++
id = "ref/spell/eyebite"
kind = "spell"
title = "Eyebite"
aon = "SpellDisplay.aspx?ItemName=Eyebite"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eyebite", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "280"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "pain"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Alchemist, Arcanist, Bard, Investigator, Mesmerist, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature
Descriptors: emotion, pain
:::

Each round, you can target a single living creature, striking it with waves of power. Depending on
the target's HD, this attack has as many as three effects.

|HD|Effect|
| --- | --- |
|10 or more|Sickened|
|5-9|Panicked, sickened|
|4 or less|Comatose, panicked, sickened|

The effects are cumulative and concurrent.

_Sickened:_ Sudden pain and fever sweeps over the subject's body. A creature affected by this spell
remains sickened for 10 minutes per caster level. The effects cannot be negated by a
[remove disease](ref/spell/remove-disease) or [heal](ref/spell/heal) spell, but a
[remove curse](ref/spell/remove-curse) is effective.

_Panicked:_ The subject becomes panicked for 1d4 rounds. Even after the panic ends, the creature
remains shaken for 10 minutes per caster level, and it automatically becomes panicked again if it
comes within sight of you during that time. This is a fear effect.

_Comatose:_ The subject falls into a catatonic coma for 10 minutes per caster level. During this
time, it cannot be awakened by any means short of dispelling the effect. This is not a sleep effect,
and thus elves are not immune to it.

You must spend a swift action each round after the first to target a foe.
