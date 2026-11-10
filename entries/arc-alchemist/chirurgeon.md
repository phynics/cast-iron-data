+++
id = "ref/arc-alchemist/chirurgeon"
kind = "archetype"
title = "Chirurgeon"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Chirurgeon"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chirurgeon", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "18"

[fields]
kind = "archetype"
replaces = ["Poison use", "Poison resistance +4", "Poison immunity"]
replaces_features = ["poison-use"]
+++

An alchemist who studies anatomy and uses this knowledge to heal is a chirurgeon. A chirurgeon has
the following class features.

**Infused Curative**

**Gained:** At 2nd Level

**Passive:** A chirurgeon's extracts of cure spells automatically act as infusions, and can be used
by non-alchemists. When a chirurgeon prepares his extracts, he may choose to render any or all of
his infused curatives inert and prepare other extracts to replace them (unlike infusions, which
continue to occupy the alchemist's daily extract slots until consumed or used).

**Replaces:** Poison use

**Anaesthetic**

**Gained:** At 5th Level

**Passive:** A chirurgeon learns how to supplement uses of the Heal skill with painkilling drugs. He
gains [Skill Focus](ref/feat/skill-focus) (Heal) as a bonus feat. Any use of the Heal skill that has
a risk of harming the patient (such as extracting a barb) only deals the minimum damage when
performed by a chirurgeon.

**Replaces:** Poison resistance +4

**Power Over Death**

**Gained:** At 10th Level

**Passive:** A chirurgeon adds [breath of life](ref/spell/breath-of-life) to his formula book as a
4th-level extract. His _infused curative_ ability applies to this extract.

**Replaces:** Poison immunity

**Discoveries:** The following discoveries complement the chirurgeon archetype:
[elixir of life](ref/discovery/elixir-of-life), [healing touch](ref/discovery/healing-touch),
[infusion](ref/discovery/infusion), and [spontaneous healing](ref/discovery/spontaneous-healing).
