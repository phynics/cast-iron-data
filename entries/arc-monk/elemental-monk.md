+++
id = "ref/arc-monk/elemental-monk"
kind = "archetype"
title = "Elemental Monk"
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
replaces = ["Alignment requirement", "All bonus feats", "stunning fist", "Evasion", "purity of body", "diamond body"]
alters = ["Ki pool"]
+++

Elemental monks draw inspiration from genies to create their fighting style. Their adaptability and
versatility make them capable of serving as emissaries of elemental balance.

**Alignment**

**Info:** An elemental monk must be true neutral.

**Replaces:** Alignment requirement

**Elemental Strike (Ex)**

**Ability:** An elemental monk gains [Elemental Fist](ref/feat/elemental-fist) as a bonus feat, even
if she doesn't meet the prerequisites. She does not have to select an element; instead, each time
she hits with an Elemental Fist attack, she can choose acid, cold, electricity, or fire for the type
of the additional damage granted by that feat.

**Replaces:** All bonus feats, stunning fist

**Genie Style (Ex, Sp)**

**At 10th Level:** While the elemental monk is using a genie style feat, she also gains the benefits
of a feat from the following list, as appropriate for that style's feat path:
[Djinni Spin](ref/feat/djinni-spin), [Efreeti Touch](ref/feat/efreeti-touch),
[Janni Rush](ref/feat/janni-rush), [Marid Coldsnap](ref/feat/marid-coldsnap), and
[Shaitan Earthblast](ref/feat/shaitan-earthblast).

**At 18th Level:** When the elemental monk gains the benefits of Djinni Spirit, Efreeti Stance,
Marid Spirit, or Shaitan Skin, her elemental resistance from that feat instead becomes immunity to
that element, as long as she is not denied her Dexterity bonus to AC. While she is using Janni
Style, she gains the effects of [enlarge person](ref/spell/enlarge-person) or
[reduce person](ref/spell/reduce-person) (her choice), even if she is not humanoid. This is a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to the elemental monk's
level.

**At 2nd Level:** As a **swift action** an elemental monk can gain the benefits of one of the
following style feats, based on one of the five types of genies. When she does so, she automatically
enters that feat's stance: [Djinni Style](ref/feat/djinni-style),
[Efreeti Style](ref/feat/efreeti-style), [Janni Style](ref/feat/janni-style),
[Marid Style](ref/feat/marid-style), or [Shaitan Style](ref/feat/shaitan-style).

**At 6th Level:** While the elemental monk is using a genie style feat, she also gains the benefits
of a feat from the following list, as appropriate for that style's feat path:
[Djinni Spirit](ref/feat/djinni-spirit), [Efreeti Stance](ref/feat/efreeti-stance),
[Janni Tempest](ref/feat/janni-tempest), [Marid Spirit](ref/feat/marid-spirit), and
[Shaitan Skin](ref/feat/shaitan-skin).

**Replaces:** Evasion, purity of body, diamond body

**Elemental Precision (Ex)**

**Ability:** Instead of treating her unarmed strikes as lawful for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction), an elemental monk overcomes all damage reduction of
creatures with the air, earth, fire, or water subtypes except DR/- and DR/epic.

**Alters:** Ki pool

**Gained:** At 10th Level

**Planar Guide (Sp)**

**Gained:** At 14th Level

**Standard:** An elemental monk can spend 1 ki point to transport herself and up to seven additional
willing creatures, as per the [plane shift](ref/spell/plane-shift) spell, to one of the four
Elemental Planes. Each additional creature increases the cost by 1 ki point.
