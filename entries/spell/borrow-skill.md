+++
id = "ref/spell/borrow-skill"
kind = "spell"
title = "Borrow Skill"
aon = "SpellDisplay.aspx?ItemName=Borrow%20Skill"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "borrow_skill", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "207"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "up to 1 round/level (see description)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Bard, Medium, Psychic, Skald
Casting time: 1 standard action
Components: S
Range: touch
Duration: up to 1 round/level (see description)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You borrow one of the target's known skills. After touching the subject, you can make a single check
with the chosen skill using the subject's skill ranks, but modified by your own key ability. If you
take longer than the spell's duration to make the check or the check requires more time, then it
fails and you must use your own skill ranks (if any). If the borrowed skill is a class skill for
you, you gain the +3 bonus on checks using that skill.
