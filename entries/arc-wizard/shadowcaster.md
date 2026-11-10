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
replaces = ["Arcane bond", "5th-level bonus feat", "10th-level bonus feat"]
+++

Trained in the dark mysteries of Nidal's Umbral Court and its Kuthonite dogma, your training allows
you to harness the power of shadows to bolster your spellcasting. A shadowcaster has the following
class features.

**Shadow Spells (Su)**

**Ability:** A shadowcaster uses his shadow to prepare additional spells. He must spend his entire
period of spell preparation in [dim illumination](ref/rule/vision-and-light) to use this ability.

**Ability2:** He may prepare a number of additional spell levels of spells equal to the level of the
highest-level wizard spell he can cast. For example, if he can cast 6th-level wizard spells, he
could prepare six 1st-level spells, two 3rd level-spells, or any similar combination that adds up to
a total of six spell levels. These spells are stored in his shadow. He can only cast these spells
when he is in an area of normal light or dim light.

**Gained:** At 1st Level

**Replaces:** Arcane bond

**Special:** He gains Shadowtongue as a bonus language.

**Shadowsight (Ex)**

**Ability:** A shadowcaster gains [darkvision](ref/rule/darkvision) 60 feet.

**Gained:** At 5th Level

**Replaces:** 5th-level bonus feat

**Shadowy Specialization (Ex)**

**Ability:** When a shadowcaster casts [shades](ref/spell/shades),
[shadow conjuration](ref/spell/shadow-conjuration), [shadow evocation](ref/spell/shadow-evocation),
and similar illusion spells that have a listed fraction of the strength of real effects, he
increases the percentage of damage caused by the spell's effect or summoned creatures by one-fifth
(+20%) against creatures that make their saving throw against the effect, up to a maximum of 100% of
the strength. For example, _[shadow evocation](ref/spell/shadow-evocation)_ and
_[shadow conjuration](ref/spell/shadow-conjuration)_ deal 40% normal damage on a successful save
instead of 20%.

**Gained:** At 10th Level

**Replaces:** 10th-level bonus feat
