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
  { class = "Adept", level = 4 },
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "3 rounds"
components = "V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)"
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
Level: 4: Adept, Alchemist, Cleric, Inquisitor, Investigator, Mesmerist, Oracle, Paladin, Shaman, Spiritualist, Warpriest
Casting time: 3 rounds
Components: V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
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
