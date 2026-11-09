+++
id = "ref/arc-paladin/tranquil-guardian"
kind = "archetype"
title = "Tranquil Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Tranquil%20Guardian"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tranquil_guardian", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-race-guide"
page = "86"

[fields]
kind = "archetype"
replaces = ["Smite evil", "Aura of courage", "Aura of resolve", "Aura of justice", "Holy champion"]
+++

A tranquil guardian is a missionary of peace and tranquility, a soothing voice of succor in a
violent and dangerous world. A tranquil guardian gains the following class features.

**Prerequisites:** Aasimar

**Touch of Serenity (Su)**

**Ability:** A tranquil guardian gains [Touch of Serenity](ref/feat/touch-of-serenity) as a bonus
feat, even if she does not meet the prerequisites.

**At 6th Level:** The duration of a tranquil guardian's Touch of Serenity is increased by an amount
of rounds equal to [one-sixth](ref/misc/fractions-and-rounding) of her paladin level. Each round on
its turn, the target may attempt a new Will save to end the effect. The duration does not stack;
only the longest remaining duration applies.

**Gained:** At 1st Level

**Replaces:** Smite evil

**Serene Strike (Su)**

**Free:** When a tranquil guardian confirms a critical hit, she may convert all damage from her
attack to nonlethal damage, and when she does, she can activate Touch of Serenity through her weapon
or unarmed strike.

**Gained:** At 3rd Level

**Replaces:** Aura of courage

**Divine Bond (Su)**

**Info:** A tranquil guardian who chooses a weapon as her _divine bond_ may only increase her
weapon's enhancement bonus or add the following properties to her weapon: _conductive, defending,
disruptive, grayflame,_ or _merciful._

**Aura of Calm (Su)**

**Gained:** At 8th Level

**Passive:** A tranquil guardian is immune to all spells and
[spell-like abilities](ref/umr/spell-like-abilities) with the emotion descriptor, as well as all
fear effects. Each ally within 10 feet of her gains a +4 morale bonus on saving throws against these
effects.

**Replaces:** Aura of resolve

**Special:** This ability functions only while the tranquil guardian is conscious, not if she is
unconscious or dead.

**Waves of Peace (Su)**

**Ability:** A tranquil guardian may expend 2 uses of her Touch of Serenity to affect each opponent
within 5 feet of her with that effect. She does not need to touch the creature for the effect to
take hold.

**Gained:** At 11th Level

**Replaces:** Aura of justice

**Apostle of Peace (Su)**

**Gained:** At 20th Level

**Passive:** A tranquil guardian's DR increases to 10/evil, and whenever she channels positive
energy or uses _lay on hands_ to heal, she heals the maximum possible amount. In addition, any
creature struck by her Touch of Serenity, even if it saves, must make an additional Will save (DC
10 + 1/2 her tranquil guardian level + her Charisma modifier) the next time it tries to attack. If
it fails this save, the attack (including spells or special abilities) automatically fails.

**Replaces:** Holy champion
