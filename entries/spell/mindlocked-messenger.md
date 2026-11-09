+++
id = "ref/spell/mindlocked-messenger"
kind = "spell"
title = "Mindlocked Messenger"
aon = "SpellDisplay.aspx?ItemName=Mindlocked%20Messenger"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindlocked_messenger", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "187"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing living creature" },
]
duration = "permanent until discharged (see text)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Skald\
3: Arcanist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent until discharged (see text)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one willing living creature
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

You speak a short message (up to 10 words per caster level), implanting both it and the identity of
the message's intended recipient in the mind of a willing creature. The creature is aware of the
message and who the recipient is. Any attempt to speak, write, or otherwise communicate the message
to anyone other than its intended recipient causes the target to forget the message for 1d6 minutes.
Attempts to read the target's mind (such as with detect thoughts) or to force the target to reveal
the message (such as with torture or magical compulsion) likewise cause temporary amnesia regarding
the message.

The target can communicate the message only to someone it believes is the intended recipient, which
means that disguises, illusions, and polymorph effects might fool the target into delivering the
message. Once the target communicates the message, the message is permanently erased from the
target's memory.
