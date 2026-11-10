+++
id = "ref/spell/arcane-cannon"
kind = "spell"
title = "Arcane Cannon"
aon = "SpellDisplay.aspx?ItemName=Arcane%20Cannon"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_cannon", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "223"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 round"
components = "V, S, F (an ornate miniature cannon forged with a drop of your blood that costs 5,000 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one magically animated cannon" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, F (an ornate miniature cannon forged with a drop of your blood that costs 5,000 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: one magically animated cannon
:::

Your focus becomes a Medium arcane cannon that appears in an unoccupied square within the spell's
range. If no unoccupied square is within range, the spell fails. The cannon comes into existence
loaded. Each round thereafter, the cannon can either fire or load. A cannon must be loaded to fire.
You do not need to supply ammunition for the cannon.

On your turn, you can spend a move action to direct the cannon to wheel itself to a new location,
moving the cannon up to 20 feet. If the arcane cannon ever leaves your line of sight, it winks out
of existence, and the spell's duration ends.

The cannon has a range increment of 50 feet. It targets touch attack in the first range increment,
and it has no misfire chance. The cannon acts as a weapon with the
[conductive](ref/magic-enh/conductive) special weapon ability, which you can use to channel your
spell-like or supernatural abilities as long as you are within the range of arcane cannon. The
cannon's attack bonus is equal to your caster level + your Intelligence bonus or your Charisma bonus
(for wizards or sorcerers, respectively) with an additional +1 per four caster levels (maximum +5 at
20th level). On a hit, the cannon deals 4d10 damage. The arcane cannon attacks have a critical
modifier of ×4.

The cannon has AC 10, [hardness](ref/umr/hardness) 10, and 80 hit points. If the cannon is subject
to a spell or effect that requires a save, it uses your saving throw modifiers. The cannon never
provokes attacks of opportunity. If the cannon is destroyed, so is your focus.
