+++
id = "ref/spell/fable-tapestry"
kind = "spell"
title = "Fable Tapestry"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fable_tapestry", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shadow-conjuration" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 round"
components = "V, S, F (your kapenia)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1 legendary character/4 caster levels" },
]
duration = "1 round/level"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Bard, Skald
Casting time: 1 round
Components: V, S, F (your kapenia)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will disbelief
Spell resistance: yes
Effect: 1 legendary character/4 caster levels
Subschool: Shadow
Descriptors: shadow
:::

**Sources:** Inner Sea Races pg 219

> _The following spell is available to the indicated race or ethnicity: Varisian_

The spell weaves shadows and colors from your kapenia into the shape of legendary characters from
Varisian folktales. This spell functions as [shadow conjuration](ref/spell/shadow-conjuration)
emulating [summon monster I](ref/spell/summon-monster-1), except as noted here. You can summon only
one copy of the same character at the same time, even with multiple castings of this spell. The
shadow creatures are 40% real and are drawn from the list below.

- Anelda the beautiful ([freelance thief](ref/npc/freelance-thief))
- Old Mother Toad ([giant toad](ref/monster/toad-giant-toad) with
  [fey animal](ref/template/fey-animal) template)
- Sonnorae the storyteller ([con artist](ref/npc/con-artist))
- Vyushbaro the savior ([carousing champion](ref/npc/carousing-champion))
- Winter's Son ([evasive slip](ref/npc/evasive-slip))
- Zykomso the slaver ([bearded devil](ref/monster/devil-bearded-devil-barbazu)
