+++
id = "ref/arc-gunslinger/black-powder-vaulter"
kind = "archetype"
title = "Black Powder Vaulter"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Black%20Powder%20Vaulter"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "black_powder_vaulter", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "mobile-reload" },
  { anchor = "daring-vault" },
  { anchor = "shot-on-the-run", level = 3 },
  { anchor = "art-of-the-gun", level = 7 },
  { anchor = "dual-shot-on-the-run", level = 11 },
]
trades = [
  { replaces = "Deadeye deed", feature = "deeds", power = "deadeye", by = ["mobile-reload"] },
  { replaces = "Gunslinger's dodge deed", feature = "deeds", power = "gunslinger's dodge", by = ["daring-vault"] },
  { replaces = "Gunslinger initiative deed", feature = "deeds", power = "gunslinger initiative", by = ["shot-on-the-run"] },
  { replaces = "Startling shot deed", feature = "deeds", power = "startling shot", by = ["art-of-the-gun"] },
  { replaces = "Expert loading deed", feature = "deeds", power = "expert loading", by = ["dual-shot-on-the-run"] },
]
+++

While firearms were designed to allow combatants to fight their foes from a distance, some
gunslingers like to get into the thick of the battle, maneuvering among the fray to find the most
advantageous positions from which to kill their enemies. The daredevil fighting style of the black
powder vaulter has arisen simultaneously in two places—among Mana Wastes gunslingers inspired by the
graceful fighting styles of Mwangi tribes, and among pirates from Tian Xia and the Shackles who
encountered and inspired one another.

## Deeds {#deeds}

A black powder vaulter gains the following deeds.

## Mobile Reload (Ex) {#mobile-reload}

If a black powder vaulter has at least 1 grit point, she can reload a firearm as part of a move
action to move, provided that the action to reload that firearm with that type of ammunition would
normally take only a move action or swift action. At 3rd level, she can use this deed while also
using the shot on the run deed.

This deed replaces the deadeye deed.

## Daring Vault (Ex) {#daring-vault}

A black powder vaulter can spend 1 grit point as a swift action to increase her land speed by 20
feet (gaining the appropriate bonus on [Acrobatics](ref/skill/acrobatics) checks to jump) until the
end of her turn. If the black powder vaulter jumps while affected by this deed, she can make a
second jump while midair if she is adjacent to a wall, column, or other solid, permanent structure.
The second jump counts as having a running start even if the direction is different from the first
jump.

This deed replaces the gunslinger's dodge deed.

## Shot on the Run (Ex) {#shot-on-the-run}

At 3rd level, if the black powder vaulter has at least 1 grit point, she gains the benefits of the
[Shot on the Run](ref/feat/shot-on-the-run) feat. She gains this benefit only when making an attack
with a firearm with which she is proficient. At 7th level, she can use the targeting deed as part of
the same full-round action as using Shot on the Run.

This deed replaces the gunslinger initiative deed.

## Art of the Gun (Ex) {#art-of-the-gun}

At 7th level, if the black powder vaulter has at least 1 grit point, she doesn't provoke attacks of
opportunity when attacking with a firearm or reloading a firearm. Additionally, whenever she is
wielding a firearm, she counts as threatening an area around her as though she were wielding a melee
weapon. If an opponent provokes an attack of opportunity from her, she can use the
[pistol-whip](ref/deed/pistol-whip) deed as her attack of opportunity, spending 1 grit point as
normal. Alternatively, if her firearm is loaded, she can spend 1 grit point to fire her gun as her
attack of opportunity.

This deed replaces the startling shot deed.

## Dual Shot on the Run (Ex) {#dual-shot-on-the-run}

At 11th level, the black powder vaulter can make two attacks with firearms while using the shot on
the run deed.

This deed replaces the expert loading deed.
