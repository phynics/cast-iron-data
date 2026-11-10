+++
id = "ref/spell/jealous-rage"
kind = "spell"
title = "Jealous Rage"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jealous_rage", path = "json/spells6.json" },
]
[[sources]]
publication = "occult-origins"
page = "28"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Bloodrager, Bard, Mesmerist, Skald, Spiritualist\
3: Psychic, Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: no
Target: one living creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill the target with a sense of entitled self-importance, making the subject unable to bear the
indignity of another creature getting something that it doesn't have. Whenever an ally of the target
receives a harmless spell or [spell-like ability](ref/umr/spell-like-abilities), beneficial
supernatural effect, or assisting action (including the aid another action, first aid using the Heal
skill, etc.) that doesn't also include the target, the target is driven into a murderous rage
against either the producer of that effect or the nearest creature that benefited from that effect,
whichever is closer. The target must attack that creature on its next turn. Any ability that deals
lethal damage is considered an attack for this purpose. Once the target deals lethal damage to the
object of his jealous rage, the compulsion to attack that creature ends.
