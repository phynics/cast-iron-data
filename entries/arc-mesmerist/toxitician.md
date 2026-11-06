+++
id = "ref/arc-mesmerist/toxitician"
kind = "archetype"
title = "Toxitician"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxitician", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]

[fields]
kind = "none"
+++

**Sources:** Occult Adventures pg 98\
Toxiticians forgo the mesmerist's stare, instead combining their psychic power with their alchemical
knowledge to craft injections that torment their foes and bolster themselves and their allies.

**Deft Fingers (Ex)**

**Passive:** A toxitician adds 1/2 his class level (minimum 1) as a bonus on all Sleight of Hands
checks.

**Replaces:** Consummate liar

**Injections (Su)**

**Action:** Ability

**At 8th Level:** The penalty on Will saves becomes -3.

**Gained:** At 1st Level

**Replaces:** Hypnotic stare

The toxitician uses his skill with alchemy and his own psychic powers to create injections. The
toxitician can create a number of injections per day equal to his mesmerist level + his Charisma
modifier. It takes 1 hour to create the injections. An injection is inert until the toxitician
attempts to use it, taking a **swift action** to infuse it with his psychic power to activate it.

Using an injection requires taking a **standard action** to attempt a melee touch attack. If the
attack hits, the target of an injection takes a -2 penalty on its Will saving throws for a number of
minutes equal to 1/2 the toxitican's class level (minimum 1). The toxitician can simultaneously
attempt a DC 20 Sleight of Hand check to inject the target surreptitiously. If the toxitician uses
Sleight of Hand, the target can attempt a Perception check to detect the attempt, opposed by the
Sleight of Hand check result, but detecting the attempt doesn't prevent the creature from being
injected. Whenever the toxitician uses Sleight of Hand to administer one of his injections, he can
implant it rather than injecting it and then trigger the effect of the injection at a later time. At
any point before he regains his injections, the toxitician can trigger an implanted injection as a
**free action**. The toxitician must be within medium range (100 feet + 10 feet per mesmerist level)
of the target of the implanted injection.

If either the melee touch attack or the Sleight of Hand check (if attempted) fails, the injection
isn't delivered but can still be used again - once activated, it remains potent for 1 day. An
injection that hasn't been administered becomes inert if it leaves the toxitician's possession,
reactivating as soon as it returns to his keeping.

The penalties from multiple injections don't stack, nor do the penalties from injections stack with
penalties from mesmerist _stares_ or witches' [evil eye](ref/hex/evil-eye) hexes. Injections are
mind-affecting effects.

**Painful Injection (Su)**

**Ability:** The toxitician's injection causes intense pain. This increases the damage the subject
takes in the same way as the mesmerist's _painful stare_ class feature. This extra damage is dealt
automatically, without being triggered by the toxitician, but doesn't increase when the toxitician
damages the target and can still be dealt only once per round.

**Replaces:** Painful stare

**Injection Improvement (Su)**

**Ability:** A toxitician can select one improvement (from those listed below) to add to his
injections. The toxitician doesn't have to select the improvements when he prepares his injections
at the start of the day; the choice is made as part of the **swift action** to activate the
injection. The target can attempt a Fortitude saving throw to resist an injection with an
improvement added to it. The DC is 10 + 1/2 the toxitician's class level + the toxitician's Charisma
modifier. On a successful save, the target still takes the penalty on its Will saving throws, but
not the effects of the improvement.

**Free:** A toxitician can sacrifice one use of his injections to increase the DC of another
injection by 2.

**Gained:** At 3rd Level

**Replaces:** Bold stare

**Special:** The toxitician can't choose the same improvement more than once.

At 7th level: He can select a 2nd improvement.

At 11th level: He can select a 3rd improvement.

At 15th level: He can select a 4th improvement.

At 19th level: He can select a 5th improvement.

**Ability Decrease**

**Ability:** The target takes a -2 penalty to one ability score of the toxitician's choosing.

**At 11th Level:** The penalty becomes -4.

**Excruciating**

**Ability:** The extra damage from _painful injection_ increases by an amount equal to 2 points + 1
point per 3 mesmerist levels the toxitician possesses.

**Fortitude Decrease**

**Ability:** The target's immune system weakens, imposing a -2 penalty on Fortitude saving throws.

**At 11th Level:** The penalty becomes -4.

**Natural Armor Decrease**

**Ability:** The target's skin becomes looser, decreasing its natural armor (if any) by 2.

**At 11th Level:** Its natural armor bonus instead decreases by 4.

**Reflex Decrease**

**Ability:** The target's body becomes stiffer, imposing a -2 penalty on the target's Reflex saving
throws.

**At 11th Level:** The penalty becomes -4.

**Slow**

**Ability:** The target's actions become sluggish, reducing its base movement by 10 feet and
imposing a -1 penalty on attack rolls.

**At 11th Level:** The penalty on attack rolls becomes -2.

**Treatment Vials (Su)**

**Ability:** A toxitician can create treatment vials when he creates his injections for the day;
creating each treatment vial expends one use of _touch treatment._ A treatment vial has the same
benefit as his _touch treatment,_ but anyone can administer it as a **standard action**. A vial can
remove any condition the toxitician is able to remove at his mesmerist level, but can't be used for
a _[break enchantment](ref/spell/break-enchantment)_ effect. A treatment vial becomes inert after 24
hours.

**Alters:** Touch treatment

**Gained:** At 3rd Level

**Improved Injections (Su)**

**Ability:** The toxitician can add two different improvements to an injection. The injection still
requires only one save.

**Gained:** At 11th Level

**Replaces:** Glib lie
