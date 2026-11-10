+++
id = "ref/arc-spiritualist/scourge"
kind = "archetype"
title = "Scourge"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Scourge"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scourge", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "22"

[fields]
kind = "archetype"
replaces = ["Spiritual interference", "Devotion", "Calm spirit", "Greater spiritual interference"]
replaces_features = ["spiritual-interference", "calm-spirit", "greater-spiritual-interference"]
+++

Scourges are students of pain and have a rare connection to tormented and wracked spirits. Most are
worshipers of [Zon-Kuthon](ref/faith/zon-kuthon) who are more attracted to his mastery of pain than
his lordship over darkness. As a result, scourges are found not only in Nidal, but also in Cheliax,
Geb, and Irrisen. Faithful of the Midnight Lord often claim the spirits bound to scourges are
tortured souls who begged to be given some boon by their deity, and that having their torment extend
into death is a reward, rather than a punishment. Scourges seek to share their phantoms' miseries
with all around them, using the spirit's pain as a weapon. A scourge's phantom is a broken and
wretched creature, and the torments it suffered in life are reflected in its ghostly or ectoplasmic
appearance as wounds, scars, grotesque malformations, and tattered garments.

**Spell Scourge (Su)**

**Ability:** When a scourge's phantom damages a creature, it causes severe pain, requiring that
creature to succeed at a [concentration](ref/rule/concentration) check (DC = 20 + spell level) to
use spells, [spell-like abilities](ref/umr/spell-like-abilities), and other abilities that require
concentration for 1 round.

**Gained:** At 4th Level

**Passive:** The phantom gains a +2 bonus on attack and damage rolls when making attacks of
opportunity. Any creature threatened by the scourge's phantom takes a -2 penalty on concentration
checks.

**Replaces:** Spiritual interference

**Endure Torment (Ex)**

**Gained:** At 6th Level

**Passive:** A scourge's phantom gains immunity to pain effects and gains a +4 bonus on saving
throws against effects that could cause it to become [staggered](ref/misc/staggered) or
[stunned](ref/misc/stunned).

**Replaces:** Devotion

**Inflict Pain (Sp)**

**Ability:** A scourge can use [inflict pain](ref/spell/inflict-pain) as a
[spell-like ability](ref/umr/spell-like-abilities). If her phantom is fully manifested, it can also
use this ability, though doing so takes the phantom a **full-round action**, and it still counts
against the scourge's daily uses of this ability.

**Gained:** At 7th Level

**Replaces:** Calm spirit

**Usage:** 1 time/day + 1 per 4 spiritualist levels beyond 7th

**Ectoplasmic Swarm (Su)**

**Gained:** At 12th Level

**Replaces:** Greater spiritual interference

**Special:** In this form, the phantom is too diffuse to use
_[inflict pain](ref/spell/inflict-pain)_ or any of its abilities from emotional focus (even passive
abilities).

**Standard:** A scourge with a phantom manifested in ectoplasmic form can command it to break apart
in a gruesome display of gore and agony, transforming it into a swarm of Diminutive ectoplasmic
organs and viscera. The phantom gains the [swarm](ref/subtype/swarm) subtype, dealing its unmodified
slam damage die as damage for its swarm attack. Its distraction DC is equal to 10 + 1/2 the
phantom's Hit Dice + its Constitution modifier.
