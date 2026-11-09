+++
id = "ref/spell/siphon-magic"
kind = "spell"
title = "Siphon Magic"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siphon_magic", path = "json/spells9.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "60"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a coiled length of copper wire wrapped around the palm)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a coiled length of copper wire wrapped around the palm)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: creature touched
:::

This spell attempts to transfer a magical effect from a creature you touch to yourself. When you
touch the creature, siphon magic attempts to end one ongoing spell that has been cast on that
creature, as if via a targeted [dispel magic](ref/spell/dispel-magic). If you know the specific
spell effect you wish to target, you can name that spell effect to target that specific spell;
otherwise siphon magic begins with the highest-level spell in effect and works its way down through
all spells affecting the target until it dispels one or runs out of effects, as per
_[dispel magic](ref/spell/dispel-magic)._

If siphon magic successfully ends a spell effect on the target, the remaining duration of that spell
effect is transferred to you. That spell effect plays out for the rest of its duration as if you had
been the original target. If the spell allows a saving throw to resist the effect, you gain a saving
throw as if the spell were just being cast upon you, although this does not "reset" the spell's
duration.
