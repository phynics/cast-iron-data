+++
id = "ref/arc-slayer/butterfly-blade"
kind = "archetype"
title = "Butterfly Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Butterfly%20Blade"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "butterfly_blade", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-stalker", level = 1 },
  { anchor = "butterfly-s-kiss" },
  { anchor = "innocent-butterfly", level = 7 },
  { anchor = "deadly-butterfly", level = 19 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["studied-stalker"] },
  { replaces = "Sneak attack", feature = "sneak-attack", by = ["butterfly-s-kiss"] },
  { replaces = "Stalker", feature = "stalker", by = ["innocent-butterfly"] },
  { replaces = "swift tracker", feature = "swift-tracker", by = ["innocent-butterfly"] },
  { replaces = "quarry", feature = "quarry", by = ["innocent-butterfly"] },
  { replaces = "Improved quarry", feature = "improved-quarry", by = ["deadly-butterfly"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-stalker"] },
  { alters = "Slayer talents", feature = "slayer-talents" },
]
+++

Followers of a tradition dating back to the ancient empire of Yixing, the yellow-robed agents known
as butterfly blades now operate primarily in Goka, where many serve the city's politically savvy
ruler. Butterfly blades work in the shadows, eliminating threats with their namesake weapons and
intimidating troublesome nobles.

## Studied Stalker (Ex) {#studied-stalker}

A butterfly blade gains the stalker class feature at 1st level, rather than at 7th level. The
butterfly blade doesn't add his studied target bonus on Knowledge or Survival checks.

This ability alters studied target and replaces track.

## Bonus Feats {#bonus-feats}

Whenever a butterfly blade would gain a slayer talent, he can instead select a feat from the
following list: [Cutting Humiliation](ref/feat/cutting-humiliation), [Enforcer](ref/feat/enforcer),
[Intimidating Prowess](ref/feat/intimidating-prowess),
[Nerve-Racking Negotiator](ref/feat/nerve-racking-negotiator), or
[Threatening Negotiator](ref/feat/threatening-negotiator). The butterfly blade does not need to meet
the feat's prerequisites.

This alters slayer talents.

## Butterfly's Kiss (Ex) {#butterfly-s-kiss}

Butterfly blades train to inflict painful cuts rather than lethal ones. A butterfly blade can deal
nonlethal damage with [butterfly swords](ref/eq-weapon/butterfly-sword) without taking a penalty on
attack rolls. At 3rd level, a butterfly blade gets a +1 bonus on attack rolls with butterfly swords,
and the damage die of any butterfly sword he wields increases
[by one step](ref/misc/damage-die-adjustments); at 9th level and again at 15th level, the attack
bonus increases by 1 and the damage die increases by an additional step.

At 6th level, the butterfly blade gains the knockout class feature (_Pathfinder RPG Advanced Class
Guide_ 24), as per a [brawler](ref/class/brawler) of his class level - 2.

This ability replaces sneak attack.

## Innocent Butterfly (Sp) {#innocent-butterfly}

At 7th level, a butterfly blade can use
_[aura of the unremarkable](ref/spell/aura-of-the-unremarkable)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities). At 11th level, he can use it twice per day, and
at 14th level, it becomes a constant [spell-like ability](ref/umr/spell-like-abilities) that he can
activate or deactivate as a free action. The ability's caster level is equal to his slayer class
level, and the DC is equal to 10 + the number of ranks the butterfly blade has in either Bluff or
Intimidate, whichever is higher.

This ability replaces stalker, swift tracker, and quarry.

## Deadly Butterfly (Ex) {#deadly-butterfly}

At 19th level, a butterfly blade becomes a bloody whirlwind in combat. When he strikes a foe with a
butterfly sword, he automatically confirms critical threats. In addition, any butterfly sword he
wields is treated as if it has the _[speed](ref/magic-enh/speed)_ weapon special ability. If the
weapon already has the _speed_ weapon special ability, this doesn't stack.

This ability replaces improved quarry.
