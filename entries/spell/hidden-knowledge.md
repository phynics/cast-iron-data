+++
id = "ref/spell/hidden-knowledge"
kind = "spell"
title = "Hidden Knowledge"
aon = "SpellDisplay.aspx?ItemName=Hidden%20Knowledge"
source_ids = ["adventurers-guide", "second-darkness-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hidden_knowledge", path = "json/spells5.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "60"
[[sources]]
publication = "second-darkness-players-guide"
page = "26"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 round"
components = "V, S, M (a drop of ink)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "up to 1 day/level (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (a drop of ink)
Range: personal
Duration: up to 1 day/level (see text)
Saving throw: none
Spell resistance: no
Target: you
:::

This subtle but useful spell allows you to safeguard important knowledge - even from yourself. While
casting this spell, you recite one piece of knowledge (up to a maximum of 50 words). Upon completion
of the spell's casting, you transfer the knowledge from your mind to your skin in the form of an
intricate, runic tattoo placed anywhere you choose on your body. The knowledge disappears utterly
from your mind, and you might not realize you forgot something. The magic of the spell patches over
gaps in your memory with recollections from the past. Until the spell's duration ends, the knowledge
is lost to you. When you cast this spell, you decide how long you wish the spell's duration to be,
up to a maximum duration of 1 day per level.

Many [Cyphermages](ref/rule/aff-i-tradition) commission nonmagical tattoos to disguise the effects
of this spell. A [detect magic](ref/spell/detect-magic) spell or a successful Linguistics or
Spellcraft check (DC 20 + your Intelligence modifier) reveals an enchanted tattoo, but not its
contents. The effects of hidden knowledge can be dispelled normally, in which case the knowledge is
completely lost.
