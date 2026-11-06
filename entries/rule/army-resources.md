+++
id = "ref/rule/army-resources"
kind = "rule"
title = "Army Resources"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "army_resources", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 241

Resources are physical assets the army can use to improve its abilities. You must spend the BP for a
resource before you can apply it to the army. Some armies can't use certain resources - an army of
wolves can't use healing potions or improved weapons, mindless creatures can't use siege engines,
and so on.

The cost of a resource doesn't end when you purchase it. Units must be trained to use new equipment,
elite units demand higher pay, expensive items are more costly to maintain and repair, and so on.
Each resource added to an army increases the army's weekly Consumption by the listed amount.

The costs listed are for a Medium army. Resources for a smaller or larger army cost proportionately
less or more than this amount, as per Table 4-16: Resource Scaling.

### Table 4-16: Resource Scaling

|Army Size|Multiplier|
| --- | --- |
|Fine|×1/8|
|Diminutive|×1/6|
|Tiny|×1/4|
|Small|×1/2|
|Medium|×1|
|Large|×2|
|Huge|×4|
|Gargantuan|×10|
|Colossal|×20|

The multiplier affects the resource's initial cost and the increase to Consumption. The multiplier
can't reduce the cost of a resource below 1 BP

**Healing Potions (10 BP):** Each unit is equipped with several healing potions. At any point during
a battle (but no more than twice per battle), the commander can order her units to drink their
potions. The army doesn't attempt an Offense check that phase, but heals a number of hit points
equal to twice its ACR. Each time an army uses its healing potions, increase its Consumption that
week by 3. To purchase this resource, a settlement in your kingdom must have an Alchemist, Caster's
Tower, Cathedral, Herbalist, Magic Shop, Magical Academy, or Temple.

**Improved Armor (3 BP):** The army is armed with masterwork armor, increasing DV and Consumption
by 1. For 15 BP, you can outfit the army with magic armor, increasing DV and Consumption by 2
instead. To purchase this, a settlement in your kingdom must have a Foreign Quarter, Military
Academy, or Smithy.

**Improved Weapons (5 BP):** The army is armed with masterwork weapons, increasing OM and
Consumption by 1. For 50 BP, you can outfit the army with magic weapons, increasing OM and
Consumption by 2 instead. To purchase this resource, a settlement in your kingdom must have a
Foreign Quarter, Military Academy, or Smithy.

**Mounts (BP = Mount's ACR):** The army is mounted on horses or other combat-trained animals.
Increase its OM and DV by 2, and increase its Consumption by 1. If your army uses mounts that are
more powerful than the units themselves, your army's ACR and derived scores might increase (see
[ACR](ref/rule/army-statistics)). To purchase this resource, a settlement in your kingdom must have
a Foreign Quarter, Stable, or Stockyard.

**Ranged Weapons (2 BP):** The army is equipped with ranged weapons (such as crossbows, slings, or
bows), gaining ranged attack capability. Increase its Consumption by 1.

**Siege Engines (15 BP per engine):** Your army includes catapults, rams, trebuchets, ballistae, and
other siege engines designed to break down fortifications. Increase OM by 2 (regardless of the total
number of siege engines in the army) and Consumption by 3 per siege engine. Each Melee phase, reduce
the enemy's bonus to DV from fortifications by 1d4 per siege engine in your army. Unlike other
resources, the cost of a siege engine doesn't scale with the army's size. To purchase this resource,
a settlement in your kingdom must have an Academy, Foreign Quarter, Military Academy, or University.
