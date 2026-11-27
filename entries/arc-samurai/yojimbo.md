+++
id = "ref/arc-samurai/yojimbo"
kind = "archetype"
title = "Yojimbo"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Yojimbo"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "yojimbo", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "resolute-defense", level = 1 },
  { anchor = "armor-expertise", level = 3 },
  { anchor = "intercept", level = 4 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["resolute-defense"] },
  { replaces = "Weapon expertise", feature = "weapon-expertise", by = ["armor-expertise"] },
  { replaces = "Mounted archer", feature = "mounted-archer", by = ["intercept"] },
]
+++

Yojimbo are highly trained bodyguards favored by the nobles and warlords of distant Minkai. Yojimbo
who follow the order of the warrior loyally guard a single master, while ronin serve whoever can pay
for their protection. Yojimbo often accompany visitors to the Inner Sea region from Tian Xia; a few
have chosen to stay, and some have even passed on their training to bodyguards of this region.

## Resolute Defense (Ex) {#resolute-defense}

At 1st level, whenever a yojimbo issues a challenge, he can select one ally as his ward for the
duration of the challenge. Whenever the yojimbo is adjacent to his ward, he can use resolve, greater
resolve, and true resolve on his ward rather than targeting himself.

This ability replaces mount.

## Armor Expertise (Ex) {#armor-expertise}

At 3rd level, a yojimbo selects one type of armor, such as [chain shirt](ref/eq-armor/chain-shirt)
or [scale mail](ref/eq-armor/scale-mail). The yojimbo gains armor training, treating his samurai
level as his [fighter](ref/class/fighter) level, when wearing the selected armor.

This ability replaces weapon expertise.

## Intercept (Ex) {#intercept}

At 4th level, a yojimbo learns to better disrupt the attacks of his enemies. He gains
[Bodyguard](ref/feat/bodyguard) as a bonus feat, even if he does not meet the prerequisite. In
addition, whenever the yojimbo uses the [aid another](ref/rule/aid-another-2) action to increase an
ally's Armor Class, the bonus to Armor Class from the aid another action increases by 1.

This ability replaces mounted archer.
