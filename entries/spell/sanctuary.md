+++
id = "ref/spell/sanctuary"
kind = "spell"
title = "Sanctuary"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctuary", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "336"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Cleric, Inquisitor, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: no
Target: creature touched
:::

Any opponent attempting to directly attack the warded creature, even with a targeted spell, must
attempt a Will save. If the save succeeds, the opponent can attack normally and is unaffected by
that casting of the spell. If the save fails, the opponent can't follow through with the attack,
that part of its action is lost, and it can't directly attack the warded creature for the duration
of the spell. Those not attempting to attack the subject remain unaffected. This spell does not
prevent the warded creature from being attacked or affected by area of effect spells. The subject
cannot attack without breaking the spell but may use non-attack spells or otherwise act.
