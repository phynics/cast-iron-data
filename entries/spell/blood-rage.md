+++
id = "ref/spell/blood-rage"
kind = "spell"
title = "Blood Rage"
source_ids = ["orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_rage", path = "json/spells2.json" },
]
[[sources]]
publication = "orcs-of-golarion"
page = "28"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood from each creature to be affected)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing living creature per 2 levels, no two of which may be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald\
3: Adept, Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of blood from each creature to be affected)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one willing living creature per 2 levels, no two of which may be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

The targets of this spell become angrier as they fight, the pain of their wounds fueling their
strength. An affected creature gains a cumulative +2 morale bonus to Strength and a cumulative -1
penalty to AC for every 5 points of damage it takes (maximum +10 Strength, -5 AC) for the duration
of the spell. These bonuses last until the spell expires or the target falls unconscious.
