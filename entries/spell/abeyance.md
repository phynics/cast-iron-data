+++
id = "ref/spell/abeyance"
kind = "spell"
title = "Abeyance"
aon = "SpellDisplay.aspx?ItemName=Abeyance"
source_ids = ["pathfinder-82-secrets-of-the-sphinx"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abeyance", path = "json/spells.json" },
]
[[sources]]
publication = "pathfinder-82-secrets-of-the-sphinx"
page = "74"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 minute"
components = "V, S, DF, M (a flask of holy water worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 minute
Components: V, S, DF, M (a flask of holy water worth 25 gp)
Range: touch
Duration: 24 hours
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

Abeyance suppresses the effects of a single curse on a creature. It does not restore any damage or
drain that might have been caused by the curse. Abeyance cannot suppress curses that cannot be
removed by [remove curse](ref/spell/remove-curse), but it can suppress curses such as lycanthropy
that require remove curse along with additional measures. An individual curse can be suppressed only
once by abeyance, even if cast by a different caster.

Abeyance does not allow a creature to divest itself of cursed objects, though it can suppress a
curse contracted from an object.
