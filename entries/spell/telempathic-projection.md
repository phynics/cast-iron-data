+++
id = "ref/spell/telempathic-projection"
kind = "spell"
title = "Telempathic Projection"
aon = "SpellDisplay.aspx?ItemName=Telempathic%20Projection"
source_ids = ["occult-adventures", "occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telempathic_projection", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "188"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Spiritualist", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Mesmerist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You alter the target's mood, adjusting its attitude toward you or another creature you designate by
one step either positively or negatively (see the [Diplomacy skill](ref/skill/diplomacy)). You can
instead use this spell to assist your own or an ally's Bluff, Diplomacy, Intimidate, Perform, or
Sense Motive check, granting that check a +5 insight bonus against the target of your telempathic
projection with no save. In this case, the spell's duration expires immediately when the skill check
is complete.
