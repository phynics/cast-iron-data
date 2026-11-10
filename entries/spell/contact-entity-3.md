+++
id = "ref/spell/contact-entity-3"
kind = "spell"
title = "Contact Entity III"
aon = "SpellDisplay.aspx?ItemName=Contact%20Entity%20III"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contact_entity_3", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/contact-entity-2" },
]
[[sources]]
publication = "horror-adventures"
page = "113"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 minute"
components = "V, S, M (see text)"
range = "100 miles"
effects = [
  { label = "Target", value = "up to 20 entities of 6 HD or fewer; see text" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Medium\
2: Arcanist, Cleric, Occultist, Oracle, Psychic, Shaman, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 minute
Components: V, S, M (see text)
Range: 100 miles
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: up to 20 entities of 6 HD or fewer; see text
:::

### Contact Entity III

This spell functions like _[contact entity II](ref/spell/contact-entity-2),_ except that you can
contact creatures from the _contact entity III_ list, and as noted above. Additionally, if a
contacted creature has telepathy, it can send a telepathic message to you of up to 10 words.

|Contact Entity III|Material Component|
| --- | --- |
|[Aatheriexa](ref/monster/aatheriexa)|A swatch of flesh recently damaged by magic \[evil\]|
|[Deep one elder](ref/monster/deep-one-elder-deep-one)|Engraved stone tablet|
|[Flying polyp](ref/monster/flying-polyp)|Eerie music played upon a wind instrument carved from the bone of a living creature \[chaotic, evil\]|
|[Gug](ref/monster/gug)|Fresh flesh of a creature of 5 HD or more \[chaotic, evil\]|
|[Leng hound](ref/monster/leng-hound)|A corpse with grave goods worth 2,000 gp for the Leng hound to guard^[1](ref/spell/contact-entity-3#footnote-l)^|
|[Leng spider](ref/monster/leng-spider)|Head of a denizen of Leng \[evil\]|
|[Moon-beast](ref/monster/moon-beast)|Intelligent humanoid sacrificed while dreaming \[chaotic, evil\]|
|[Spawn of Yog-Sothoth](ref/monster/spawn-of-yog-sothoth)|All blood drained from a sacrificed intelligent humanoid \[chaotic, evil\]|
|[Wendigo](ref/monster/wendigo)|Must devour the flesh of sentient creatures with 8 HD total \[chaotic, evil\]|
|[Yithian](ref/monster/yithian)|Quartz geode|

###### ^1^ {#footnote-l}

No alignment-based descriptors were provided, but a Leng hound is chaotic evil and your GM may
determine the spell gains the chaotic and evil descriptors.
