+++
id = "ref/spell/conditional-favor"
kind = "spell"
title = "Conditional Favor"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conditional_favor", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 swift action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level (D)"
saving_throw = "none (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Antipaladin, Paladin\
2: Bard, Cleric, Inquisitor, Mesmerist, Occultist, Oracle, Skald, Warpriest, Witch
Casting time: 1 swift action
Components: V
Range: touch
Duration: 1 day/level (D)
Saving throw: none (see below)
Spell resistance: yes
Target: one creature
:::

**Sources:** Ultimate Intrigue pg 206

You must cast this spell immediately before casting another spell on the same creature, eliciting a
promise or warning against a behavior and binding the target to the paired spell. If you don't cast
a paired spell, conditional favor has no effect. The paired spell must be from the abjuration,
conjuration (healing), enchantment, or transmutation school or subschool, and must be cast on a
willing creature. If the spell's recipient violates the oath or prohibition while conditional favor
remains in effect, the paired spell is undone as if never cast. If the spell was a healing spell,
the hit point damage or condition you removed returns immediately, even if the subject has enjoyed
subsequent rest or healing. Poisons, diseases, curses, restored ability damage, and negative levels
removed by the paired spell return as well.

Conditional favor recognizes the spirit of your condition and doesn't trigger a violation due to
unintended consequences or circumstances that the subject could not predict with her current
knowledge of the situation. For instance, if the prohibition prevented the subject from laying a
finger on royalty, touching a disguised prince would not count as a violation if the subject did not
recognize the prince, nor would touching a member of royalty while dominated.

The subject of the spell intuitively knows beforehand whether an action will cause it to lose the
paired spell's benefit.
