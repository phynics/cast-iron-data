+++
id = "ref/spell/phantasmal-killer"
kind = "spell"
title = "Phantasmal Killer"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantasmal_killer", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will disbelief, then Fortitude partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium\
4: Arcanist, Bloodrager, Magus, Mesmerist, Psychic, Red Mantis Assassin, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will disbelief, then Fortitude partial; see text
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: emotion, fear, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 319

You create a phantasmal image of the most fearsome creature imaginable to the subject simply by
forming the fears of the subject's subconscious mind into something that its conscious mind can
visualize: this most horrible beast. Only the spell's subject can see the phantasmal killer. You see
only a vague shape. The target first gets a Will save to recognize the image as unreal. If that save
fails, the phantasm touches the subject, and the subject must succeed on a Fortitude save or die
from fear. Even if the Fortitude save is successful, the subject takes 3d6 points of damage.

If the subject of a phantasmal killer attack succeeds in disbelieving and possesses telepathy or is
wearing a [helm of telepathy](ref/magic-wondrous/helm-of-telepathy), the beast can be turned upon
you. You must then disbelieve it or become subject to its deadly fear attack.

### Mythic Phantasmal Killer

**Sources:** Mythic Adventures pg 103\
If the target fails its Will save but succeeds at its Fortitude save, the phantasmal killer persists
in the target's mind, giving it the dazed condition until your next turn. On your next turn, the
target must attempt another Fortitude save against the phantasm. Success means it takes 3d6 points
of damage; failure means it dies from fear.

_Augmented (6th):_ If you expend two uses of mythic power, the spell can affect a living target that
is immune to fear, illusions, or mind-affecting effects.
