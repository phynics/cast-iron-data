+++
id = "ref/spell/calm-emotions"
kind = "spell"
title = "Calm Emotions"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calm_emotions", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "creatures in a 20-ft.-radius spread" },
]
duration = "concentration, up to 1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Cleric, Inquisitor, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: concentration, up to 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: creatures in a 20-ft.-radius spread
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 252

This spell calms agitated creatures. You have no control over the affected creatures, but calm
emotions can stop raging creatures from fighting or joyous ones from reveling. Creatures so affected
cannot take violent actions (although they can defend themselves) or do anything destructive. Any
aggressive action against or damage dealt to a calmed creature immediately breaks the spell on all
calmed creatures.

This spell automatically suppresses (but does not dispel) any morale bonuses granted by spells such
as bless, good hope, and rage, and also negates a bard's ability to inspire courage or a barbarian's
rage ability. It also suppresses any fear effects and removes the confused condition from all
targets. While the spell lasts, a suppressed spell, condition, or effect has no effect. When the
calm emotions spell ends, the original spell or effect takes hold of the creature again, provided
that its duration has not expired in the meantime.
