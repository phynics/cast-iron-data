+++
id = "ref/spell/sentry-skull"
kind = "spell"
title = "Sentry Skull"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sentry_skull", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "143"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 hour"
components = "V, S, M (an onyx gem worth at least 10 gp)"
range = "touch"
effects = [
  { label = "Target", value = "severed head touched" },
]
duration = "permanent (d); see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin\
2: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 hour
Components: V, S, M (an onyx gem worth at least 10 gp)
Range: touch
Duration: permanent (d); see text
Saving throw: none
Spell resistance: no
Target: severed head touched
Descriptors: evil
:::

> _[Orcs](ref/race/orc) have access to the following spell._

You restore the senses to the severed head of a humanoid or monstrous humanoid killed within the
past 24 hours, creating a grisly sentinel. The head must be affixed to a pole, spear, tree branch,
or other stable object, and the spell ends if the head or its object is moved. The head has
[darkvision](ref/rule/darkvision) 60 feet and [low-light vision](ref/rule/low-light-vision), can
swivel in place to look in any direction, and has a +5 bonus on Perception checks.

If you are within 30 feet of the head, as a standard action you can shift your senses to it, seeing
and hearing from its location and gaining the benefit of its [darkvision](ref/rule/darkvision) and
[low-light vision](ref/rule/low-light-vision), and you may use its Perception skill instead of your
own. While your senses are in the severed head, your body is blind and deaf until you spend a free
action to shift your senses back to your own body.

When you create the head, you can imprint it with a single triggering condition, similar to
[magic mouth](ref/spell/magic-mouth). Once this triggering condition is set, it can never be
changed. If you are within 30 feet of the head, you immediately know if it is triggered (if you have
multiple active sentry skulls, you also know which one was triggered). This wakens you from normal
sleep but does not otherwise disturb your concentration. For example, you could have a sentry skull
alert you if any humanoid comes into view, if a particular rival approaches, if your guard animal is
killed, and so on, as long as it occurs where the severed head can see it.

This spell does not give the head any ability to speak, think, or take any kind of action other than
to turn itself, though it is a suitable target for other spells such as magic mouth.
