+++
id = "ref/spell/reloading-hands"
kind = "spell"
title = "Reloading Hands"
aon = "SpellDisplay.aspx?ItemName=Reloading%20Hands"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reloading_hands", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "242"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "projectile weapon touched" },
]
duration = "1 round/caster level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Hunter, Magus, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/caster level (D)
Saving throw: none
Spell resistance: no
Target: projectile weapon touched
Subschool: Creation
:::

Once per round, phantom hands load a single ranged weapon or firearm with conjured ammunition. This
ammunition counts as magical for overcoming [damage reduction](ref/rule/damage-reduction) and
attacking incorporeal creatures, but is the standard for its type (a normal bullet or pellets and
black powder in the case of firearms). Conjured ammunition ceases to exist 1 round after it is
removed from the weapon, or at the end of the duration, whichever comes first.
