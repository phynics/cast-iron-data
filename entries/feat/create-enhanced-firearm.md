+++
id = "ref/feat/create-enhanced-firearm"
kind = "feat"
title = "Create Enhanced Firearm"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_enhanced_firearm", path = "json/feat03.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/gunsmithing", label = "or" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "26"

[fields]
kind = "feat"
feat_types = ["Item Creation"]
prerequisites = "Craft Magic Arms and Armor; Craft (weapons) 1 rank or Gunsmithing."
prerequisite_feats = ["ref/feat/craft-magic-arms-and-armor", "ref/feat/gunsmithing"]
benefit = "When you craft a firearm or magical firearm, you can use reinforced components to make the weapon more reliable. This increases the item's total construction cost by 10%. The misfire chance of the weapon is reduced by 1. This can never reduce a firearm's misfire chance by more than 1."
+++

## Create Enhanced Firearm (Item Creation)

You can craft superior firearms.\
**Prerequisites:** [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor); Craft
(weapons) 1 rank or [Gunsmithing](ref/feat/gunsmithing).\
**Benefit:** When you craft a firearm or magical firearm, you can use reinforced components to make
the weapon more reliable. This increases the item's total construction cost by 10%. The misfire
chance of the weapon is reduced by 1. This can never reduce a firearm's misfire chance by more
than 1.
