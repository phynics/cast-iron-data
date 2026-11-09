+++
id = "ref/spell/absorbing-inhalation"
kind = "spell"
title = "Absorbing Inhalation"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorbing_inhalation", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one cloud-like effect, up to one 10-ft. cube/level" },
]
duration = "1 round/level; see text"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Bloodrager, Druid, Hunter, Investigator, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level; see text
Saving throw: see text
Spell resistance: no
Target: one cloud-like effect, up to one 10-ft. cube/level
Descriptors: air
:::

> _[Sylphs](ref/race/sylph) have access to the following spell._

You grant your lungs inhuman strength and capacity, allowing you to harmlessly and completely inhale
one gas, fog, smoke, mist, or similar cloud-like effect. If the targeted cloud is a magical effect,
you must succeed at a caster level check (DC 11 + the effect's caster level) to inhale it. Inhaling
the cloud removes it from the area, leaving normal air in its place. If the cloud is too large for
you to affect with a single casting of this spell, you may instead inhale a portion of the cloud,
but you must inhale the portion of the cloud closest to you. This spell has no effect on gaseous
creatures. It can only affect an instantaneous-duration cloud (such as a breath weapon) if you ready
an action to cast the spell in response.

While inhaled, the cloud does not harm you. You may keep the cloud harmlessly contained within you
for up to 1 round per level, but you must [hold your breath](ref/misc/hold-your-breath) to do so
(even if you do not normally have to breathe). If the cloud has a duration, the time the cloud is
contained within you counts toward that duration. As a standard action, you may release the stored
cloud as a breath weapon, filling a 60-foot cone (or the cloud's original area, if smaller than a
60-foot cone). Any creature in the breath's area is subject to its normal effects, making saving
throws and [spell resistance](ref/rule/spell-resistance) checks as appropriate against the cloud's
original DC. The exhaled cloud resumes its duration, if any. Exhaling the stored cloud ends this
spell. If you do not exhale the cloud before this spell's duration expires, you suffer the cloud's
effects and automatically fail any saving throw to resist it.
