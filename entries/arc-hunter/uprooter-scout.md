+++
id = "ref/arc-hunter/uprooter-scout"
kind = "archetype"
title = "Uprooter Scout"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Uprooter%20Scout"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "uprooter_scout", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-origins"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "lore-of-the-blight", level = 6 },
  { anchor = "unnatural-stride", level = 10 },
  { anchor = "demon-s-end", level = 17 },
]
trades = [
  { replaces = "Improved empathic link", feature = "improved-empathic-link", by = ["lore-of-the-blight"] },
  { replaces = "speak with master", feature = "speak-with-master", by = ["lore-of-the-blight"] },
  { replaces = "greater empathic link", feature = "greater-empathic-link", by = ["lore-of-the-blight"] },
  { replaces = "Raise animal companion", feature = "raise-animal-companion", by = ["unnatural-stride"] },
  { replaces = "One with the wild", feature = "one-with-the-wild", by = ["demon-s-end"] },
]
+++

The Uprooters are an elite band of Kyonin elves skilled and brave enough to foray into the
Tanglebriar and take the offensive in the fight against [Treerazer](ref/monster/treerazer). Uprooter
scouts rely on their close bonds with their animal companions to survive such raids. One Uprooter
scout who accompanied an expedition into the Worldwound to put his
[demon](ref/family/demon)-fighting skills to work there has retired to Mendev to teach his
techniques to others, so these skills are slowly being passed on to non-elves.

## Lore of the Blight (Ex) {#lore-of-the-blight}

At 6th level, an Uprooter scout and her animal companion gain a +2 bonus on initiative checks and on
Knowledge (geography), Perception, Stealth, and Survival skill checks when she's in
[the Abyss](ref/rule/the-abyss) or Abyss-tainted terrain (such as Tanglebriar or the Worldwound).
When she travels through this terrain, she leaves no trail and can't be tracked (though she can
leave a trail if she so chooses). This bonus increases to +4 at 11th level and +6 at 16th level.
This ability replaces improved empathic link, speak with master, and greater empathic link.

## Unnatural Stride (Ex) {#unnatural-stride}

At 10th level, the Uprooter scout and her animal companion learn how to move through undergrowth (as
[woodland stride](ref/ability/woodland-stride)) that has been enchanted, corrupted, or magically
manipulated. This ability replaces raise animal companion.

## Demon's End (Ex) {#demon-s-end}

At 17th level, even demons must respect the number of their kindred an Uprooter scout has slain, and
lesser demons quake before her. The Uprooter scout and her companion can attempt to demoralize a
demon as a swift action, rolling 1d20 and adding the scout's level and her Charisma modifier to
determine the [Intimidate](ref/skill/intimidate) check result. This ability replaces one with the
wild.
