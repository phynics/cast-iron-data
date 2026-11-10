+++
id = "ref/arc-mesmerist/material-manipulator"
kind = "archetype"
title = "Material Manipulator"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "material_manipulator", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "psychic-anthology"
page = "18"

[fields]
kind = "archetype"
replaces = ["Consummate liar", "mesmerist trick gained at 2nd level", "manifold tricks", "Touch treatment", "rule minds"]
alters = ["Spellcasting"]
+++

Rather than waste time limiting himself to ruling minds, a material manipulator forces his whims
upon reality and uses his magic to ensure that those around him comply with his demands.

**Manipulator Spells**

**Ability:** A material manipulator casts psychic spells drawn from the mesmerist spell list and
augmented by a select list of sorcerer/wizard. All illusion (glamer), illusion (shadow), and
transmutation spells of 6th level and lower are considered to be part of the material manipulator's
spell list. These are psychic spells.

**Alters:** Spellcasting

**Replaces:** Consummate liar, mesmerist trick gained at 2nd level, manifold tricks

**Revision (Su)**

**Ability:** Using _revision_ is a **standard action** (or a **swift action** if the material
manipulator uses it on himself), and the material manipulator must be able to touch his target. An
unwilling target must succeed at a Fortitude save (DC = 10 + half the material manipulator's
mesmerist level + his Charisma modifier) to negate the effect. This effect lasts for 10 minutes per
mesmerist level.

**Flavor:** A material manipulator can revise a creature's body to change its appearance.

**At 10th Level:** He can adjust the target's age, rewinding the target's age to as young as a young
adult (approximately 8 years old for a human) or progressing it to as old as venerable. This causes
the target to gain aging bonuses and penalties and adjust its size
[as appropriate for its new age](ref/rule/age), but doesn't confer any other benefits gained from
aging (such as additional racial Hit Dice, supernatural abilities, and so on). The effects of
_revision_ now last for 1 hour per mesmerist level.

**At 14th Level:** He can adjust the target's type or subtype, as per
[polymorph](ref/spell/polymorph). This _revision_ only lasts 1 minute per mesmerist level.

**At 20th Level:** He can instead adjust the target's type as per
[greater polymorph](ref/spell/polymorph-greater). The effect of _revision_ lasts indefinitely, or 10
minutes per mesmerist level if the material manipulator uses it as
_[greater polymorph](ref/spell/polymorph-greater)_ and causes the target to assume a form with a
different type than its true form.

**At 3rd Level:** The material manipulator can adjust the target's height and weight, increasing it
or decreasing it to any height or weight within the standard range for creatures of the target's
[type and size category](ref/rule/height-and-weight).

**At 6th Level:** He can adjust the target's gender, physical traits (such as nose size, fingernail
length, and foot shape), and pigmentation (including eye, hair, and skin color) to any natural
variation for creatures of the target's type (and heritage, if applicable).

**Gained:** At 3rd Level

**Replaces:** Touch treatment, rule minds

**Special:** The mesmerist can dismiss this effect as a **free action**. This ability is a polymorph
effect, and the subject of a _revision_ cannot end the effect early by any means unless the material
manipulator permits it. The material manipulator can stack multiple adjustments from this ability
into the same polymorph effect - for instance, a 14th-level material manipulator can adjust himself
into an orc, reduce his age to that of a young adult, give himself large feet and a bulbous nose,
and change his gender. Clothing and equipment worn by the target is not affected by this effect -
gear does not resize to suit the wearer's new form, nor does it merge into her body. Gear unable to
be worn or wielded as a result of this effect falls to the ground in the wearer's space.

**Usage:** Charisma3 modifier times/day
