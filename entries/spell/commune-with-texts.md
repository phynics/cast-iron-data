+++
id = "ref/spell/commune-with-texts"
kind = "spell"
title = "Commune with Texts"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "commune_with_texts", path = "json/spells12.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "59"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 minute"
components = "V, S, M (incense worth 250 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "a collection of texts" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Medium, Occultist\
5: Arcanist, Bard, Skald, Sorcerer, Wizard\
6: Cleric, Inquisitor, Oracle, Psychic, Spiritualist, Warpriest
Casting time: 1 minute
Components: V, S, M (incense worth 250 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: a collection of texts
:::

You quickly absorb the knowledge in the target, which can be any assortment of books, scrolls, or
other texts. During the spell's duration, you can search the texts and immediately find the most
relevant information regarding any topic the collection holds, potentially including singling out
spellbooks or scrolls containing individual or particular types of spells. You can attempt Knowledge
checks related to the collection's topics as if you were trained in those skills, and you know
whether the collection contains any information about which you failed a Knowledge check in the past
24 hours. The bonus on Knowledge checks granted by the collection of texts (if any) increases by 2.

Additionally, you always deplete the maximum number of knowledge points from a library whenever you
succeed at a Research check using the target texts while this spell is in effect, even if completing
the Research check takes longer than this spell lasts. Once during the duration of this spell, for a
number of minutes equal to your caster level, you can also speak with the texts about anyone who has
read or handled them previously, as per stone tell.
