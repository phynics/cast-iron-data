+++
id = "ref/feat/aligned-crafting"
kind = "feat"
title = "Aligned Crafting"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aligned_crafting", path = "json/feat01.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/craft-magic-arms-and-armor", label = "or" },
  { kind = "prerequisite", target = "ref/feat/craft-wondrous-item", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Item Creation"]
prerequisites = "Craft Magic Arms and Armor or Craft Wondrous Item."
prerequisite_feats = ["ref/feat/craft-magic-arms-and-armor", "ref/feat/craft-wondrous-item"]
benefit = "When you craft a magic weapon, magic armor, a magic shield, or a wondrous item, you can infuse it with a bit of your convictions. Creatures that are more than one alignment step away from you are sickened while using or wearing this item. An item that has been infused with your alignment can never have an opposing special ability added to it later (for example, a longsword infused with your lawful good alignment cannot later gain the anarchic weapon special ability). Infusing the item with your alignment in this way increases the items total construction cost by 10%."
+++

## Aligned Crafting (Item Creation)

**Sources:** People of the Wastes pg 26

Your magical creations reject those you oppose.\
**Prerequisites:** [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor) or
[Craft Wondrous Item](ref/feat/craft-wondrous-item).\
**Benefit:** When you craft a magic weapon, magic armor, a magic shield, or a wondrous item, you can
infuse it with a bit of your convictions. Creatures that are more than one alignment step away from
you are [sickened](ref/misc/sickened) while using or wearing this item. An item that has been
infused with your alignment can never have an opposing special ability added to it later (for
example, a longsword infused with your lawful good alignment cannot later gain the
[anarchic](ref/magic-enh/anarchic) weapon special ability). Infusing the item with your alignment in
this way increases the items total construction cost by 10%.
