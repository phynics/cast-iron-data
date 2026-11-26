+++
id = "ref/arc-monk/elemental-monk"
kind = "archetype"
title = "Elemental Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Elemental%20Monk"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "disciples-doctrine"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-strike", level = 1 },
  { anchor = "genie-style", level = 2 },
  { anchor = "elemental-precision", level = 10 },
  { anchor = "planar-guide", level = 14 },
]
trades = [
  { replaces = "Alignment requirement" },
  { replaces = "All of the monk's bonus feats", feature = "bonus-feat", by = ["elemental-strike"] },
  { replaces = "stunning fist", feature = "stunning-fist", by = ["elemental-strike"] },
  { replaces = "Evasion", feature = "evasion", by = ["genie-style"] },
  { replaces = "purity of body", feature = "purity-of-body", by = ["genie-style"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["genie-style"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["elemental-precision"] },
]
+++

Elemental monks draw inspiration from genies to create their fighting style. Their adaptability and
versatility make them capable of serving as emissaries of elemental balance.

## Alignment {#alignment}

An elemental monk must be true neutral.

This replaces the monk's alignment requirement.

## Elemental Strike (Ex) {#elemental-strike}

An elemental monk gains [Elemental Fist](ref/feat/elemental-fist) as a bonus feat, even if she
doesn't meet the prerequisites. She does not have to select an element; instead, each time she hits
with an Elemental Fist attack, she can choose acid, cold, electricity, or fire for the type of the
additional damage granted by that feat.

This replaces all of the monk's bonus feats and stunning fist.

## Genie Style (Ex, Sp) {#genie-style}

At 2nd level, as a swift action an elemental monk can gain the benefits of one of the following
style feats, based on one of the five types of genies. When she does so, she automatically enters
that feat's stance: [Djinni Style](ref/feat/djinni-style), [Efreeti Style](ref/feat/efreeti-style),
[Janni Style](ref/feat/janni-style), [Marid Style](ref/feat/marid-style), or
[Shaitan Style](ref/feat/shaitan-style). These feats, as well as those mentioned below, appear in
Chapter 2 of _Pathfinder RPG Ultimate Combat_, and rules for style feats are on page 78 of that
book.

At 6th level, while the elemental monk is using a genie style feat, she also gains the benefits of a
feat from the following list, as appropriate for that style's feat path:
[Djinni Spirit](ref/feat/djinni-spirit), [Efreeti Stance](ref/feat/efreeti-stance),
[Janni Tempest](ref/feat/janni-tempest), [Marid Spirit](ref/feat/marid-spirit), and
[Shaitan Skin](ref/feat/shaitan-skin).

At 10th level, while the elemental monk is using a genie style feat, she also gains the benefits of
a feat from the following list, as appropriate for that style's feat path:
[Djinni Spin](ref/feat/djinni-spin), [Efreeti Touch](ref/feat/efreeti-touch),
[Janni Rush](ref/feat/janni-rush), [Marid Coldsnap](ref/feat/marid-coldsnap), and
[Shaitan Earthblast](ref/feat/shaitan-earthblast).

At 18th level, when the elemental monk gains the benefits of Djinni Spirit, Efreeti Stance, Marid
Spirit, or Shaitan Skin, her elemental resistance from that feat instead becomes immunity to that
element, as long as she is not denied her Dexterity bonus to AC. While she is using Janni Style, she
gains the effects of _[enlarge person](ref/spell/enlarge-person)_ or
_[reduce person](ref/spell/reduce-person)_ (her choice), even if she is not humanoid. This is a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to the elemental monk's
level.

This replaces evasion, purity of body, and diamond body. (For an unchained monk built using
_Pathfinder RPG Pathfinder Unchained_, this replaces the 10th-level ki power instead of diamond
body.)

## Elemental Precision (Ex) {#elemental-precision}

At 10th level, instead of treating her unarmed strikes as lawful for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction), an elemental monk overcomes all damage reduction of
creatures with the air, earth, fire, or water subtypes except DR/— and DR/epic.

This alters the monk's ki pool.

## Planar Guide (Sp) {#planar-guide}

At 14th level as a standard action, an elemental monk can spend 1 ki point to transport herself and
up to seven additional willing creatures, as per the _[plane shift](ref/spell/plane-shift)_ spell,
to one of the four Elemental Planes. Each additional creature increases the cost by 1 ki point.
