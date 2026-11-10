+++
id = "ref/spell/magic-aura"
kind = "spell"
title = "Magic Aura"
aon = "SpellDisplay.aspx?ItemName=Magic%20Aura"
source_ids = ["core-rulebook", "ultimate-intrigue", "adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_aura", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "307"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (a small square of silk that must be passed over the object that receives the aura)"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing up to 5 lbs./level" },
]
duration = "1 day/level (D)"
saving_throw = "none; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a small square of silk that must be passed over the object that receives the aura)
Range: touch
Duration: 1 day/level (D)
Saving throw: none; see text
Spell resistance: no
Target: one touched object weighing up to 5 lbs./level
Subschool: Glamer
Descriptors: glamer
:::

You alter an item's aura so that it registers to detect spells (and spells with similar
capabilities) as though it were nonmagical, or a magic item of a kind you specify, or the subject of
a spell you specify. If the object bearing magic aura has identify cast on it or is similarly
examined, the examiner recognizes that the aura is false and detects the object's actual qualities
if he succeeds on a Will save. Otherwise, he believes the aura and no amount of testing reveals what
the true magic is.

If the targeted item's own aura is exceptionally powerful (if it is an artifact, for instance),
magic aura doesn't work.

_Note:_ A magic weapon, shield, or suit of armor must be a masterwork item, so a sword of average
make, for example, looks suspicious if it has a magical aura.
