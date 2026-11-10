+++
id = "ref/spell/disrupt-silence"
kind = "spell"
title = "Disrupt Silence"
aon = "SpellDisplay.aspx?ItemName=Disrupt%20Silence"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disrupt_silence", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "212"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "S, M (tiny silver bell, chime, or gong)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on a creature, object, or point in space" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Bard, Skald\
3: Cleric, Inquisitor, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: S, M (tiny silver bell, chime, or gong)
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 10-ft.-radius emanation centered on a creature, object, or point in space
:::

You suppress magical sound-dampening effects within the area. Disrupt silence temporarily negates
magical silence within its area, so that normal sounds can be heard within the overlapping areas of
effect. Additionally, disrupt silence can automatically counter or dispel any magical silence effect
of equal or lower level cast upon the same target, such as silence. If you cast disrupt silence on
the target of a higher-level silence effect, it functions as [dispel magic](ref/spell/dispel-magic)
instead of its normal function.
