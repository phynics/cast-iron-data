+++
id = "ref/arc-shaman/primal-warden"
kind = "archetype"
title = "Primal Warden"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_warden", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]

[fields]
kind = "archetype"
replaces = ["Abilities the spirit animal gains from the shaman's chosen spirit", "Hex gained at 8th level", "Hexes gained at 4th and 12th levels"]
alters = ["Spirit magic", "Hexes"]
+++

**Sources:** People of the Wastes pg 7\
The influence of [primal magic](ref/rule/primal-magic) extends beyond what is visible and material.
Spirits that linger in areas where primal magic reigns can become warped, losing touch with their
former selves and experiencing random surges of power. A shaman who communes with such spirits
learns to stabilize these erratic energies and draw upon them to her benefit. Such shamans gradually
learn to guide their spirits toward coherence and lucidity, and in the process learn to bend chance
and fortune in their favor.

**Spirit Animal**

**Info:** A primal warden's spirit animal exhibits unusual physical features for a creature of its
type, such as unnatural colorations and extra or missing appendages.

**Passive:** Each day, the spirit animal gains resistance 10 against a random element. Roll 1d4 to
determine the type of resistance (1 = acid, 2 = cold, 3 = electricity, 4 = fire).

**Replaces:** Abilities the spirit animal gains from the shaman's chosen spirit

**Unstable Spellcasting**

**Ability:** When the primal warden would spontaneously cast a 1st- through 8th-level spell using
the _spirit magic_ class feature, she produces a random spell from the list of shaman spells of 1
spell level higher than the spell slot expended; use an appropriate die or another randomization
method to determine the spell. When she would spontaneously cast a 9th-level spell using _spirit
magic,_ she instead casts a random 9th-level spell from the shaman spell list, treating her caster
level as 2 higher. There is no way to predict the spell before the shaman begins casting it using
_spirit magic,_ and she cannot enhance the spell using metamagic feats. The spell uses the shaman's
caster level, even if that caster level would normally be too low to cast the spell.

**Alters:** Spirit magic

**Flavor:** A primal warden's spirit is ever shifting, and the spells it grants the primal warden
change from moment to moment.

**At 12th Level:** She cannot use this ability more than once in the same round.

**At 8th Level:** After determining the spell that she would cast using _spirit magic,_ once per day
as a **free action**, the primal warden shaman can choose to randomly select another spell instead,
using the same method of randomization as she used before (if she obtains the same result a second
time, she must keep that result).

**Replaces:** Hex gained at 8th level

**Special:** There are 126 potential 2nd-level spells, 111 potential 3rd-level spells, 102 potential
4th-level spells, 71 potential 5th-level spells, 50 potential 6th-level spells, 40 potential
7th-level spells, 28 potential 8th-level spells, and 20 potential 9th-level spells.^1^

At 12th level: She can choose to randomly select a different _spirit magic_ spell 2 times per day.

At 16th level: She can choose to randomly select a different _spirit magic_ spell 3 times per day.

At 20th level: She can choose to randomly select a different _spirit magic_ spell 4 times per day.

**Hexes**

**Ability:** A primal warden shaman gains the hexes below at the specified levels. A primal warden
shaman cannot select the _chant_ hex, the _evil eye_ hex, the _misfortune_ hex, or any witch hexes.

**Alters:** Hexes

**Replaces:** Hexes gained at 4th and 12th levels

**Primal Blessing (Su)**

**Ability:** The shaman gains the ability to channel primal magic into a target within 30 feet. Roll
1d4 to determine the effect. **On a result of 1,** the target takes a -2 penalty on attack rolls,
saving throws, and skill checks. **On a result of 2,** the target's size is enlarged or reduced, as
per [enlarge person](ref/spell/enlarge-person) or [reduce person](ref/spell/reduce-person), and the
effect functions even if the target is not a humanoid; roll randomly to determine the effect. **On a
result of 3,** the target gains a +20-foot enhancement bonus to her base speed. **On a result of
4,** all attacks against the target suffer a 20% miss chance.

**Gained:** At 4th Level

**Special:** The effects of this hex last for 1 minute. A creature affected by this hex cannot be
affected by it again for 24 hours.

**Greater Primal Blessing (Su)**

**Ability:** The shaman's _primal blessing_ hex improves. This functions as the _primal blessing_
hex in all ways, except that the shaman has a chance to bestow greater benefits upon her targets.
Roll 1d6 to determine the effect. On a result of 1-4, refer to the primal blessing ability to
determine the effect. **On a roll of 5,** the target gains a luck bonus on attack rolls and saving
throws and to her Armor Class. **On a roll of 6,** the target gains the benefit of the
[haste](ref/spell/haste) spell, using the primal warden's shaman level as her caster level.

**Gained:** At 12th Level

^1^ As a suggestion: \*\*2nd level:\*\* Roll a d8, rerolling any 8s. Subtract 1 from that number,
then multiply it by 20 and add 1d20. Reroll for results over 126. \*\*3rd level:\*\* Roll a d6 and
subtract 1 from the result, then multiply it by 20 and add 1d20. Reroll for results higher than 111.
\*\*4th level:\*\* Use the 3rd-level process, or roll a d10, rerolling any 10s. Subtract 1 from that
number, then multiply it by 12 and add 1d12. Reroll for numbers higher than 102. \*\*5th level:\*\*
Roll a d6 and subtract 1 from the result, then multiply it by 12 and add 1d12. Reroll if the result
is 72. \*\*6th level:\*\* Roll 1d100, then divide the result by 2, rounding up. \*\*7th level:\*\*
Roll a d4, subtract 1 from the result, then multiply it by 10 and add 1d10. \*\*8th level:\*\* Roll
a d8, rerolling any 8s. Subtract 1 from that number, then multiply it by 4 and add 1d4. \*\*9th
level:\*\* Roll 1d20.
