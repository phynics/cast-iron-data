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
features = [
  { anchor = "infused-curative", level = 2 },
  { anchor = "anaesthetic", level = 5 },
  { anchor = "power-over-death", level = 10 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["infused-curative"] },
  { replaces = "Poison resistance +4", feature = "poison-resistance", levels = [5], by = ["anaesthetic"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["power-over-death"] },
]
+++

An alchemist who studies anatomy and uses this knowledge to heal is a chirurgeon. A chirurgeon has
the following class features.

## Infused Curative {#infused-curative}

At 2nd level, a chirurgeon's extracts of _cure_ spells automatically act as infusions, and can be
used by non-alchemists. When a chirurgeon prepares his extracts, he may choose to render any or all
of his infused curatives inert and prepare other extracts to replace them (unlike infusions, which
continue to occupy the alchemist's daily extract slots until consumed or used). This ability
replaces poison use.

## Anaesthetic {#anaesthetic}

At 5th level, a chirurgeon learns how to supplement uses of the Heal skill with pain-killing drugs.
He gains [Skill Focus](ref/feat/skill-focus) (Heal) as a bonus feat. Any use of the Heal skill that
has a risk of harming the patient (such as extracting a barb) only deals the minimum damage when
performed by a chirurgeon. This ability replaces poison resistance +4.

## Power Over Death {#power-over-death}

At 10th level, a chirurgeon adds _[breath of life](ref/spell/breath-of-life)_ to his formula book as
a 4th-level extract. His infused curative ability applies to this extract. This ability replaces
poison immunity.

## Discoveries {#discoveries}

The following discoveries complement the chirurgeon archetype:
[elixir of life](ref/discovery/elixir-of-life), [healing touch](ref/discovery/healing-touch),
[infusion](ref/discovery/infusion), and [spontaneous healing](ref/discovery/spontaneous-healing).
