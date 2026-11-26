+++
id = "ref/arc-kineticist/elysiokineticist"
kind = "archetype"
title = "Elysiokineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Elysiokineticist"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elysiokineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "elysium-s-soul" },
  { anchor = "basic-elysiokinesis" },
  { anchor = "elysian-infusion", level = 1 },
  { anchor = "elysian-aura", level = 2 },
  { anchor = "ghaelelight-blast", level = 15 },
]
trades = [
  { replaces = "Expanded element", feature = "expanded-element", by = ["elysium-s-soul"] },
  { replaces = "Basic phytokinesis utility wild talent granted by the wood element", feature = "elemental-focus", power = "basic utility wild talent", by = ["basic-elysiokinesis"] },
  { replaces = "Infusion gained at 1st level", feature = "infusion", levels = [1], by = ["elysian-infusion"] },
  { replaces = "Flesh of wood defense wild talent granted by the wood element", feature = "elemental-defense", by = ["elysian-aura"] },
  { alters = "Elemental focus", feature = "elemental-focus", by = ["elysium-s-soul"] },
  { alters = "The class skills granted by the wood element", by = ["elysium-s-soul"] },
]
+++

Similar to how phytokineticists (_Pathfinder RPG Ultimate Wilderness_ 58) draw their power from the
First World, elysiokineticists trace their abilities to the riotous wilderness of the plane known as
Elysium. Many such kineticists vow to fight against evil planar intrusions into the Material Plane,
particularly the Worldwound.

## Elysium's Soul {#elysium-s-soul}

An elysiokineticist must be chaotic good, and she has alignment auras of chaotic and good as if she
were a chaotic good [outsider](ref/type/outsider) with a number of Hit Dice equal to her kineticist
level. She must choose wood (_Ultimate Wilderness_ 58) as her primary
[element](ref/ability/elements) and [positive blast](ref/kinetic/positive-blast) as her first simple
blast. At 7th level, she gains [verdant blast](ref/kinetic/verdant-blast) and
[wood blast](ref/kinetic/wood-blast), as well as a 3rd-level or lower wild talent of her choice. At
15th level, she gains a 7th-level wild talent of her choice. She gains Heal and Knowledge (religion)
as class skills but does not gain Handle Animal and Knowledge (nature) as class skills.

This alters elemental focus and the class skills granted by the wood element, and it replaces
expanded element.

## Basic Elysiokinesis (Sp) {#basic-elysiokinesis}

An elysiokineticist can use the power of Elysium to assist others and bolster their vigor, allowing
her to cast _[resistance](ref/spell/resistance), [stabilize](ref/spell/stabilize)_, or
_[virtue](ref/spell/virtue)_ as a [spell-like ability](ref/umr/spell-like-abilities) at will as a
standard action.

This replaces the basic phytokinesis utility wild talent granted by the wood element.

## Elysian Infusion (Su) {#elysian-infusion}

An elysiokineticist can infuse her positive blast with the power of Elysium to battle evil. The
infused blast damages evil outsiders as if they were undead and counts as both chaotic and good.
This is a 1st-level substance infusion that costs 1 point of burn and can be used with positive
blast.

This replaces the infusion gained at 1st level.

## Elysian Aura (Su) {#elysian-aura}

At 2nd level, an elysiokineticist infuses herself with a holy aura, granting her protection against
evil attacks. She gains a +1 deflection bonus to AC and a +1 resistance bonus on saving throws; both
apply only against attacks from evil creatures. By accepting 1 point of burn, she can increase both
bonuses by 1. At 5th level and every 3 levels thereafter, she can accept 1 additional point of burn
to further increase both bonuses by 1 (to a maximum of +7 at 17th level). Whenever she accepts burn
while using a wood wild talent, the energy causes her elysian aura bonuses to apply against all
attacks for 1 round, and during that time she is protected from evil mental and possession effects,
as per _[protection from evil](ref/spell/protection-from-evil)_. She can dismiss or restore this
effect as an immediate action.

This replaces the flesh of wood defense wild talent granted by the wood element.

## Ghaelelight Blast (Su) {#ghaelelight-blast}

At 15th level, an elysiokineticist gains the ghaelelight composite blast, which costs 2 points of
burn. A ghaelelight blast is an energy blast that deals damage as a simple energy blast instead of a
composite energy blast and deals chaotic and good damage. It is associated with the same infusions
as positive blast.
