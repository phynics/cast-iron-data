+++
id = "ref/arc-bloodrager/ancestral-harbinger"
kind = "archetype"
title = "Ancestral Harbinger"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Ancestral%20Harbinger"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ancestral_harbinger", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit-guardian", level = 2 },
  { anchor = "spirit-servants", level = 5 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["spirit-guardian"] },
  { replaces = "bloodline feats gained at 6th and 18th levels", feature = "bloodline", levels = [6, 18], power = "bloodline feat", by = ["spirit-guardian"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["spirit-servants"] },
  { replaces = "the bloodline feat gained at 12th level", feature = "bloodline", levels = [12], power = "bloodline feat", by = ["spirit-servants"] },
]
+++

While all bloodragers tap into their bloodlines to fuel the arcane energies they use in battle, some
have the ability to call directly to the spirits of their ancestors to aid them, summoning spirits
to fight for them or inspire their allies. Ancestral harbingers are particularly common among
Shoanti bloodragers and among Bonuwat tribes living along the coast of western Garund.

## Spirit Guardian (Sp) {#spirit-guardian}

At 2nd level, an ancestral harbinger can call upon her ancestors to aid her in combat, summoning a
weapon of force that functions as per _[spiritual weapon](ref/spell/spiritual-weapon)_. At 6th
level, her ancestral spirit can take the form of a savage creature, functioning as per
_[summon nature's ally II](ref/spell/summon-natures-ally-2) (_this can't be used to summon multiple
creatures from the _[summon nature's ally I](ref/spell/summon-natures-ally-1)_ list). At 12th level,
her ancestor can manifest physically as a ghostly figure, functioning as per
_[spiritual ally](ref/spell/spiritual-ally)_. At 18th level, her ancestral spirit can manifest
either as a single powerful creature or as multiple lesser ancestors, functioning as per
_[summon nature's ally VI](ref/spell/summon-natures-ally-6)_. The harbinger chooses which spell this
ability functions as at the time of casting, and can use this ability while in a bloodrage. The
ancestral harbinger can use this ability once per day, plus an additional time per day for every 4
bloodrager levels she possesses beyond 2nd.

This ability replaces uncanny dodge and the bloodline feats gained at 6th and 18th levels.

## Spirit Servants {#spirit-servants}

At 5th level, an ancestral harbinger adds _summon monster I_ to her class spell list and gains it as
a bonus spell known. She also gains _summon monster II_ at 8th level, _summon monster III_ at 11th
level, and _summon monster IV_ at 14th level. These spells can be used only to summon types of
monsters with strong ties to the ancestral harbinger's family history, ranging from clan totems to
monsters of the same type as those famously killed by her forebears. For each of these spells, the
ancestral harbinger selects a number of monsters she can summon equal to her Charisma bonus (minimum
1) to represent these spirits. These monsters are selected from the options on the
_[summon monster](ref/spell/summon-monster)_ creature list or the expanded summoning list (see page
28) that are appropriate for the spell level. At 7th level and every 2 bloodrager levels thereafter,
the ancestral harbinger can swap one selected monster from one of these spells for a new monster
from the same level's summoning lists.

The ancestral harbinger has a mystic tie to the spirit servants summoned with this ability. When the
ancestral harbinger is in a bloodrage, all of her spirit servants gain a +2 morale bonus to AC and
on attack rolls, damage rolls, and saving throws. The spirit servants also gain 2
[temporary hit points](ref/rule/temporary-hit-points) per Hit Die. At 11th level, the morale bonus
increases to +3 and the number of temporary hit points per Hit Die increases to 3. At 20th level,
the morale bonus increases to +4 and the number of temporary hit points per Hit Die increases to 4.
The morale bonus and temporary hit points last until the bloodrage ends. This ability replaces
improved uncanny dodge and the bloodline feat gained at 12th level.
