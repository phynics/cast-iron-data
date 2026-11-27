+++
id = "ref/arc-cleric/appeaser"
kind = "archetype"
title = "Appeaser"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Appeaser"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "appeaser", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "agents-of-evil"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "aura", level = 1 },
  { anchor = "channel-utility", level = 5 },
  { anchor = "divine-apologist" },
  { anchor = "mollified-domain", level = 1 },
]
trades = [
  { alters = "Aura", feature = "aura", by = ["aura"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-utility"] },
  { alters = "Alignment", by = ["divine-apologist"] },
  { alters = "spells", feature = "spells", by = ["divine-apologist"] },
  { alters = "Domains", feature = "domains", by = ["mollified-domain"] },
]
+++

A rare few seek the power of dark forces for brighter ends by focusing on the utilitarian aspects of
a god's portfolio, appeasing their deities through high praise and glorifying their chosen gods'
unaligned aspects.

## Aura (Ex) {#aura}

An appeaser always has an evil aura regardless of his actual alignment. This alters aura.

## Channel Utility (Su) {#channel-utility}

An appeaser channels negative energy, but also gains limited access to positive energy. At 5th
level, an appeaser can channel positive energy as a full-round action, but he treats his cleric
level as if it were 4 lower when determining the amount of damage he can deal to undead and the
amount of hit points he can restore to living creatures. This ability alters channel energy.

## Divine Apologist (Ex) {#divine-apologist}

An appeaser must worship an evil god. His alignment must be within one step of his deity's, but he
himself cannot have an evil alignment. An appeaser cannot cast any spells with the good or evil
descriptor. This alters the cleric's alignment and spells.

## Mollified Domain (Su) {#mollified-domain}

At 1st level, an appeaser gains no domain or domain bonus spells. Once per day as a standard action,
he can sacrifice his own force of will to gain divine providence. Doing so deals 1d3 points of
[Charisma damage](ref/rule/ability-damage-drain) to the appeaser, and allows him to select a single
domain offered by his deity (except the Evil domain or its subdomains). The appeaser gains access to
any granted powers offered by the domain he would otherwise qualify for, and can sacrifice a
prepared spell to cast a domain spell from that domain just as if he were spontaneously casting a
cure or inflict spell. He retains access to this domain for a number of minutes equal to 1/2 the
appeaser's cleric level plus his Wisdom modifier. Any domain abilities that can be used a limited
number of times per day can be used only once each time that particular domain is invoked.

An appeaser can gain a mollified domain one additional time per day (taking Charisma damage each
time) at 4th level and every 3 levels thereafter, to a maximum of seven times per day at 19th level.
An appeaser can invoke only a single mollified domain at a time.

This ability modifies the cleric's domains class feature.
