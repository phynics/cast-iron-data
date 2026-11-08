+++
id = "ref/spell/hollow-heroism"
kind = "spell"
title = "Hollow Heroism"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hollow_heroism", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heroism" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Medium, Skald\
3: Alchemist, Arcanist, Bloodrager, Inquisitor, Investigator, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Hollow Heroism

**Sources:** Ultimate Intrigue pg 216

This spell functions as [heroism](ref/spell/heroism), except that you can reverse the spell by
issuing a special command as a standard action if you are within medium range (100 feet + 10 feet
per caster level) of the target. The target loses the bonuses and instead takes a -2 penalty on
attack rolls, saving throws, and skill checks until the spell's duration ends (no save).

Attempts to identify hollow heroism with a skill check incorrectly identify it as heroism.
