+++
id = "ref/spell/ricochet-shot"
kind = "spell"
title = "Ricochet Shot"
aon = "SpellDisplay.aspx?ItemName=Ricochet%20Shot"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ricochet_shot", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "243"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a wishbone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one projectile weapon" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Hunter, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a wishbone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one projectile weapon
:::

You imbue a projectile weapon with the ability to ricochet any projectiles that hit one target so
that they also hit another. When the wielder ricochets a projectile, she selects a primary target to
attack. If she hits the primary target, the projectile ricochets instead of being destroyed. The
wielder can then select a secondary target that is within 20 feet of the primary target. She makes
an attack roll against the secondary target at the same base attack bonus, but does not gain the
benefit from any enhancement bonuses or magic qualities on the projectile. If the shot comes from a
firearm, the ricochet targets normal AC rather than touch AC.

While the spell lasts, the target weapon's wielder can ricochet one projectile per three caster
levels you possess, to a maximum of six at caster level 18th. Once the target weapon's wielder
ricochets that many shots, the spell is discharged. If the weapon's wielder fails to use all the
ricochets before the spell end, those ricochets are wasted.
