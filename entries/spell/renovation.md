+++
id = "ref/spell/renovation"
kind = "spell"
title = "Renovation"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "renovation", path = "json/spells8.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 5 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "8 hours"
components = "V, S, M (silver dust worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one unoccupied structure" },
]
duration = "instantaneous"
saving_throw = "none (object"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Red Mantis Assassin, Sorcerer, Wizard\
5: Bard, Skald
Casting time: 8 hours
Components: V, S, M (silver dust worth 1,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none (object
Spell resistance: no
Target: one unoccupied structure
:::

Upon casting this spell, you permanently rearrange and resize the rooms in a building you
constructed as a [downtime activity](ref/rule/downtime-activities). You may reorganize and remap the
building however you please, as if each room had just been constructed and is being positioned for
the first time. You cannot make any changes to a building that changes how much a room would cost to
create or that alters the benefits a room provides. The structure also must remain in the same
general position within the district. If you don't wholly own the structure, all of the structure's
owners must consent to the changes being made before the spell is cast; otherwise, it fails
immediately.
