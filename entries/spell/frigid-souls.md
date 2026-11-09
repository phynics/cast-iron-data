+++
id = "ref/spell/frigid-souls"
kind = "spell"
title = "Frigid Souls"
aon = "SpellDisplay.aspx?ItemName=Frigid%20Souls"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frigid_souls", path = "json/spells13.json" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "27"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a bloody icicle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one 5-ft. cube/level" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Hunter, Ranger\
4: Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a bloody icicle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: one 5-ft. cube/level
Descriptors: emotion, fear, haunted, mind-affecting
:::

You harness the Irriseni people's palpable fear of their frozen environment and cruel Jadwiga
overlords into a haunt that withers defenses against the cold. Any creature that enters the affected
area must succeed at a Will save or gain [spell resistance](ref/rule/spell-resistance) equal to 11 +
your caster level against any abjuration effect that provides resistance to or protection against
cold damage or cold climates. This spell resistance cannot be voluntarily lowered. Once every 30
minutes as an immediate action, the haunt attempts a dispel check (1d20 + your caster level) against
an active abjuration effect currently protecting a creature in the affected area against cold, even
if it was active before the creature was haunted or it successfully bypassed the spell resistance
imposed by the haunt. Against creatures with multiple layers of protection, these dispel checks
start with the highest-level abjuration effects and work their way down the list. Each time the
haunt attempts a dispel check, the spell's haunt-like manifestation occurs during that round.

#### Haunt Statistics

**Notice:** Perception 25 (to feel a biting chill as if through the touch of a frozen hand)

**Hit points:** 2 hp/level

**Trigger:** proximity

**Reset:** none
