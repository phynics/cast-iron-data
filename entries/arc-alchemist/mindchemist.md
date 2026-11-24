+++
id = "ref/arc-alchemist/mindchemist"
kind = "archetype"
title = "Mindchemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Mindchemist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindchemist", path = "json/archetypes_alchemist2.json" },
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
  { anchor = "cognatogen", level = 1 },
  { anchor = "perfect-recall", level = 2 },
  { anchor = "languages" },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["cognatogen"] },
  { replaces = "Poison use", feature = "poison-use", by = ["perfect-recall"] },
]
+++

While most alchemists use mutagens to boost their physical ability at the cost of mental ability,
some use alchemy for the opposite purpose - to boost the power of the mind and memory. A mindchemist
can reach incredible levels of mental acuity, but suffers lingering debilitating effects to his
physique. A mindchemist has the following class features.

## Cognatogen {#cognatogen}

At 1st level, a mindchemist learns how to create a [cognatogen](ref/discovery/cognatogen), as per
the cognatogen discovery. This ability replaces the [mutagen](ref/discovery/mutagen) class ability
(a mindchemist cannot create mutagens unless he selects mutagen as a discovery).

## Perfect Recall {#perfect-recall}

At 2nd level, a mindchemist has honed his memory. When making a Knowledge check, he may add his
Intelligence bonus on the check a second time. Thus, a mindchemist with 5 ranks in Knowledge
(history) and a +2 Intelligence bonus has a total skill bonus of +9 (5 + 2 + 2) using this ability.
The mindchemist can also use this ability when making an Intelligence check to remember something.
This ability replaces poison use.

## Bonus Feats {#bonus-feats}

A mindchemist may select [Skill Focus](ref/feat/skill-focus) (Disable Device, Disguise, Heal, any
Knowledge skill, Sense Motive, or Spellcraft) in place of a discovery.

## Languages {#languages}

A mindchemist may learn three languages in place of a discovery.

## Discoveries {#discoveries}

The following discoveries complement the mindchemist archetype:
[grand cognatogen](ref/discovery/grand-cognatogen),
[greater cognatogen](ref/discovery/greater-cognatogen),
[infuse mutagen](ref/discovery/infuse-mutagen).
