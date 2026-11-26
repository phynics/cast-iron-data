+++
id = "ref/spell/demanding-message"
kind = "spell"
title = "Demanding Message"
aon = "SpellDisplay.aspx?ItemName=Demanding%20Message"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demanding_message", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/message" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "210"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of copper wire)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level" },
]
duration = "10 minutes/level, then 1 hour/level or until completed (d); see text"
saving_throw = "Will negates (see text)"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Medium, Mesmerist, Psychic, Skald\
4: Arcanist, Occultist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of copper wire)
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level, then 1 hour/level or until completed (d); see text
Saving throw: Will negates (see text)
Spell resistance: yes; see text
Targets: one creature/level
Subschool: compulsion
Descriptors: language-dependant, mind-affecting
:::

### Demanding Message

This spell initially functions as [message (allowing no](ref/spell/message) save or
[spell resistance](ref/rule/spell-resistance)). Once during the message effect, you can concentrate
as a standard action to issue a suggestion to one target as part of delivering a message. Spell
resistance and a Will save apply to the suggestion, and it lasts for 1 hour per level or until
completed.
