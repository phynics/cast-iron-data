+++
id = "ref/arc-medium/spirit-dancer"
kind = "archetype"
title = "Spirit Dancer"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_dancer", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "occult-adventures"
page = "94"

[fields]
kind = "archetype"
replaces = ["Spirit bonus", "spirit surge", "Shared seance", "Trance of three", "Spacious soul", "Astral beacon"]
alters = ["Spirit"]
replaces_features = ["spirit-bonus", "spirit-surge", "shared-seance", "trance-of-three", "spacious-soul", "astral-beacon"]
alters_features = ["spirit"]
+++

A spirit dancer enacts an exuberant dance to the spirits, accepting many roles in the shifting dance
and changing dance partners quickly.

**Spirit Dance (Su)**

**Action:** Ability

**Alters:** Spirit

**Replaces:** Spirit bonus, spirit surge

Each day during his _seance,_ a spirit dancer makes all his spirit power choices as if he were
channeling one spirit of each of the six legends. He can't choose to channel a weaker spirit to
reduce his influence from _spirit surge._ He does not always possess the _seance_ boon, spirit
bonus, spirit powers, or _spirit surge_ ability from any of these six spirits.

Instead, he can enter a spirit dance as a **free action** to gain the aforementioned abilities from
one of the six spirits he prepared during his _seance_ for the duration of his spirit dance. He can
spirit dance for a total number of rounds per day equal to his Charisma modifier + double his medium
level; these rounds don't need to be consecutive.

After his spirit dance ends, the spirit dancer takes a -2 penalty on attack rolls, saving throws,
and skill checks for 1 minute and can't enter a spirit dance again during that time. He also can't
enter a spirit dance while [shaken](ref/misc/shaken), [frightened](ref/misc/frightened), or
[panicked](ref/misc/panicked).

He combines all influence incurred during spirit dances into a single pool. At 3 points of influence
or higher, he takes a -2 penalty on initiative checks even when he's not in a spirit dance, and at 5
points of influence or higher, his current spirit takes control as it would for a normal medium
(this control is not limited by rounds of spirit dance). A spirit dancer can accept 1 point of
influence to recover 4 rounds of spirit dance, up to his normal daily maximum.

A spirit dancer continues to track daily uses of abilities from each of his spirits even while he is
not in a spirit dance. A spirit dancer with the _supreme spirit power_ ability can use only one
once-per-day ability from the _supreme spirit power_ each day; he can't use any other spirit's
once-per-day _supreme spirit power_ until after his next _seance._

**Nothing Is Taboo (Ex)**

**Ability:** A spirit dancer doesn't gain the _taboo_ class feature.

**Spirit Aura (Su)**

**Ability:** A spirit dancer's weaving forms create an aura that grants his current _seance_ boon to
all allies within 30 feet.

**Gained:** At 2nd Level

**Replaces:** Shared seance

**Special:** When he grants a _seance_ boon that requires a decision, each ally makes the
appropriate decision the first time that ally receives that spirit's aura each day. That decision
remains in effect if the ally is affected by that spirit's aura again later that day.

**Spirit Troika (Su)**

**Ability:** A spirit dancer learns to dance with two partners. When using _spirit dance,_ he can
choose to spend 3 rounds of spirit dance each round to gain access to the abilities of any two of
the six spirits he prepared during his _seance_ for 1 round.

**Gained:** At 15th Level

**Replaces:** Trance of three

**Attacca (Su)**

**Ability:** A spirit dancer learns how to shift rapidly into the next movement of his dance. He no
longer takes a penalty after his _spirit dance_ ends and can enter another _spirit dance_
immediately.

**Gained:** At 18th Level

**Replaces:** Spacious soul

**Dance of Infinite Forms (Su)**

**Ability:** A spirit dancer has perfected his dance. He can now use each of his _supreme spirit
powers'_ once-per-day abilities one time each day, instead of just one ability. He can use his
_spirit troika_ by spending 2 rounds of _spirit dance_ instead of 3. Finally, he can enter a _spirit
dance_ with all six of his prepared spirits at once by spending 4 rounds of _spirit dance_ each
round.

**Gained:** At 20th Level

**Replaces:** Astral beacon
