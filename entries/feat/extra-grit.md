+++
id = "ref/feat/extra-grit"
kind = "feat"
title = "Extra Grit"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "extra_grit", path = "json/feat06.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]
[[sources]]
publication = "ultimate-combat"
page = "100"

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Grit class feature or the Amateur Gunslinger feat."
prerequisite_feats = ["ref/feat/amateur-gunslinger"]
benefit = "You gain 2 extra grit points at the start of each day, and your maximum grit increases by 2."
normal = "If you are a gunslinger, you gain your Wisdom modifier in grit points at the start of each day, which is also your maximum grit. If you have the Amateur Gunslinger feat, you gain 1 grit point at the start of each day, and your maximum grit is equal to your Wisdom modifier."
special = "If you possess levels in the gunslinger class, you can take this feat multiple times."
+++

## Extra Grit (Grit)

You have more grit than the ordinary gunslinger.\
**Prerequisites:** Grit class feature or the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat.\
**Benefit:** You gain 2 extra grit points at the start of each day, and your maximum grit increases
by 2.\
**Normal:** If you are a [gunslinger](ref/class/gunslinger), you gain your Wisdom modifier in grit
points at the start of each day, which is also your maximum grit. If you have the Amateur Gunslinger
feat, you gain 1 grit point at the start of each day, and your maximum grit is equal to your Wisdom
modifier.\
**Special:** If you possess levels in the gunslinger class, you can take this feat multiple times.
