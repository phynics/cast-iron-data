+++
id = "ref/spell/allegro"
kind = "spell"
title = "Allegro"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "allegro", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "205"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (d) or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Skald
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level (d) or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

This spell allows you to act more swiftly while maintaining a bardic performance. You must already
be maintaining a bardic performance before you can cast allegro. You gain the benefits of the spell
haste for as long as you maintain that bardic performance. If you cease maintaining the bardic
performance or it is interrupted, this spell's duration ends. As an immediate action while you are
maintaining a bardic performance, you can dismiss allegro to reroll a Reflex save or Dexterity-based
skill check-you must choose to reroll before the result of the original roll is known. You must take
the result of the reroll, even if it's worse than the original roll. Allegro dispels and is
dispelled by [slow](ref/spell/slow).
