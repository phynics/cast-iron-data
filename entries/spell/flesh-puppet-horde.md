+++
id = "ref/spell/flesh-puppet-horde"
kind = "spell"
title = "Flesh Puppet Horde"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flesh_puppet_horde", path = "json/spells4.json" },
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

## Flesh Puppet

**Sources:** Horror Adventures pg 117

You animate one corpse that has been dead no more than 48 hours. It rises as a zombie that is
magically tethered to you and obeys your commands. As noted in
[animate dead](ref/spell/animate-dead), you can't control more than 4 HD per caster level worth of
undead in total, nor can a single casting create more than 2 HD per caster level.

This spell disguises the zombie's appearance and allows you to control it. The zombie's outward
appearance, movement, and voice appear the same as if it were still alive. The zombie's normal
staggered condition doesn't apply (though it can still be staggered by other means). Successfully
detecting the flesh puppet as a zombie without magic requires an opposed Perception check against
your Disguise check, and you add your caster level as a bonus on this Disguise check.

An ephemeral string connects you to the zombie. Through this string, you have a mental link to the
zombie and can command it as a swift action. The zombie uses its own actions to complete your
commands. The zombie can speak up to 25 words in 1 round, but you must mentally impart what you
intend it to say as a swift action. It is incapable of articulating speech on its own. The zombie
can be ordered to perform very simple tasks it knew in life but can't make attacks, cast spells, or
perform complex or difficult tasks requiring constant concentration.

The string connecting you and the zombie is nearly invisible. A DC 30 Perception check is required
to detect it. It has [hardness](ref/umr/hardness) 0 and 1 hp. The length of string you can create is
100 feet + 10 feet per caster level you have. The string snaps if you and the zombie move farther
apart than this length, though the zombie won't move out of range unless forced to do so or unless
you command it to do so. If the string to the zombie is severed, the spell immediately ends. The
ephemeral string can pass through physical barriers, but not barriers of magical force, and it can
be damaged as though it were a physical object.

When this spell ends, the zombie immediately reverts back to a normal corpse. The spell ends
automatically if you cast flesh puppet or flesh puppet horde on a new corpse.

### Flesh Puppet Horde

**Sources:** Horror Adventures pg 117

This spell functions as flesh puppet, but can animate multiple zombies. As noted in animate dead,
you can't control more than 4 HD per caster level worth of undead in total, nor can a single casting
create more than 2 HD per caster level. A separate string attaches to each zombie in your horde.
Severing a zombie's string reverts that zombie to a corpse, but doesn't end the spell for other
zombies. Because commanding a flesh puppet requires a swift action, you can issue commands to only
one zombie per round, though zombies you previously commanded continue to follow their orders.
Likewise, you can command only one zombie to speak per round.

Unlike with flesh puppet, you can command a zombie to attack. If you do, all your zombies
immediately gain the staggered quality and no longer appear to be alive.

This spell ends automatically if you cast flesh puppet or flesh puppet horde on a new corpse.
