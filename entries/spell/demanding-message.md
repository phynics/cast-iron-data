+++
id = "ref/spell/demanding-message"
kind = "spell"
title = "Demanding Message"
aon = "SpellDisplay.aspx?ItemName=Demanding%20Message"
source_ids = ["core-rulebook", "ultimate-intrigue"]
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
school = "transmutation"
descriptors = ["language-dependant"]
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 0 },
  { class = "Medium", level = 0 },
  { class = "Mesmerist", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Skald", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Spiritualist", level = 0 },
  { class = "Summoner", level = 0 },
  { class = "Unchained Summoner", level = 0 },
  { class = "Witch", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of copper wire)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 0: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of copper wire)
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Targets: one creature/level
Descriptors: language-dependant
:::

### Demanding Message

This spell initially functions as [message (allowing no](ref/spell/message) save or
[spell resistance](ref/rule/spell-resistance)). Once during the message effect, you can concentrate
as a standard action to issue a suggestion to one target as part of delivering a message. Spell
resistance and a Will save apply to the suggestion, and it lasts for 1 hour per level or until
completed.
