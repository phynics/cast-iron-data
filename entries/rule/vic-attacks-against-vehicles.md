+++
id = "ref/rule/vic-attacks-against-vehicles"
kind = "rule"
title = "Attacks against Vehicles"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vic_attacks_against_vehicles", path = "json/rules_rulesets02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 174

A vehicle has a base Armor Class based on its size and other defenses the vehicle has. To calculate
the vehicle's actual AC, add the current driver's driving skill modifier (or Wisdom modifier, if it
is using that ability to drive the vehicle) to the vehicle's base AC. Touch attacks against a
vehicle ignore its driver's driving skill or ability modifier; thus a vehicle's base AC is its touch
AC. A vehicle is never considered flat-footed.

A vehicle has a base saving throw listed in its stat block. This determines its base Fortitude and
Reflex saving throw. A vehicle is immune to effects that require a Will saving throw (though
drivers, crew members, passengers, and creatures providing muscle propulsion typically are not). To
determine the vehicle's actual Fortitude and Reflex saving throws, add half the driver's driving
skill modifier (or half the driver's Wisdom modifier) to the vehicle's base saving throw.

Vehicles have hit points, but do not have ability scores, and are immune to ability score damage or
drain. They are also immune to bleed damage. A vehicle that takes damage in excess of half its total
hit points gains the broken condition. When a vehicle reaches 0 or fewer hit points, but has not yet
reached negative hit points equal to the number of squares of its space, it is wrecked. When a
vehicle reaches a negative number of hit points equal to the number of squares it takes up, it is
destroyed (see [Damaging a Vehicle](ref/rule/vic-damaging-a-vehicle)).

Unlike other objects, vehicles do not take half damage from energy attacks, but do take half damage
from all ranged weapons except siege weapons.

When attacking a vehicle, you can attack the vehicle's structure, occupant, propulsion, driving
device, or conveyance (if any).

> **Attacking the Structure:** This is an attack against the vehicle itself. If successful, the
> vehicle takes damage normally.
>
> **Attacking an Occupant:** This is a normal attack against an occupant creature. Occupants get
> partial cover or greater if the attack is coming from outside of the vehicle. Grappling the driver
> is one method for taking control of the vehicle.
>
> **Attacking Propulsion:** Propulsion often has its own set of statistics, while creatures
> propelling a vehicle use their own statistics. Other types of propulsion have hit points and
> [hardness](ref/umr/hardness) determined by multiplying the values listed in
> [Propulsion Devices](ref/rule/propulsion-devices) by the vehicle's total number of squares of that
> type. Individual vehicle stat blocks also detail their propulsion.
>
> If a vehicle is being pulled by creatures, and any of those creatures is killed, dazed, stunned,
> or becomes unconscious, the vehicle comes to a sudden stop (see
> [Sudden Stops](ref/rule/vic-initiative-and-movement)). If a vehicle has a crew, and half or more
> of that crew is killed, dazed, stunned, or rendered unconscious, the vehicle can no longer be
> controlled.
>
> **Attacking the Driving Device:** A driving device is its own object with its own statistics. When
> a driving device gains the broken condition or is disabled, all driving checks are increased
> by 10. When a driving device is destroyed, the vehicle can no longer be driven. Driving devices
> are typically objects with object immunities and resistances.
>
> **Attacking Conveyance:** An attack against wheels, rudders, or similar forms of conveyance takes
> a -10 penalty on the attack roll, but does maximum damage to the vehicle (no roll necessary). If
> the attack is a critical hit, multiply this maximum damage by the critical multiplier of the
> attack. Conveyances are typically objects with object immunities and resistances.

### Table 4-5: Vehicle AC and CMB Modifier by Size

|Vehicle Size|AC|CMB Modifier|
| --- | --- | --- |
|Large vehicle|9|+1|
|Huge vehicle|8|+2|
|Gargantuan vehicle|6|+4|
|Colossal vehicle|2|+8|
