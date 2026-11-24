+++
id = "ref/arc-alchemist/preservationist"
kind = "archetype"
title = "Preservationist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Preservationist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "preservationist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "bottled-ally-i", level = 2 },
  { anchor = "bottled-ally-ii", level = 5 },
  { anchor = "bottled-ally-iii", level = 8 },
  { anchor = "bottled-ally-iv", level = 10 },
  { anchor = "bottled-ally-v", level = 14 },
  { anchor = "bottled-ally-vi", level = 18 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["bottled-ally-i"] },
  { replaces = "Poison resistance +4", feature = "poison-resistance", levels = [5], by = ["bottled-ally-ii"] },
  { replaces = "Poison resistance +6", feature = "poison-resistance", levels = [8], by = ["bottled-ally-iii"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["bottled-ally-iv"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["bottled-ally-v"] },
  { replaces = "18th-level discovery", feature = "discovery", levels = [18], by = ["bottled-ally-vi"] },
]
+++

Some alchemists are obsessed with collecting and preserving exotic creatures. These preservationists
may use bottled animals and monsters as teaching tools, but some learn how to reanimate them for
short periods to battle on the alchemist's behalf. A preservationist has the following class
features.

## Bottled Ally I {#bottled-ally-i}

At 2nd level, a preservationist adds [Handle Animal](ref/skill/handle-animal) to his list of class
skills. He adds _[summon nature's ally I](ref/spell/summon-natures-ally-1)_ to his formula book as a
1st-level extract. When he prepares that extract, he actually prepares a tiny, preserved specimen in
a bottle (as with a caster casting the spell, the preservationist doesn't have to choose the
creature until he uses the extract). When the alchemist opens the bottle, the specimen animates and
grows to normal size, serving the preservationist as per the spell and otherwise being treated as a
summoned creature. When the duration expires, the preserved creature decays into powder. If the
preservationist has the [infusion](ref/discovery/infusion) discovery, another character can use the
infused specimen. The [Augment Summoning](ref/feat/augment-summoning) feat can be applied to these
specimens. This ability replaces poison use.

## Bottled Ally II {#bottled-ally-ii}

At 5th level, a preservationist adds _[summon nature's ally II](ref/spell/summon-natures-ally-2)_ to
his formula book as a 2nd-level extract. This ability replaces poison resistance +4.

## Bottled Ally III {#bottled-ally-iii}

At 8th level, a preservationist adds _[summon nature's ally IV](ref/spell/summon-natures-ally-4)_ to
his formula book as a 3rd-level extract. This ability replaces poison resistance +6.

## Bottled Ally IV {#bottled-ally-iv}

At 10th level, a preservationist adds _[summon nature's ally V](ref/spell/summon-natures-ally-5)_ to
his formula book as a 4th-level extract. This ability replaces poison immunity.

## Bottled Ally V {#bottled-ally-v}

At 14th level, a preservationist adds _[summon nature's ally VII](ref/spell/summon-natures-ally-7)_
to his formula book as a 5th-level extract. This ability replaces persistent mutagen.

## Bottled Ally VI {#bottled-ally-vi}

At 18 level, a preservationist adds _[summon nature's ally IX](ref/spell/summon-natures-ally-9)_ to
his formula book as a 6th-level extract. This ability replaces his 18th-level discovery.

## Discoveries {#discoveries}

The following discoveries complement the preservationist archetype:
[bottled ooze](ref/discovery/bottled-ooze), [preserve organs](ref/discovery/preserve-organs),
[tentacle](ref/discovery/tentacle), [vestigial arm](ref/discovery/vestigial-arm), and
[wings](ref/discovery/wings).
