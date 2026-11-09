+++
id = "ref/arc-slayer/avalancher"
kind = "archetype"
title = "Avalancher"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "avalancher", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "86"

[fields]
kind = "archetype"
replaces = ["Studied target", "Track", "swift tracker", "Stalker", "Quarry", "improved quarry", "Master slayer"]
+++

Avalanchers attack from overhead cliffs and mesas like a landslide of arrows and blades.

**Falling Strike (Ex)**

**Flavor:** An avalancher excels at dropping onto opponents from higher ground.

**Passive:** He gains a bonus on Stealth checks and attack and damage rolls when he falls at least
10 feet before attacking an opponent. These bonuses are equal to 1 + one-fifth of his slayer level,
and they stack with any bonuses the avalancher receives for [charging](ref/rule/charge) or attacking
from [higher ground](ref/rule/combat-modifiers).

**Replaces:** Studied target

**Cliff Jumper (Ex)**

**Ability:** Whenever he attempts an [Acrobatics](ref/skill/acrobatics) check to soften an
intentional fall, he reduces the falling damage he takes by an additional 1d6 for every increment of
10 by which his Acrobatics check result exceeds the DC (a 2d6 reduction at DC 25, 3d6 at DC 35, and
so on).

**At 11th Level:** The avalancher reduces the DC of his Acrobatics checks to soften a fall by 5.

**Passive:** An avalancher adds half his level on Acrobatics checks to jump or soften a fall.

**Replaces:** Track, swift tracker

**Falling Dodge (Ex)**

**Ability:** An avalancher gains his bonus to AC from the _falling strike_ ability when a jump or
fall carries him through threatened squares.

**Gained:** At 7th Level

**Replaces:** Stalker

**Special:** This bonus applies only when he's jumping, not when he's using Acrobatics to try to
avoid attacks of opportunity from moving through threatened squares.

**Fall-By Attack (Ex)**

**Ability:** If the avalancher makes a single jump of at least 20 feet in any direction and lands at
an elevation at least 10 feet lower than his starting elevation, he can make ranged or melee attacks
during his fall as if he were making a full-round attack. He can make any number of attacks in any
combination of squares along this single jump, up to his maximum number of attacks, but he can
attack a given creature once at most. If the avalancher attempts a jump but fails the Acrobatics
check, he makes no attacks and suffers the consequences of his failed jump normally.

**At 19th Level:** He can add his extra damage from _sneak attack_ against each creature he hits
while using this ability, even if the targets have acted in combat or retain their Dexterity bonuses
to AC.

**Gained:** At 14th Level

**Replaces:** Quarry, improved quarry

**Death from Above (Ex)**

**Ability:** During a round, if he falls at least 10 feet (the action type depends on how he comes
to be falling), he can make a single attack at his full base attack bonus as a **standard action**,
choosing one of the following effects: kill, knock unconscious for 1d4 hours, or paralyze for 2d6
rounds. If the attack hits, the target takes damage normally and must succeed at a Fortitude save or
suffer the additional effect. The save DC is equal to 20 + 1 for every 10 feet the avalancher fell
before making the attack (to a maximum of DC 30 for a fall of 100 feet or more).

**Flavor:** An avalancher can take down his foe with a single attack.

**Gained:** At 20th Level

**Replaces:** Master slayer

**Special:** Whether or not the target succeeds, it can't be targeted by this ability again (by any
avalancher) for 24 hours.
