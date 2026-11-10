+++
id = "ref/spell/magic-weapon-greater"
kind = "spell"
title = "Greater Magic Weapon"
aon = "SpellDisplay.aspx?ItemName=magic%20weapon%2C%20greater"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_weapon_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-weapon" },
]
[[sources]]
publication = "core-rulebook"
page = "310"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (powdered lime and carbon)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one weapon or 50 projectiles (all of which must be together at the time of casting)" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Antipaladin, Arcanist, Bloodrager, Inquisitor, Magus, Occultist, Paladin, Red Mantis Assassin, Sorcerer, Wizard\
4: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (powdered lime and carbon)
Range: close (25 ft. + 5 ft./2 levels)
Target: one weapon or 50 projectiles (all of which must be together at the time of casting)
Duration: 1 hour/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
:::

### Greater Magic Weapon

This spell functions like [magic weapon](ref/spell/magic-weapon), except that it gives a weapon an
enhancement bonus on attack and damage rolls of +1 per four caster levels (maximum +5). This bonus
does not allow a weapon to bypass [damage reduction](ref/rule/damage-reduction) aside from magic.

Alternatively, you can affect as many as 50 arrows, bolts, or bullets. The projectiles must be of
the same kind, and they have to be together (in the same quiver or other container). Projectiles,
but not thrown weapons, lose their transmutation after they are used. Treat shuriken as projectiles,
rather than as thrown weapons, for the purpose of this spell.
