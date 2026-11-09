+++
id = "ref/rule/spell-resistance-um"
kind = "rule"
title = "Spell Resistance"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_resistance_um", path = "json/rules_adv_magic01.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "132"

[fields]
kind = "none"
+++

Whether or not spell resistance applies to a spell depends mostly on whether or not it is an
instantaneous or ongoing magical effect. Spell resistance applies to instantaneous magical effects
(such as [fireball](ref/spell/fireball)) and ongoing magical effects (such as
[wall of fire](ref/spell/wall-of-fire)), but not to nonmagical effects or spells that create
nonmagical effects, whether instantaneous or ongoing. For example,
[wall of stone](ref/spell/wall-of-stone) conjures an instantaneous wall of stone that cannot be
dispelled; spell resistance doesn't help you walk through the spell's wall any more than it would if
you tried to walk through a mortared stone wall in a castle - neither wall is magical, and both
walls remain there even if you use [dispel magic](ref/spell/dispel-magic) or
[antimagic field](ref/spell/antimagic-field) on them.

The general rule is that most spells allow spell resistance. Only when you're deliberately designing
a spell that creates a nonmagical object or nonmagical effect is spell resistance likely to be
irrelevant. You can use [move earth](ref/spell/move-earth) (instantaneous duration) to create a
hill, and spell resistance won't help you get over or through the hill because the spell moves the
earth and thereafter stops being magical; likewise, you can use _[move earth](ref/spell/move-earth)_
to create a pit, and spell resistance won't help you ignore the pit because it's a nonmagical pit,
just as if you had created it with a shovel. [Magic stone](ref/spell/magic-stone) adds magical power
to stones, but spell resistance doesn't help protect against being hit by the stones any more than
spell resistance helps protect against a +1 arrow because the magic is focused on the stones, not on
the creature with spell resistance.

It's a common trick to design a spell that doesn't allow spell resistance so the caster can use it
against creatures who have spell resistance. In many cases, the idea behind the design is just
silly, like a spell that creates a sphere of burning oil and hurls it at the intended area, where it
bursts in an explosion of flame; clearly the intent is to create a nonmagical
_[fireball](ref/spell/fireball)_ that bypasses spell resistance. Golems in particular are often the
intended targets of these spell designs, as their immunity to magic ability makes them completely
immune to any effect that allows spell resistance. You should avoid letting these sorts of trick
spells into your campaign, as they meddle with the balance of encounters (some monsters are designed
to be harder for melee characters to fight, some are designed to be harder for spellcasters to
fight, and some are just supposed to be difficult all around).

Whether or not a spell allows spell resistance is not an indicator of the spell's power; for most
encounters, spell resistance isn't a factor.

If a spell's saving throw entry is marked as "(harmless)" or "(object)," the spell resistance entry
should say that as well.
