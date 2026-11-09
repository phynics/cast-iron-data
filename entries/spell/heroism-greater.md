+++
id = "ref/spell/heroism-greater"
kind = "spell"
title = "Greater Heroism"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heroism_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/heroism" },
]
[[sources]]
publication = "core-rulebook"
page = "295"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 min./level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Skald, Summoner\
6: Arcanist, Psychic, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Target: creature touched
Duration: 1 min./level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Greater Heroism

This spell functions like [heroism](ref/spell/heroism), except the creature gains a +4 morale bonus
on attack rolls, saves, and skill checks, immunity to fear effects, and temporary hit points equal
to your caster level (maximum 20).
