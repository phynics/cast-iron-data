+++
id = "ref/arc-bloodrager/untouchable-rager"
kind = "archetype"
title = "Untouchable Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Untouchable%20Rager"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "untouchable_rager", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "85"

[fields]
kind = "archetype"
features = [
  { anchor = "raging-resistance", level = 4 },
  { anchor = "resistance-control", level = 14 },
]
trades = [
  { replaces = "Spells", feature = "spells", by = ["raging-resistance"] },
  { replaces = "blood casting", feature = "blood-casting", by = ["raging-resistance"] },
  { replaces = "eschew materials", feature = "eschew-materials", by = ["raging-resistance"] },
  { replaces = "bloodline spells", feature = "bloodline", power = "bloodline spell", by = ["raging-resistance"] },
]
+++

While most bloodragers are known for their inexplicable ability to focus their bloodline into a
horrifying mix of martial terror and spellcasting fury, from time to time a bloodrager's bloodline
acts differently. Instead of empowering the bloodrager, it shields the bloodrager from magic of all
types, often keeping the bloodrager untouched within the midst of magical effects.

## Raging Resistance (Ex) {#raging-resistance}

At 4th level, instead of gaining spells, a bloodrager becomes resistant to spells. While
bloodraging, he gains [spell resistance](ref/rule/spell-resistance) equal to 8 + his bloodrager
level. Unlike normal [spell resistance](ref/rule/spell-resistance), the untouchable rager's spell
resistance cannot be voluntarily lowered. As long as the untouchable is bloodraging, the spell
resistance is persistent, and can only be lowered by ending the bloodrage. At 7th, 10th, 13th, and
16th levels (when other bloodragers would gain bloodline spells), an untouchable rager's spell
resistance from raging resistance is increased by 1. This ability replaces the spells, blood
casting, eschew materials, and bloodline spells class features.

## Resistance Control (Ex) {#resistance-control}

At 14th level, an untouchable rager gains the [spell resistance](ref/rule/spell-resistance) from
raging resistance even while not in a bloodrage. Additionally, as long as the untouchable rager
isn't bloodraging, he can turn off this spell resistance.
