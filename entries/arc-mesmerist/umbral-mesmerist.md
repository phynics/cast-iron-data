+++
id = "ref/arc-mesmerist/umbral-mesmerist"
kind = "archetype"
title = "Umbral Mesmerist"
source_ids = ["occult-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_mesmerist", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]

[fields]
kind = "none"
+++

**Sources:** Occult Realms pg 16\
Trained in secret, umbral mesmerists are clandestine weapons who spend years learning how to shape
terrifying creatures from the inky darkness in which they revel.

**Diminished Spellcasting**

**Alters:** Spellcasting

**Info:** An umbral mesmerist can cast one fewer spell of each level than normal. If this reduces
the number of spells for a level to 0, he can cast spells of that level only if his Charisma score
allows [bonus spells](ref/rule/determine-bonuses) of that level.

**Shadow Summoning (Sp)**

**Action:** Ability

**At 12th Level:** This ability increases to that of
[summon monster IV](ref/spell/summon-monster-4).

**At 16th Level:** This power increases to [summon monster V](ref/spell/summon-monster-5).

**At 20th Level:** This power of this ability increases to
[summon monster VI](ref/spell/summon-monster-6).

**At 4th Level:** This power of this ability increases to
[summon monster II](ref/spell/summon-monster-2).

**At 8th Level:** This power increases to [summon monster III](ref/spell/summon-monster-3).

**Replaces:** Mesmerist tricks gained at 1st, 4th, 8th, 12th, 16th, and 20th levels

**Usage:** Charisma3 modifier times/day

An umbral mesmerist gains the ability to summon quasi-real creatures as per the
[summon monster I](ref/spell/summon-monster-1) spell. The umbral mesmerist can use this ability as a
**standard action**, and the creatures remain for 1 minute per level (instead of 1 round per level).
The creatures summoned are only partly real, but have normal effects unless a creature affected by
the illusion succeeds at a Will save to disbelieve (as per
[shadow conjuration](ref/spell/shadow-conjuration).) The DC for this save is equal to 10 + 1/2 the
umbral mesmerist's mesmerist level + the umbral mesmerist's Charisma modifier. This is an illusion
with the shadow descriptor.

A shadow creature has half the hit points of a normal creature of its kind (regardless of whether it
is recognized as a shadow creature). It deals the normal amount of damage and has all of the base
creature's normal abilities and weaknesses. Against a creature that recognizes it as a shadow
creature, however, the shadow creature's damage is halved, and all special abilities that do not
deal lethal damage are only 50% likely to work. (Roll for each use and each affected character
separately.) Furthermore, the shadow creature's AC bonuses are halved. A creature that succeeds at
its save to disbelieve sees the summoned creature as transparent images superimposed on vague,
shadowy forms. Objects automatically succeed at their Will saves against this spell. The umbral
mesmerist cannot use this ability to summon creatures from more than one
_[summon monster](ref/spell/summon-monster)_ spell in this way at one time.

**Umbral Solipsism (Su)**

**Gained:** At 2nd Level

**Passive:** When a creature attempts a Will save to disbelieve a quasi-real creature created by
_shadow summoning,_ it takes a penalty on the save equal to the mesmerist's Charisma modifier
(minimum 0).

**Replaces:** Towering ego

**Ephemeral Stare (Su)**

**Ability:** The umbral mesmerist is treated as if he were invisible by the target of his _hypnotic
stare_ (as per the [invisibility](ref/spell/invisibility) spell), provided neither he nor any
creatures conjured by _shadow summoning_ take hostile actions against the target. Once the umbral
mesmerist or any creature conjured by his _shadow summoning_ ability takes a hostile action against
the target, the mesmerist becomes visible to the target and the target cannot be affected again by
that umbral mesmerist's _ephemeral stare_ ability for 24 hours (although it can be affected by other
effects of his _hypnotic stare_).

**Gained:** At 5th Level

**Replaces:** Mental potency
