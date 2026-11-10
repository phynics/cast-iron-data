+++
id = "ref/feat/battering-ram"
kind = "feat"
title = "Battering Ram"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "battering_ram", path = "json/feat02.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "10"

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Craft (alchemy) 3 ranks; grit class feature or Amateur Gunslinger; pistol-whip gunslinger deed; quick clear gunslinger deed."
prerequisite_feats = ["ref/feat/amateur-gunslinger"]
benefit = "You can ignore the broken condition of a firearm you're wielding to perform the pistol-whip deed. If you hit a creature with this deed, you can spend 1 grit point as an immediate action to remove the broken condition from the firearm, but only if the firearm gained that condition from a misfire."
+++

## Battering Ram (Grit)

Sometimes smacking your firearm against a solid surface is all that's needed to unjam it. Sometimes
that solid surface is a creature.\
**Prerequisites:** Craft (alchemy) 3 ranks; grit class feature or
[Amateur Gunslinger](ref/feat/amateur-gunslinger); [pistol-whip](ref/deed/pistol-whip) gunslinger
deed; [quick clear](ref/deed/quick-clear) gunslinger deed.\
**Benefit:** You can ignore the broken condition of a firearm you're wielding to perform the
pistol-whip deed. If you hit a creature with this deed, you can spend 1 grit point as an immediate
action to remove the broken condition from the firearm, but only if the firearm gained that
condition from a misfire.
