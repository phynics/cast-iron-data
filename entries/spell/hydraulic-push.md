+++
id = "ref/spell/hydraulic-push"
kind = "spell"
title = "Hydraulic Push"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hydraulic_push", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature or object" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Druid, Hunter, Magus, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one creature or object
Descriptors: water
:::

**Sources:** Advanced Player's Guide pg 228

You call forth a quick blast of water that knocks over and soaks one creature or square. You can use
this blast of water to make a bull rush against any one creature or object. Your CMB for this bull
rush is equal to your caster level plus your Intelligence, Wisdom, or Charisma modifier, whichever
is highest. This bull rush does not provoke an attack of opportunity. Hydraulic push extinguishes
any normal fires on a creature, object, or in a single 5-foot square which it is targeted against.
Magical fires are unaffected.

### Mythic Hydraulic Push

**Sources:** Mythic Adventures pg 98\
The water is boiling hot or freezing cold, dealing 1d6 points of fire or cold damage per 2 caster
levels. Add your tier to your CMB for the spell.
