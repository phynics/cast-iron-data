+++
id = "ref/rule/vic-initiative-and-movement"
kind = "rule"
title = "Initiative, Movement, and Sudden Stops"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vic_initiative_and_movement", path = "json/rules_rulesets02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Combat pg 174

### Initiative

A vehicle moves on its driver's initiative. If a driver delays or readies an action, the vehicle
goes out of control, and does nothing except take the uncontrolled action until it stops or someone
becomes its new driver.

### Movement

At the start of the driver's turn, she makes a driving check to control the vehicle as detailed in
the [Driving Vehicles](ref/rule/driving-vehicles) section. When doing so, she takes whatever action
is required before doing anything else that turn.

Vehicles usually ignore difficult terrain due to rubble and foliage, but treat steep inclines as
difficult terrain, and depending on the vehicle type and GM judgment, they may be affected by other
difficult terrain types as well.

Vehicles and creatures that occupy vehicles can enter the spaces of other vehicles and creatures,
though doing so usually provokes a vehicular overrun or ramming maneuver (see
[Vehicle Combat Maneuvers](ref/rule/vic-vehicle-combat-maneuvers)). A vehicle can even end its turn
in the space of a creature or another vehicle.

### Sudden Stops

When a vehicle comes to a sudden stop - its movement is reduced to 0 in some way other than the
driver using a drive action to slow the vehicle - both creatures and items on the vehicle are
violently pushed toward the vehicle's forward facing a number of squares equal to 1/2 the vehicle's
current speed before it came to the sudden stop. This movement does not provoke attacks of
opportunity. At the end of this movement, creatures and objects take 1d6 points of damage, and
creatures must succeed at a DC 20 Reflex saving throw or be knocked prone. If the movement pushes
creatures or objects into solid objects, that creature or object takes an additional 1d6 points of
damage for each 5-foot square the push was reduced by the solid object.

For instance, if a vehicle with a movement of 60 feet makes a sudden stop due to hitting a brick
wall, its driver is thrown 30 feet toward the brick wall. If the brick wall was only 5 feet away
from the driver at the point of impact, the driver moves forward 5 feet, hits the wall, and takes
5d6 points of damage. She then takes the original 1d6 points of damage, after which she makes a
Reflex saving throw to see if she falls prone for the sudden stop.
