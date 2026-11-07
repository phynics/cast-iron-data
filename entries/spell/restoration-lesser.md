+++
id = "ref/spell/restoration-lesser"
kind = "spell"
title = "Lesser Restoration"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restoration_lesser", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "3 rounds"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Paladin\
2: Alchemist, Cleric, Druid, Hunter, Inquisitor, Investigator, Mesmerist, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 3 rounds
Components: V, S
Range: touch
Target: creature touched
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
:::

## Restoration

**Sources:** PRPG Core Rulebook pg 334

This spell functions like lesser restoration, except that it also dispels temporary negative levels
or one permanent negative level. If this spell is used to dispel a permanent negative level, it has
a material component of diamond dust worth 1,000 gp. This spell cannot be used to dispel more than
one permanent negative level possessed by a target in a 1-week period.

Restoration cures all temporary ability damage, and it restores all points permanently drained from
a single ability score (your choice if more than one is drained). It also eliminates any fatigue or
exhaustion suffered by the target.

### Greater Restoration

**Sources:** PRPG Core Rulebook pg 334

This spell functions like lesser restoration, except that it dispels all permanent and temporary
negative levels afflicting the healed creature. Greater restoration also dispels all magical effects
penalizing the creature's abilities, cures all temporary ability damage, and restores all points
permanently drained from all ability scores. It also eliminates fatigue and exhaustion, and removes
all forms of insanity, confusion, and similar mental effects.

### Lesser Restoration

**Sources:** PRPG Core Rulebook pg 334

Lesser restoration dispels any magical effects reducing one of the subject's ability scores or cures
1d4 points of temporary ability damage to one of the subject's ability scores. It also eliminates
any fatigue suffered by the character, and improves an exhausted condition to fatigued. It does not
restore permanent ability drain.
