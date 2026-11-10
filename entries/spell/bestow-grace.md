+++
id = "ref/spell/bestow-grace"
kind = "spell"
title = "Bestow Grace"
aon = "SpellDisplay.aspx?ItemName=Bestow%20Grace"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_grace", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "205"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Paladin", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "one good creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will (harmless)
Spell resistance: yes
Target: one good creature touched
:::

With this spell you can bestow your divine grace on another good creature for a short amount of
time, infusing that creature with a portion of your holy virtue. When you touch the subject, you
grant that creature a sacred bonus to its saving throws equal to its Charisma bonus (if any) on all
saving throws.
