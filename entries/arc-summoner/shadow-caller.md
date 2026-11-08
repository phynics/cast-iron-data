+++
id = "ref/arc-summoner/shadow-caller"
kind = "archetype"
title = "Shadow Caller"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_caller", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]

[fields]
kind = "archetype"
replaces = ["Magical symbol that identifies the summoner and his eidolon"]
alters = ["Eidolon"]
+++

**Sources:** Advanced Race Guide pg 110\
While most summoners can call any manner of creature from across the planes to serve them in combat,
supplementing the skills of their eidolon with a diverse range of creatures, others eschew this
broad utility and instead concentrate upon calling forth entities from the
[Shadow Plane](ref/rule/shadow-plane). A shadow caller has the following class features.

**Prerequisites:** Fetchling

**Gained class skills:** stl

**Lost class skills:** umd

;;;ab\{title="Shadow Summoning (Sp)" icon=magic action=Ability replace=" summon monster
spell-like"\}

When a shadow caller uses his _[summon monster](ref/spell/summon-monster)_ ability or casts the
[summon monster](ref/spell/summon-monster) spell, he typically summons creatures from the Shadow
Plane or creatures closely associated with shadow. When a creature on the
_[summon monster](ref/spell/summon-monster)_ spell list indicates that it is summoned with either
the celestial or the fiendish template based on the alignment of the caster, the creature summoned
by the shadow caller has the [shadow](ref/template/shadow) creature template instead. Furthermore,
the _[summon monster](ref/spell/summon-monster)_ lists are modified in the following ways (these
changes also apply to using a higher-level
_[summon](ref/carried/bestiary/rules/universal-monster-rules/summon)_ spell to summon multiple
creatures from a lower-level list).

_**Summon Monster I**_

**Details:** No changes.

_**Summon Monster II**_

**Details:** A shadow caller cannot summon Small elementals or lemures, but instead can summon
[zoogs](ref/monster/zoog).

_**Summon Monster III**_

**Details:** A shadow caller cannot summon dretches or lantern archons, but can summon
[augur kytons](ref/monster/kyton-augur).

_**Summon Monster IV**_

**Details:** A shadow caller cannot summon Medium elementals, hell hounds, hound archons, or
mephits, but can summon [allips](ref/monster/allip), [gloomwings](ref/monster/gloomwing), and
[shadows](ref/monster/shadow).

_**Summon Monster V**_

**Details:** A shadow caller cannot summon babau, bearded devils, bralani azatas, Large elementals,
salamanders, or xills, but can summon [shadow mastiffs](ref/monster/shadow-mastiff) and
[shae](ref/monster/shae).

_**Summon Monster VI**_

**Details:** A shadow caller cannot summon Huge elementals, erinyes, lillend azatas, or succubi, but
can summon [cloakers](ref/monster/cloaker).

_**Summon Monster VII**_

**Details:** A shadow caller cannot summon bebiliths, bone devils, greater elementals, or vrocks,
but can summon [greater shadows](ref/monster/shadow-greater-shadow).

_**Summon Monster VIII**_

**Details:** A shadow caller can only summon [derghodaemons](ref/monster/daemon-derghodaemon) and
young [umbral dragons](ref/family/dragon-primal-umbral).

_**Summon Monster IX**_

**Details:** A shadow caller can only summon [interlocutor kytons](ref/monster/kyton-interlocutor)
and [nightwings](ref/monster/nightshade-nightwing).

;;;

**Shadow Eidolon**

**Alters:** Eidolon

**Info:** A shadow caller's eidolon is at once a thing of shadow called from the deep of the Shadow
Plane and his own shadow; the two are inseparable. When his eidolon manifests, his shadow lengthens
and finally detaches from him as a creature unto itself. For as long as the shadow caller's eidolon
is manifested, he and the eidolon do not have distinct shadows, regardless of the presence or
absence of light.

**Replaces:** Magical symbol that identifies the summoner and his eidolon
