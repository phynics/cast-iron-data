+++
id = "ref/arc-druid/survivor"
kind = "archetype"
title = "Survivor"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Survivor"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "survivor", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "champions-of-balance"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "nature-bond", level = 1 },
  { anchor = "element-of-surprise", level = 4 },
  { anchor = "trap", level = 4 },
  { anchor = "launch-trap", level = 9 },
]
trades = [
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["element-of-surprise"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["trap"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["launch-trap"] },
  { alters = "Spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
]
+++

The survivor embodies the neutral aspect of the natural world and eschews druidic magic in favor of
more pragmatic and worldly survival methods.

## Class Skills {#class-skills}

A survivor adds Stealth to her list of class skills.

## Weapon Proficiencies {#weapon-proficiencies}

In addition to the normal druid weapon proficiencies, a survivor is proficient with the
[shortbow](ref/eq-weapon/shortbow) and [longbow](ref/eq-weapon/longbow).

## Diminished Spellcasting {#diminished-spellcasting}

A survivor's number of spells per day for each spell level is one less than normal (for example, a
4th-level survivor can cast three cantrips, two 2nd-level spells, and one 1st-level spell per day).
If this reduces the number of spells for a level to 0, she gains only the bonus spells for that
level she would be entitled to based on her Wisdom score.

## Nature Bond (Ex) {#nature-bond}

At 1st level, a survivor must select an animal companion as her nature bond.

## Element of Surprise (Ex) {#element-of-surprise}

At 4th level, if a survivor makes a successful attack during a surprise round against a target that
is unaware of her, her victim takes a penalty on its initiative check during the following round
equal to [half](ref/misc/fractions-and-rounding) the damage dealt by the survivor's attack (minimum
0, maximum equal to the survivor's class level). This cannot reduce an initiative result below 1.
This ability replaces resist nature's lure.

## Trap {#trap}

At 4th level, a survivor learns how to create a [snare trap](ref/rangertrap/snare-trap) and one
other ranger trap of her choice (see page 25 or _Ultimate Magic_ 64). At 6th level and every 2
levels thereafter, she learns another trap. The survivor can use these traps a total number of times
per day equal to 1/2 her druid level + her Wisdom modifier. Once a trap is learned, it can't be
unlearned and replaced with a different type of trap. The survivor cannot select an individual trap
more than once. This ability replaces wild shape.

## Launch Trap {#launch-trap}

At 9th level, a survivor can affix a magical ranger trap to an arrow or thrown weapon, allowing her
to set the trap remotely or use it as a direct attack. Attaching the trap to the projectile is part
of the full-round action of creating a new trap. The trapped projectile is fired or thrown in the
normal manner. If the projectile is fired at a square, the trap is treated as if the survivor had
set the trap in that square, except the DC is 5 lower than normal. If the projectile is fired at a
creature, the target takes damage from the ranged weapon and is treated as if it had triggered the
trap (saving throw applies, if any). The attack has a maximum range of 60 feet, and range increments
apply to the attack roll. The duration of the trapped projectile starts from when it is created, not
from when it is used. This ability replaces venom immunity.
