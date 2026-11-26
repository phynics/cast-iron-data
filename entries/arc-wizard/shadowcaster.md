+++
id = "ref/arc-wizard/shadowcaster"
kind = "archetype"
title = "Shadowcaster"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Shadowcaster"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadowcaster", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "inner-sea-magic"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "shadow-spells", level = 1 },
  { anchor = "shadowsight", level = 5 },
  { anchor = "shadowy-specialization", level = 10 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["shadow-spells"] },
  { replaces = "5th-level bonus feat", feature = "bonus-feats", levels = [5], by = ["shadowsight"] },
  { replaces = "10th-level bonus feat", feature = "bonus-feats", levels = [10], by = ["shadowy-specialization"] },
]
+++

Trained in the dark mysteries of Nidal's Umbral Court and its Kuthonite dogma, your training allows
you to harness the power of shadows to bolster your spellcasting. A shadowcaster has the following
class features.

## Shadow Spells (Su) {#shadow-spells}

At 1st level, a shadowcaster uses his shadow to prepare additional spells. He must spend his entire
period of spell preparation in [dim illumination](ref/rule/vision-and-light) to use this ability. He
may prepare a number of additional spell levels of spells equal to the level of the highest-level
wizard spell he can cast. For example, if he can cast 6th-level wizard spells, he could prepare six
1st-level spells, two 3rd level-spells, or any similar combination that adds up to a total of six
spell levels. These spells are stored in his shadow. He can only cast these spells when he is in an
area of normal light or dim light. He gains Shadowtongue as a bonus language. This ability replaces
arcane bond.

## Shadowsight (Ex) {#shadowsight}

At 5th level, a shadowcaster gains [darkvision](ref/rule/darkvision) 60 feet. This ability replaces
the shadowcaster's 5th-level wizard bonus feat.

## Shadowy Specialization (Ex) {#shadowy-specialization}

At 10th level, when a shadowcaster casts _[shades](ref/spell/shades)_,
_[shadow conjuration](ref/spell/shadow-conjuration)_,
_[shadow evocation](ref/spell/shadow-evocation),_ and similar illusion spells that have a listed
fraction of the strength of real effects, he increases the percentage of damage caused by the
spell's effect or summoned creatures by one-fifth (+20%) against creatures that make their saving
throw against the effect, up to a maximum of 100% of the strength. For example,
_[shadow evocation](ref/spell/shadow-evocation)_ and
_[shadow conjuration](ref/spell/shadow-conjuration)_ deal 40% normal damage on a successful save
instead of 20%. This ability replaces the shadowcaster's 10th-level wizard bonus feat.
