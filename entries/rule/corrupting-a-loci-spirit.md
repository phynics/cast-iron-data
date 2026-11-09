+++
id = "ref/rule/corrupting-a-loci-spirit"
kind = "rule"
title = "Corrupting a Loci Spirit"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "corrupting_a_loci_spirit", path = "json/rules_campaign_types08.json" },
]
[[sources]]
publication = "occult-adventures"
page = "227"

[fields]
kind = "none"
+++

Loci spirits can't be damaged conventionally, but are susceptible to corruption if certain actions
occur within their areas. Each loci spirit has a number of hit points equal to twice its CR, which
it uses to resist corruption. Certain particularly vile acts reduce a loci spirit's hit points and
bring it closer to corruption, while certain acts of good can restore hit points and protect the
loci spirit from corruption.

If a loci spirit is reduced to 0 hit points, it becomes corrupted; thereafter, it acts as a
[haunt](ref/rule/haunts) of the same CR and loses any loci spirit permanent effects. Once a loci
spirit has been corrupted, its effects instead manifest as mind-affecting fear effects. These new
effects should have a similar power level to that of the ceremonial effect the loci spirit
previously manifested. A corrupted loci spirit has the aura of an evil outsider for the purposes of
[detect evil](ref/spell/detect-evil) and similar effects. Unlike a haunt, a corrupted loci spirit
can't take the tricked by [hide from undead](ref/spell/hide-from-undead) weakness, but it can take
most other haunt modifiers as long as its CR remains the same. The haunt has the same number of hit
points as the loci spirit originally did; these are separate from its loci spirit hit points, which
remain at 0 until the loci spirit is purified.

Corrupted loci spirits can be neutralized or destroyed in the same fashion as haunts. While a
corrupted loci spirit is inactive because of being neutralized, characters can use effects that
restore a loci spirit's hit points to attempt to purify it (see the table below). For the purpose of
purification, increasing the loci spirit's hit points does not restore the haunt's hit points. If a
character manages to restore the full hit points of the uncorrupted loci spirit, the character has
purged the corruption entirely, and the loci spirit returns to its former benevolence. This could
potentially occur over the course of multiple encounters with the corrupted spirit. Until then, the
haunt continues to reset.

|Act|Effect|
| --- | --- |
|Committing a violent act|Reduces hit points by 1|
|Committing murder|Reduces hit points by 1 for every 3 Hit Dice of the victim (minimum 1 hit point)|
|Casting [animate dead](ref/spell/animate-dead)|Reduces hit points by 1 per undead created|
|Casting [create undead](ref/spell/create-undead) or [create greater undead](ref/spell/create-greater-undead)|Reduces hit points by 1 per level of spell cas|
|Summoning an evil outsider|Reduces hit points by 1 per evil outsider summoned|
|Calling an evil outsider|Reduces hit points by 1 per level of spell cast|
|Casting [desecrate](ref/spell/desecrate)|Reduces hit points by 2|
|Casting [unhallow](ref/spell/unhallow)|Reduces hit points by 4|
|Successfully performing the loci spirit's ceremony|Restores 2 hit points|
|Casting [consecrate](ref/spell/consecrate)|Restores 2 hit points (maximum once per day)|
|Casting [hallow](ref/spell/hallow)|Restores 4 hit points|
