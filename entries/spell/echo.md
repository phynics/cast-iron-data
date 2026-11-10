+++
id = "ref/spell/echo"
kind = "spell"
title = "Echo"
aon = "SpellDisplay.aspx?ItemName=Echo"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "echo", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "229"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "S, F (a conch shell)"
range = "close (25 ft. + 5 ft./2 levels) or long (400 ft. + 40 ft./level); see text"
effects = [
  { label = "Area", value = "one 10-ft. cube/level (S)" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Bard, Druid, Hunter, Medium, Mesmerist, Occultist, Psychic, Ranger, Skald, Spiritualist, Witch
Casting time: 1 standard action
Components: S, F (a conch shell)
Range: close (25 ft. + 5 ft./2 levels) or long (400 ft. + 40 ft./level); see text
Duration: 1 round/level (D)
Saving throw: Will disbelief (if interacted with)
Spell resistance: yes
Area: one 10-ft. cube/level (S)
Subschool: Figment
:::

You cause a sound heard in the target area up to 1 round ago and lasting up to 1 round in duration
to repeat at a regular interval. The original sound need not have come from the area, but it echoes
from the target area at its original full volume. Any special effects of the sound are not
duplicated by this spell. If the area is naturally prone to echoes, such as a space surrounded on at
least two sides by cliffs or high river banks, the spell's range is long. Otherwise, the spell's
range is close.

You can concentrate as a standard action to alter the echo. You can change it to be any sound
audible in the area within the last 1 round, move the apparent source of the sound within the area,
or attempt a Bluff check to create a distraction to hide with a bonus equal to your caster level.
