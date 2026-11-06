+++
id = "ref/spell/protection-from-technology"
kind = "spell"
title = "Protection from Technology"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_technology", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a pinch of powdered copper)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless), see text"
spell_resistance = "no, see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a pinch of powdered copper)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless), see text
Spell resistance: no, see text
Target: creature touched
:::

**Sources:** Technology Guide pg 10

This spell wards a creature from attacks by technological objects and creatures of the robot
subtype, and protects against mental control from technological sources. It creates a magical
barrier around the subject at a distance of 1 foot. The barrier moves with the subject and has two
major effects.

First, the target gains a +2 deflection bonus to AC and a +2 resistance bonus on saving throws. Both
of these bonuses apply against attacks made or effects caused by technological objects and creatures
with the robot subtype.

Second, the target immediately receives another saving throw (if one was allowed to begin with)
against any technological effects that exercise mental control over the creature, including the
effects of pharmaceuticals such as torpinal. The target gains a +2 morale bonus on this saving
throw, using the same DC as the original effect. If the target succeeds at this save, such effects
are suppressed for the duration of this spell. The effects resume when the duration of this spell
expires. While under the effects of this spell, the target is immune to any new attempts to exercise
mental control over her using technological means.
