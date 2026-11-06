+++
id = "ref/spell/shadow-weapon"
kind = "spell"
title = "Shadow Weapon"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_weapon", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one shadow weapon" },
]
duration = "1 minute/level"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bloodrager, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level
Saving throw: Will disbelief (if interacted with)
Spell resistance: yes
Effect: one shadow weapon
Subschool: Shadow
Descriptors: shadow
:::

**Sources:** Ultimate Magic pg 237

Drawing upon the Plane of Shadow, you shape a quasi-real masterwork melee weapon of a type you are
proficient with. You may use this weapon to make attacks as if it were a real weapon, dealing normal
damage for a weapon of its type. The first time you hit a creature with the weapon, it may make a
Will save to disbelieve; failure means the weapon deals damage normally, success means it only takes
1 point of damage from the weapon's attacks. The weapon only deals 1 point of damage to objects.

If an attacked creature has [spell resistance](ref/rule/spell-resistance), you make a caster level
check (1d20 + caster level) against that spell resistance the first time the shadow weapon strikes
it. If the weapon is successfully resisted, the spell is dispelled. If not, the target may save to
disbelieve as normal.

At 5th level, the weapon gains a +1 enhancement bonus. At 10th-level, you may increase the
enhancement bonus to +2 or add the frost or keen weapon property. The frost and keen properties have
no effect if the target makes its disbelief save.

The spell ends if the weapon leaves your possession.

### Mythic Shadow Weapon

**Sources:** Mythic Adventures pg 107\
Add your tier to your caster level when determining what enhancement bonus or weapon special
abilities the weapon can have. The weapon deals half damage to creatures that disbelieve in it and
to objects, instead of only 1 point.

You can spend a swift action to transform the weapon into a dull black metal ring on your finger, or
to return it from its ring form to its weapon form in your hand.
