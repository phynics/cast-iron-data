+++
id = "ref/spell/guardian-of-faith"
kind = "spell"
title = "Guardian of Faith"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_of_faith", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "abjuration [see text]"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (parchment with a holy text written on it)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one ally" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration \[see text\]
Level: 4: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, M (parchment with a holy text written on it)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: one ally
:::

**Sources:** Advanced Class Guide pg 183

The target gains the benefit of [shield of faith](ref/spell/shield-of-faith) and your choice of
[protection from chaos, evil, good, or law](ref/spell/protection-from-chaos-evil-good-law). As a
move action, the target can transfer this spell to a touched ally, who becomes the new target of the
spell.

The alignment descriptor of this spell matches the alignment descriptor of the protection spell you
chose when casting it. For example, granting the target protection from evil gives this spell the
good descriptor.
