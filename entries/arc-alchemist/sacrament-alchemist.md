+++
id = "ref/arc-alchemist/sacrament-alchemist"
kind = "archetype"
title = "Sacrament Alchemist"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacrament_alchemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Mutagen", "Swift alchemy"]
+++

**Sources:** Healer's Handbook pg 11\
Sacrament alchemists serve in a great variety of priestly roles for their deities. A sacrament
alchemist is often invaluable even to like-minded allies who are not adherents of the alchemist's
religion but who nonetheless rely on his divine abilities.

**Prerequisites:** Like a cleric, a sacrament alchemist must worship a deity, and must be within one
step of his deity's alignment.

**Sacramental Cognatogen (Su)**

**Ability:** Instead of providing physical benefits, the sacramental cognatogen grants the sacrament
alchemist access to the domain powers of one domain or subdomain belonging to his deity as if he
were a [cleric](ref/class/cleric) of his alchemist level. The sacrament alchemist must choose the
domain or subdomain when he brews the sacramental cognatogen. A sacrament alchemist can select an
alignment domain only if his alignment matches that domain. He treats his alchemist level as his
cleric level for purposes of using these domain powers, and treats his Intelligence modifier as his
Wisdom modifier for purposes of variable effects. The effects of the sacramental cognatogen last for
10 minutes per alchemist level.

**Info:** A sacrament alchemist can anoint himself as his deity's servant using his own special
version of a mutagen called a sacramental cognatogen. This is brewed, imbibed, maintained, and can
nauseate non-alchemists in the same way as a mutagen. While a sacramental cognatogen is in effect,
the sacrament alchemist takes a -2 penalty to Dexterity.

**Replaces:** Mutagen

**Special:** A sacrament alchemist doesn't gain the bonus spells listed for each domain, nor does he
gain any bonus spell slots. Levels of classes that normally provide access to domains stack with the
sacrament alchemist's alchemist level for purposes of determining domain powers and abilities, but
not for purposes of determining bonus spells. Discoveries, feats, and effects that interact with the
mutagen class feature do not affect sacramental cognatogen. A sacrament alchemist cannot take the
_cognatogen_ or _mutagen_ discoveries.

**Divinely Inspired Alchemy (Su)**

**Ability:** Once per day while preparing extracts, for a period of 24 hours, a sacrament alchemist
can gain an alchemist discovery for which he qualifies. He treats his alchemist level as 2 lower for
the purpose of this discovery.

**Flavor:** A sacrament alchemist's faith inspires him with ideas for novel alchemical achievements,
although the mental strain means that he can't reliably repeat them.

**Gained:** At 3rd Level

**Replaces:** Swift alchemy

**Discoveries:** The following discoveries complement the sacrament alchemist archetype:
[combine extracts](ref/discovery/combine-extracts), [dilution](ref/discovery/dilution),
[infusion](ref/discovery/infusion), and [ranged baptism](ref/discovery/ranged-baptism).
