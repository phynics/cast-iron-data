+++
id = "ref/arc-inquisitor/expulsionist"
kind = "archetype"
title = "Expulsionist"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Expulsionist"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "expulsionist", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "expel-spirit", level = 1 },
  { anchor = "expulsionist-lore", level = 1 },
  { anchor = "spirit-sleuth", level = 5 },
]
trades = [
  { replaces = "Domain", feature = "domain", by = ["expel-spirit"] },
  { replaces = "Monster lore", feature = "monster-lore", by = ["expulsionist-lore"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["spirit-sleuth"] },
]
+++

Most common among [Pharasmins](ref/faith/pharasma) but found within any faith that loathes undead or
evil spirits, expulsionists are inquisitors who seek to rid the material world of the corrupting
influences of wicked spirits that twist mortals to their own ends.

## Expel Spirit (Su) {#expel-spirit}

At 1st level, an expulsionist receives [Alignment Channel](ref/feat/alignment-channel) and
[Turn Undead](ref/feat/turn-undead) as bonus feats. She can
[channel energy](ref/ability/channel-energy) a number of times per day equal to 3 + her Charisma
modifier as per a cleric with an effective level equal to her inquisitor level, but only to harm or
turn evil outsiders or undead (treating all evil outsiders as undead creatures for the purpose of
determining whether they can be affected by Turn Undead). She can take other feats that add to this
ability, such as [Extra Channel](ref/feat/extra-channel) or
[Improved Channel](ref/feat/improved-channel), but not other feats that fundamentally alter this
ability, such as [Elemental Channel](ref/feat/elemental-channel), and she cannot select Alignment
Channel multiple times. The DC to save against this ability is equal to 10 + 1/2 the expulsionist's
inquisitor level + her Charisma modifier.

At 8th level, an expulsionist can expend one use of her channel energy ability to attempt to force a
possessing creature from its host body. The expulsionist must make a melee touch attack against the
possessed creature; if successful, the expulsionist deals damage to the possessing creature as if it
were targeted by the expulsionist's channel energy ability (regardless of the possessing creature's
creature type), and the possession effect ceases as the possessing creature is ejected from the host
body. A successful Will save (DC = the expulsionist's channel energy DC) halves the damage taken and
negates the expulsion.

This ability replaces domain.

## Expulsionist Lore (Ex) {#expulsionist-lore}

At 1st level, an expulsionist gains a bonus equal to 1/2 her inquisitor level (minimum +1) on skill
checks to notice [haunts](ref/rule/haunts) and incorporeal creatures; on Knowledge (religion) checks
to identify the abilities and weaknesses of haunts and incorporeal creatures; and on Sense Motive
checks to determine whether a creature is possessed, under the effects of an enchantment or curse,
or otherwise magically controlled.

This ability replaces monster lore.

## Spirit Sleuth (Ex) {#spirit-sleuth}

At 5th level, upon interacting with a rejuvenating undead (such as a [ghost](ref/template/ghost)) or
haunt for the first time (such as by attacking the ghost or channeling energy to damage the haunt),
an expulsionist can attempt a Sense Motive check as a free action to determine the specific course
of action required to permanently neutralize the spirit of haunt (DC = 20 + the target's CR).

This ability replaces discern lies.
