+++
id = "ref/spell/black-spot"
kind = "spell"
title = "Black Spot"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "black_spot", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Oracle, Warpriest, Witch\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** Pirates of the Inner Sea pg 28

The black spot is a specific and feared pirate curse. An intangible, illusory black spot manifests
above the target's head and remains until the target dies or the curse is lifted. The black spot
cannot be covered or hidden by any means, including other illusions.

The black spot radiates a cursed aura in a 10-foot radius around its target. Anyone within the aura
gains a +2 bonus on weapon attack and damage rolls against the target. In addition, the target has a
-4 penalty on saving throws against death effects.

Every day in which a creature bears a black spot, it must make a Fortitude save. On a failed save,
the creature takes 1 point of Constitution damage. The damage cannot be healed until the black spot
is removed. If the creature's Constitution reaches 0, it dies. Pirates killed by this spell often
return as ghosts, but that is not a direct effect of this spell.

The black spot cannot be dispelled, but it can be removed with
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish).
