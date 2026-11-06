+++
id = "ref/spell/masochistic-shadow"
kind = "spell"
title = "Masochistic Shadow"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "masochistic_shadow", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "shadow"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates, then Reflex partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Arcanist, Bloodrager, Magus, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates, then Reflex partial, see text
Spell resistance: yes
Target: one creature
Descriptors: evil, shadow
:::

**Sources:** Blood of Shadows pg 30

You animate the target's shadow with semi-living energies drawn from the Shadow Plane, instilling a
maddening hunger for its owner's life energy within it. If the target fails its Will save, it takes
1d4 points of Strength damage as a quasi-real shadow manifests in its space and attacks it. This
shadow remains attached to the target and moves wherever the target moves.

At the start of each subsequent round, the target must succeed at a Reflex save or take 1d4
additional points of Strength damage; a successful save reduces the Strength damage to 1 point. If
its Strength score is reduced to 0 by this spell's effects, the target dies. If the target is in
bright light, it gains a +2 bonus on Reflex saves against this spell. If the target is in darkness,
it takes a -2 penalty on Reflex saves against this spell.
