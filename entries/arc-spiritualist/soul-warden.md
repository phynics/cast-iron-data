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
replaces = ["Phantom", "etheric tether", "shared consciousness", "spiritual interference", "fused consciousness", "greater spiritual interference", "Bonded manifestation", "Bonded manifestation increases", "dual bond", "Empowered consciousness"]
alters = ["Bonded senses", "phantom recall"]
replaces_features = ["phantom", "etheric-tether", "shared-consciousness", "spiritual-interference", "fused-consciousness", "greater-spiritual-interference", "bonded-manifestation", "dual-bond", "empowered-consciousness"]
alters_features = ["bonded-senses", "phantom-recall"]
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

**Nosoi Scribe**

**Ability:** A soul warden gains a fledgling nosoi [familiar](ref/ability/familiars). Treat this as
a [raven familiar](ref/monster/familiar-raven) until the soul warden reaches 4th level, at which
point it is treated as a [nosoi](ref/monster/psychopomp-nosoi) (as though the soul warden had taken
the [Improved Familiar](ref/feat/improved-familiar) feat).

**At 10th Level:** The nosoi scribe gains the ability to use its _touch the spirit world_ ability
three times per day, instead of once per day.

**At 12th Level:** It also gains the Repose domain's _ward against death_ ability.

**Info:** The familiar uses the soul warden's spiritualist level as its Hit Dice for the purpose of
determining the effects and duration of its _haunting melody_ ability and all other effects related
to its HD.

**Gained:** At 1st Level

**Replaces:** Phantom, etheric tether, shared consciousness, spiritual interference, fused
consciousness, greater spiritual interference

**Ward Against Death (Su)**

**Flavor:** Text from the Respose domain ability.

**Standard:** You can emit a 30-foot aura that wards against death. Living creatures in this area
are immune to all death effects, energy drain, and effects that cause
[negative levels](ref/rule/energy-drain-and-negative-levels). This ward does not remove negative
levels that a creature has already gained, but the negative levels have no effect while the creature
is inside the warded area.

**Usage:** 1 time/day per cleric level

**Psychopomp's Bond (Su)**

**Alters:** Bonded senses, phantom recall

**Flavor:** A soul warden's bond with her nosoi scribe is stronger than usual for a master and
familiar.

**At 2nd Level:** She can use _bonded senses_ with her nosoi scribe.

**At 6th Level:** She can use _phantom recall_ to recall her nosoi scribe to her side.

**Warding Vessel (Su)**

**Ability:** A soul warden can allow a spirit, soul, or incorporeal creature to hide inside her.
While within the soul warden, the warded creature can communicate with the soul warden, and it can
be targeted only by effects that could target a creature possessing another creature's body. The
warded creature has no other influence over the soul warden or her body.

**Gained:** At 3rd Level

**Replaces:** Bonded manifestation

**Special:** If the soul warden is reduced below 0 hit points, the warded creature is expelled.

**Phantom Elegy (Su)**

**At 17th Level:** The nosoi scribe can blend any two of the phantom aura abilities into a single
_phantom elegy,_ although it uses 3 rounds of its _haunting melody_ for each round it does so.

**At 8th Level:** A soul warden's nosoi scribe learns to sing elegies that build on the soul
warden's conduit to her former phantom. This allows it to create an effect identical to the
7th-level _aura_ ability of an [anger](ref/emotionalfocus/anger),
[dedication](ref/emotionalfocus/dedication), [despair](ref/emotionalfocus/despair),
[fear](ref/emotionalfocus/fear), [hatred](ref/emotionalfocus/hatred),
[jealousy](ref/emotionalfocus/jealousy), or [zeal](ref/emotionalfocus/zeal) phantom, except that the
_phantom elegy_ is also a sonic effect and continues only as long as the nosoi scribe sings. Each
round of _phantom elegy_ uses 1 round of the nosoi scribe's _haunting melody._

**Replaces:** Bonded manifestation increases, dual bond

**Algea Call (Su)**

**Gained:** At 20th Level

**Replaces:** Empowered consciousness

**Standard:** Once per hour, a soul warden's nosoi scribe can summon countless other nosoi, which
flock together to form an [algea](ref/monster/psychopomp-algea). This transformation lasts for 1
minute, after which the nosoi scribe returns unharmed, unless the algea is brought to 0 hit points
or killed, in which case the nosoi scribe returns unconscious at 0 hit points. This is a summoning
effect.
