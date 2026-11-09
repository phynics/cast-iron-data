+++
id = "ref/spell/apparent-master"
kind = "spell"
title = "Apparent Master"
source_ids = ["guardians-of-dragonfall"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "apparent_master", path = "json/spells.json" },
]
[[sources]]
publication = "guardians-of-dragonfall"
page = "32"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one construct; see text" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Skald\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one construct; see text
:::

This charm makes a construct regard you as its master. The spell only affects mindless constructs
that are attuned to the commands of a master, such as animated objects, golems, retrievers, and
shield guardians. All constructs with Intelligence scores, even those that explicitly follow the
commands of their creator, such as an homunculus, are unaffected. If the construct is currently
being threatened or attacked by you or your allies it receives a +5 bonus on its saving throw.

The spell enables you to control the construct completely, with the sole exception that commands
directly resulting in damage break the spell. Any act by you or your apparent allies that damages
the construct also breaks the spell. You can communicate your commands in any spoken language. The
construct reverts to obeying the last commands given by its true master when the spell's duration
expires.

If the construct's true master attempts to command a construct affected by apparent master, you must
win an opposed Charisma check for the construct to continue to follow your commands. Failing this
check breaks the spell.
