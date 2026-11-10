+++
id = "ref/spell/underbrush-decoy"
kind = "spell"
title = "Underbrush Decoy"
aon = "SpellDisplay.aspx?ItemName=Underbrush%20Decoy"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "underbrush_decoy", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "228"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 swift action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one non-creature plant of size Tiny, Small, or Medium" },
]
duration = "1 round"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 swift action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one non-creature plant of size Tiny, Small, or Medium
:::

You cause a plant to rustle noisily, distracting nearby creatures. You can attempt a Bluff check to
create a distraction to hide, using your caster level + your Wisdom modifier in place of your total
Bluff skill bonus and applying the result to all creatures within 30 feet. You count the target as
distracted, as do any creatures that knew about your distraction in advance. Creatures might not be
distracted if they detect you casting the spell or otherwise anticipate your subterfuge.
