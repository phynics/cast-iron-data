+++
id = "ref/spell/weaponwand"
kind = "spell"
title = "Weaponwand"
aon = "SpellDisplay.aspx?ItemName=Weaponwand"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weaponwand", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "63"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 round"
components = "V, S, F (a magic wand)"
range = "touch"
effects = [
  { label = "Target", value = "one weapon" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Bard, Cleric, Inquisitor, Magus, Oracle, Skald, Warpriest
Casting time: 1 round
Components: V, S, F (a magic wand)
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one weapon
:::

When you cast this spell on a weapon, you cause a portion of the weapon to open like the skin of a
partially peeled apple, revealing a space large enough to insert a single wand within. As part of
the spell's casting, you can insert a single wand into the weapon, at which point the weapon returns
to its original form with the wand held inside of it without negatively impacting the weapon's
integrity. For the spell's duration, a character who wields the transmuted weapon is also considered
to be wielding the wand as well. You can attack normally with the weapon or use the weapon as if it
were the encased wand. If the effect created by the wand requires an attack roll to successfully
strike a foe, you may make the attack roll as if you were making an attack with the weapon at its
highest bonus (including any bonuses the weapon would normally receive) rather than just a normal
attack with the wand-doing so does not allow you to add the weapon's damage to the wand's attack
roll, but instead allows you to use your skill with the weapon to boost your chance of hitting with
the spell.

At the end of the spell's duration, the encased wand is ejected from the weapon. If you have a free
hand, you may catch the weapon as a free action; otherwise, the wand drops to the ground. If the
weapon housing the wand is broken or destroyed during the duration of weaponwand, the encased wand
is similarly broken or destroyed.
