+++
id = "ref/arc-medium/storyteller"
kind = "archetype"
title = "Storyteller"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storyteller", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]

[fields]
kind = "archetype"
replaces = ["Spirit bonus", "Shared seance", "taboo", "haunt channeler", "propitiation", "trance of three", "Connection channel", "spirit mastery", "Astral beacon"]
alters = ["Spirit", "Spirit surge"]
+++

**Sources:** Occult Adventures pg 95\
While all mediums connect to legendary spirits, storyteller mediums take their obsession with
legends to the extreme, suffusing their lives with epic tales at the cost of some of their spiritual
power.

**Diminished Spirits (Ex)**

**Alters:** Spirit

**Info:** A storyteller does not receive his spirit's _seance_ boon. He can't choose to channel a
weaker spirit to reduce his influence from _spirit surge._ Because of his obsession with legends, he
begins with 2 points of influence after a _seance_ rather than 1.

**Knowledge of Tales (Ex)**

**Passive:** A storyteller gains a bonus on all Knowledge skill checks with Knowledge skills in
which he's trained. This bonus is equal to 1 + one-fourth of his medium level.

**Replaces:** Spirit bonus

**Versatile Surge (Su)**

**Ability:** A storyteller's _spirit surge_ can be used after the storyteller fails any ability
check, skill check, or saving throw.

**Alters:** Spirit surge

**Storyteller's Performance (Su)**

**Ability:** A storyteller gains the ability to recall snippets of tales that are relevant to the
current situation. This ability is similar in all respects to bardic performance as used by a bard
of the storyteller's medium level (including interactions with feats, spells, and other abilities),
and uses Perform (act), Perform (comedy), or Perform (oratory) as the storyteller's performance
skill. However, a storyteller gains only the following types of bardic performance:
[inspire courage](ref/performance/inspire-courage) (2nd level),
[inspire competence](ref/performance/inspire-competence) (3rd level),
[inspire greatness](ref/performance/inspire-greatness) (9th level), and
[inspire heroics](ref/performance/inspire-heroics) (15th level).

**Gained:** At 2nd Level

**Replaces:** Shared seance, taboo, haunt channeler, propitiation, trance of three

**Learn the Story (Sp)**

**At 10th Level:** He can spend 1d4 &times& 10 minutes and 10 rounds of _storyteller's performance_
to gain the effects of [legend lore](ref/spell/legend-lore). The subject must be at hand for the
\*legend lore \*to function.

**At 19th Level:** The storyteller can spend a **standard action** and 1 round of _storyteller's
performance_ to gain the effects of [vision](ref/spell/vision) on any subject.

**At 7th Level:** A storyteller becomes a master at learning a place's tales. He can perform for a
full minute, spending 10 rounds of _storyteller's performance,_ to gain the effects of
[retrocognition](ref/spell/retrocognition).

**Replaces:** Connection channel, spirit mastery

**Living Story (Sp)**

**Ability:** A storyteller gains the ability to sweep others away into a story of his own making. He
must perform for 1 full round, telling a tale to set the snare for his _living story_ and spending 1
round of his _storyteller's performance._ At the end of that round, he can affect up to 30 Hit Dice
of listeners within range with [microcosm](ref/spell/microcosm). Unlike with a normal
_[microcosm](ref/spell/microcosm),_ this is also a sonic and language-dependent ability, and a
creature with 16 or more Hit Dice that succeeds at its save is immune to the storyteller's _living
story_ ability for 24 hours.

**Gained:** At 20th Level

**Replaces:** Astral beacon
