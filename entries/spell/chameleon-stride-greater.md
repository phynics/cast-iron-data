+++
id = "ref/spell/chameleon-stride-greater"
kind = "spell"
title = "Greater Chameleon Stride"
source_ids = ["advanced-players-guide", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chameleon_stride_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/chameleon-stride" },
]
[[sources]]
publication = "advanced-class-guide"
page = "177"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "5 ft."
effects = [
  { label = "Area", value = "allies in a 10-ft.-radius emanation centered on you" },
]
duration = "1 minute/level (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: 5 ft.
Area: allies in a 10-ft.-radius emanation centered on you
Duration: 1 minute/level (see text)
Saving throw: none
Spell resistance: no
Subschool: Glamer
Descriptors: glamer
:::

### Greater Chameleon Stride

This spell functions as [chameleon stride](ref/spell/chameleon-stride), except it confers its
bonuses upon all allies within 10 feet of you at the time the spell is cast. Those affected by this
spell are able to see each other and themselves as if they were unaffected by the spell. If an
affected creature moves out of the area, it loses the benefit of the spell. Creatures that move into
the area after the spell is cast do not gain its benefit.
