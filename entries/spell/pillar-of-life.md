+++
id = "ref/spell/pillar-of-life"
kind = "spell"
title = "Pillar of Life"
aon = "SpellDisplay.aspx?ItemName=Pillar%20of%20Life"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pillar_of_life", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "236"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["light"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "5-ft.-square pillar of positive energy, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: 5-ft.-square pillar of positive energy, 20 ft. high
Subschool: Healing
Descriptors: light
:::

You conjure a pillar of positive energy in a single 5-foot square within range that radiates light
as if it were a sunrod. Living creatures adjacent to the pillar can spend a standard action to touch
the pillar and heal 2d8 points of damage + 1 point per caster level (maximum +20). Creatures can
move into the square containing the pillar, but if an undead creature moves into the pillar it takes
1d6 points of damage per caster level (maximum 10d6). Undead creatures vulnerable to bright light
take 1d8 points if damage per caster level (maximum 10d8). A creature cannot benefit or suffer more
than once from a single casting of this spell.
