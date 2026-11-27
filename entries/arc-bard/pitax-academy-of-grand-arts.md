+++
id = "ref/arc-bard/pitax-academy-of-grand-arts"
kind = "archetype"
title = "Pitax: Academy of Grand Arts"
source_ids = ["guide-to-the-river-kingdoms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pitax_academy_of_grand_arts", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "guide-to-the-river-kingdoms"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "focused-performance", level = 2 },
]
trades = [
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["focused-performance"] },
]
+++

While not as popular as some of the great bardic schools of the Inner Sea, Pitax's Academy of Grand
Arts still manages to attract some students seeking greater specialization.

Bards who have successfully mastered the strict curriculum of Pitax's Academy of Grand Arts to
graduate are more adept in their assigned field of performance, at the expense of versatility in
other areas. Such bards have the focused performance alternate class ability, which replaces
versatile performance.

## Focused Performance (Ex) {#focused-performance}

At 2nd level, a bard must choose one type of Perform skill. The bard gains
[Extra Performance](ref/feat/extra-performance) as a bonus feat, usable only with the chosen
category of the Perform skill. At 8th level, and every 6 levels thereafter, the bard gains Extra
Performance as an additional bonus feat. The additional uses of bardic performance gained from these
feats cannot be used with any category of the Performance skill other than the one chosen at 2nd
level.
