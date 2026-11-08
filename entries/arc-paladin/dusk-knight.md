+++
id = "ref/arc-paladin/dusk-knight"
kind = "archetype"
title = "Dusk Knight"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dusk_knight", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Channel positive energy", "Divine bond", "Aura of resolve", "Aura of justice"]
alters = ["Smite evil"]
+++

**Sources:** Blood of Shadows pg 18\
Some paladins focus their training to combat the shadows and use darkness to their advantage. Known
as dusk knights, these paladins are primarily worshipers of [Abadar](ref/faith/abadar), but dusk
knights who serve [Iomedae](ref/faith/iomedae) and [Irori](ref/faith/irori), though rare, do exist.

**Gained class skills:** stl

**Lost class skills:** sm

**Shadow Smite (Su)**

**Ability:** A dusk knight gains [concealment](ref/rule/concealment) for 1 round per paladin level
against the target of her _smite evil_ ability in addition to its other effects. The dusk knight
doesn't deal additional damage with her _smite evil_ ability.

**Alters:** Smite evil

**Illuminating Zeal (Su)**

**Flavor:** A dusk knight gains the ability to grant [darkvision](ref/rule/darkvision) to her
allies.

**Gained:** At 4th Level

**Replaces:** Channel positive energy

**Special:** If the dusk knight targets herself, using this ability is a **swift action**. Using
this ability consumes two uses of her _lay on hands_ ability.

**Standard:** The dusk knight grants one target touched [darkvision](ref/rule/darkvision) with a
range of 60 feet for 1 hour. If the target already has darkvision, the range increases by 60 feet
instead.

**Shadow's Embrace (Su)**

**Ability:** She gains [Blind-Fight](ref/feat/blind-fight) as a bonus feat and
[darkvision](ref/rule/darkvision) with a range of 60 feet. If she already has darkvision, the range
increases by 30 feet instead.

**Flavor:** A dusk knight learns to fight effectively in areas of darkness.

**At 10th Level:** A dusk knight gains [Improved Blind-Fight](ref/feat/improved-blind-fight) as a
bonus feat.

**At 15th Level:** A dusk knight gains the [see in darkness](ref/umr/see-in-darkness) ability.

**Gained:** At 5th Level

**Replaces:** Divine bond

**Cloak of Shadow (Su)**

**Flavor:** A dusk knight becomes adept at moving through darkness.

**Gained:** At 8th Level

**Passive:** She ignores her armor penalty when attempting Stealth checks and gains a bonus on
Stealth checks equal to half her paladin level while in areas of
[dim light](ref/rule/vision-and-light) or darkness.

**Replaces:** Aura of resolve

**Clouding Smite (Su)**

**Ability:** When a dusk knight successfully smites a foe, she reduces the target's
[darkvision](ref/rule/darkvision) by 60 feet for the duration of the smite. If the target has the
_[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness)_ ability, it
must succeed at a Fortitude save or lose this ability for the duration of the smite. The save DC is
equal to 10 + 1/2 the dusk knight's paladin level + her Charisma modifier.

**Flavor:** A dusk knight's smite impairs her foe's abilities in the dark.

**Gained:** At 11th Level

**Replaces:** Aura of justice
