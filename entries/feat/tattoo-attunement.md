+++
id = "ref/feat/tattoo-attunement"
kind = "feat"
title = "Tattoo Attunement"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tattoo_attunement", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/inscribe-magical-tattoo", label = "or" },
  { kind = "prerequisite", target = "ref/feat/varisian-tattoo", label = "or" },
]

[fields]
kind = "feat"
prerequisites = "Inscribe Magical Tattoo or Varisian Tattoo; Spellcraft 5 ranks."
prerequisite_feats = ["ref/feat/inscribe-magical-tattoo", "ref/feat/varisian-tattoo"]
benefit = "As a standard action, you can touch a single creature that you've summoned, instantly transforming it into a magical tattoo on your body. This tattoo takes up one magic item slot if the summoned creature is Medium or smaller, and one additional adjacent slot for each size category larger than Medium. You can have only one such tattoo at a time."
+++

**Sources:** Monster Summoner's Handbook pg 14

You've learned to absorb summoned creatures into temporary spell tattoos.\
**Prerequisites:** [Inscribe Magical Tattoo](ref/feat/inscribe-magical-tattoo) or
[Varisian Tattoo](ref/feat/varisian-tattoo); Spellcraft 5 ranks.\
**Benefit:** As a standard action, you can touch a single creature that you've summoned, instantly
transforming it into a magical tattoo on your body. This tattoo takes up one magic item slot if the
summoned creature is Medium or smaller, and one additional adjacent slot for each size category
larger than Medium. You can have only one such tattoo at a time.

While in tattoo form, the summoned creature can't take actions and doesn't need to eat, sleep, or
breathe; it retains the remaining duration of the summoning spell used to conjure it. The creature
can stay in tattoo form for a number of hours equal to your caster level. If the creature is still
in tattoo form at the end of that time, the tattoo disappears, the creature is sent back to the
plane from which it was summoned, and the remaining duration of the summon is wasted. As a standard
action that provokes attacks of opportunity, you can cause the creature to change from a tattoo back
into creature form, and appear in a square adjacent to you. The remaining duration of the spell is
then expended as normal. The creature is [staggered](ref/misc/staggered) for 1 round after emerging
from tattoo form. This is a supernatural ability.
