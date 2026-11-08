+++
id = "ref/spell/flesh-puppet-horde"
kind = "spell"
title = "Flesh Puppet Horde"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flesh_puppet_horde", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/flesh-puppet" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (an onyx worth 25gp and a silken string)"
range = "touch"
effects = [
  { label = "Target", value = "one corpse touched" },
]
duration = "permanent (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin\
3: Cleric, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (an onyx worth 25gp and a silken string)
Range: touch
Duration: permanent (D)
Saving throw: none
Spell resistance: no
Target: one corpse touched
Descriptors: evil
:::

### Flesh Puppet Horde

**Sources:** Horror Adventures pg 117

This spell functions as [flesh puppet](ref/spell/flesh-puppet), but can animate multiple zombies. As
noted in animate dead, you can't control more than 4 HD per caster level worth of undead in total,
nor can a single casting create more than 2 HD per caster level. A separate string attaches to each
zombie in your horde. Severing a zombie's string reverts that zombie to a corpse, but doesn't end
the spell for other zombies. Because commanding a flesh puppet requires a swift action, you can
issue commands to only one zombie per round, though zombies you previously commanded continue to
follow their orders. Likewise, you can command only one zombie to speak per round.

Unlike with flesh puppet, you can command a zombie to attack. If you do, all your zombies
immediately gain the staggered quality and no longer appear to be alive.

This spell ends automatically if you cast flesh puppet or flesh puppet horde on a new corpse.
