+++
id = "ref/spell/bite-the-hand-mass"
kind = "spell"
title = "Mass Bite the Hand"
aon = "SpellDisplay.aspx?ItemName=Bite%20the%20Hand%2C%20Mass"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bite_the_hand_mass", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bite-the-hand" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "57"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature summoned by a spell or spell-like ability/ level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Druid, Hunter, Inquisitor, Summoner, Unchained Summoner\
7: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Target: one creature summoned by a spell or spell-like ability/ level, no two of which can be more than 30 ft. apart
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
:::

### Mass Bite the Hand

This spell functions like [bite the hand](ref/spell/bite-the-hand), except as noted above. The
target creatures do not need to have all been summoned by the same being.
