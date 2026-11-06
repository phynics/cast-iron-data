+++
id = "ref/arc-witch/witch-watcher"
kind = "archetype"
title = "Witch-Watcher"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "witch_watcher", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]

[fields]
kind = "none"
+++

**Sources:** Heroes of the High Court pg 9\
For reasons known only to them, witch-watchers offer protection to nobles across Golarion. While
they serve openly in Irrisen and Varisia, they watch from the shadows in courts in Brevoy, Mendev,
the River Kingdoms, and Ustalav, where their presence is barely tolerated.

**Diminished Spellcasting**

**Alters:** Spellcasting

**Info:** A witch-watcher gains one fewer spell of each level than normal. If this reduces the
number to zero, she can cast spells of that level only if her Intelligence score is high enough to
grant [bonus spells](ref/rule/determine-bonuses) of that level.

**Covenant Ally (Su)**

**Ability:** Once per day when preparing her spells, a witch-watcher makes a covenant with her
patron to provide protection to a single creature, known as her _covenant ally._

**Special:** Unless otherwise noted, each ability lasts for a number of minutes equal to the
witch-watcher's Intelligence modifier. She can grant a number of abilities per day equal to 1/2 her
witch level (minimum 1).

**Standard:** When her _covenant ally_ is within 30 feet, a witch-watcher can grant it one of the
abilities listed below.

**Health**

**Ability:** The _covenant ally_ gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to the witch-watcher's witch level + her
Intelligence modifier (minimum 1). The temporary hit points from this ability do not stack with
themselves, but additional uses cause the total number of temporary hit points and the duration to
reset.

**Safeguard**

**Passive:** The _covenant ally_ gains a deflection bonus to AC or a resistance bonus on saving
throws equal to 1/2 the witch-watcher's witch level (minimum 1). When given, this bonus can be
divided between the AC and saving throws as the witch-watcher wishes, up to a maximum of +5 for
either.

**Solace**

**Ability:** The witch-watcher temporarily disrupts a spell affecting her _covenant ally_ by
succeeding at a dispel check against the spell, as per [dispel magic](ref/spell/dispel-magic). The
ability suppresses a spell effect for a number of rounds equal to the witch-watcher's Intelligence
modifier (minimum 1). If the spell affects multiple creatures, this ability suppresses the spell
effect only for the _covenant ally._

At the end of this duration, the spell resumes and the suppressed rounds do not count against its
total duration.

**Special:** This ability has no effect on spells that are instantaneous or have a duration of
permanent.

**Spell Resistance**

**At 10th Level:** The [spell resistance](ref/rule/spell-resistance) increases to 11 + the
witch-watcher's witch level.

**Passive:** The _covenant ally_ gains [spell resistance](ref/rule/spell-resistance) equal to 6 +
the witch-watcher's witch level for a number of rounds equal to the witch-watcher's Intelligence
modifier.

**Special:** The [spell resistance](ref/rule/spell-resistance) cannot be suppressed, but it doesn't
affect spells cast by the witch-watcher.
