+++
id = "ref/spell/curse-of-the-outcast"
kind = "spell"
title = "Curse of the Outcast"
aon = "SpellDisplay.aspx?ItemName=Curse%20of%20the%20Outcast"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_the_outcast", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "209"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "emotion", "mind-affecting"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of earthworms)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Inquisitor, Mesmerist\
5: Skald\
6: Cleric, Oracle, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a handful of earthworms)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, emotion, mind-affecting
:::

Everything about the target seems off-putting and grating, and everyone he meets is compelled to see
the worst in him. Whenever the target attempts a Bluff, Diplomacy, Intimidate, or Perform check, he
must roll twice and take the lower result.

Additionally, each creature he encounters has its initial attitude toward him reduced by one step
(helpful becomes friendly, friendly becomes indifferent, and so on).
