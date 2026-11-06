+++
id = "ref/spell/call-the-void"
kind = "spell"
title = "Call the Void"
source_ids = ["dragon-empires-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_the_void", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "Reflex for half, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: Reflex for half, see text
Spell resistance: yes
Target: you
:::

**Sources:** Dragon Empires Primer pg 29

This spell surrounds you with an aura of nothingness that channels the mysterious energies of the
Dark Tapestry. Creatures adjacent to you when this spell is cast and at the start of your turn take
2d6 points of damage. In addition, creatures affected by your aura are fatigued, cannot breathe, and
cannot speak or cast spells with somatic components. Creatures adjacent to you are allowed a Reflex
save to halve the damage and negate the fatigue effect, but cannot breathe or speak regardless of
whether their save is successful as long as they are adjacent to you.
