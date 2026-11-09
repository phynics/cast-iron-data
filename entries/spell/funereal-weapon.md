+++
id = "ref/spell/funereal-weapon"
kind = "spell"
title = "Funereal Weapon"
aon = "SpellDisplay.aspx?ItemName=Funereal%20Weapon"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "funereal_weapon", path = "json/spells13.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "42"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched or 50 projectiles (all of which must be together at the time of casting)" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Inquisitor, Occultist, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: weapon touched or 50 projectiles (all of which must be together at the time of casting)
:::

You imbue a weapon with a faint silvery glow that dimly illuminates a 5-foot square. An affected
weapon also easily bypasses the physical defenses of undead creatures, ignoring 5 points of an
undead creature's [damage reduction](ref/rule/damage-reduction), as long as the damage reduction is
not DR/epic. For example, attacks with a weapon affected by this spell completely ignore a zombie's
DR 5/slashing or reduce a lich's damage reduction to DR 10/bludgeoning and magic.

You can't cast this spell on a natural weapon, such as an unarmed strike. Funereal weapon affects
the DR of only undead creatures.
