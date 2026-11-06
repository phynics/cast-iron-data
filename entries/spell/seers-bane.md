+++
id = "ref/spell/seers-bane"
kind = "spell"
title = "Seer's Bane"
source_ids = ["pathfinder-102-breaking-the-bones-of-hell"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seers_bane", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 round
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: creature or object touched
:::

**Sources:** Pathfinder \#102: Breaking the Bones of Hell pg 75

> _Priests of [Mephistopheles](ref/faith/mephistopheles) have access to the following spell._

This spell functions as [nondetection](ref/spell/nondetection), except that those who cast
divination spells targeting the warded creature or item must succeed on a caster level check (DC =
15 + your caster level). If the caster of the divination fails, deadly magical feedback strikes at
him, dealing 1d6 points of electricity damage per 2 caster levels you have (maximum 10d6 at 20th
level).

Alternatively, if you cast bestow curse, chaos hammer, contagion, holy smite, order's wrath, poison,
or unholy blight in the round immediately following seer's bane, you can replace the spell's
damaging effect with the effects of that second spell (the divination's caster - and potentially
those around him - save as normal for the modifying spell).
