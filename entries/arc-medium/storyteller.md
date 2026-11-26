+++
id = "ref/arc-medium/storyteller"
kind = "archetype"
title = "Storyteller"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Storyteller"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storyteller", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "occult-adventures"
page = "95"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spirits", level = 1 },
  { anchor = "knowledge-of-tales", level = 1 },
  { anchor = "versatile-surge", level = 1 },
  { anchor = "storyteller-s-performance", level = 2 },
  { anchor = "learn-the-story", level = 7 },
  { anchor = "living-story", level = 20 },
]
trades = [
  { replaces = "Spirit bonus", feature = "spirit-bonus", by = ["knowledge-of-tales"] },
  { replaces = "Shared seance", feature = "shared-seance", by = ["storyteller-s-performance"] },
  { replaces = "taboo", feature = "taboo", by = ["storyteller-s-performance"] },
  { replaces = "haunt channeler", feature = "haunt-channeler", by = ["storyteller-s-performance"] },
  { replaces = "propitiation", feature = "propitiation", by = ["storyteller-s-performance"] },
  { replaces = "trance of three", feature = "trance-of-three", by = ["storyteller-s-performance"] },
  { replaces = "Connection channel", feature = "connection-channel", by = ["learn-the-story"] },
  { replaces = "spirit mastery", feature = "spirit-mastery", by = ["learn-the-story"] },
  { replaces = "Astral beacon", feature = "astral-beacon", by = ["living-story"] },
  { alters = "Spirit", feature = "spirit", by = ["diminished-spirits"] },
  { alters = "Spirit surge", feature = "spirit-surge", by = ["versatile-surge"] },
]
+++

While all mediums connect to legendary spirits, storyteller mediums take their obsession with
legends to the extreme, suffusing their lives with epic tales at the cost of some of their spiritual
power.

## Diminished Spirits (Ex) {#diminished-spirits}

A storyteller does not receive his spirit's seance boon. He can't choose to channel a weaker spirit
to reduce his influence from spirit surge. Because of his obsession with legends, he begins with 2
points of influence after a seance rather than 1.

This ability alters spirit.

## Knowledge of Tales (Ex) {#knowledge-of-tales}

A storyteller gains a +1 bonus on all Knowledge skill checks with Knowledge skills in which he's
trained. This bonus increases by 1 for every 4 medium levels that he possesses.

This ability replaces spirit bonus.

## Versatile Surge (Su) {#versatile-surge}

A storyteller's spirit surge can be used after the storyteller fails any ability check, skill check,
or saving throw.

This ability alters spirit surge.

## Storyteller's Performance (Su) {#storyteller-s-performance}

At 2nd level, a storyteller gains the ability to recall snippets of tales that are relevant to the
current situation. This ability is similar in all respects to bardic performance as used by a bard
of the storyteller's medium level (including interactions with feats, spells, and other abilities),
and uses Perform (act), Perform (comedy), or Perform (oratory) as the storyteller's performance
skill. However, a storyteller gains only the following types of bardic performance:
[inspire courage](ref/performance/inspire-courage) (2nd level),
[inspire competence](ref/performance/inspire-competence) (3rd level),
[inspire greatness](ref/performance/inspire-greatness) (9th level), and
[inspire heroics](ref/performance/inspire-heroics) (15th level).

This ability replaces shared seance, taboo, haunt channeler, propitiation, and trance of three.

## Learn the Story (Sp) {#learn-the-story}

At 7th level, a storyteller becomes a master at learning a place's tales. He can perform for a full
minute, spending 10 rounds of storyteller's performance, to gain the effects of
_[retrocognition](ref/spell/retrocognition)_. At 10th level, he can spend 1d4 × 10 minutes and 10
rounds of storyteller's performance to gain the effects of _[legend lore](ref/spell/legend-lore)_.
The subject must be at hand for the _legend lore_ to function. At 19th level, the storyteller can
spend a standard action and 1 round of storyteller's performance to gain the effects of
_[vision](ref/spell/vision)_ on any subject. This ability replaces connection channel and spirit
mastery.

## Living Story (Sp) {#living-story}

At 20th level, a storyteller gains the ability to sweep others away into a story of his own making.
He must perform for 1 full round, telling a tale to set the snare for his living story and spending
1 round of his storyteller's performance. At the end of that round, he can affect up to 30 Hit Dice
of listeners within range with _[microcosm](ref/spell/microcosm)_. Unlike with a normal
_[microcosm](ref/spell/microcosm)_, this is also a sonic and language-dependent ability, and a
creature with 16 or more Hit Dice that succeeds at its save is immune to the storyteller's living
story ability for 24 hours.

This ability replaces astral beacon.
