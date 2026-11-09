+++
id = "ref/spell/astral-projection-lesser"
kind = "spell"
title = "Lesser Astral Projection"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "astral_projection_lesser", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/astral-projection" },
]
[[sources]]
publication = "ultimate-magic"
page = "207"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "30 minutes"
components = "V, S, M (1,000 gp jacinth)"
range = "touch"
effects = [
  { label = "Targets", value = "you plus one additional willing creature touched per two caster levels" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 30 minutes
Components: V, S, M (1,000 gp jacinth)
Range: touch
Targets: you plus one additional willing creature touched per two caster levels
Duration: see text
Saving throw: none
Spell resistance: yes
:::

### Lesser Astral Projection

This spell functions as [astral projection](ref/spell/astral-projection), except you cannot leave
the Astral Plane and explore other planes (though you can still return to the plane you were on when
you cast this spell).
