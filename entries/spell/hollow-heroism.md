+++
id = "ref/spell/hollow-heroism"
kind = "spell"
title = "Hollow Heroism"
aon = "SpellDisplay.aspx?ItemName=Hollow%20Heroism"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hollow_heroism", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heroism" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "216"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting", "ruse"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Medium, Skald\
4: Arcanist, Bloodrager, Inquisitor, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: compulsion
Descriptors: mind-affecting, ruse
:::

### Hollow Heroism

This spell functions as [heroism](ref/spell/heroism), except that you can reverse the spell by
issuing a special command as a standard action if you are within medium range (100 feet + 10 feet
per caster level) of the target. The target loses the bonuses and instead takes a -2 penalty on
attack rolls, saving throws, and skill checks until the spell's duration ends (no save).

Attempts to identify hollow heroism with a skill check incorrectly identify it as heroism.
