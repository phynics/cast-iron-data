+++
id = "ref/spell/terrible-remorse"
kind = "spell"
title = "Terrible Remorse"
aon = "SpellDisplay.aspx?ItemName=Terrible%20Remorse"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terrible_remorse", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "243"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 living creature" },
]
duration = "1 round/level"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Inquisitor, Mesmerist, Skald\
4: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial (see text)
Spell resistance: yes
Target: 1 living creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill a target with such profound remorse that it begins to harm itself. Each round, the target
must save or deal 1d8 points of damage + its Strength modifier to itself using an item held in its
hand or with unarmed attacks. If the creature saves, it is staggered for 1 round and takes a -2
penalty to Armor Class, after which the spell ends.
