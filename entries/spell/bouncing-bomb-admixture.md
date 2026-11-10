+++
id = "ref/spell/bouncing-bomb-admixture"
kind = "spell"
title = "Bouncing Bomb Admixture"
aon = "SpellDisplay.aspx?ItemName=Bouncing%20Bomb%20Admixture"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bouncing_bomb_admixture", path = "json/spells2.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "10"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Investigator", level = 3 },
]
casting_time = "1 swift action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Investigator
Casting time: 1 swift action
Components: V, S
Range: personal
Duration: 1 round
Saving throw: Will negates (harmless)
Spell resistance: no
Target: you
:::

Upon drinking an extract created with this formula, you make a significant change to your magical
reserve that modifies the nature of the next bomb you create and throw during this extract's
duration. This effect on your magical reserve has no effect on any discoveries that you use to
modify your bombs, but you can only have one admixture effect (a formula with "bomb admixture" in
its title) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the new one becomes active.

When you throw your next bomb, choose one target that would normally be hit by the bomb's splash
damage. The target is affected as if it suffered a direct hit from the bomb instead.
