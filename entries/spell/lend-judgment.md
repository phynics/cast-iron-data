+++
id = "ref/spell/lend-judgment"
kind = "spell"
title = "Lend Judgment"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lend_judgment", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Inquisitor", level = 1 },
]
casting_time = "1 standard action"
components = "V, DF"
range = "touch"
effects = [
  { label = "Target", value = "one ally" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Inquisitor
Casting time: 1 standard action
Components: V, DF
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one ally
:::

**Sources:** Ultimate Magic pg 226

You create a conduit of divine knowledge and outrage between you and an ally. That ally gains the
benefit of one of your active judgments (as do you). If you cannot use a judgment (for example, if
you are not in combat, are frightened or unconscious, and so on) or change judgments, the ally loses
the benefit of the judgment. If you have multiple judgments active, the ally gains only one, chosen
when you cast this spell.
