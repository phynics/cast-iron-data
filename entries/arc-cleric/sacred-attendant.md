+++
id = "ref/arc-cleric/sacred-attendant"
kind = "archetype"
title = "Sacred Attendant"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Sacred%20Attendant"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_attendant", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "healers-handbook"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-beauty" },
  { anchor = "domains" },
  { anchor = "nimble" },
  { anchor = "nurture-grace" },
  { anchor = "inspiring-camaraderie", level = 8 },
]
trades = [
  { replaces = "Proficiency with light", feature = "weapon-and-armor-proficiencies", power = "light armor", by = ["nimble"] },
  { replaces = "medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["nimble"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-beauty"] },
  { alters = "Domains", feature = "domains", by = ["domains"] },
]
+++

Sacred attendants bring out the varied beauty in everyone they help, and they typically worship
deities of beauty, love, and sex.

## Channel Beauty (Su) {#channel-beauty}

Whenever a sacred attendant channels energy to heal, she can opt to reduce the number of dice she
rolls by 1 or more. For every die the sacred attendant subtracts, each of the targets of the
channeled energy is healed of 1 point of [Charisma damage](ref/rule/ability-damage-drain).

This ability alters channel energy.

## Domains {#domains}

The sacred attendant can choose only one domain from those belonging to her deity.

This ability alters domains.

## Nimble (Ex) {#nimble}

The sacred attendant gains a +1 dodge bonus to AC and CMD when unarmored, unencumbered, and not
denied her Dexterity bonus to AC (regardless of whether she has a Dexterity bonus). At 2nd level and
every 4 cleric levels thereafter, the dodge bonus increases by 1 (to a maximum of +6 at 18th level).

This ability replaces the cleric's proficiency with light and medium armor.

## Nurture Grace (Su) {#nurture-grace}

The sacred attendant can coax forth the charm and beauty within a willing, touched creature as a
standard action. For 1 round, the subject gains an enhancement bonus equal to 1/2 the sacred
attendant's cleric level (minimum +1) on Charisma checks and Charisma-based skill checks. The sacred
attendant can spend two uses of this ability to instead counsel a subject for 10 minutes; in this
case, the ability's duration lasts for 1 day. The sacred attendant can use this ability a number of
times per day equal to 3 + her Wisdom modifier.

## Inspiring Camaraderie (Sp) {#inspiring-camaraderie}

At 8th level, as a swift action whenever a sacred attendant casts a cure spell (a spell with "cure"
in its name) that targets a single ally, the sacred attendant can infuse that ally with inspired
vigor. For a number of rounds equal to 1/2 the sacred attendant's cleric level, the ally's attack
rolls gain a competence bonus equal to the sacred attendant's cleric level. These rounds begin as
soon as the sacred attendant uses this ability and elapse consecutively. The sacred attendant can
use this ability once per day at 8th level, and an additional time per day for every 4 cleric levels
beyond 8th.
