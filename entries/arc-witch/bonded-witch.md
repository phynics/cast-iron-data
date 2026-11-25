+++
id = "ref/arc-witch/bonded-witch"
kind = "archetype"
title = "Bonded Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Bonded%20Witch"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bonded_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "advanced-race-guide"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "bonded-item", level = 1 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["bonded-item"] },
]
+++

While all witches commune with the unknown, the blend of human ingenuity and adept learning mixed
with elven blood gives some half-elves a unique conduit to channel the powers of the arcane. Bonded
witches forsake familiars as vessels of power in favor of a specific object that grants them powers
above and beyond those of their patron alone, as they tap into the powerful magic of the item
itself. A bonded witch has the following class features.

## Bonded Item (Sp) {#bonded-item}

At 1st level, a bonded witch gains a bonded item instead of a familiar. This bonded item is similar
to a [wizard's](ref/class/wizard) arcane bond bonded item, and follows all the rules of such an item
with the following exceptions.

A bonded witch's bonded item serves as a vessel for her spells and a conduit for communication with
her patron. A bonded witch must commune with her bonded item each day to prepare her spells. The
bonded item stores all of the spells that the bonded witch knows, and the bonded witch cannot
prepare spells that are not stored within it. A bonded witch starts with the same number of spells
and gains new spells the same way as a witch, and can even add spells by learning them from scrolls
in the same way, but a bonded witch cannot learn spells from another bonded item.

Since a bonded witch does not have a spellbook, starting at 2nd level, a bonded witch's bonded item
can be used once per day to cast a spell dependent on the type of bonded object chosen by the bonded
witch. The spell is treated like any other spell cast by the bonded witch, including its casting
time, duration, and other effects dependent of the bonded witch's level. This spell cannot be
further modified by metamagic feats or any other ability. As the bonded witch gains levels, the
bonded item gains new spells that the bonded witch can cast in this way. She can cast any one of
these spells once per day using her bonded object, but gains greater flexibility in what spells she
can cast, and gains more powerful spells as she gains new levels. The bonded item spells associated
with each item type are as follows.

### Amulet {#amulet}

2nd—_stonefist_; 4th—_bear's endurance_; 6th—_burst of speed_; 8th—_mnemonic enhancer;_
10th—_stoneskin;_ 12th—_monstrous physique IV_; 14th—_firebrand_; 16th—_iron body_;
18th—_overwhelming presence_.

### Ring {#ring}

2nd—_shield;_ 4th—_ablative barrier_; 6th—_protection from energy;_ 8th—_nondetection;_ 10th—_life
bubble_; 12th—_resinous skin_; 14th—_antimagic field;_ 16th—_deflection_; 18th—_spell immunity_.

### Staff {#staff}

2nd—_shillelagh;_ 4th—_warp wood;_ 6th—_plant growth;_ 8th—_arboreal hammer_; 10th—_passwall_;
12th—_move earth;_ 14th—_change staff;_ 16th—_control plants;_ 18th—_wooden phalanx_.

### Wand {#wand}

2nd—_magic missile;_ 4th—_knock;_ 6th—_fireball;_ 8th—_restoration;_
10th—[maximized](ref/feat/maximize-spell) _scorching ray_; 12th—_bull's strength_ (mass);
14th—_greater restoration;_ 16th—[empowered](ref/feat/empower-spell) and maximized _fireball_;
18th—empowered and maximized _fire shield_.

### Weapon {#weapon}

2nd—_warding weapon_; 4th—_versatile weapon_; 6th—_greater magic weapon_; 8th—_telekinetic charge_;
10th—_energy siege shot_; 12th—_blade barrier_; 14th—_arcane cannon_; 16th—_earthquake_; 18th—_ride
the lightning_.

This ability replaces the witch's familiar class feature.
