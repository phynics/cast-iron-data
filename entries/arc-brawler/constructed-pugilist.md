+++
id = "ref/arc-brawler/constructed-pugilist"
kind = "archetype"
title = "Constructed Pugilist"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Constructed%20Pugilist"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "constructed_pugilist", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "constructed-limb" },
  { anchor = "limb-modifications", level = 1 },
  { anchor = "bonus-item-creation-feats", level = 2 },
]
trades = [
  { replaces = "Martial flexibility", feature = "martial-flexibility", by = ["limb-modifications"] },
  { alters = "Bonus combat feats", feature = "bonus-combat-feats", by = ["bonus-item-creation-feats"] },
  { alters = "Class skills" },
]
+++

Mutants whose mutations make using standard weapons or other gear difficult sometimes attach
mechanical prostheses to their existing limbs. Many develop combat skills that use their prostheses
so they always have a weapon at hand. Over time, these brawlers (_Pathfinder RPG Advanced Class
Guide_ 23) customize their mechanical limbs, adding additional weaponry and other mechanisms.

## Class Skills {#class-skills}

A constructed pugilist gains Craft (weapons) as a class skill.

This alters the brawler's class skills.

## Constructed Limb (Ex) {#constructed-limb}

A constructed pugilist begins play with a special prosthetic limb built for fighting and typically
made of iron, steel, stone, or wood, with the corresponding [hardness](ref/umr/hardness) and hit
points (see page 175 of the _Pathfinder RPG Core Rulebook_). She treats attacks with this limb as
unarmed strikes that gain all the benefits of the brawler's unarmed strike class feature. She treats
the limb as a light weapon and is proficient with it. Removing or reattaching the constructed limb
takes 10 minutes.

The constructed pugilist can improve her constructed limb as if it were a normal melee weapon. For
the purpose of rebuilding the limb as a masterwork weapon, rebuilding the limb out of a special
material, or adding certain magical special abilities to it, the limb counts as a one-handed melee
weapon that costs 60 gp and weighs 6 pounds—though it is specially fitted to the constructed
pugilist and can't be resold or used by anyone else. A constructed limb can benefit from either its
own enhancement bonus and special abilities or those granted by an
_[amulet of mighty fists](ref/magic-wondrous/amulet-of-mighty-fists)_, but if it would benefit from
both simultaneously, it benefits only from the source with the higher effective enhancement bonus
(the limb benefits from its own abilities in the case of a tie).

## Limb Modifications {#limb-modifications}

A constructed pugilist chooses one of the following limb modifications at 1st level and another at
6th, 10th, 12th, and 20th levels. These modifications do not require the constructed pugilist to
rebuild her constructed limb.

This replaces martial flexibility.

### Flex Limb {#flex-limb}

The limb is divided into jointed segments held in place with rigid rods. As a standard action, the
constructed pugilist can release the rods and turn her limb into a whiplike appendage. In this mode,
the prosthesis can be used to make [trip](ref/rule/trip) attempts, and it grants a +2 bonus on
[disarm](ref/rule/disarm) attempts made using it. The constructed pugilist doesn't run the risk of
dropping her limb if she fails. Returning the limb to its rigid form takes a standard action. As a
standard action, a constructed pugilist with both flex limb and limb extender can activate or
deactivate one of those limb modifications or both simultaneously; when the constructed pugilist has
both flex limb and limb extender activated, she gains the benefits of reach with the flex limb
abilities.

### Grapnel Arm {#grapnel-arm}

The constructed pugilist can fire a grappling hook built into her prosthesis. The grappling hook is
attached to a 40-foot-long fine chain affixed to the limb. The constructed pugilist can attack with
the grappling hook as a standard action, making a ranged touch attack against the target. The
grappling hook can't be used as part of a [full attack](ref/rule/full-attack). On a successful hit,
the grappling hook deals no damage, but it functions as though it had the
[grapple](ref/misc/grapple) weapon special feature, except it requires only a hit (not a critical
hit) and the grapple ends if the constructed pugilist moves more than 40 feet away from the grappled
creature. The constructed limb can't be used to make melee attacks until the grappling hook has been
reloaded (a standard action).

### Limb Extender {#limb-extender}

As a standard action, the constructed pugilist can activate an extender, giving her limb the
[reach](ref/misc/reach) weapon special feature. Returning the limb to its normal length is a
standard action.

### Shielding Limb {#shielding-limb}

The constructed pugilist learns to block blows with her mechanical limb. She gains a +2 shield bonus
to AC, though she loses this bonus anytime she loses her Dexterity bonus to AC.

### Tight Grip {#tight-grip}

Special tensors allow the constructed pugilist to lock her grip in place. When using her constructed
limb, the constructed pugilist gains a +1 bonus on Climb checks and combat maneuver checks to disarm
and grapple, as well as to her CMD against attempts to disarm items held in the limb. This
modification can be chosen only if the limb includes a hand or other gripping appendage.

### Vicious Blades {#vicious-blades}

Razor-sharp blades on the surface of the limb cause it to deal bludgeoning and slashing damage and
increase its critical threat range to 19–20. A constructed pugilist who has the vicious spikes limb
modification can't select this modification.

### Vicious Spikes {#vicious-spikes}

Long spikes protrude from the limb, causing it to deal bludgeoning and piercing damage and
increasing its critical multiplier to ×3. A constructed pugilist who has the vicious blades limb
modification can't select this modification.

## Bonus Item Creation Feats {#bonus-item-creation-feats}

At 2nd level, a constructed pugilist adds
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor),
[Master Craftsman](ref/feat/master-craftsman) (Craft \[weapons\]), and
[Skill Focus](ref/feat/skill-focus) (Craft \[weapons\]) to the list of bonus feats she can choose
(instead of just combat feats).

This alters bonus combat feats.
