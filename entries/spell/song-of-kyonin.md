+++
id = "ref/spell/song-of-kyonin"
kind = "spell"
title = "Song of Kyonin"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "song_of_kyonin", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "60"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to 3 creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level or until performance ends or changes (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until performance ends or changes (see text)
Saving throw: none
Spell resistance: no
Targets: up to 3 creatures, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

Certain elven bards of Kyonin are known for the restorative power of their performances-mostly as a
result of this spell. You must have a bardic performance in effect to cast this spell (although this
spell is called song of Kyonin, the bardic performance need not be singing). As long as that
performance continues, up to 3 creatures affected by the performance gain
[fast healing](ref/umr/fast-healing) 2. When this bardic performance ends or you change to a
different bardic performance, the fast healing granted by this spell ends as well, but all creatures
affected by this spell heal 1d8 points of damage + 1 point per caster level (maximum +15) and are
cured of any of the following conditions: exhausted, fatigued, nauseated, paralyzed, sickened, or
stunned.
