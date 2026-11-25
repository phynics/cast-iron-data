+++
id = "ref/arc-spiritualist/soul-warden"
kind = "archetype"
title = "Soul Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Soul%20Warden"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_warden", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "planar-adventures"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "nosoi-scribe", level = 1 },
  { anchor = "psychopomp-s-bond" },
  { anchor = "warding-vessel", level = 3 },
  { anchor = "phantom-elegy", level = 8 },
  { anchor = "algea-call", level = 20 },
]
trades = [
  { replaces = "Phantom", feature = "phantom", by = ["nosoi-scribe"] },
  { replaces = "etheric tether", feature = "etheric-tether", by = ["nosoi-scribe"] },
  { replaces = "shared consciousness", feature = "shared-consciousness", by = ["nosoi-scribe"] },
  { replaces = "spiritual interference", feature = "spiritual-interference", by = ["nosoi-scribe"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["nosoi-scribe"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["nosoi-scribe"] },
  { replaces = "Bonded manifestation", feature = "bonded-manifestation", by = ["warding-vessel"] },
  { replaces = "Bonded manifestation increases", by = ["phantom-elegy"] },
  { replaces = "dual bond", feature = "dual-bond", by = ["phantom-elegy"] },
  { replaces = "Empowered consciousness", feature = "empowered-consciousness", by = ["algea-call"] },
  { alters = "Bonded senses", feature = "bonded-senses", by = ["psychopomp-s-bond"] },
  { alters = "phantom recall", feature = "phantom-recall", by = ["psychopomp-s-bond"] },
]
+++

Normally, the bond a spiritualist shares with his phantom persists for the duration of the
spiritualist's life, but in certain rare instances, a spiritualist can guide the phantom hiding
within her on to the afterlife, choosing to release the phantom and abandoning many of the classic
powers her class normally grants her. When this unusual circumstance happens, the spiritualist
retains all the psychic potential from her time serving as a conduit and a vessel, even though she
is no longer accompanied by her phantom. While some who would have otherwise become adventuring
spiritualists take this as an opportunity to instead choose a normal life, others are galvanized to
become wardens of the soulstream, serving [Pharasma](ref/faith/pharasma) and working with
[psychopomps](ref/family/psychopomp) to protect vulnerable souls from those who seek to capture,
corrupt, or devour them. At the GM's discretion, a spiritualist might help her phantom move on
during play, and if the attempt is successful, she can apply this archetype retroactively, making
the appropriate modifications to her class choices as if she had been a soul warden from first
level.

## Nosoi Scribe {#nosoi-scribe}

At 1st level, a soul warden gains a fledgling [nosoi](ref/monster/psychopomp-nosoi)
[familiar](ref/ability/familiars). Treat this as a [raven familiar](ref/monster/familiar-raven)
until the soul warden reaches 4th level, at which point it is treated as a nosoi (as though the soul
warden had taken the [Improved Familiar](ref/feat/improved-familiar) feat). The familiar uses the
soul warden's spiritualist level as its Hit Dice for the purpose of determining the effects and
duration of its haunting melody ability and all other effects related to its HD. At 10th level, the
nosoi scribe gains the ability to use its touch the spirit world ability three times per day,
instead of once per day. At 12th level, it also gains the Repose domain's ward against death
ability.

This replaces phantom, etheric tether, shared consciousness, spiritual interference, fused
consciousness, and greater spiritual interference.

## Psychopomp's Bond (Su) {#psychopomp-s-bond}

A soul warden's bond with her nosoi scribe is stronger than usual for a master and familiar. At 2nd
level, she can use bonded senses with her nosoi scribe, and at 6th level, she can use phantom recall
to recall her nosoi scribe to her side.

This alters bonded senses and phantom recall.

## Warding Vessel (Su) {#warding-vessel}

At 3rd level, a soul warden can allow a spirit, soul, or incorporeal creature to hide inside her.
While within the soul warden, the warded creature can communicate with the soul warden, and it can
be targeted only by effects that could target a creature possessing another creature's body. The
warded creature has no other influence over the soul warden or her body. If the soul warden is
reduced below 0 hit points, the warded creature is expelled.

This replaces bonded manifestation.

## Phantom Elegy (Su) {#phantom-elegy}

At 8th level, a soul warden's nosoi scribe learns to sing elegies that build on the soul warden's
conduit to her former phantom. This allows it to create an effect identical to the 7th-level aura
ability of an [anger](ref/emotionalfocus/anger), [dedication](ref/emotionalfocus/dedication),
[despair](ref/emotionalfocus/despair), [fear](ref/emotionalfocus/fear),
[hatred](ref/emotionalfocus/hatred), [jealousy](ref/emotionalfocus/jealousy), or
[zeal](ref/emotionalfocus/zeal) phantom, except that the phantom elegy is also a sonic effect and
continues only as long as the nosoi scribe sings. Each round of phantom elegy uses 1 round of the
nosoi scribe's haunting melody. At 17th level, the nosoi scribe can blend any two of the phantom
aura abilities into a single phantom elegy, although it uses 3 rounds of its haunting melody for
each round it does so.

This replaces bonded manifestation increases and dual bond.

## Algea Call (Su) {#algea-call}

At 20th level, as a standard action once per hour, a soul warden's nosoi scribe can summon countless
other nosoi, which flock together to form an [algea](ref/monster/psychopomp-algea). This
transformation lasts for 1 minute, after which the nosoi scribe returns unharmed, unless the algea
is brought to 0 hit points or killed, in which case the nosoi scribe returns unconscious at 0 hit
points. This is a summoning effect.

This replaces empowered consciousness.
