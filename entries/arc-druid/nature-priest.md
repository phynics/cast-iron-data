+++
id = "ref/arc-druid/nature-priest"
kind = "archetype"
title = "Nature Priest"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nature_priest", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "healers-handbook"
page = "23"

[fields]
kind = "archetype"
replaces = ["Nature sense", "Resist nature's lure", "Venom immunity"]
alters = ["Weapon proficiencies", "Nature bond"]
replaces_features = ["nature-sense", "resist-nature-s-lure", "venom-immunity"]
alters_features = ["nature-bond"]
+++

Nature priests serve two masters: their deities and nature itself, and can call upon the power of
both to fuel their divine abilities.

**Prerequisites:** Like a cleric, a nature priest must worship a deity and her alignment must be
within one step of her deity's.

**Gained class skills:** kr

**Lost class skills:** kg

**Weapon Proficiencies**

**Alters:** Weapon proficiencies

**Info:** A nature priest is proficient with her deity's favored weapon in addition to a druid's
typical weapon proficiencies.

**Studious Piety (Ex)**

**Passive:** A nature priest gains a +1 bonus on Knowledge (religion) checks. This bonus increases
to +2 when attempting checks that involve knowledge of her deity or her faith.

**Replaces:** Nature sense

**Chosen Druid (Ex)**

**Alters:** Nature bond

**Choice:** If a nature priest chooses a domain for her _nature bond,_ she must choose one of her
deity's domains (or subdomains) in place of those typically available to a druid.

**Shepherd of the Faithful (Su)**

**Gained:** At 4th Level

**Passive:** A nature priest and all allies within 60 feet that can see or hear her gain a +2
insight bonus on skill checks to notice or avoid natural hazards, difficult terrain, and rough winds
or water, as well as on saving throws against natural hazards. This ability offers no protection
against the abilities of creatures or the effects of spells or items.

**Replaces:** Resist nature's lure

**Divine Servants (Su)**

**Gained:** At 9th Level

**Passive:** A nature priest adds the spells [lesser planar ally](ref/spell/planar-ally-lesser),
[planar ally](ref/spell/planar-ally), and [greater planar ally](ref/spell/planar-ally-greater) to
her druid spell list at their cleric spell levels. When she casts these spells, the planar allies
summoned require half the payment described in those spells.

**Replaces:** Venom immunity
