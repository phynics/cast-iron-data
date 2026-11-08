+++
id = "ref/spell/object-possession"
kind = "spell"
title = "Object Possession"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "object_possession", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/object-possession-lesser" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "unattended Tiny or Small object" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium, Occultist\
3: Mesmerist, Psychic, Spiritualist\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: unattended Tiny or Small object
:::

### Object Possession

**Sources:** Occult Adventures pg 179

This spell functions as [lesser object possession](ref/spell/object-possession-lesser), except as
noted above. The possessed animated object has a number of Construction Points appropriate for its
size (up to 3 CP for Large objects).

You can return your consciousness to your body as a standard action. On your next turn, you can
attempt to possess a different object as a standard action instead of ending the spell.
