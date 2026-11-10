+++
id = "ref/spell/spear-of-purity"
kind = "spell"
title = "Spear of Purity"
aon = "SpellDisplay.aspx?ItemName=Spear%20of%20Purity"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spear_of_purity", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "240"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "spear-shaped projectile of good energy" },
]
duration = "instantaneous (1 round)"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous (1 round)
Saving throw: Will partial (see text)
Spell resistance: yes
Effect: spear-shaped projectile of good energy
Descriptors: good
:::

You hurl a pure white or golden spear of light from your holy symbol, affecting any one target
within range as a ranged touch attack.

An evil creature struck by the spear takes 1d8 points of damage per two caster levels (maximum 5d8).
An evil outsider instead takes 1d6 points of damage per caster level (maximum 10d6) and is blinded
for 1 round. A successful Will save reduces the damage to half and negates the blinded effect. This
spell deals only half damage to creatures that are neither evil nor good, and they are not blinded.
The spear has no effect on good creatures.
