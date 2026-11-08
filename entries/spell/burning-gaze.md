+++
id = "ref/spell/burning-gaze"
kind = "spell"
title = "Burning Gaze"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_gaze", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (eye of a mundane salamander)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Magus, Mesmerist, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (eye of a mundane salamander)
Range: personal
Duration: 1 round/level
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Target: you
Descriptors: fire
:::

**Sources:** Advanced Player's Guide pg 208

Your eyes burn like hot coals, allowing you to set objects or foes alight with a glance.

As a standard action as long as this spell's effects persist, you may direct your burning gaze
against a single creature or object within 30 feet of your location. Targeted creatures must succeed
at a Fortitude save or take 1d6 points of fire damage. Unattended objects do not get a save.
Creatures damaged by the spell must make a Reflex save or catch fire. Each round, burning creatures
may attempt a Reflex save to quench the flames; failure results in another 1d6 points of fire
damage. Flammable items worn by a creature must also save or take the same damage as the creature.
If a creature or object is already on fire, it suffers no additional effects from burning gaze.

Note that this spell does not grant an actual gaze attack-foes and allies are not in danger of
catching on fire simply by meeting your gaze.
