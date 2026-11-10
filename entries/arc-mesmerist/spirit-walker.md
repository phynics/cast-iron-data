+++
id = "ref/arc-mesmerist/spirit-walker"
kind = "archetype"
title = "Spirit Walker"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Spirit%20Walker"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_walker", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "occult-adventures"
page = "97"

[fields]
kind = "archetype"
replaces = ["Consummate liar", "mental potency", "3rd- and 14th-level touch treatments", "6th- and 10th-level touch treatments", "Rule minds"]
alters = ["Spell list"]
replaces_features = ["consummate-liar", "mental-potency", "rule-minds"]
+++

Some mesmerists specialize in dominating and controlling undead rather than the living.

**Spells**

**Alters:** Spell list

**Info:** A spirit walker adds additional spells to his spell list at the spell levels indicated. He
can choose these as spells known, but doesn't gain them automatically.

**Spells:** Hide from undead

**Spells:** Command undead

**Spells:** Halt undead

**Spells:** Speak with haunt

**Undead Inception (Su)**

**Ability:** A spirit walker can affect undead creatures with his _hypnotic stare_ as the _psychic
inception_ bold stare ability. This allows him to affect only undead; he must actually choose the
_psychic inception bold stare_ improvement if he wants to also affect other mindless creatures.

**At 3rd Level:** When the spirit walker uses this ability, undead targets don't receive a saving
throw bonus (if they did to begin with), have only a 25% chance of ignoring the spirit walker's
mind-affecting spells and abilities, and no longer need to be under the spirit walker's gaze to be
affected.

**At 5th Level:** When the spirit walker uses his mind-affecting spells and abilities, they affect
all undead normally, with no chance of failure.

**Gained:** At 1st Level

**Replaces:** Consummate liar, mental potency

**Continued Animation (Su)**

**Immediate:** When a spirit walker is using _hypnotic stare_ on a humanoid target and the target
dies, the spirit walker can force the target's soul to remain in the body. The spirit walker can
then control the target as if using [dominate person](ref/spell/dominate-person) for a number of
rounds equal to 1/2 the spirit walker's class level. The creature gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to 2 &times& the spirit walker's class
level and continues acting as though it were alive and conscious until it loses those temporary hit
points or the duration expires. During this time, the creature counts as undead, but it can't be
healed by negative energy.

**At 14th Level:** The spirit walker can apply this ability to any type of target as if using
[dominate monster](ref/spell/dominate-monster).

**Gained:** At 3rd Level

**Replaces:** 3rd- and 14th-level touch treatments

**Special:** The target receives a Will saving throw (DC = 10 + 1/2 the spirit walker's class
level + his Charisma modifier) to avoid this effect and die normally. This ability ends immediately
if at any point the target's body is completely destroyed (such as by
[disintegrate](ref/spell/disintegrate)) or restored to life.

**Usage:** 1 time/day per 3 mesmerist levels

**Command Undead (Su)**

**Ability:** A spirit walker gains [Command Undead](ref/feat/command-undead) as a bonus feat. A
spirit walker can use Command Undead a number of times per day equal to 1 + his Charisma modifier
(minimum 1), using his mesmerist level as his cleric level.

**At 10th Level:** The DC to resist this effect increases by 2.

**Gained:** At 6th Level

**Replaces:** 6th- and 10th-level touch treatments

**Master of the Dead (Su)**

**Ability:** A spirit walker gains mastery of the undead. Once per day, a spirit walker can use
[control undead](ref/spell/control-undead) as a [spell-like ability](ref/umr/spell-like-abilities)
on one target. If that creature fails its saving throw and has 20 or fewer Hit Dice, it falls
permanently under the spirit walker's control until the spirit walker dies. A creature that fails
its save but has more than 20 HD suffers the effect of _[command undead](ref/spell/command-undead)._
A creature that succeeds at its save can't be affected by _master of the dead_ for 24 hours. A
spirit walker can control only one undead creature in this fashion at a time. If he permanently
controls a new undead creature, the previous one is set free.

**Gained:** At 20th Level

**Replaces:** Rule minds
