+++
id = "ref/arc-vigilante/hidden-current"
kind = "archetype"
title = "Hidden Current"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Hidden%20Current"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hidden_current", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "guise-of-the-land-walker", level = 1 },
  { anchor = "sea-s-return", level = 11 },
  { anchor = "stealthy-swimmer", level = 2 },
]
trades = [
  { replaces = "1st-level social talent", feature = "social-talent", levels = [1], by = ["guise-of-the-land-walker"] },
  { replaces = "Frightening appearance", feature = "frightening-appearance", by = ["sea-s-return"] },
  { replaces = "The hidden current's 2nd-level vigilante talent", feature = "vigilante-talent", levels = [2], by = ["stealthy-swimmer"] },
]
+++

Sometimes the best place to hide is in plain sight. The hidden current operates above and below the
sea. When operating underwater, he blends easily with the locals, passing himself off as one of them
or as an experienced aquatic traveler. When operating on land, he erases all traces of his aquatic
heritage. When the hidden current needs to avoid pursuit, he slips away into his native environment.

## Guise of the Land Walker (Ex) {#guise-of-the-land-walker}

At 1st level, a hidden current gains the [many guises](ref/soctalent/many-guises) social talent, but
the mundane identity assumed must be of a nonaquatic humanoid and functions only when he is on land.

This ability replaces the hidden current's 1st-level social talent.

## Sea's Return (Sp) {#sea-s-return}

At 11th level, a hidden current can magically slip between the sea and the land, as if using the
spell _[dimension door](ref/spell/dimension-door)_ with a caster level equal to the hidden current's
vigilante level. The starting point of this ability must be on land and the ending point in water at
least waist deep, or vice versa. Using this ability is a move action. The hidden current cannot take
other creatures with him when he uses this ability. A hidden current can use this ability once per
day at 11th level and an additional time per day every 4 levels thereafter (to a maximum of three
uses per day at 19th level).

This ability replaces frightening appearance.

## Stealthy Swimmer (Ex) {#stealthy-swimmer}

Hidden currents can transition between land and sea at a moment's notice. If a hidden current begins
his movement on land and ends his movement in water at least waist deep, or vice versa, he gains a
+5 circumstance bonus on a Stealth check in the same turn.

This ability replaces the hidden current's 2nd-level vigilante talent.
