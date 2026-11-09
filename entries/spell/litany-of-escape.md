+++
id = "ref/spell/litany-of-escape"
kind = "spell"
title = "Litany of Escape"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_escape", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "234"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
descriptors = ["language-dependant"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Paladin", level = 3 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing creature that is grappled" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Antipaladin, Paladin\
4: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one willing creature that is grappled
Subschool: Teleportation
Descriptors: language-dependant
:::

With a powerful prayer, you call upon the servants of your god to whisk a friend out of a grapple.
The target loses the grappled and pinned conditions and is teleported 10 feet. If there is no
available space for the target to teleport to, the spell fails.
