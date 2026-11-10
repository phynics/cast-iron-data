+++
id = "ref/spell/teleport-trap"
kind = "spell"
title = "Teleport Trap"
aon = "SpellDisplay.aspx?ItemName=Teleport%20Trap"
source_ids = ["inner-sea-world-guide", "seekers-of-secrets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teleport_trap", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-world-guide"
page = "296"
[[sources]]
publication = "seekers-of-secrets"
page = "18"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered lodestone and silver worth 100 gp per 40-ft. cube)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one 40-ft. cube/level (S)" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, M (powdered lodestone and silver worth 100 gp per 40-ft. cube)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Area: one 40-ft. cube/level (S)
:::

Teleport trap wards an area, redirecting all teleportation into or out of the area to a specific
point within the area determined by you at the time of casting. The destination must be an open
space on a solid surface. The spell's area overlaps walls and other solid and liquid objects
(preventing intruders from bypassing the ward by teleporting into a wall or through similar means).
A teleporting creature that is affected by a teleport trap can resist the effect with a Will save -
if the save is successful, the creature simply doesn't teleport at all (but the use of the teleport
effect is still consumed) - either to the intended location or the teleport trap's actual
destination. A DC 27 Knowledge (arcana) allows such a creature to recognize the teleport trap's
presence, but does not reveal the trap's linked destination.

At your discretion, the teleport trap can exclude a category of creatures, such as an alignment, a
type of creature, or creatures that carry a specific item or know a password (though this only works
if the creature is teleporting out of the area, not into it). You select this option and the
conditions at the time you cast the spell. Overly complicated conditions may cause the spell to fail
entirely. Multiple castings of teleport trap can be linked to cover a larger area, allowing
teleported creatures to be directed to a single point within the combined area of the spells.

Teleport trap can be made permanent at the cost of 7,000 gp. A single
[permanency](ref/spell/permanency) spell can be used on all teleport traps that share a linked
destination, but the gold piece cost must be paid for each individual spell.

The Pathfinders of the Grand Lodge make use of permanent teleport traps in several key locations,
trapping would-be intruders in a small wing of jail cells. At least one crypt of the Whispering
Tyrant makes use of the spell as well, trapping grave robbers in coffin-sized stone cysts, there to
die a slow and agonizing death from thirst and starvation.
