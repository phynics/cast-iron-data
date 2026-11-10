+++
id = "ref/arc-monk/menhir-guardian"
kind = "archetype"
title = "Menhir Guardian"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "menhir_guardian", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "64"

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiency", "Unarmed strike", "ki strike", "Stunning fist", "high jump", "quivering palm"]
alters = ["Alignment requirement", "Ki pool", "Furry of blows"]
replaces_features = ["unarmed-strike", "stunning-fist", "high-jump", "quivering-palm"]
alters_features = ["ki-pool"]
+++

Menhir guardians are ascetic protectors of sacred druidic sites, less concerned with structure and
maintaining internal order than they are with preserving the natural balance of the world.

**Alignment**

**Alters:** Alignment requirement

**Info:** A menhir guardian can be lawful neutral, neutral good, neutral evil, or neutral. While
they can work with chaotic allies, they cannot themselves be chaotic.

**Weapon and Armor Proficiency**

**Ability:** A menhir guardian is proficient with the [club](ref/eq-weapon/club),
[dagger](ref/eq-weapon/dagger), [dart](ref/eq-weapon/dart),
[quarterstaff](ref/eq-weapon/quarterstaff), [sickle](ref/eq-weapon/sickle),
[shortspear](ref/eq-weapon/shortspear), [sling](ref/eq-weapon/sling), and
[spear](ref/eq-weapon/spear). A menhir guardian can use these weapons in conjunction with his _wild
flurry_ ability.

**Replaces:** Weapon and armor proficiency

**Claws (Ex)**

**Ability:** He gains the [shifter's](ref/class/shifter) _shifter claws_ class feature and treats
his monk level as his shifter level for the purposes of this ability.

**Alters:** Ki pool

**Flavor:** A menhir guardian learns to draw upon natural forces to subtly change his body.

**Replaces:** Unarmed strike, ki strike

**Shifter Claws (Su)**

**Flavor:** Text from the shifter class

**At 11th Level:** Your claw damage becomes 1d8 (1d6 if Small).

**At 17th Level:** Your claws' critical multiplier becomes &times&3.

**At 19th Level:** Your claws ignore DR/adamantine and DR/-.

**At 3rd Level:** Your claws ignore DR/cold iron, DR/magic, and DR/silver.

**At 7th Level:** Your claw damage becomes 1d6 (1d4 if Small).

**Info:** The claws on each hand can be used as a primary [natural attack](ref/umr/natural-attacks),
dealing 1d4 points of piercing and slashing damage (1d3 if you are Small). If you use one of your
claw attacks in concert with a weapon held in the other hand, the claw acts as a secondary natural
attack instead.

**Swift:** In your natural form, you can extend your claws to use as a weapon.

**Wild Flurry (Ex)**

**Ability:** A menhir guardian gains _flurry of blows._ He can use this ability with the natural
attacks provided by his _shifter claws_ ability or the weapons specified above under weapon and
armor proficiency.

**Alters:** Furry of blows

**Rebuking Strike (Ex)**

**Ability:** A menhir guardian must declare that he is using _rebuking strike_ before making a
natural attack with his claws. On a hit, a foe damaged by the menhir guardian's claws must succeed
at a Fortitude saving throw (DC = 10 + half the menhir guardian's level + his Wisdom modifier) or be
pushed back 5 feet directly away from the menhir guardian.

**Flavor:** A menhir guardian can channel his ki into a devastating strike that repels his enemies.

**At 15th Level:** A pushed creature is also affected by [aversion](ref/spell/aversion), making it
avoid the menhir guardian's current location for 1 round per level the menhir guardian has.

**At 5th Level:** A creature pushed also has its speed reduced by half for a number of rounds equal
to the menhir guardian's level.

**Gained:** At 1st Level

**Replaces:** Stunning fist, high jump, quivering palm

**Special:** If this movement would be blocked by a solid object, the target of _rebuking strike_
takes 1d6 points of damage per 10 feet moved and falls [prone](ref/rule/prone) at the end of the
movement.

**Usage:** The menhir guardian can attempt a _rebuking strike_ a number of times per day equal to
his monk level, but only once per round.

**Usage:** The menhir guardian can attempt a _rebuking strike_ a number of times per day equal to
his monk level, but only once per round.

At 5th level: The distance the foe is pushed 10 feet.

At 9th level: The distance the foe is pushed 15 feet.

At 13th level: The distance the foe is pushed 20 feet.

At 17th level: The distance the foe is pushed 25 feet.
