+++
id = "ref/spell/domination-link"
kind = "spell"
title = "Domination Link"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "domination_link", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a copper piece)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Bard, Inquisitor, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a copper piece)
Range: 60 ft.
Duration: concentration, up to 1 min./level (D)
Saving throw: Will negates, see text
Spell resistance: no
Area: cone-shaped emanation
Descriptors: mind-affecting
:::

**Sources:** Blood of the Night pg 30

This spell functions like detect thoughts, with the additional ability to find echoes of the
thoughts of a creature mentally controlling the target. For example, if the target has been
dominated by a vampire, you can use evidence left in the target's mind to learn about that vampire.
Each minute you concentrate on the spell, you can learn your choice of one of the following pieces
of information.

_Direction:_ The controller's general direction and distance.

_Emotion:_ The controller's emotional state (gloating, sated, frightened, angry, and so on).

_Image:_ A powerful iconic image relevant to the controller or its connection to the target, such as
a symbol on a door or a name on a gravestone.

_Location:_ The controller's general location, such as "in a large city" or "in a large city"

_Name:_ The name by which the target knows its controller (if any).

All of this information is based on the last time the influencing creature linked itself to the
target, either to issue a command or to receive sensory input from the target. For example, if at
nightfall a vampire commanded a dominated victim to walk to a cemetery, this spell can reveal the
vampire's general location at that time, though it may have moved since then.
