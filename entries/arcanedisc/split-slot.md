+++
id = "ref/arcanedisc/split-slot"
kind = "rule"
title = "Split Slot"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "split_slot", path = "json/class_ability_arcane_discoveries.json" },
]

[fields]
kind = "none"
+++

**Split Slot**

**Ability:** Once per day when you prepare spells, you may treat any one of your open spell slots as
if it were two spell slots that were two spell levels lower. For example, a 9th-level wizard can
split a 5th-level slot into two 3rd-level slots, preparing [fireball](ref/spell/fireball) and
[lightning bolt](ref/spell/lightning-bolt) in those 3rd-level slots. For all purposes, the two
lower-level slots are treated as that lower level (so the split 5th-level slot used for a fireball
has a DC as if it were in a normal 3rd-level slot). Splitting a 2nd-level slot lets you prepare two
additional cantrips (which you can cast over and over, just like normally prepared cantrips).

**Prereq:** 5th-level wizard

**Special:** This discovery has no effect on cantrips or 1st-level spells. You may select this
discovery multiple times; each time you select it, you may split another spell slot when you prepare
spells. You cannot split a slot that you created by splitting a higher-level slot.
