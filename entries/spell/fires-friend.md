+++
id = "ref/spell/fires-friend"
kind = "spell"
title = "Fire's Friend"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fires_friend", path = "json/spells4.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "220"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a flame of any size)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Bloodrager, Investigator, Magus
Casting time: 1 standard action
Components: V, S, M (a flame of any size)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: fire
:::

> _The following spell is available to the indicated race or ethnicity: [Goblin](ref/race/goblin)_

You cloak yourself in flames that do not harm you or your carried equipment but damage other
creatures and objects. The flames cast light as a torch. Any creature that attacks you with a
non-reach melee weapon or that begins its turn engaged in a grapple with you takes 1d6 points of
fire damage and must succeed at a Reflex save or catch fire. The creature can negate the damage (and
avoid catching fire) with [spell resistance](ref/rule/spell-resistance). Any time you end your
movement in the same square as a flammable object or creature, that creature or object must succeed
at a Reflex save or catch fire.
