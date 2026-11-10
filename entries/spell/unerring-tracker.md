+++
id = "ref/spell/unerring-tracker"
kind = "spell"
title = "Unerring Tracker"
aon = "SpellDisplay.aspx?ItemName=Unerring%20Tracker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unerring_tracker", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "228"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Hunter, Occultist, Ranger\
5: Alchemist, Investigator\
6: Druid
Casting time: 10 minutes
Components: V, S, DF
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

During this spell's duration, you can touch the sign of a creature's passage that you have
identified using the Survival skill to make the other steps in the creature's path perfectly clear
to you, no matter how minute. This trail can't be more than 24 hours old. You can follow the trail
at any speed, provided you have line of sight to the trail. You can distinguish the trail of the
particular creature followed even if it joins and splits with other trails. Once you have selected a
trail to follow using this spell, it can't be changed.

The spell is unable to follow teleportation or interplanar travel for any distance. The trail
appears to end where the creature teleported (though a successful Spellcraft check allows you to
determine the method of teleportation, if a spell was used). Unerring tracker can't track creatures
under the effect of a pass without trace spell, as those creatures leave no trail at all, but can
track creatures using nondetection (though not mind blank).

This spell can be used to track flying creatures, but the trail must at least begin on a solid
surface.

This spell doesn't reveal the creature's current position or any shorter path than the one it
followed (for instance, it will not reveal that the creature doubled back upon the trail until you
reach the point where the creature turned around.) It doesn't reveal traps or other hazards along
the trail.
