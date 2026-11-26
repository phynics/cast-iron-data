+++
id = "ref/arc-bard/dirge-bard"
kind = "archetype"
title = "Dirge Bard"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Dirge%20Bard"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dirge_bard", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "dance-of-the-dead", level = 10 },
  { anchor = "haunted-eyes", level = 2 },
  { anchor = "secrets-of-the-grave", level = 2 },
  { anchor = "haunting-refrain", level = 5 },
]
trades = [
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["dance-of-the-dead"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["haunted-eyes"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["secrets-of-the-grave"] },
  { replaces = "Lore master", feature = "lore-master", by = ["haunting-refrain"] },
]
+++

A composer of sonorous laments for the dead and elaborate requiems for those lost yet long
remembered, dirge bards master musical tools and tropes that must appeal to the ears and hearts of
both the living and the dead.

## Bardic Performance {#bardic-performance}

A dirge bard gains the following type of bardic performance.

## Dance of the Dead (Su) {#dance-of-the-dead}

At 10th level, a dirge bard can use his bardic performance to cause dead bones or bodies to rise up
and move or fight at his command. This ability functions like
_[animate dead](ref/spell/animate-dead)_, but the created skeletons or zombies remain fully animate
only as long as the dirge bard continues the performance. Once it stops, any created undead collapse
into carrion. Bodies or bones cannot be animated more than once using this ability. Unlike
_[animate dead](ref/spell/animate-dead)_, dance of the dead requires no components and does not have
the evil descriptor. This performance replaces jack-of-all-trades.

## Haunted Eyes (Ex) {#haunted-eyes}

At 2nd level, a dirge bard gains a +4 bonus on saves against fear, energy drain, death effects, and
necromantic effects. This ability replaces well-versed.

## Secrets of the Grave (Ex) {#secrets-of-the-grave}

At 2nd level, a dirge bard gains a bonus equal to [half](ref/misc/fractions-and-rounding) his bard
level on Knowledge (religion) checks made to identify undead creatures and their abilities. A dirge
bard may use mind-affecting spells to affect undead as if they were living creatures, even if they
are mindless (though spells that affect only humanoids do not affect them, even if they were
humanoids in life). In addition, he may add one necromancy spell from the spell list of any arcane
spellcasting class to his list of spells known at 2nd level and every four levels thereafter. This
ability replaces versatile performance.

## Haunting Refrain (Su) {#haunting-refrain}

At 5th level, a dirge bard is able to stir primal terrors in the hearts of listeners. He can use a
Perform (keyboard) or Perform (percussion) check in place of an Intimidate check to demoralize an
opponent, with a bonus equal to half his bard level. In addition, saving throws against any fear
effect he creates are made with a -2 penalty, and this penalty increases by -1 every 5 levels beyond
5th. This ability replaces lore master.
