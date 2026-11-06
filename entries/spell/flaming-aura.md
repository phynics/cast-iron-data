+++
id = "ref/spell/flaming-aura"
kind = "spell"
title = "Flaming Aura"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flaming_aura", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a small piece of charcoal)"
range = "personal"
effects = [
  { label = "Target", value = "you (see text)" },
]
duration = "1 minute/level"
saving_throw = "none (harmless, see text)"
spell_resistance = "no (harmless, see text)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Bloodrager, Cleric, Magus, Oracle, Shaman, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a small piece of charcoal)
Range: personal
Duration: 1 minute/level
Saving throw: none (harmless, see text)
Spell resistance: no (harmless, see text)
Target: you (see text)
Descriptors: fire
:::

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 70

The spell allows you channel fire into your very being. If you don't already have the fire subtype,
this spell grants you the fire subtype. If you already have the fire subtype, you instead channel
the flames from your being outward, creating a 10-foot-radius aura of fire centered on you.
Creatures who enter or end their turns in the aura must succeed at a Fortitude saving throw or take
1d8 points of fire damage.

Multiple castings of this spell stack; you can cast it once on yourself to gain the fire subtype,
then again to manifest the aura of flames around you.
