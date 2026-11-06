+++
id = "ref/spell/lissalan-snake-sigil"
kind = "spell"
title = "Lissalan Snake Sigil"
source_ids = ["pathfinder-65-into-the-nightmare-rift"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lissalan_snake_sigil", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "multiple (see text)"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered amber worth 500 gp and a snake scale)"
range = "touch"
effects = [
  { label = "Target", value = "one touched book or written work" },
]
duration = "permanent or until discharged; 1 day/level; see text"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: multiple (see text)
Level: 3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S, M (powdered amber worth 500 gp and a snake scale)
Range: touch
Duration: permanent or until discharged; 1 day/level; see text
Saving throw: Reflex negates
Spell resistance: no
Target: one touched book or written work
:::

**Sources:** Pathfinder \#65: Into the Nightmare Rift pg 75

> _Priests of [Lissala](ref/faith/lissala) have access to the following spell._

There are seven variants of this spell, one for each of the Thassilonian schools of magic. Each
functions like [sepia snake sigil](ref/spell/sepia-snake-sigil) (and counts as that spell for the
purpose of combining other spells that hide or garble text), except instead of trapping the subject,
the triggered sigil's effect depends on this spell's school. This effect lasts for 1 day/level. This
is a curse effect that can be removed via [remove curse](ref/spell/remove-curse).

_Abjuration:_ All beneficial magical effects on the target last half as long as normal.

_Conjuration:_ The target is nauseated. This is a poison effect.

_Enchantment:_ The target takes a 1d6 penalty to Intelligence, Wisdom, and Charisma. This is a
compulsion effect.

_Evocation:_ The target gains vulnerability to an energy type, chosen randomly from the following:
acid, cold, electricity, or fire. This is an acid, cold, electricity, or fire effect.

_Illusion:_ The target's vision is blurred, giving it a -4 penalty on Perception checks relating to
vision, and the target treats all other creatures as having displacement. This is a glamer effect.

_Necromancy:_ The target is exhausted. This condition cannot be removed with rest.

_Transmutation:_ Target is affected by slow.
