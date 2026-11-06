+++
id = "ref/spell/hellfire-ray"
kind = "spell"
title = "Hellfire Ray"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-1-princes-of-darkness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hellfire_ray", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (any unholy symbol or heretical tome)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "none (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Cleric, Magus, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (any unholy symbol or heretical tome)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none (see text)
Spell resistance: yes
Effect: ray
Descriptors: evil
:::

**Sources:** Book of the Damned pg 184, Book of the Damned - Volume 1: Princes of Darkness pg 46

A blast of hellfire blazes from your hands. You can fire one ray, plus one additional ray for every
4 caster levels beyond 11th (to a maximum of three rays at 19th level). Each ray requires a ranged
touch attack to hit and deals 1d6 points of damage per caster level (maximum 15d6). Half the damage
is fire damage, but the other half results directly from unholy power and is therefore not subject
to being reduced by fire resistance. The rays can be fired at the same target or at different
targets, but all rays must be fired simultaneously and aimed at targets within 30 feet of each
other.

Any creature killed by this spell must attempt a Will saving throw; failure means the creature's
soul is damned to Hell as a burst of brimstone appears around its corpse. A nonevil spellcaster
attempting to bring the creature back from the dead must attempt a caster level check (DC = 10 + the
slain creature's level) to succeed; failure means the spellcaster cannot try again for 1 day. Evil
spellcasters can raise the slain character normally, without requiring a check. A raised character's
soul is no longer automatically consigned to Hell.
