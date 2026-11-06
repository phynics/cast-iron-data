+++
id = "ref/spell/analyze-aura"
kind = "spell"
title = "Analyze Aura"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "analyze_aura", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Spiritualist", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "concentration, up to 1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Medium, Occultist\
3: Mesmerist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration, up to 1 round/level
Saving throw: none
Spell resistance: no
Target: one creature or object
:::

**Sources:** Occult Adventures pg 156

You peer into the aura of one target creature or object, gaining valuable information about its
condition and nature. Each round, choose one of the target's four auras. This spell functions
similarly to the read aura occult skill unlock, but doesn't require checks and returns results on
all the target's auras in an instant.

_Alignment Aura:_ You study the target's spiritual nature to determine its alignment. You also learn
the type and power of its alignment aura, as [detect evil](ref/spell/detect-evil).

_Emotion Aura:_ The colors playing within the target's aura reveal its emotional state, granting
valuable insight into its psyche. You learn a general summary of the target's current disposition,
as well as its attitude toward any other creatures within 30 feet of it. For the duration of the
spell and for 1 hour afterward, you gain a +2 circumstance bonus on Bluff, Diplomacy, Intimidate,
and Sense Motive checks you attempt against the target. Objects do not have emotion auras, except
intelligent weapons and similar sentient oddities.

_Health Aura:_ The flow of vital force animating the target becomes plainly visible, giving you
insight into its physical condition. You know whether the target is unharmed or wounded, whether it
is poisoned or diseased, and whether it is under any of the following conditions: confused,
disabled, dying, nauseated, panicked, staggered, stunned, or unconscious. Further, your insight into
the overall strength of the target's vital force reveals the total number of points available in its
ki pool, grit pool, or similar resource. Objects and most undead creatures don't have health auras.

_Magic Aura:_ You determine the number and power of all magical auras on the target (as
[detect magic](ref/spell/detect-magic) to determine a magic aura's power), as well as the school of
each aura. You can attempt Knowledge (arcana) or Spellcraft skill checks to determine the school or
identify properties of a magic item, as normal. If cast on an item, analyze aura cuts through the
obfuscation of the magic aura spell.
