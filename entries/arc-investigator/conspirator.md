+++
id = "ref/arc-investigator/conspirator"
kind = "archetype"
title = "Conspirator"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Conspirator"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conspirator", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "33"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Trap sense", "investigator talent gained at 7th level"]
alters = ["Inspiration"]
+++

A conspirator uses his knowledge of investigations to make sure he avoids any investigations that
his rivals perform, carefully plotting acts of intrigue behind closed doors. Paranoid to a fault, a
conspirator always seems to know when someone else is watching him, and he takes numerous
precautions to prevent anyone from observing his most illict actions.

**Underhanded (Ex)**

**Ability:** A conspirator can use _inspiration_ on any Bluff, Disable Device, Disguise, Intimidate,
and Sleight of Hand check without expending a use of _inspiration,_ provided he is trained in the
skill, instead of on any Knowledge, Linguistics, and Spellcraft check. He can later choose to trade
an investigator talent for the ability to use _inspiration_ on any Knowledge, Linguistics, and
Spellcraft check without expending a use of inspirtation, provided he is trained in the skill.

**Alters:** Inspiration

**Flavor:** Conspirators find their skill sets firmly aligned with the goals of the criminal
underworld.

**Gained:** At 1st Level

**Passive:** A conspirator adds half his investigator level (minimum 1) on Bluff checks to appear
innocent and on Disguise checks.

**Replaces:** Trapfinding

**Watcher Sense (Ex)**

**Ability:** A conspirator is able to sense when someone else is watching him. He gains a bonus on
Perception checks to notice [scrying](ref/spell/scrying) sensors,
[prying eyes](ref/spell/prying-eyes), and other magical effects used to watch him, as well as on
Perception checks to act on the surprise round. This bonus is equal to one-third of his investigator
level.

**At 7th Level:** If a scrying sensor is invisible, the invisibility does not increase the DC of the
conspirator's Perception check to notice it, regardless of whether or not he is using an ability
that allows him to see invisible things. The DC for his Perception check is equal to 20 + the
spell's level (with no +20 increase to the Perception DC for a moving invisible sensor or no +40
increase for an immobile invisible sensor).

**Gained:** At 3rd Level

**Replaces:** Trap sense, investigator talent gained at 7th level
