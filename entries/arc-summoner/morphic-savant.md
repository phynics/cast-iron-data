+++
id = "ref/arc-summoner/morphic-savant"
kind = "archetype"
title = "Morphic Savant"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Morphic%20Savant"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "morphic_savant", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "16"

[fields]
kind = "archetype"
alters = ["Eidolon", "Summon monster", "Spells known"]
+++

A morphic savant is an agent of change who draws power from the Abyss, Elysium, or the Maelstrom to
fulfill whatever goals strike his fancy. Chaotic evil and chaotic neutral morphic savants often
train with [Blackfire Adepts](ref/pclass/blackfire-adept) in the hopes of learning greater powers of
chaotic unmaking, and chaotic good morphic savants are most common as agents of the
[Bellflower Network](ref/rule/aff-antislavery).

**Prerequisites:** Chaotic alignment

**Eidolon of Chaos**

**Ability:** A morphic savant's eidolon must be of a chaotic alignment. The morphic savant's eidolon
has three base forms: biped, quadruped, and serpentine. Each form has the same feats and skills, but
has its own set of evolutions. When the summoner meditates and regains his spell slots for the day,
he can select any of the three base forms of his eidolon. The eidolon has 1 fewer evolution point
than normal for an eidolon of the morphic savant's summoner level, and has 1 fewer skill point per
Hit Die.

**Alters:** Eidolon

**Morphic Monsters**

**Action:** Info

**Alters:** Summon monster

**At 2nd Level:** The morphic savant can grant one 1-point evolution to all the creatures he summons
with his _[summon monster](ref/spell/summon-monster)_
[spell-like ability](ref/umr/spell-like-abilities). He can't grant an evolution that duplicates the
function of, or has the same name as, any ability the summoned creatures already possess (for
example, he can't grant a creature with a bite attack another bite attack), nor can he add an
evolution that causes the summoned monsters to have more attacks than his eidolon's maximum number
of attacks. The creatures do not have to be of the correct subtype to gain an evolution, but do have
to meet any other prerequisites.

**Gained:** At 1st Level

Since a morphic savant's power is drawn from planar energies aligned with chaos, all the creatures
he summons must be of a chaotic alignment. If a creature would normally be celestial or fiendish, it
is instead an [entropic creature](ref/template/entropic).

This also causes the morphic savant's summoning power to be less reliable than a standard
summoner's. Each time he uses his _[summon monster](ref/spell/summon-monster)_
[spell-like ability](ref/umr/spell-like-abilities) to summon multiple creatures, there is a 50%
chance he summons one more monster than normal for the _[summon monster](ref/spell/summon-monster)_
spell he uses, in which case the creatures remain for only 1 round per level (instead of 1 minute
per level).

**Chaos Magic**

**Alters:** Spells known

**Info:** A morphic savant gains the following bonus spells known at the listed spell level. The
morphic savant gains one fewer spell known per spell level for spell levels 1-6.

**Spells:** Protection from law

**Spells:** Shard of chaos

**Spells:** Magic circle against law

**Spells:** Chaos hammer

**Spells:** Dispel law

**Spells:** Word of chaos
