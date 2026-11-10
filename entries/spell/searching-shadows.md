+++
id = "ref/spell/searching-shadows"
kind = "spell"
title = "Searching Shadows"
aon = "SpellDisplay.aspx?ItemName=Searching%20Shadows"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "searching_shadows", path = "json/spells15.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "62"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "shadows in a 10-foot-radius spread" },
]
duration = "concentration"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: concentration
Saving throw: Reflex partial
Spell resistance: yes
Effect: shadows in a 10-foot-radius spread
Subschool: Shadow
Descriptors: shadow
:::

Strands of shadow probe an area, searching for a creature or object you specify by shape, size, or
texture. Each round, the shadows attempt a Perception check on the squares they touch with a total
bonus equal to your caster level + your Charisma or Intelligence modifier, whichever is higher. You
can move the shadows up to 30 feet or change the search criteria as part of concentrating on the
spell. Whenever the shadows come into contact with a creature with
[spell resistance](ref/rule/spell-resistance), you must attempt a caster level check to overcome its
spell resistance. If you fail, the spell ends.

When the shadows locate a desired item or creature, you are aware of its shape and size and can
order the shadows to try to seize it. If the shadows are seeking a creature, the area they cover
becomes difficult terrain for that creature, and the creature must succeed at a Reflex saving throw
or become entangled and unable to move. Changing the criteria of the creature or object sought or
moving the shadows away from an entangled target frees it. If the target is an object carried by a
creature, the shadows attempt a disarm or steal combat maneuver check as appropriate, using the same
modifier as for their Perception check. The shadows can pick up and move unattended, nonmagical
objects that weigh up to 5 pounds.
