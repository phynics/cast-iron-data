+++
id = "ref/arc-barbarian/cave-dweller"
kind = "archetype"
title = "Cave Dweller"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Cave%20Dweller"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cave_dweller", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "tight-tunnels", level = 1 },
  { anchor = "tunnel-vision", level = 3 },
  { anchor = "sun-walker", level = 7 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["tight-tunnels"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["tunnel-vision"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["sun-walker"] },
]
+++

Unused to the light of the sun, cave dwellers use their subterranean expertise to protect their
clans from the manifold dangers of deep caverns and tunnels. The typical cave dweller is perfectly
content to live his entire life underground, and he may even view the light of the sun as
particularly abhorrent or taboo.

While this lifestyle doesn't in and of itself imply evil or sinister intent, many outlanders
ignorantly assume that cave dwellers avoid the light of the sun for malicious reasons. In truth,
cave dwellers are as capable of goodness and kindness as any other—they just see little reason to
venture out of their preferred homelands. When a cave dweller joins an adventuring party, she may
retain an inherent nervousness about sleeping under the open sky and may long for the familiar
confines of a comforting cavern, but this rarely translates directly into a notable disadvantage.
Indeed, many adventuring groups come to value the specialized talents and skills the cave dweller
brings to the party.

## Skills {#skills}

A cave dweller gains Stealth as a class skill in place of Ride.

This alters the barbarian's skills.

## Tight Tunnels (Ex) {#tight-tunnels}

Cave dwellers pursue prey through the winding tunnels of the deep, which rarely accommodate open
sprints. A cave dweller can make a single turn up to 90 degrees while [running](ref/rule/run)
(though not while [charging](ref/rule/charge)). Additionally, a cave dweller takes no penalties to
movement speed while [squeezing](ref/misc/squeezing).

This replaces fast movement.

## Tunnel Vision (Ex) {#tunnel-vision}

At 3rd level, a cave dweller's senses become sharp in the dark. She gains
[darkvision](ref/rule/darkvision) to a range of 60 feet and a +1 bonus on Perception checks to
detect ambushes, movement, and sound while in darkness. This bonus increases by 1 at 6th level and
every 3 levels thereafter.

This replaces trap sense.

## Sun Walker (Ex) {#sun-walker}

At 7th level, a cave dweller gains a +1 dodge bonus to AC and on saving throws against effects with
the light descriptor or that produce bright or sudden light. Any penalties on attack rolls, saving
throws, or skill checks because of bright light are reduced by 1. At 10th level and every 3 levels
after 10th, the bonus to AC and saving throws, as well as the reduction of light-based penalties,
increases by 1.

This replaces [damage reduction](ref/rule/damage-reduction).

## Rage Powers {#rage-powers}

The following rage powers complement the cave dweller archetype:
[animal fury](ref/ragepower/animal-fury), [bestial climber](ref/ragepower/bestial-climber),
[eclipsing rage](ref/ragepower/eclipsing-rage),
[greater eclipsing rage](ref/ragepower/greater-eclipsing-rage),
[greater ground breaker](ref/ragepower/greater-ground-breaker),
[ground breaker](ref/ragepower/ground-breaker), [night vision](ref/ragepower/night-vision),
[raging climber](ref/ragepower/raging-climber), [primal scent](ref/ragepower/primal-scent), and
[sprint](ref/ragepower/sprint).
