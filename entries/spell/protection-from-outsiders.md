+++
id = "ref/spell/protection-from-outsiders"
kind = "spell"
title = "Protection from Outsiders"
aon = "SpellDisplay.aspx?ItemName=Protection%20from%20Outsiders"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_outsiders", path = "json/spells15.json" },
]
[[sources]]
publication = "demon-hunters-handbook"
page = "26"

[fields]
kind = "spell"
school = "abjuration [see text]"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration \[see text\]
Level: 2: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

This spell wards a creature from attacks by outsiders with a specific racial subtype, from mental
control exerted by creatures of the chosen subtype, and from summoned creatures of that subtype.
Only the subtypes of specific outsider races - angel, azata, demon, oni, psychopomp, protean, and so
on - can be chosen as the subtype this spell protects against. Alignment subtypes or other general
subtypes (like elemental, extraplanar, or native) cannot be selected. Outsiders without an outsider
racial subtype (like genies, night hags, yeth hounds, or xills) are not affected by this spell.

This spell creates a magical barrier around the subject at a distance of 1 foot. The barrier moves
with the subject and has three major effects.

First, the subject gains a +4 deflection bonus to AC and a +4 resistance bonus on saves when
targeted by creatures of the chosen subtype.

Second, the subject immediately receives another saving throw (if one was allowed to begin with)
against any spells or effects that possess or exercise mental control over the target creature. This
functions in the same fashion as [protection from evil](ref/spell/protection-from-evil), but only
when the effect stems from outsiders of the chosen subtype, and the target's saving throw is made
with a +4 morale bonus (using the same DC as the original effect).

Third, the spell prevents bodily contact by summoned creatures of the chosen subtype in the same
manner as detailed in protection from evil.

This spell's descriptor varies depending on the outsider race selected, gaining the alignment
descriptors opposite to the alignment of the outsider race-for example, lawful and good if the race
is chaotic and evil, chaotic if the selected race is lawful, or none if the selected race is
neutral.
