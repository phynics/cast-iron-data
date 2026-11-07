+++
id = "ref/spell/shadow-transmutation-greater"
kind = "spell"
title = "Greater Shadow Transmutation"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_transmutation_greater", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Target", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief (if interacted with), varies, see text"
spell_resistance = "yes, see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 9: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Target: see text
Duration: see text
Saving throw: Will disbelief (if interacted with), varies, see text
Spell resistance: yes, see text
Subschool: Shadow
Descriptors: shadow
:::

## Shadow Transmutation

**Sources:** Blood of Shadows pg 30

You suffuse one subject's body with energy from the Shadow Plane, altering its form to match a
creature from the Shadow Plane. Shadow transmutation can mimic any of the following spells: animal
growth, anthropomorphic animal, enlarge person, fins to feet, longarm, polymorph, reduce person, and
stone fist. If using shadow transmutation as polymorph, the target does not gain any sensory
abilities that its new form has (such as [low-light vision](ref/rule/low-light-vision) or
[darkvision](ref/rule/darkvision)) and the speed of any movement types gained from the spell cannot
exceed the target's base speed or natural speed with those movement types (whichever is higher). A
creature under the effects of shadow transmutation deals normal damage and has all the normal
abilities and weaknesses of whatever form it assumes using the spell.

Any creature that interacts with a target under the effects of the spell (including attacking or
being attacked by that creature) can attempt a Will save to recognize the target's true nature.
Creatures that succeed at their Will saves to disbelieve the illusion take one-fifth (20%) of the
normal damage from the target's natural attacks or special abilities granted by the target's shadowy
form (if any), and the target's special abilities that don't deal damage have only a 20% chance of
working against them. Creatures that succeed at their saves see the shadow transmutation as
transparent images superimposed over the target.

### Greater Shadow Transmutation

**Sources:** Blood of Shadows pg 31

This spell functions like shadow transmutation, except it can mimic greater polymorph instead of
polymorph. The illusory attacks and special abilities of any shape assumed using greater shadow
transmutation deal three-fifths (60%) damage to nonbelievers, and non-damaging effects are 60%
likely to work against nonbelievers.
