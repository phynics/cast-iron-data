+++
id = "ref/spell/fly"
kind = "spell"
title = "Fly"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fly", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "284"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (a wing feather)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Medium, Occultist, Psychic, Red Mantis Assassin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a wing feather)
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

The subject can fly at a speed of 60 feet (or 40 feet if it wears medium or heavy armor, or if it
carries a medium or heavy load). It can ascend at half speed and descend at double speed, and its
maneuverability is good. Using a fly spell requires only as much concentration as walking, so the
subject can attack or cast spells normally. The subject of a fly spell can charge but not run, and
it cannot carry aloft more weight than its maximum load, plus any armor it wears. The subject gains
a bonus on Fly skill checks equal to 1/2 your caster level.

Should the spell duration expire while the subject is still aloft, the magic fails slowly. The
subject floats downward 60 feet per round for 1d6 rounds. If it reaches the ground in that amount of
time, it lands safely. If not, it falls the rest of the distance, taking 1d6 points of damage per 10
feet of fall. Since dispelling a spell effectively ends it, the subject also descends safely in this
way if the fly spell is dispelled, but not if it is negated by an antimagic field.
