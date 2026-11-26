+++
id = "ref/arc-cleric/idealist"
kind = "archetype"
title = "Idealist"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Idealist"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "idealist", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "planar-adventures"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-bond", level = 1 },
  { anchor = "invoke-realm" },
]
trades = [
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["planar-bond"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["invoke-realm"] },
]
+++

In the Great Beyond, belief is power. Idealist clerics are personifications of this power, each
embracing the purest ideal of his deity's realm. In doing so an idealist becomes a powerful conduit,
gaining the power to channel the essence of his deity's plane.

## Planar Bond (Su) {#planar-bond}

At 1st level, an idealist must choose one plane as his planar bond. This plane must be his deity's
home plane. An idealist can spontaneously cast the 1st-, 4th-, and 7th-level spells listed below for
his chosen plane (provided he can cast spells of that level), in addition to cure or inflict spells.

_Abaddon: Protection from good_, _unholy blight_, and _blasphemy_.

_Abyss: Doom_, _unholy blight_, and _blasphemy_.

_Astral: Summon monster I_, _dismissal_, and _lesser create demiplane_.

_Axis: Protection from chaos_, _order's wrath_, and _dictum_.

_Boneyard: Deathwatch_, _death ward_, and _arbitrament_ (page 39).

_Elysium: Remove fear_, _freedom of movement_, and _word of chaos_.

_Ethereal: Obscuring mist_, _sending_, and _ethereal jaunt_.

_First World: Entropic shield_, _giant vermin_, and _regenerate_.

_Heaven: Sanctuary_, _discern lies_, and _holy word_.

_Hell: Command_, _tongues_, and _dictum_.

_Maelstrom: Protection from law_, _chaos hammer_, and _word of chaos_.

_Nirvana: Protection from evil_, _holy smite_, and _holy word_.

_Plane of Air: Alter winds_, _air walk_, and _control weather_.

_Plane of Earth: Magic stone_, _stoneskin_, and _statue_.

_Plane of Fire: Produce flame_†, _wall of fire_, and _delayed blast fireball_.

_Plane of Water: Hydraulic push_, _control water_, and _vortex_.

_Shadow Plane: Cause fear_, _shadow conjuration_†, and _destruction_.

_Other (Including Positive and Negative Energy Planes, Material Plane, or Demiplane):_ Work with
your GM to select three spells that match the themes of the deity you worship.

†This spell is not added to your cleric list—you can cast it spontaneously only using planar bond.

This alters spontaneous casting.

## Invoke Realm (Su) {#invoke-realm}

When an idealist channels energy, she channels raw essence rather than positive or negative energy,
superimposing a portion of her deity's planar realm over her location. This effect extends out to a
radius of 10 feet, plus 5 feet for every 2 cleric levels she has beyond 1st, to a maximum radius of
55 feet at 19th level. This effect lasts for 1 round plus 1 round per point of the idealist's
Charisma bonus. While this effect is active, the idealist gains a +1 bonus on Diplomacy checks
against creatures who worship her deity and a +1 bonus on Intimidate checks against creatures who do
not. This bonus increases by 1 at 5th level and every 5 levels thereafter.

This channeled energy imposes itself over the current terrain, changing its visual appearance to
more thematically suit the energy's associated planar realm, but cannot hide obvious hazards or
otherwise allow for a creature to hide any more effectively than the normal terrain would. This is
an illusion (glamer) effect with a caster level equal to the idealist's level.

Within the radius of the idealist's channeling, all alignment and magic
[planar traits](ref/rule/planar-traits) are suppressed and replaced with the traits of the plane
that matches the idealist's planar bond. This includes alignment, gravity, and magic traits (see
pages 58–63 for information on planar traits.) In the case of the Astral Plane, since the time trait
remains unaltered, your spellcasting only feels fast—you gain a +4 bonus on all
[concentration](ref/rule/concentration) checks rather than the ability to apply Quickened Spell
effects.

This ability is considered channel energy for purposes of feats that grant additional uses of
channel energy or allow the cleric to exclude creatures from channel energy's effects.

This alters channel energy.
