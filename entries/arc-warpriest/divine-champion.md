+++
id = "ref/arc-warpriest/divine-champion"
kind = "archetype"
title = "Divine Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Divine%20Champion"
source_ids = ["divine-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_champion", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "divine-anthology"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "devotion" },
  { anchor = "obedient-champion", level = 3 },
  { anchor = "know-the-infidel", level = 6 },
  { anchor = "fervent-boon", level = 9 },
]
trades = [
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["obedient-champion"] },
  { replaces = "Bonus feats gained at 6th, 12th, and 18th levels", feature = "bonus-feats", levels = [6, 12, 18], by = ["know-the-infidel"] },
  { replaces = "Bonus feat gained at 9th level", feature = "bonus-feats", levels = [9], by = ["fervent-boon"] },
]
+++

Divine champions are unswervingly devoted to their causes, and specialize in bringing battle to the
enemies of their faiths. They are similar to [divine paragons](ref/arc-cleric/divine-paragon) in
many ways, but tend to focus more on their deity's combat prowess rather than seeking to become a
physical manifestation of the deity's will.

## Obedient Archetypes {#obedient-archetypes}

The following archetypes are often taken by those who have studied from _Meditations and
Revelations_ and taken its message to heart. Both archetypes require the character to perform
regular obediences to her chosen deity, just as one must to gain the benefits of the Divine
Obedience feat. These obediences are identical to those required by Divine Obedience—for religions
that do not have official obediences printed, you can either work with your GM to create appropriate
obediences or simply assume that the obedience in question is something relatively minor that your
character can take care of during your spell preparation ritual. Failure to follow this daily
obedience causes you to lose all of the abilities granted by your chosen archetype. In this event,
you do not regain the abilities you altered or replaced via the archetype—you simply lose access to
that element of power granted until you next perform the obedience.

## Devotion {#devotion}

A divine champion's power comes from his close connection to his deity. He must worship a deity, and
must maintain the same alignment as that deity.

## Obedient Champion {#obedient-champion}

At 3rd level, the divine champion gains [Deific Obedience](ref/feat/deific-obedience) as a bonus
feat, even if he doesn't meet the feat's prerequisites. When a divine champion gains boons from this
feat, he gains the appropriate sentinel boon offered by his deity, rather than gaining the exalted
boon.

This replaces the bonus feat gained at 3rd level.

## Know the Infidel (Ex) {#know-the-infidel}

At 6th level, the divine champion becomes an expert at combating enemies of his faith. He must
choose a deity whose alignment is opposed to his own deity's alignment in at least one way (good
versus evil or law versus chaos); preferably, he should choose a deity whose alignment diametrically
opposes that of his own deity. If the divine champion worships a deity whose alignment is neutral,
he must instead select a deity whose alignment is chaotic evil, chaotic good, lawful evil, or lawful
good. The choice of this enemy deity is subject to GM approval. At the GM's discretion, the divine
champion may be allowed to choose a philosophy or religious organization that's not affiliated with
a deity, such as the [Green Faith](ref/faith/green-faith), the Pure Legion, or the
[Whispering Way](ref/rule/f-gravepath), but only if that philosophy or religious organization is an
enemy of the divine champion's deity. The divine champion gains a +2 bonus on Bluff, Intimidate,
Knowledge, Perception, and Sense Motive checks against followers of the enemy faith, as well as a +2
bonus on weapon attack and damage rolls made against them. Additionally, he can attempt Knowledge
skill checks relating to the deity and its church untrained, even if the DC is higher than 10.

Every 6 warpriest levels thereafter (12th and 18th level), the divine champion can select an
additional deity to oppose. In addition, at each such interval, the bonus against the followers of
any one deity he selected previously (including the one just selected, if so desired) increases by
+2.

This replaces the bonus feats gained at 6th, 12th, and 18th levels.

## Fervent Boon (Sp) {#fervent-boon}

Beginning at 9th level, a divine champion can call upon his deity for minor boons. By expending one
or more uses of his fervor ability, he can cast one of the
[spell-like abilities](ref/umr/spell-like-abilities) included in his deity's first sentinel boon. By
expending one use of fervor, he can cast the [spell-like ability](ref/umr/spell-like-abilities) that
the boon normally grants three uses of per day; by expending two uses of fervor he can cast the
spell-like ability that the boon normally grants twice per day; and by expending three uses of
fervor, he can cast the spell-like ability that the boon normally grants once per day. These uses
don't count against any uses granted by the boon.

This replaces the bonus feat gained at 9th level.
