+++
id = "ref/feat/distant-spell-link"
kind = "feat"
title = "Distant Spell Link"
aon = "FeatDisplay.aspx?ItemName=Distant%20Spell%20Link"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "distant_spell_link", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/enlarge-spell", label = "or" },
  { kind = "prerequisite", target = "ref/feat/reach-spell", label = "or" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "12"

[fields]
kind = "feat"
prerequisites = "Enlarge Spell or Reach Spell; animal companion, eidolon, familiar, or other allied creature with the share spells ability."
prerequisite_feats = ["ref/feat/enlarge-spell", "ref/feat/reach-spell"]
benefit = "The range of your allied creature's share spells ability increases to close (25 feet + 5 feet for every 2 levels) as long as you have line of effect to the creature when you cast the shared spell. If your allied creature has the deliver touch spells ability, you can designate your allied creature as the spell's source when you cast a touch spell as long as you are within close range of it. The creature must still deliver the touch spell at its touch range."
normal = "You must be adjacent to your familiar to share spells with it or designate touch spells for it to deliver."
+++

You can share spells and grant touch spells to your companion creature over a great distance.\
**Prerequisites:** [Enlarge Spell](ref/feat/enlarge-spell) or [Reach Spell](ref/feat/reach-spell);
animal companion, eidolon, familiar, or other allied creature with the share spells ability.\
**Benefit:** The range of your allied creature's share spells ability increases to close (25 feet +
5 feet for every 2 levels) as long as you have line of effect to the creature when you cast the
shared spell. If your allied creature has the deliver touch spells ability, you can designate your
allied creature as the spell's source when you cast a touch spell as long as you are within close
range of it. The creature must still deliver the touch spell at its touch range.\
**Normal:** You must be adjacent to your familiar to share spells with it or designate touch spells
for it to deliver.
