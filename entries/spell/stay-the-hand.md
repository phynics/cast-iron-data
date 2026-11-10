+++
id = "ref/spell/stay-the-hand"
kind = "spell"
title = "Stay the Hand"
aon = "SpellDisplay.aspx?ItemName=Stay%20the%20Hand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stay_the_hand", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "246"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Paladin", level = 4 },
]
casting_time = "1 immediate action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level and special; see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Paladin
Casting time: 1 immediate action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level and special; see text
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You cause a creature's arm to waver and prevent it from striking another creature. You can cast this
spell when the target is about to make a melee attack against another creature. On a failed saving
throw, the target does not follow through with its attack, and its entire action is wasted for the
round. On a successful saving throw, the target can make its attack, forcing its strike though the
compulsion but losing both accuracy and power, taking a -5 penalty on its attack and damage rolls.
Whether or not the target makes its initial save or not, it is subject to a -2 penalty on attack and
damage rolls against the creature it originally targeted for the duration of the spell.
