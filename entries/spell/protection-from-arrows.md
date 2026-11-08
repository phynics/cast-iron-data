+++
id = "ref/spell/protection-from-arrows"
kind = "spell"
title = "Protection from Arrows"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_arrows", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of tortoiseshell or turtle shell)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Arcanist, Bloodrager, Investigator, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of tortoiseshell or turtle shell)
Range: touch
Duration: 1 hour/level or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 327

The warded creature gains resistance to ranged weapons. The subject gains
[damage reduction](ref/rule/damage-reduction) 10/magic against ranged weapons. This spell doesn't
grant you the ability to damage creatures with similar damage reduction. Once the spell has
prevented a total of 10 points of damage per caster level (maximum 100 points), it is discharged.

### Mythic Protection from Arrows

**Sources:** Mythic Adventures pg 104

The [damage reduction](ref/rule/damage-reduction) increases to 15/magic. The maximum damage
prevented by the spell increases to 15 points per caster level (maximum 150 points). If the spell
prevents all damage from a ranged weapon attack, it turns the projectile or weapon back on the
attacker, using the same attack roll result. If the attacker is also protected by mythic protection
from arrows and its spell completely prevents the damage from the rebounded attack, the weapon or
projectile is destroyed.
