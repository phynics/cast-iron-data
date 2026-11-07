+++
id = "ref/spell/guardian-monument-lesser"
kind = "spell"
title = "Lesser Guardian Monument"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_monument_lesser", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
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
Level: 3: Arcanist, Bard, Inquisitor, Magus, Occultist, Paladin, Psychic, Skald, Sorcerer, Witch, Wizard\
4: Shaman
Casting time: 1 full-round action
Components: V, S, F (an unattended, nonmagical object)
Range: touch
Area: 40-ft. radius from touched object or 60-ft. radius from touched object; see text
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

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

This spell functions as lesser guardian monument, except it grants DR 4/magic.
