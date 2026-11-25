+++
id = "ref/arc-paladin/forest-preserver"
kind = "archetype"
title = "Forest Preserver"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Forest%20Preserver"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forest_preserver", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "70"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-terrain", level = 3 },
  { anchor = "woodland-stride", level = 3 },
  { anchor = "sacred-botany", level = 4 },
  { anchor = "fireproof-aura", level = 8 },
  { anchor = "sacred-grove", level = 11 },
  { anchor = "aura-of-preservation", level = 14 },
]
trades = [
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["favored-terrain"] },
  { replaces = "Divine health", feature = "divine-health", by = ["woodland-stride"] },
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["sacred-botany"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["fireproof-aura"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["sacred-grove"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["aura-of-preservation"] },
]
+++

Forest preservers are sacred defenders of the woodlands and of the wild creatures and natural beauty
within them.

## Class Skills {#class-skills}

A forest preserver adds Climb, Knowledge (nature), and Survival to her list of class skills. She
does not gain Diplomacy, Knowledge (nobility), or Sense Motive as class skills.

This alters the paladin's class skills.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a forest preserver gains the ranger's [favored terrain](ref/ability/favored-terrain)
ability but must select either forest or jungle as her favored terrain. The bonuses granted by this
ability increase by 2 for every 5 levels after 3rd, but she does not gain additional favored
terrains.

This replaces aura of courage.

## Woodland Stride (Ex) {#woodland-stride}

At 3rd level, a forest preserver (as well as her divine bond creature, if she has one) gains
[woodland stride](ref/ability/woodland-stride), as per the druid class feature.

This replaces divine health.

## Sacred Botany (Ex) {#sacred-botany}

At 4th level, a forest preserver adds the following spells to her spell list: 1st—_detect animals or
plants_, _entangle_, _goodberry_, _shillelagh_; 2nd—_barkskin_, _eagle eye_, _tree shape_, _warp
wood_, _wood shape_; 3rd—_diminish plants_, _plant growth_, _snare_, _speak with plants_, _spike
growth_; 4th—_antiplant shell_, _awaken_ (trees only), _blight_, _command plants_, _commune with
nature_, _thorn body_, _tree stride_, _wall of thorns_. In addition, she treats her caster level as
1 higher when casting these spells in her favored terrain.

This replaces channel positive energy.

## Fireproof Aura (Su) {#fireproof-aura}

At 8th level, a forest preserver and creatures within 10 feet of her gain a +2 bonus on saving
throws against fire effects and gain fire resistance 5; these are doubled for plant allies, which
also gain [evasion](ref/ability/evasion) against fire effects only. Whenever a fire spell would
affect a creature within the fireproof aura, the forest preserver can expend three uses of her lay
on hands ability as an immediate action to attempt to counter the effect, as if she had readied a
_[dispel magic](ref/spell/dispel-magic)_ spell (caster level = her paladin level) to counterspell.
This ability functions only if the forest preserver is conscious.

This replaces aura of resolve.

## Sacred Grove (Su) {#sacred-grove}

At 11th level, a forest preserver can expend two uses of her smite evil ability to consecrate a
20-foot-radius area that must contain a living tree. This fills the area with dense undergrowth,
though it does not impede her allies' movement. In addition, animals, fey, and plants allied with
the forest preserver gain a +1 sacred bonus on attack rolls, damage rolls, and saving throws, and
animals, fey, and plants called or summoned within this area gain 1 hit point per Hit Die as long as
the calling or summoning effect lasts or until the sacred grove effect ends (whichever comes first).
If the area contains a shrine or hallowed area dedicated to a good-aligned deity (or at the GM's
discretion, a place of natural magical power, such as a natural portal to the First World), these
bonuses are doubled.

When she uses this ability in her favored terrain, she can also imbue plants in the area with
limited animation, allowing them to obscure vision and impede movement and attacks as if the area
were affected by _[solid fog](ref/spell/solid-fog)_.

A sacred grove remains enhanced in this way for a number of minutes equal to the paladin's level.

This replaces aura of justice.

## Aura of Preservation (Su) {#aura-of-preservation}

At 14th level, a forest preserver grants animals and plants within 10 feet
[spell resistance](ref/rule/spell-resistance) equal to 11 + her paladin level. This spell resistance
doesn't apply against harmless effects created by the forest preserver or allies within 10 feet of
her. This ability functions only if the forest preserver is conscious.

This replaces aura of faith.
