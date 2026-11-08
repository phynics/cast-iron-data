+++
id = "ref/arc-bard/fortune-teller"
kind = "archetype"
title = "Fortune-Teller"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fortune_teller", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]

[fields]
kind = "archetype"
replaces = ["Countersong", "distraction", "Well-versed", "Dirge of doom"]
alters = ["Spell list", "Bardic performance"]
+++

**Sources:** Villain Codex pg 32\
Instead of using song and dance, a fortune-teller influences people by divining their fate. Though
he learns a great deal about the paths of destiny, his true skill is in making others think he knows
more than he truly does.

**Fortune-Teller's Divinations**

**Alters:** Spell list

**Info:** Add the following spells to the fortune-teller's bard spell list. He doesn't automatically
gain them and must still select them as spells known if he wants to use them.
0-[guidance](ref/spell/guidance); 1st-[object reading](ref/spell/object-reading);
2nd-[augury](ref/spell/augury); 3rd-[analyze aura](ref/spell/analyze-aura);
4th-[divination](ref/spell/divination); 5th-[retrocognition](ref/spell/retrocognition);
6th-[true seeing](ref/spell/true-seeing), [vision](ref/spell/vision).

**Oracular Performance**

**Action:** Ability

**Alters:** Bardic performance

**Flavor:** A fortune-teller can use Perform (oratory) to read a fortune as part of a bardic
performance.

**Replaces:** Countersong, distraction

Once per hour when the bard performs a fortune-telling using a fortune-teller's deck, a crystal
ball, or a similar item, he can read the fortune of one subject of the bardic performance. This is
part of the same action used to activate the performance. The fortune-teller rolls d%, adds his bard
level to the result, and consults the list below. The outcome depends on whether the chosen creature
is an ally (for a beneficial performance) or an enemy (for a detrimental performance).

- 01-35%

  - Ally: **Woe**
  - Enemy: **Weal**
- 36-65%

  - **Inconclusive**
- 66%+

  - Ally: **Weal**
  - Enemy: **Woe**

On an inconclusive result, the bard fails to get any information from the reading and the subject is
affected by the performance normally. For an ally, on a weal result the subject's bonus from the
performance increases by 1, and on a woe result the subject's bonus decreases by 1 (minimum 0). This
affects only numeric bonuses. For example, a subject wouldn't gain another Hit Die from _inspire
greatness._

For an enemy, on a weal result the subject gains a +2 bonus on its saving throw to negate the bard's
performance, and on a woe result it takes a -2 penalty on its save. An oracular performance has no
effect on an enemy if the performance doesn't require a saving throw.

All adjustments from an oracular performance on a foe last only for that instance of the bardic
performance. All adjustments on an ally last for 1 minute, applying each time the fortune-teller
uses that particular bardic performance on that ally but ending when the duration expires, even if
the performance continues.

**Fortune-Teller's Acumen**

**Ability:** Whenever he casts a spell from the divination school, a fortune-teller can use a
fortune-teller's deck, crystal ball, or similar item instead of the spell's material component, as
long as the cost of the material component is no more than 100 gp per bard level. If he chooses to
cast the spell using such an item and the spell's normal material component (regardless of that
component's cost), he casts the spell at caster level.

**Gained:** At 2nd Level

**Replaces:** Well-versed

**Special:** This special focus can't be used with other special foci that have a similar effect,
but can be used with spells that normally require a focus component (which must also be provided).

**Bardic Performance**

**Info:** A fortune-teller gains the following bardic performance.

**Transparent Fate (Su)**

**Action:** Ability

**Gained:** At 8th Level

**Replaces:** Dirge of doom

**Special:** A creature that was targeted by oracular performance when this performance began
applies any save DC adjustment to this secondary save as well. At the GM's discretion, the
revelation of the creature's fate might have other consequences; for example, a creature's allies
might see it was planning to betray them.

The fortune-teller can cause all enemies within 30 feet to have their near future revealed for all
to see. A successful Will saving throw (DC = 10 [half](ref/misc/fractions-and-rounding) the
fortune-teller's level the fortune-teller's Cha modifier) negates the effect. This ability causes
any creature attacked by an affected enemy to gain a +2 bonus to AC and on saving throws against the
attack.

As a secondary effect, if an affected creature's hit points are reduced to less than its
Constitution score, it also sees a vision of its own death and must succeed at another Will save or
become frightened for 1 round. A given creature needs to save against this secondary effect at most
once per performance of transparent fate, even if its hit points are reduced to less than its
Constitution score multiple times.
