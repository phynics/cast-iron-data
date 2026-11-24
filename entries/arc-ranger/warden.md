+++
id = "ref/arc-ranger/warden"
kind = "archetype"
title = "Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Warden"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "68"

[fields]
kind = "archetype"
features = [
  { anchor = "master-of-terrain", level = 1 },
  { anchor = "live-in-comfort", level = 2 },
  { anchor = "terrain-bond", level = 4 },
  { anchor = "able-explorer", level = 5 },
  { anchor = "wilderness-whispers", level = 20 },
]
trades = [
  { replaces = "1st favored enemy", feature = "favored-enemy", levels = [1], by = ["master-of-terrain"] },
  { replaces = "All combat style feats", feature = "combat-style-feat", by = ["live-in-comfort"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["terrain-bond"] },
  { replaces = "2nd, 3rd, and 4th favored enemies", feature = "favored-enemy", levels = [5, 10, 15], by = ["able-explorer"] },
  { replaces = "5th favored enemy", feature = "favored-enemy", levels = [20], by = ["wilderness-whispers"] },
  { replaces = "master hunter", feature = "master-hunter", by = ["wilderness-whispers"] },
]
+++

All rangers have a bond with the wilderness, but the warden may have the strongest. This protector
sits guard in the middle of the wilderness, keeping a lookout for any dangers that might spill from
the deeper wilderness beyond, and protecting civilization from the savagery of nature—and vice
versa. His long weeks, months, and sometimes years of isolation cause him to "hear" what the land is
saying. Not all are crazy.

## Master of Terrain (Ex) {#master-of-terrain}

At 1st level, a warden selects his first favored terrain. He gains another one at 3rd level, and
then every five levels thereafter (for a maximum of five favored terrains at 18th level). This
ability replaces the ranger's first favored enemy ability.

## Live in Comfort (Ex) {#live-in-comfort}

At 2nd level, a warden is truly at home within his favored terrains. He knows all the signs of the
wilderness. He rarely gets lost. He can easily live off the land in comfort, and can provide for
companions. The warden can take 10 on any Survival check involving any of his favored terrains, even
when in immediate danger and distracted. If the warden is not in immediate danger and distracted, he
can take 20 even if the check has a penalty for failure. This ability replaces all combat style
feats.

## Terrain Bond (Ex) {#terrain-bond}

At 4th level, a warden forms a bond with the land itself, enabling him to direct others in such
terrain. When in his favored terrain, the warden grants all allies within line of sight and that can
hear him a +2 bonus on initiative checks and Perception, Stealth, and Survival skill checks. Also,
as long as they travel with him, the warden's allies leave no trail and can't be tracked. The warden
can choose for the group to leave a trail, or even for specific members of the group to leave a
trail if he so desires. This ability replaces hunter's bond.

## Able Explorer (Ex) {#able-explorer}

At 5th level, when making an Acrobatics, Climb, Fly, Ride, or Swim check in any of his favored
terrains, a warden can make two skill checks and take the higher. This ability replaces the ranger's
second, third, and fourth favored enemies.

## Wilderness Whispers (Su) {#wilderness-whispers}

At 20th level, a warden cannot be surprised and always acts as if he had rolled a natural 20 on any
initiative check while within any of his favored terrains. A warden can always move at full speed
while using Survival to follow tracks without penalty. This ability replaces the ranger's fifth
favored enemy and master hunter.
