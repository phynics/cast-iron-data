+++
id = "ref/arc-monk/harrow-warden"
kind = "archetype"
title = "Harrow Warden"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harrow_warden", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]

[fields]
kind = "archetype"
replaces = ["Stunning fist", "Improved evasion", "Diamond body", "Quivering palm"]
+++

**Sources:** The Harrow Handbook pg 7\
Some who study the mysteries of the harrow do so to restore lost knowledge and pride to the Varisian
people. The harrow warden fulfills this role as she seeks to bring her mind and body into alignment,
and she protects her people by invoking the folklore that has guided them for so long. In mastering
her own place in fate, a harrow warden learns how to misalign the destinies of others.

**Weapon and Armor Proficiency**

**Info:** The harrow warden is proficient with all simple weapons, as well as with the
[klar](ref/eq-armor/klar), [rapier](ref/eq-weapon/rapier), [short sword](ref/eq-weapon/short-sword),
and [starknife](ref/eq-weapon/starknife). Additionally, harrow wardens treat starknives as monk
weapons.

**Idiot Strike (Su)**

**Ability:** The harrow warden can make an unarmed strike against a target and curse the creature
with bad luck. Foes damaged by an _idiot strike_ must succeed at a Will save (DC 10 + 1/2 the monk's
level + the monk's Wisdom modifier) or become jinxed. A jinxed creature must roll twice whenever it
attempts an attack roll, a saving throw, a skill check, or a caster level check for 1 round, taking
the lower result in each instance. She must declare that she is using an _idiot strike_ before
making the attack roll; thus, a failed roll wastes the attempt.

**At 12th Level:** The jinxed condition lasts for 3 rounds.

**At 16th Level:** A harrow warden can expend two uses of _idiot strike_ to instead curse her target
as the [bestow curse](ref/spell/bestow-curse) spell.

**At 4th Level:** The jinxed condition lasts for 2 rounds.

**Gained:** At 1st Level

**Replaces:** Stunning fist

**Usage:** 1 time/day per monk level

**Mute Hag Stance (Su)**

**Flavor:** The harrow warden can block opponents' metaphysical ties to one another.

**Gained:** At 9th Level

**Passive:** Enemies threatened by the harrow warden do not gain the effects of any morale or
insight bonuses on attack rolls or skill checks as long as they are within the harrow warden's
threatened area.

**Replaces:** Improved evasion

**Big Sky Stance (Su)**

**Flavor:** The harrow warden becomes secure in her role within the larger story.

**Gained:** At 11th Level

**Passive:** She gains immunity to curses and polymorph effects.

**Replaces:** Diamond body

**Eclipse Strike (Su)**

**Ability:** Foes damaged by the harrow warden's _idiot strike_ can attempt a Fortitude save (DC
10 + 1/2 the monk's level + the monk's Wisdom modifier). Those that fail are transmuted into a
harmless form, as per the [baleful polymorph](ref/spell/baleful-polymorph) spell.

**Flavor:** The harrow warden can strike a target with enough force to realign its place in the
world.

**Gained:** At 15th Level

**Replaces:** Quivering palm
