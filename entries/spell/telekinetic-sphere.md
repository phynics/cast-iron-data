+++
id = "ref/spell/telekinetic-sphere"
kind = "spell"
title = "Telekinetic Sphere"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telekinetic_sphere", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/resilient-sphere" },
]
[[sources]]
publication = "core-rulebook"
page = "358"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a crystal sphere and a pair of small magnets)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1-ft.-diameter/level sphere, centered around creatures or objects" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Psychic\
8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a crystal sphere and a pair of small magnets)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Reflex negates (object)
Spell resistance: yes (object)
Effect: 1-ft.-diameter/level sphere, centered around creatures or objects
Descriptors: force
:::

This spell functions like [resilient sphere](ref/spell/resilient-sphere), but the creatures or
objects caught inside the globe created by the spell are made nearly weightless. Anything contained
within a telekinetic sphere weighs only one-sixteenth of its normal weight. You can telekinetically
lift anything in the sphere that normally weighs 5,000 pounds or less. The telekinetic control
extends from you out to medium range (100 feet + 10 feet per caster level) after the sphere has
succeeded in encapsulating its contents.

You can move the sphere, along with the objects and creatures it contains that weigh a total of
5,000 pounds or less, by concentrating on the sphere. You can begin moving a sphere in the round
after casting the spell. If you concentrate on doing so (a standard action), you can move the sphere
as much as 30 feet in a round. If you cease concentrating, the sphere does not move in that round
(if on a level surface) or descends at its falling rate (if aloft) until it reaches a level surface.
You can resume concentrating on your next turn or any later turn during the spell's duration.

The sphere falls at a rate of only 60 feet per round, which is not fast enough to cause damage to
the contents of the sphere.

You can move the sphere telekinetically even if you are in it.
