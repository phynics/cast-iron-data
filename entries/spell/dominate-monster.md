+++
id = "ref/spell/dominate-monster"
kind = "spell"
title = "Dominate Monster"
aon = "SpellDisplay.aspx?ItemName=Dominate%20Monster"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dominate_monster", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dominate-person" },
]
[[sources]]
publication = "core-rulebook"
page = "274"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Summoner\
9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions like [dominate person](ref/spell/dominate-person), except that the spell is not
restricted by creature type.
