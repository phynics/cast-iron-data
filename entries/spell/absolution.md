+++
id = "ref/spell/absolution"
kind = "spell"
title = "Absolution"
aon = "SpellDisplay.aspx?ItemName=Absolution"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absolution", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "203"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 round"
components = "V, S, DF, M (a vial of holy water)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 round
Components: V, S, DF, M (a vial of holy water)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: living creature touched
:::

You purge impure thoughts from the target's mind and fill him with exultant relief at the
forgiveness of his sins. Absolution ends all charm or compulsion effects affecting the target
(including harmless compulsions, such as [heroism](ref/spell/heroism)) as per
[break enchantment](ref/spell/break-enchantment). If the target was forced to perform any actions
contrary to his alignment, monk vows, paladin oath, or similar code of conduct by that charm or
compulsion effect, that action doesn't cause him to lose access to class abilities, including divine
spellcasting.

Unlike an [atonement](ref/spell/atonement) spell, absolution can't reverse alignment change or the
effects of willing transgressions, induce a creature to change its alignment, or restore class
abilities lost because of misdeeds performed in the past. Absolution automatically works if the
caster and the target share the same alignment or the same patron deity. If they don't, but their
alignments are within one step of each other, absolution has a 5% chance of success per caster
level. If neither of these is true, the spell automatically fails.

If using the honor subsystem, casting absolution also eliminates the honor loss for events and
actions committed by the target while he was affected by a charm or compulsion effect that the spell
ended.
