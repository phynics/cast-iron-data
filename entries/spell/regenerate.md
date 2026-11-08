+++
id = "ref/spell/regenerate"
kind = "spell"
title = "Regenerate"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "regenerate", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 9 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "3 rounds"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Cleric, Oracle, Shaman, Witch\
9: Druid
Casting time: 3 rounds
Components: V, S, DF
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Healing
:::

**Sources:** PRPG Core Rulebook pg 331

The subject's severed body members (fingers, toes, hands, feet, arms, legs, tails, or even heads of
multiheaded creatures), broken bones, and ruined organs grow back. After the spell is cast, the
physical regeneration is complete in 1 round if the severed members are present and touching the
creature. It takes 2d10 rounds otherwise.

Regenerate also cures 4d8 points of damage + 1 point per caster level (maximum +35), rids the
subject of exhaustion and fatigue, and eliminates all nonlethal damage the subject has taken. It has
no effect on nonliving creatures (including undead).
