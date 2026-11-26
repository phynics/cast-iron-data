+++
id = "ref/arc-swashbuckler/courser"
kind = "archetype"
title = "Courser"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Courser"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "courser", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "swift-target", level = 1 },
  { anchor = "nimble-toes", level = 3 },
  { anchor = "confounding-target", level = 4 },
  { anchor = "deeds" },
  { anchor = "wall-run", level = 3 },
  { anchor = "impossible-leap", level = 7 },
  { anchor = "swift-strikes", level = 11 },
]
trades = [
  { replaces = "Opportune parry and riposte deeds", feature = "deeds", power = "opportune parry and riposte", by = ["swift-target"] },
  { replaces = "Bonus feat gained at 4th level", feature = "bonus-feats", levels = [4], by = ["confounding-target"] },
  { replaces = "Menacing swordplay", feature = "deeds", power = "menacing swordplay", by = ["wall-run"] },
  { replaces = "Superior feint deed", feature = "deeds", power = "superior feint", by = ["impossible-leap"] },
  { replaces = "Bleeding wound deed", feature = "deeds", power = "bleeding wound", by = ["swift-strikes"] },
  { alters = "Nimble", feature = "nimble", by = ["nimble-toes"] },
]
+++

Many [tengus](ref/race/tengu) still hold some bitterness at their lack of wings, and while a small
number cultivate enough magic in themselves to recall the gift of flight, those tengu denizens of
Golarion's greatest cities have refined their own way to fly. Coursers move with grace and ease,
racing across rooftops, dashing up walls, and clearing vast gaps between buildings. These daredevils
clash for territory and rob vastly superior enemies, trusting in their incredible speed and mobility
to keep them safe rather than resorting to swordplay.

## Swift Target (Ex) {#swift-target}

At 1st level, the courser gains [Dodge](ref/feat/dodge) as a bonus feat even if she does not meet
the prerequisites. As long as she has at least 1 panache point and is wearing light armor or no
armor, her base speed increases by 5 feet.

This ability replaces the swashbuckler's opportune parry and riposte deeds.

## Nimble Toes (Ex) {#nimble-toes}

At 3rd level, the AC bonus gained from the nimble class feature increases by 1 as long as the
courser moves at least 20 feet during her turn, though it is reduced by 1 if she does not move at
least 10 feet on her turn. These modifiers last until the beginning of the courser's next turn.

This ability modifies nimble.

## Confounding Target (Ex) {#confounding-target}

At 4th level, the courser gains [Spring Attack](ref/feat/spring-attack) as a bonus feat even if she
does not meet the prerequisites. As long as she has at least 1 panache point and is wearing light
armor or no armor, her base speed increases by 10 feet rather than 5 feet.

This ability replaces the bonus feat gained at 4th level.

## Deeds {#deeds}

A courser gains the following deeds, each of which replaces an existing deed.

## Wall Run (Ex) {#wall-run}

At 3rd level, the courser can run horizontally across vertical surfaces for 1 round by spending 1
panache point. She can perform this deed only while wearing light armor or no armor, and she must
end her movement for the round on solid ground or else fall [prone](ref/rule/prone). The courser can
use this deed to run straight up vertical surfaces as well, but every 5 feet up counts as 10 feet of
movement.

This deed replaces menacing swordplay.

## Impossible Leap (Ex) {#impossible-leap}

At 7th level, as long as the courser has at least 1 panache point and is wearing light armor or no
armor, she adds her swashbuckler level on all [Acrobatics](ref/skill/acrobatics) checks to jump. She
can spend 1 panache point as an immediate action to jump 10 feet in the direction of her choice.
This ability can be used to extend another jump or change direction mid-jump. If used in response to
an attack, this deed functions as the [dodging panache](ref/swashdeed/dodging-panache) deed, but it
allows the courser to move 10 feet.

This deed replaces the superior feint deed.

## Swift Strikes (Ex) {#swift-strikes}

At 11th level, the courser can spend 1 panache point to target two separate creatures when she uses
the Spring Attack feat. She rolls the attack once and compares the result to each target's Armor
Class separately. Additional damage—such as from a critical hit or weapon property—applies to only
the first target struck. Her movement still provokes attacks of opportunity normally from any
creature she doesn't attack.

This deed replaces the bleeding wound deed.
