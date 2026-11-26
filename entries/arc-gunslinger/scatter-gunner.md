+++
id = "ref/arc-gunslinger/scatter-gunner"
kind = "archetype"
title = "Scatter Gunner"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Scatter%20Gunner"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scatter_gunner", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "scatter-specialist" },
  { anchor = "careful-shot", level = 1 },
  { anchor = "scatter-artist", level = 3 },
  { anchor = "overload", level = 7 },
  { anchor = "satchel-shot", level = 7 },
]
trades = [
  { replaces = "Deadeye deed", feature = "deeds", power = "deadeye", by = ["careful-shot"] },
  { replaces = "Utility shot deed", feature = "deeds", power = "utility shot", by = ["scatter-artist"] },
  { replaces = "Dead shot deed", feature = "deeds", power = "dead shot", by = ["overload"] },
  { replaces = "Targeting deed", feature = "deeds", power = "targeting", by = ["satchel-shot"] },
  { alters = "Gunsmith", feature = "gunsmith", by = ["scatter-specialist"] },
]
+++

Punishing firearms such as the blunderbuss and dragon pistol can lay waste to invaders in tight
corridors, and the dwarves of Dongun Hold have pioneered masterful methods for making the most of
these indiscriminate weapons.

## Scatter Specialist {#scatter-specialist}

A scatter gunner must take a [blunderbuss](ref/eq-weapon/blunderbuss) or
[dragon pistol](ref/eq-weapon/dragon-pistol) when he chooses a battered firearm at 1st level.

This alters gunsmith.

## Deeds {#deeds}

A scatter gunner gains the following deeds, each of which functions only when he uses a weapon with
the [scatter](ref/misc/scatter) weapon quality to make a scattering shot.

## Careful Shot (Ex) {#careful-shot}

As long as a scatter gunner has at least 1 grit point when making a scattering shot, he takes a
penalty equal to his Wisdom modifier on his attack rolls against any allies in the area. He can
spend 1 grit point when making a scattering shot to automatically miss a number of creatures equal
to his Wisdom modifier.

This replaces the deadeye deed.

## Scatter Artist (Ex) {#scatter-artist}

At 3rd level, when using a firearm to make a scattering shot, a scatter gunner can spend 1 grit
point to add one of the following effects to his attack. • _Restricted Barrel:_ The scattering shot
attacks all creatures in a line rather than in a cone. The line's length is twice the length of the
weapon's cone (30 feet for most early firearms). • _Shaped Blast:_ Select one additional square
adjacent to the scattering shot's area of effect; creatures in this square are also affected by the
scattering shot. • _Vortex:_ The firearm releases an explosive torrent of air in the scattering
shot's affected area for 1 round, creating a strong [wind](ref/rule/winds) effect (25 mph) that can
disperse fog and smoke effects such as those created by _[fog cloud](ref/spell/fog-cloud)_.

This replaces the utility shot deed.

## Overload (Ex) {#overload}

At 7th level, a scatter gunner knows just how to hold his weapon to maximize its devastating
scattering effects. As a full-round action, a scatter gunner can make a scattering shot to fire a
concentrated payload of pellets that strains his firearm. This doubles the area affected by the
scattering shot (a 30-foot cone for most early firearms), increases the firearm's misfire value by
2, and causes each successful attack to deal an additional 1d6 points of damage that is not
multiplied on a critical hit. This additional damage increases to 2d6 at 13th level and 3d6 at 19th
level. The scatter gunner must spend 1 grit point to perform this deed.

This replaces the dead shot deed.

## Satchel Shot (Ex) {#satchel-shot}

At 7th level, as a full-round action, a scatter gunner can load and fire an explosive shell,
consuming ammunition as though he had made a scattering shot. This functions like
[throwing a splash weapon](ref/rule/throw-splash-weapon) at a grid intersection but uses his
firearm's range increment, attack bonus, and magic special abilities (if any). The shell affects
creatures in a 10-foot radius as though the scatter gunner had made a scattering shot against them,
and damaged creatures must succeed at a Reflex save (DC = 10 + half the scatter gunner's level + the
scatter gunner's Dexterity modifier) or [catch fire](ref/rule/catching-on-fire).

This replaces the targeting deed.
