+++
id = "ref/arc-ranger/fortune-finder"
kind = "archetype"
title = "Fortune-Finder"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Fortune-Finder"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fortune_finder", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "hinterlander", level = 1 },
  { anchor = "adaptable-study", level = 4 },
  { anchor = "trailblazer", level = 7 },
  { anchor = "fast-study", level = 11 },
  { anchor = "master-explorer", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["hinterlander"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["adaptable-study"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["trailblazer"] },
  { replaces = "Quarry", feature = "quarry", by = ["fast-study"] },
  { replaces = "improved quarry", feature = "improved-quarry", by = ["fast-study"] },
  { replaces = "Master hunter", feature = "master-hunter", by = ["master-explorer"] },
]
+++

Vanaras often leave home to seek fortune and sate their curiosity regarding the mysterious lands
that lie beyond their native territories. The most skilled of these thrillseekers are called
ba-sadhaks, or fortune-finders. So successful have these canny explorers been at exploring Golarion
at large that the secrets of their success are closely guarded, resulting in only extremely rare
non-vanaran fortune-finders.

## Hinterlander (Ex) {#hinterlander}

A fortune-finder adds 1/2 his level (minimum 1) on all Climb and Swim checks.

This replaces track.

## Adaptable Study (Ex) {#adaptable-study}

At 4th level, a fortune-finder can adapt and orient himself to new environments and new enemies. He
gains a +1 bonus on initiative checks and Knowledge (geography), Perception, Stealth, and Survival
checks whenever he is in a terrain he hasn't selected as one of his favored terrains. He leaves no
trail and can't be tracked in any such terrain (though he can leave a trail if he so chooses).

In addition to this, the fortune-finder can study an opponent he can see as a move action. He then
gains a bonus on Bluff, Knowledge, Perception, Sense Motive, and Survival checks attempted against
that opponent, as well as on weapon attack and damage rolls against it. The bonus is equal to half
the fortune-finder's highest favored enemy bonus. A fortune-finder can't attempt Knowledge checks
untrained to identify an opponent he has studied with adaptable study. Bonuses from adaptable study
don't stack with those from the favored enemy ability. The ranger can study only a single target at
a time.

This ability replaces hunter's bond.

## Trailblazer (Ex) {#trailblazer}

Starting at 7th level, a fortune-finder can move through any sort of
[difficult terrain](ref/rule/terrain-and-obstacles) at his normal speed. Terrain that is enchanted
or magically manipulated to impede movement, however, still affects the fortune-finder.

This ability replaces woodland stride.

## Fast Study (Ex) {#fast-study}

Beginning at 11th level, a fortune-finder can study an opponent using adaptable study as a swift or
move action. In addition to this, he can maintain bonuses from adaptable study against one
additional opponent. At 19th level, he can study an opponent using adaptable study as an immediate,
swift, or move action and can maintain the bonuses from adaptable study against a total of three
opponents.

This ability replaces quarry and improved quarry.

## Master Explorer (Ex) {#master-explorer}

A fortune-finder of 20th level becomes a master explorer. He can move through any sort of terrain
that impedes movement at his full speed, even if it is enchanted or magically manipulated to impede
motion. As a full-round action, he can study one opponent he can see and has already studied with
adaptable study, increasing the benefits he gains from that ability to equal his full favored enemy
bonus.

This ability replaces master hunter.
