+++
id = "ref/arc-rogue/shadow-walker"
kind = "archetype"
title = "Shadow Walker"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_walker", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Rogue talent gained at 2nd level", "trap sense", "Uncanny dodge", "improved uncanny dodge"]
+++

**Sources:** Blood of Shadows pg 9\
Shadow walkers are comfortable in light, darkness, and the shadows in between. Fetchling rogues
naturally gravitate toward becoming shadow walkers, but shadow walkers exist among other creatures
both above and below the surface.

**Expanded Sight (Su)**

**At 3rd Level:** The shadow walker loses the [light sensitivity](ref/umr/light-sensitivity)
weakness, if she has it. If she has [light blindness](ref/umr/light-blindness), she instead treats
it as light sensitivity.

**Gained:** At 1st Level

**Passive:** A shadow walker gains [darkvision](ref/rule/darkvision) with a range of 30 feet. If she
already has darkvision, the range of her darkvision increases by 10 feet.

**Repeat:** The range of her [darkvision](ref/rule/darkvision) increases by 10 feet., 3, 2

**Replaces:** Trapfinding

**Illumination Control (Sp)**

**Ability:** At the start of each day, a shadow walker gains a number of illumination points equal
to half her rogue level and can spend illumination points to use certain
[spell-like abilities](ref/umr/spell-like-abilities). As long as she has at least 1 illumination
point, she can cast [light](ref/spell/light) at will. She can spend 2 illumination points to cast
[darkness](ref/spell/darkness), and 3 illumination points to cast [daylight](ref/spell/daylight),
[deeper darkness](ref/spell/deeper-darkness), or
[motes of dusk and dawn](ref/spell/motes-of-dusk-and-dawn).

**Flavor:** A shadow walker can manipulate nearby illumination.

**Gained:** At 3rd Level

**Replaces:** Rogue talent gained at 2nd level, trap sense

**Special:** These [spell-like abilities](ref/umr/spell-like-abilities) have a caster level equal to
the shadow walker's rogue level. Using these spell-like abilities does not hamper the shadow
walker's vision; for example, she can see through the _[deeper darkness](ref/spell/deeper-darkness)_
she creates, and does not take penalties for light sensitivity in the area of her own
_[daylight](ref/spell/daylight)._

**Favored Illumination (Su)**

**Ability:** While she is within her chosen illumination level, she gains a bonus (equal to 1 +
[one-third](ref/misc/fractions-and-rounding) of her rogue level) on initiative checks and
Acrobatics, Perception, and Sleight of Hand skill checks, and can take 10 on any Stealth check
attempted within that illumination level.

**Choice:** A shadow walker chooses one [illumination level](ref/rule/vision-and-light): bright
light, normal light, dim light, or darkness (including supernatural darkness).

**Gained:** At 4th Level

**Replaces:** Uncanny dodge, improved uncanny dodge

**Special:** When the shadow walker confirms a critical hit with a melee attack that deals sneak
attack damage while in her chosen illumination level, she regains 1 illumination point (to a maximum
of half her rogue level). Confirming a critical hit on a creature that has fewer Hit Dice than half
the shadow walker's character level doesn't restore illumination points.

**These rogue talents complement this archetype:** Deft palm, gloom magic, greater gloom magic,
obscuring blow, surprise attack, umbral gear

**These advanced rogue talents complement this archetype:** Hide in plain sight, see in darkness,
slippery mind, unwitting ally, weapon snatcher
