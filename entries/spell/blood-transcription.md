+++
id = "ref/spell/blood-transcription"
kind = "spell"
title = "Blood Transcription"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_transcription", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "209"

[fields]
kind = "spell"
school = "divination"
descriptors = ["evil"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one dead spellcaster" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Alchemist, Arcanist, Investigator, Magus, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: one dead spellcaster
Descriptors: evil
:::

By consuming 1 pint of blood from a spellcaster killed within the last 24 hours, you can attempt to
learn a spell that spellcaster knew. Select one spell available to the dead spellcaster (this must
be a spell on your spell list); you gain the knowledge of this spell for 24 hours. During this time,
you may write it down (or teach it to your familiar, if you are a witch) using the normal rules for
copying a spell from another source. Once you have learned it, you may prepare the spell normally.
