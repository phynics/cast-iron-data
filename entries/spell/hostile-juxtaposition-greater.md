+++
id = "ref/spell/hostile-juxtaposition-greater"
kind = "spell"
title = "Greater Hostile Juxtaposition"
aon = "SpellDisplay.aspx?ItemName=Hostile%20Juxtaposition%2C%20Greater"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hostile_juxtaposition_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hostile-juxtaposition" },
]
[[sources]]
publication = "ultimate-combat"
page = "231"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/4 levels" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Mesmerist, Summoner\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a coin)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/4 levels
Duration: 1 round/level or until discharged
Saving throw: Will negates
Spell resistance: yes
Subschool: Teleportation
:::

### Greater Hostile Juxtaposition

This spell functions like [hostile juxtaposition](ref/spell/hostile-juxtaposition), except you can
target one creature for every four caster levels you have or you can target a single creature that
is larger than you are. You can switch places with each target only once while the effect lasts.
Once you have used it to teleport and switch places with each affected target, the spell is
discharged.
