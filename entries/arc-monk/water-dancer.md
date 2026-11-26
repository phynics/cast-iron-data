+++
id = "ref/arc-monk/water-dancer"
kind = "archetype"
title = "Water Dancer"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Water%20Dancer"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "water_dancer", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "65"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-focus", level = 1 },
  { anchor = "nereid-s-grace", level = 1 },
  { anchor = "unarmed-strike" },
  { anchor = "burn", level = 2 },
  { anchor = "wild-talents", level = 2 },
  { anchor = "water-dance", level = 4 },
  { anchor = "metakinesis", level = 9 },
  { anchor = "water-stride", level = 12 },
]
trades = [
  { replaces = "Flurry of blows", feature = "flurry-of-blows", by = ["elemental-focus"] },
  { replaces = "stunning fist", feature = "stunning-fist", by = ["elemental-focus"] },
  { replaces = "quivering palm", feature = "quivering-palm", by = ["elemental-focus"] },
  { replaces = "Bonus feat the monk normally gains at 1st level", feature = "bonus-feat", levels = [1], by = ["nereid-s-grace"] },
  { replaces = "Evasion", feature = "evasion", by = ["burn"] },
  { replaces = "Bonus feats at 2nd, 6th, 10th, 14th, and 18th levels", feature = "bonus-feat", levels = [2, 6, 10, 14, 18], by = ["wild-talents"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["water-dance"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["metakinesis"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["water-stride"] },
  { alters = "Unarmed strike", feature = "unarmed-strike", by = ["unarmed-strike"] },
]
+++

Water dancers derive their martial training from ancient nereid traditions jealously guarded by
these enigmatic fey.

## Elemental Focus (Su and Sp) {#elemental-focus}

A water dancer gains the elemental focus ability of the [kineticist](ref/class/kineticist) class,
but must choose water as his [element](ref/ability/elements). He gains the
[basic hydrokinesis](ref/kinetic/basic-hydrokinesis) wild talent as normal, and gains the
[kinetic blast](ref/kinetic/water-blast) feature of the kineticist class for the water element,
using his monk level as his effective kineticist level. He can't use his kinetic blast when armored
or encumbered.

This replaces flurry of blows, stunning fist, and quivering palm.

## Nereid's Grace (Su) {#nereid-s-grace}

When unarmored and unencumbered, a water dancer adds 1 point of Charisma bonus per monk level to his
Armor Class as a dodge bonus. If he is caught [flat-footed](ref/rule/flat-footed) or otherwise
denied his Dexterity bonus, he also loses this bonus. He uses his Charisma score instead of his
Wisdom score to determine the size of his ki pool and the DC and effects of monk class features.

This replaces the bonus feat the monk normally gains at 1st level.

## Unarmed Strike {#unarmed-strike}

A water dancer gains the unarmed strike monk class feature but treats his unarmed strike damage as
that of a monk 4 levels lower (minimum 1st level).

This alters unarmed strike.

## Burn (Ex) {#burn}

At 2nd level, a water dancer gains the burn class feature of the kineticist class.

This replaces evasion.

## Wild Talents {#wild-talents}

At 2nd level and every 4 levels thereafter, a water dancer selects a new
[utility wild talent](ref/ability/wild-utility-talents) from the list of options available to the
kineticist class, treating his monk level - 2 (minimum 1) as his kineticist level for the purpose of
fulfilling prerequisites as well as for level-dependent effects of the utility talent. He can select
only universal wild talents or those that match his element (see elemental focus above). At 6th,
10th, and 16th levels, he can replace one of his utility wild talents with another wild talent of
the same level or lower. He can't replace a wild talent that he used to qualify for another of his
wild talents.

This replaces the bonus feats at 2nd, 6th, 10th, 14th, and 18th levels.

## Water Dance (Su) {#water-dance}

At 4th level, a water dancer can move across any liquid surface as though it were solid ground up to
a maximum distance of 20 feet before falling through the liquid's surface as normal. This distance
increases by 10 feet at 6th level and every 2 levels thereafter, to a maximum of 90 feet at 18th
level. Additionally, at 10th level the water dancer can even move vertically up water surfaces (such
as a flowing waterfall) as though under the effects of _[spider climb](ref/spell/spider-climb)_. If
he runs out of movement before reaching a solid surface when climbing a vertical water source, he
immediately falls.

This replaces slow fall.

## Metakinesis (Su) {#metakinesis}

At 9th level, a water dancer gains the ability to alter his kinetic blasts as the kineticist's
metakinesis (empower) class feature.

This replaces improved evasion.

## Water Stride (Sp) {#water-stride}

At 12th level, a water dancer can leap from one source of water to another as per
_[dimension door](ref/spell/dimension-door)_ as a move action by expending 1 point of ki from his ki
pool. He must begin and end his movement in a space of water equal to his size. He cannot take other
creatures with him when he uses this ability.

This replaces abundant step.
