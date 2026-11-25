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
features = [
  { anchor = "spells" },
  { anchor = "undead-inception", level = 1 },
  { anchor = "continued-animation", level = 3 },
  { anchor = "command-undead", level = 6 },
  { anchor = "master-of-the-dead", level = 20 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["undead-inception"] },
  { replaces = "mental potency", feature = "mental-potency", by = ["undead-inception"] },
  { replaces = "3rd- and 14th-level touch treatments", feature = "touch-treatment", levels = [3, 14], by = ["continued-animation"] },
  { replaces = "6th- and 10th-level touch treatments", feature = "touch-treatment", levels = [6, 10], by = ["command-undead"] },
  { replaces = "Rule minds", feature = "rule-minds", by = ["master-of-the-dead"] },
  { alters = "Spell list", feature = "spells", power = "spell list", by = ["spells"] },
]
+++

Some mesmerists specialize in dominating and controlling undead rather than the living.

## Spells {#spells}

A spirit walker adds additional spells to his spell list at the spell levels indicated: _hide from
undead_ (1st), _command undead_ (2nd), _halt undead_ (3rd), and _speak with haunt_ (4th). He can
choose these as spells known, but doesn't gain them automatically. This ability alters the
mesmerist's spell list.

## Undead Inception (Su) {#undead-inception}

At 1st level, a spirit walker can affect undead creatures with his hypnotic stare as the psychic
inception bold stare ability. This allows him to affect only undead; he must actually choose the
psychic inception bold stare improvement if he wants to also affect other mindless creatures. At 3rd
level when the spirit walker uses this ability, undead targets don't receive a saving throw bonus
(if they did to begin with), have only a 25% chance of ignoring the spirit walker's mind-affecting
spells and abilities, and no longer need to be under the spirit walker's gaze to be affected. At 5th
level, when the spirit walker uses his mind-affecting spells and abilities, they affect all undead
normally, with no chance of failure. This ability replaces consummate liar and mental potency.

## Continued Animation (Su) {#continued-animation}

At 3rd level, when a spirit walker is using hypnotic stare on a humanoid target and the target dies,
as an immediate action the spirit walker can force the target's soul to remain in the body. The
spirit walker can then control the target as if using _[dominate person](ref/spell/dominate-person)_
for a number of rounds equal to 1/2 the spirit walker's class level. The creature gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to 2 × the spirit walker's class level
and continues acting as though it were alive and conscious until it loses those temporary hit points
or the duration expires. During this time, the creature counts as undead, but it can't be healed by
negative energy. The spirit walker can use this ability once per day for every 3 mesmerist levels he
possesses. The target receives a Will saving throw (DC = 10 + 1/2 the spirit walker's class level +
his Charisma modifier) to avoid this effect and die normally. This ability ends immediately if at
any point the target's body is completely destroyed (such as by
_[disintegrate](ref/spell/disintegrate)_) or restored to life. At 14th level, the spirit walker can
apply this ability to any type of target as if using
_[dominate monster](ref/spell/dominate-monster)_. This ability replaces the 3rd- and 14th-level
touch treatments.

## Command Undead (Su) {#command-undead}

At 6th level, a spirit walker gains [Command Undead](ref/feat/command-undead) as a bonus feat. A
spirit walker can use Command Undead a number of times per day equal to 1 + his Charisma modifier
(minimum 1), using his mesmerist level as his cleric level. At 10th level, the DC to resist this
effect increases by 2. This ability replaces the 6th- and 10th-level touch treatments.

## Master of the Dead (Su) {#master-of-the-dead}

At 20th level, a spirit walker gains mastery of the undead. Once per day, a spirit walker can use
_[control undead](ref/spell/control-undead)_ as a [spell-like ability](ref/umr/spell-like-abilities)
on one target. If that creature fails its saving throw and has 20 or fewer Hit Dice, it falls
permanently under the spirit walker's control until the spirit walker dies. A creature that fails
its save but has more than 20 HD suffers the effect of _[command undead](ref/spell/command-undead)_.
A creature that succeeds at its save can't be affected by master of the dead for 24 hours. A spirit
walker can control only one undead creature in this fashion at a time. If he permanently controls a
new undead creature, the previous one is set free. This ability replaces rule minds.
