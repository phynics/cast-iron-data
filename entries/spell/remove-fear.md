+++
id = "ref/spell/remove-fear"
kind = "spell"
title = "Remove Fear"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_fear", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "332"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature plus one additional creature per four levels, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes; see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Bard, Cleric, Inquisitor, Medium, Mesmerist, Oracle, Psychic, Shaman, Skald, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes; see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature plus one additional creature per four levels, no two of which can be more than 30 ft. apart
:::

You instill courage in the subject, granting it a +4 morale bonus against fear effects for 10
minutes. If the subject is under the influence of a fear effect when receiving the spell, that
effect is suppressed for the duration of the spell.

Remove fear counters and dispels [cause fear](ref/spell/cause-fear).
