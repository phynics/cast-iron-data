+++
id = "ref/spell/psychic-reading"
kind = "spell"
title = "Psychic Reading"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_reading", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-adventures"
page = "183"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Medium, Mesmerist, Occultist, Psychic, Spiritualist\
2: Arcanist, Bard, Inquisitor, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: none
Spell resistance: yes
Target: one humanoid creature
:::

You are able to read a person's surface thoughts and take cues from the person's appearance, body
language, and manner of speech to infer a great deal of information about the person, even if that
person is in disguise (including polymorph effects). When casting the spell, attempt a DC 20 Sense
Motive check with a bonus equal to your caster level. A successful skill check reveals to you one of
the following pieces of information of your choice, plus one additional piece of information for
every 5 points by which your check result exceeds 20: age, alignment, class\*, feats\*, gender,
native language, place of origin, race or ethnicity, racial traits\*, religion, sexual orientation,
or training in a Craft, Perform, or Profession skill. For items marked with an asterisk (\*), if the
target has more than one of these features, each one you discover counts as a piece of information.

There's a 70% chance that all information you receive is correct. This roll is made secretly.
Otherwise, on a roll of 71-80, you receive one false piece of information, on a roll of 81-90 you
receive two, and on a roll of 91-100 you receive three. You can't get more false information than
the total number of pieces of information you discover.
