+++
id = "ref/arc-cleric/appeaser"
kind = "archetype"
title = "Appeaser"
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
alters = ["Aura", "Channel energy", "Alignment", "spells", "Domains"]
alters_features = ["aura", "channel-energy", "spells", "domains"]
+++

A rare few seek the power of dark forces for brighter ends by focusing on the utilitarian aspects of
a god's portfolio, appeasing their deities through high praise and glorifying their chosen gods'
unaligned aspects.

**Aura (Ex)**

**Alters:** Aura

**Info:** An appeaser always has an evil aura regardless of his actual alignment.

**Channel Utility (Su)**

**Alters:** Channel energy

**At 5th Level:** An appeaser can channel positive energy as a **full-round action**, but he treats
his cleric level as if it were 4 lower when determining the amount of damage he can deal to undead
and the amount of hit points he can restore to living creatures.

**Info:** An appeaser channels negative energy, but also gains limited access to positive energy.

**Divine Apologist (Ex)**

**Alters:** Alignment, spells

**Info:** An appeaser must worship an evil god. His alignment must be within one step of his
deity's, but he himself cannot have an evil alignment. An appeaser cannot cast any spells with the
good or evil descriptor.

**Mollified Domain (Su)**

**Alters:** Domains

**Info:** An appeaser gains no domain or domain bonus spells.

**Special:** An appeaser can invoke only a single mollified domain at a time.

**Standard:** He can sacrifice his own force of will to gain divine providence. Doing so deals 1d3
points of [Charisma damage](ref/rule/ability-damage-drain) to the appeaser, and allows him to select
a single domain offered by his deity (except the Evil domain or its subdomains). The appeaser gains
access to any granted powers offered by the domain he would otherwise qualify for, and can sacrifice
a prepared spell to cast a domain spell from that domain just as if he were spontaneously casting a
_cure_ or _inflict_ spell. He retains access to this domain for a number of minutes equal to
[half](ref/misc/fractions-and-rounding) the appeaser's cleric level + plus his Wisdom modifier. Any
domain abilities that can be used a limited number of times per day can be used only once each time
that particular domain is invoked.

**Usage:** 1 time/day + 1 per 3 cleric levels beyond 1st
