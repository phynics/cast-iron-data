+++
id = "ref/arc-fighter/mutation-warrior"
kind = "archetype"
title = "Mutation Warrior"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Mutation%20Warrior"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mutation_warrior", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "93"

[fields]
kind = "archetype"
features = [
  { anchor = "mutagen", level = 3 },
  { anchor = "mutagen-discovery", level = 7 },
]
trades = [
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["mutagen"] },
  { replaces = "Armor training 2, 3, 4", feature = "armor-training", levels = [7, 11, 15], by = ["mutagen-discovery"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["mutagen-discovery"] },
]
+++

While most fighters rely on physical fitness and rigorous training to achieve martial superiority, a
few prefer to create and imbibe dangerous concoctions that mutate them into fearsome creatures.

## Mutagen (Su) {#mutagen}

At 3rd level, a mutation warrior discovers how to create a mutagen that he can imbibe in order to
heighten his physical prowess at the cost of his personality. This ability functions as the
[alchemist's](ref/class/alchemist) mutagen ability (_Advanced Player's Guide_ 28), using his fighter
level as his alchemist level. This ability replaces armor training 1.

## Mutagen Discovery (Su) {#mutagen-discovery}

At 7th level and every 4 levels thereafter, the mutation warrior can choose one of the following
alchemist discoveries (_Advanced Player's Guide_ 28) to augment his abilities:
[feral mutagen](ref/discovery/feral-mutagen), [grand mutagen](ref/discovery/grand-mutagen),
[greater mutagen](ref/discovery/greater-mutagen), [infuse mutagen](ref/discovery/infuse-mutagen),
[nauseating flesh](ref/discovery/nauseating-flesh),
[preserve organs](ref/discovery/preserve-organs),
[rag doll mutagen](ref/discovery/rag-doll-mutagen),
[spontaneous healing](ref/discovery/spontaneous-healing), [tentacle](ref/discovery/tentacle),
[vestigial arm](ref/discovery/vestigial-arm), [wings](ref/discovery/wings). The mutagen warrior uses
his fighter level as his effective alchemist level for the purpose of these discoveries. This
ability replaces armor training 2, 3, 4, and armor mastery.
