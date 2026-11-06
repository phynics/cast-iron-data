+++
id = "ref/ragepower/spell-sunder"
kind = "rule"
title = "Spell Sunder"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_sunder", path = "json/class_ability_rage_powers.json" },
]

[fields]
kind = "none"
+++

**&L&Spell Sunder (Su)&FN&**

**Ability:** Once per _rage,_ the barbarian can attempt to [sunder](ref/rule/sunder) an ongoing
spell effect by succeeding at a combat maneuver check.

For any effect other than one on a creature, the barbarian must make her combat maneuver check
against a CMD of 15 plus the effect's caster level. To sunder an effect on a creature, the barbarian
must succeed at a normal sunder combat maneuver against the creature's CMD + 5, ignoring any miss
chance caused by a spell or [spell-like ability](ref/umr/spell-like-abilities).

If successful, the barbarian suppresses the effect for 1 round, or 2 rounds if she exceeded the CMD
by 5 to 9. If she exceeds the CMD by 10 or more, the effect is dispelled.

**Prereq:** 6th-level barbarian, [witch hunter](ref/ragepower/witch-hunter)
