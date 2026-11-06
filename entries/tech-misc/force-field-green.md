+++
id = "ref/tech-misc/force-field-green"
kind = "item"
title = "Force Field (green)"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "force_field_green", path = "json/equipment_tech_misc.json" },
]

[fields]
kind = "item"
price = "20,000 gp (black), 120,000 gp (blue), 4,000 gp (brown), 60,000 gp (gray), 80,000 gp (green), 140,000 gp (orange), 220,000 gp (prismatic), 100,000 gp (red), 40,000 gp (white)"
weight = "1 lb. (all)"
slot = "wrists"
+++

## Force field

**Sources:** Technology Guide pg 45\
**Price** 20,000 gp (black), 120,000 gp (blue), 4,000 gp (brown), 60,000 gp (gray), 80,000 gp
(green), 140,000 gp (orange), 220,000 gp (prismatic), 100,000 gp (red), 40,000 gp (white)\
**Slot** wrists; **Weight** 1 lb. (all)\
**Capacity** varies; **Usage** 1 charge/minute

### Construction

**Craft DC** 28 (black), DC 33 (blue), DC 27 (brown), DC 30 (gray), DC 31 (green), DC 34 (orange),
DC 35 (prismatic), DC 32 (red), DC 29 (white)\
**Cost** 10,000 gp (black), 60,000 gp (blue), 2,000 gp (brown), 30,000 gp (gray), 40,000 gp (green),
70,000 gp (orange), 110,000 gp (prismatic), 50,000 gp (red), 20,000 gp (white)\
[Craft Technological Item](ref/feat/craft-technological-item),
[graviton lab](ref/rule/crafting-laboratories)

Force fields are powered by a surprisingly light pair of slender, silvery bracelets. When activated
as a standard action, dozens of tiny biofeedback needles pierce the wearer's arms to interface with
the nervous system; this process is somewhat painful and the wearer must succeed at a DC 15
Fortitude save to avoid being [dazed](ref/misc/dazed) for 1 round as the force field is activated.
Once active, the device generates an invisible and intangible field of force around the target. The
force field blocks solids and liquids, but not gases or light (including laser beams). The user of a
force field can still breathe, but she cannot eat or drink.

Activating a force field is a standard action that consumes 1 charge, after which point the field
consumes 1 additional charge every minute it remains active. While a force field is active, the user
gains a number of temporary hit points that varies depending on the force field's power. All damage
dealt to the wearer of a force field is subtracted from the temporary hit points it grants first. As
long as the force field is active, the wearer is immune to critical hits (but not precision-based
damage, such as [sneak attacks](ref/ability/sneak-attack)). A force field has
[fast healing](ref/umr/fast-healing) that replenishes its temporary hit points at a fixed rate each
round, but if the force field's temporary hit points are ever reduced to 0, the force field shuts
down and cannot be reactivated for 24 hours. Force fields are automatically reduced to 0 hp by
[disintegration](ref/spell/disintegrate) effects. A force field can be deactivated as a free action.

The charge capacity, amount of temporary hit points granted, and rate of
[fast healing](ref/umr/fast-healing) these temporary hit points have varies according to the force
field's color code, as detailed below.

|Color|Capacity|Temp HP|Fast Healing|
| --- | --- | --- | --- |
|Brown|10|5|1|
|Black|15|10|2|
|White|20|15|3|
|Gray|25|20|4|
|Green|30|25|5|
|Red|35|30|6|
|Blue|40|35|7|
|Orange|45|40|8|
|Prismatic|50|60|10|
