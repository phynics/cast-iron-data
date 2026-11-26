+++
id = "ref/arc-mesmerist/vexing-trickster"
kind = "archetype"
title = "Vexing Trickster"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Vexing%20Trickster"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vexing_trickster", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "psychic-anthology"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "consummate-trickster", level = 1 },
  { anchor = "trickster-s-ego", level = 2 },
  { anchor = "bonus-feat", level = 3 },
  { anchor = "manifold-hijinks", level = 6 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["consummate-trickster"] },
  { replaces = "Towering ego", feature = "towering-ego", by = ["trickster-s-ego"] },
  { replaces = "Touch treatment (minor)", feature = "touch-treatment", levels = [3], by = ["bonus-feat"] },
  { replaces = "touch treatment (greater)", feature = "touch-treatment", levels = [10], by = ["bonus-feat"] },
  { replaces = "Touch treatment (moderate)", feature = "touch-treatment", levels = [6], by = ["manifold-hijinks"] },
  { replaces = "touch treatment (break enchantment)", feature = "touch-treatment", levels = [14], by = ["manifold-hijinks"] },
]
+++

While many mesmerists are called to embrace the art of deception, using their mind-binding powers to
make their foes believe that even the most outrageous realities are actually true, others indulge in
the various hijinks their power enables. These mesmerists are known as vexing tricksters.

## Consummate Trickster (Ex) {#consummate-trickster}

A vexing trickster gains a +1 bonus on Bluff, Disguise, Sleight of Hand, and Stealth checks. This
bonus increases by 1 at 4th level and every 3 mesmerist levels thereafter (maximum +6).

This ability replaces consummate liar.

## Trickster's Ego (Ex) {#trickster-s-ego}

At 2nd level, a vexing trickster gains [Combat Expertise](ref/feat/combat-expertise) as a bonus
feat. If his Intelligence score is less than 13, his Intelligence counts as 13 for the purpose of
meeting the prerequisites for combat feats.

This ability replaces towering ego.

## Bonus Feat (Ex) {#bonus-feat}

At 3rd level, a vexing trickster gains a trick feat (see pages 16–17) as a bonus feat. He must meet
the feat's prerequisites. At 10th level, he gains a second trick feat as a bonus feat.

This ability replaces touch treatment (minor) and touch treatment (greater).

## Manifold Hijinks (Su) {#manifold-hijinks}

At 6th level, the vexing trickster learns to implant multiple mesmerist tricks that have been
modified by trick feats (henceforth called modified tricks) in his targets' minds simultaneously. At
6th level, the vexing trickster can implant up to two modified mesmerist tricks in a single target
simultaneously. At 14th level, he can implant up to three modified mesmerist tricks in a single
target simultaneously. This ability doesn't allow a mesmerist to apply more than one trick feat to a
single mesmerist trick at a time.

This ability replaces touch treatment (moderate) and touch treatment (_break enchantment_).
