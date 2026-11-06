+++
id = "ref/spell/secret-sign"
kind = "spell"
title = "Secret Sign"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_sign", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a lemon peel)"
range = "touch"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "1 day/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Bard, Inquisitor, Shaman, Skald\
2: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a lemon peel)
Range: touch
Duration: 1 day/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one creature or object
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Black Markets pg 25

You invisibly inscribe a small mark or short message (no more than 25 words) on a creature or
object, similar to the way arcane mark works. The sign can be no more than 6 inches across, and if
it's a written message, it can be in any language you can read and write at the time of the spell's
casting. As you cast the spell, you can define one auditory, olfactory, tangible, or visual
criterion - such as all creatures wearing green bands on their left arms or only creatures who smell
of lavender or only orcs - that allows designated creatures within 30 feet to see the secret sign.

Disguises and illusions that mimic the set criterion can fool this spell. Normal darkness doesn't
conceal a visual trigger, but magical darkness or invisibility does. Auditory criteria (such as a
password) and tangible criteria (such as pressing your hand against a specific object or wall) can
be performed by anyone who learns of them. A secret sign cannot distinguish alignment, level, Hit
Dice, or class except by external garb, but can differentiate apparent races, genders, and garments.
See invisibility and invisibility purge reveal the sign, but glitterdust does not.

A caster of at least 10th level can make secret sign permanent on an object with a
[permanency](ref/spell/permanency) spell using 5,000 gp of diamond dust as a material component.
