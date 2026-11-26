+++
id = "ref/arc-witch/wyrm-witch"
kind = "archetype"
title = "Wyrm Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Wyrm%20Witch"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wyrm_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "draconic-patronage" },
  { anchor = "wyrmwitch-s-hoard", level = 1 },
]
trades = [
  { replaces = "Witch's familiar", feature = "witch-s-familiar", by = ["wyrmwitch-s-hoard"] },
]
+++

Though a dragon derives no power from accumulating precious metals and gems, its desire to acquire
and maintain vast piles of valuables is an important part of its personality. Some witch covens,
particularly those in rich mercantile nations like Druma or Katapesh, have learned to use treasure
to access other draconic powers.

## Draconic Patronage {#draconic-patronage}

A wyrmwitch must select one of the following patrons when he gains this archetype. Only witches with
the wyrmwitch archetype can select these patrons.

### Chromatic {#chromatic}

2nd—_cause fear_, 4th—_hold person_, 6th—_suggestion_, 8th—_aura of doom_, 10th—_dominate person_,
12th—_geas/quest_, 14th—_mass hold person_, 16th—_frightful aspect_, 18th—_overwhelming presence_.

### Esoteric {#esoteric}

2nd—_memory lapse_, 4th—_psychic reading_, 6th—_nondetection_, 8th—_hypercognition_, 10th—_mind
probe_, 12th—_telepathy_, 14th—_insanity_, 16th—_screen_, 18th—_bilocation_.

### Imperial {#imperial}

2nd—_endure elements_, 4th—_gust of wind_, 6th—_hydraulic torrent_, 8th—_obsidian flow_,
10th—_fickle winds_, 12th—_move earth_, 14th—_reverse gravity_, 16th—_wall of lava_, 18th—_world
wave_.

### Metallic {#metallic}

2nd—_protection from evil_, 4th—_weapon of awe_, 6th—_heroism_, 8th—_dispel evil_, 10th—_commune_,
12th—_greater heroism_, 14th—_limited wish_, 16th—_holy aura_, 18th—_miracle_.

### Outer {#outer}

2nd—_deja vu_, 4th—_darkness_, 6th—_blink_, 8th—_black tentacles_, 10th—_mindwipe_, 12th—_shadow
walk_, 14th—_lunar veil_, 16th—_orb of the void_, 18th—_weird_.

### Primal {#primal}

2nd—_burning hands_, 4th—_elemental touch_, 6th—_elemental aura_, 8th—_planar adaptation_,
10th—_elemental body II_, 12th—_chain lightning_, 14th—_vortex_, 16th—_polar ray_, 18th—_fiery
body_.

## Wyrmwitch's Hoard (Ex) {#wyrmwitch-s-hoard}

Unlike traditional witches, a wyrmwitch does not have a familiar. Instead, a wyrmwitch develops a
metaphysical link with a bonded hoard of treasure that serves as a conduit to the wyrmwitch's
patron. A wyrmwitch's hoard must have a value of 50 gp plus 100 gp for every character level he has
beyond 1st. Only nonmagical objects that are not alchemical items, weapons, armor, or useful tools
can be part of a wyrmwitch's hoard. If the hoard falls below this value, the wyrmwitch cannot sleep
on his hoard (see below) or add new spells to it until its value is restored.

A wyrmwitch's spells come from this link with his hoard, and its ability to hold spells functions in
a manner identical to the way a witch's spells are normally granted by a familiar. A wyrmwitch can
add spells to his hoard in a similar fashion to the way conventional witches store spells in their
familiars. A witch's familiar and a wyrmwitch's hoard can exchange spells in the same way two normal
witch familiars do. Also, a witch can add a spell to his hoard from a wizard's spellbook, if the
spellbook is kept in the hoard and the spell is on the witch's class spell list. The wyrmwitch must
sleep on the spellbook in his hoard for a number of days equal to the spell's level, after which he
must succeed at a Spellcraft check (DC = 15 + spell level) to learn the spell. No matter the result,
the spell is erased from the spellbook.

A wyrmwitch must commune with his hoard to ready his body and mind for casting spells. If he does
not spend at least 8 hours resting atop his hoard prior to preparing spells, he must attempt a
[concentration](ref/rule/concentration) check anytime he attempts to cast a spell (DC = 20 + the
spell's level). If the wyrmwitch does prepare spells after properly sleeping on his hoard, he gains
the ability to call on his hoard to cast any one spell it is holding and that he is capable of
casting, even if the spell is not prepared. This spell is treated like any other spell cast by the
wyrmwitch, including when determining casting time, duration, and other effects dependent on the
wyrmwitch's level. This spell cannot be modified by metamagic feats or other abilities.

This ability replaces witch's familiar.
