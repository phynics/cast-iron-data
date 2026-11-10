+++
id = "ref/rule/disabled-0-hit-points"
kind = "rule"
title = "Disabled (0 Hit Points)"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disabled_0_hit_points", path = "json/rules_combat01.json" },
]
[[sources]]
publication = "core-rulebook"
page = "189"

[fields]
kind = "none"
+++

When your current hit point total drops to exactly 0, you are disabled.

You gain the [staggered](ref/misc/staggered) condition and can only take a single move or standard
action each turn (but not both, nor can you take full-round actions). You can take move actions
without further injuring yourself, but if you perform any standard action (or any other strenuous
action) you take 1 point of damage after completing the act. Unless your activity increased your hit
points, you are now at -1 hit points and dying.

Healing that raises your hit points above 0 makes you fully functional again, just as if you'd never
been reduced to 0 or fewer hit points.

You can also become [disabled](ref/misc/disabled) when recovering from dying. In this case, it's a
step toward recovery, and you can have fewer than 0 hit points (see
[Stable Characters and Recovery](ref/rule/stable-characters-and-recovery)).
