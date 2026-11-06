+++
id = "ref/spell/frosty-aura"
kind = "spell"
title = "Frosty Aura"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frosty_aura", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold"]
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
components = "V, S, M/DF (a chunk of ice or a few drops of water melted from glacier ice)"
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
Components: V, S, M/DF (a chunk of ice or a few drops of water melted from glacier ice)
Range: personal
Duration: 1 minute/level
Saving throw: none (harmless, see text)
Spell resistance: no (harmless, see text)
Target: you (see text)
Descriptors: cold
:::

**Sources:** Pathfinder \#91: Battle of Bloodmarch Hills pg 71

The spell allows you to channel cold into your very being. If you don't already have the cold
subtype, this spell grants you the cold subtype. If you already have the cold subtype, you instead
channel the frost from your being outward, creating a 10-foot-radius aura of cold centered on you.
Creatures who enter or end their turns in the aura must succeed at a Fortitude saving throw or take
1d8 points of cold damage.

Multiple castings of this spell stack; you can cast it once on yourself to gain the cold subtype,
then again to manifest the aura of frost around you.
