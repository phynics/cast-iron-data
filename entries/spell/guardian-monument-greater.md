+++
id = "ref/spell/guardian-monument-greater"
kind = "spell"
title = "Greater Guardian Monument"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_monument_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/guardian-monument-lesser" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 full-round action"
components = "V, S, F (an unattended, nonmagical object)"
range = "touch"
effects = [
  { label = "Area", value = "40-ft. radius from touched object or 60-ft. radius from touched object; see text" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Bard, Inquisitor, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 full-round action
Components: V, S, F (an unattended, nonmagical object)
Range: touch
Area: 40-ft. radius from touched object or 60-ft. radius from touched object; see text
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

## Lesser Guardian Monument

**Sources:** Arcane Anthology pg 8

You touch an unattended, nonmagical object to create a touchstone for humans defending the area.
Such human defenders are protected by a shimmering aura as long as they are in the area. The spell
grants each subject [damage reduction](ref/rule/damage-reduction) 2/magic. Humans who leave the area
and reenter regain the damage reduction. The spell is suppressed if the object is moved from its
place, but resumes if the object is put back. Its duration continues to elapse while it is
suppressed this way.

Normally, the area of effect is 40 feet from the touched object. If the touched object is a monument
to human achievement, the area increases to a 60-foot radius.

### Greater Guardian Monument

**Sources:** Arcane Anthology pg 9

This spell functions as [lesser guardian monument](ref/spell/guardian-monument-lesser), except it
grants DR 4/magic.
