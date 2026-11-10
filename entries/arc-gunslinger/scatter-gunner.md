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
replaces = ["Deadeye deed", "Utility shot deed", "Dead shot deed", "Targeting deed"]
alters = ["Gunsmith"]
alters_features = ["gunsmith"]
+++

Punishing firearms such as the blunderbuss and dragon pistol can lay waste to invaders in tight
corridors, and the dwarves of Dongun Hold have pioneered masterful methods for making the most of
these indiscriminate weapons.

**Scatter Specialist**

**Alters:** Gunsmith

**Info:** A scatter gunner must take a [blunderbuss](ref/eq-weapon/blunderbuss) or
[dragon pistol](ref/eq-weapon/dragon-pistol) when he chooses a battered firearm at 1st level.

**Deeds**

**Info:** A scatter gunner gains the following deeds, each of which functions only when he uses a
weapon with the [scatter](ref/misc/scatter) weapon quality to make a scattering shot.

**Careful Shot (Ex)**

**Ability:** He can spend 1 grit point when making a scattering shot to automatically miss a number
of creatures equal to his Wisdom modifier.

**Passive:** As long as a scatter gunner has at least 1 grit point when making a scattering shot, he
takes a penalty equal to his Wisdom modifier on his attack rolls against any allies in the area.

**Replaces:** Deadeye deed

**Scatter Artist (Ex)**

**Action:** Ability

**Gained:** At 3rd Level

**Replaces:** Utility shot deed

When using a firearm to make a scattering shot, a scatter gunner can spend 1 grit point to add one
of the following effects to his attack.

- **Restricted Barrel:** The scattering shot attacks all creatures in a line rather than in a cone.
  The line's length is twice the length of the weapon's cone (30 feet for most early firearms).
- **Shaped Blast:** Select one additional square adjacent to the scattering shot's area of effect;
  creatures in this square are also affected by the scattering shot.
- **Vortex:** The firearm releases an explosive torrent of air in the scattering shot's affected
  area for 1 round, creating a strong [wind](ref/rule/winds) effect (25 mph) that can disperse fog
  and smoke effects such as those created by [fog cloud](ref/spell/fog-cloud).

**Overload (Ex)**

**Flavor:** A scatter gunner knows just how to hold his weapon to maximize its devastating
scattering effects.

**Fullround:** A scatter gunner can make a scattering shot to fire a concentrated payload of pellets
that strains his firearm. This doubles the area affected by the scattering shot (a 30-foot cone for
most early firearms), increases the firearm's misfire value by 2, and causes each successful attack
to deal an additional 1d6 points of damage that is not multiplied on a critical hit. The scatter
gunner must spend 1 grit point to perform this deed.

**Gained:** At 7th Level

**Replaces:** Dead shot deed

At 13th level: The additional damage 2d6.

At 19th level: The additional damage 3d6.

**Satchel Shot (Ex)**

**Fullround:** A scatter gunner can load and fire an explosive shell, consuming ammunition as though
he had made a scattering shot. This functions like
[throwing a splash weapon](ref/rule/throw-splash-weapon) at a grid intersection but uses his
firearm's range increment, attack bonus, and magic special abilities (if any). The shell affects
creatures in a 10-foot radius as though the scatter gunner had made a scattering shot against them,
and damaged creatures must succeed at a Reflex save (DC = 10 + half the scatter gunner's level + the
scatter gunner's Dexterity modifier) or [catch fire](ref/rule/catching-on-fire).

**Gained:** At 7th Level

**Replaces:** Targeting deed
