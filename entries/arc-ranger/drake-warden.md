+++
id = "ref/arc-ranger/drake-warden"
kind = "archetype"
title = "Drake Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Drake%20Warden"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drake_warden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "young-drake", level = 4 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["young-drake"] },
  { replaces = "2nd favored enemy", feature = "favored-enemy", levels = [5], by = ["young-drake"] },
  { replaces = "swift tracker", feature = "swift-tracker", by = ["young-drake"] },
]
+++

Some rangers specialize in dealing with rambunctious younger drakes, protecting them and teaching
them to tolerate, and even trust, humanoid creatures. These drake wardens follow and pass along
secret techniques for raising drakes effectively, and thanks to their methods, their drakes are both
fiercely loyal and extremely useful for scouting and stealth missions.

## Young Drake {#young-drake}

At 4th level, a drake warden gains a [drake companion](ref/sidekick/drake) instead of an animal
companion, but his effective charge's level is equal to his ranger level - 3. The young drake gains
drake powers only when its charge reaches 3rd and 7th levels (not 11th or 15th level) and increases
in size only when its charge reaches 5th level (not 9th, 13th, or 17th level).

This ability replaces hunter's bond, 2nd favored enemy, and swift tracker.
