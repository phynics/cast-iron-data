+++
id = "ref/spell/imbue-with-aura"
kind = "spell"
title = "Imbue with Aura"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_with_aura", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "225"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
:::

You infuse another creature with your divine aura, causing the target to radiate an aura identical
to your own clerical aura. The target's actual alignment is not changed, but spells like
[detect evil](ref/spell/detect-evil) or [detect good](ref/spell/detect-good) detect only the aura,
not the creature's actual alignment. For the duration of this spell, effects influenced by the
target's alignment function according to the imposed aura, not the creature's actual aura. When the
spell ends, the target's aura returns to normal, and alignment-affecting magic affects it according
to its actual alignment.
