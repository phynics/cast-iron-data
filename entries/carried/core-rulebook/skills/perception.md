+++
id = "ref/carried/core-rulebook/skills/perception"
kind = "skill"
title = "Perception"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Perception", path = "core_rulebook/skill/perception.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Wis
Trained Only: Yes
Armor Check Penalty: Yes
:::

_Your senses allow you to notice fine details and alert you to danger. Perception covers all five
senses, including sight, hearing, touch, taste, and smell._

## Check {#check}

Perception has a number of uses, the most common of which is an opposed check versus an opponent's
Stealth check to notice the opponent and avoid being surprised. If you are successful, you notice
the opponent and can react accordingly. If you fail, your opponent can take a variety of actions,
including sneaking past you and attacking you.

Perception is also used to notice fine details in the environment. The DC to notice such details
varies depending upon distance, the environment, and how noticeable the detail is. The following
table gives a number of guidelines.

### Detail {#detail}

::: table
head = [
  [
    { text = "Detail", header = true },
    { text = "Perception DC", header = true },
  ],
]
body = [
  [
    { text = "Hear the sound of battle" },
    { text = "–10" },
  ],
  [
    { text = "Notice the stench of rotting garbage" },
    { text = "–10" },
  ],
  [
    { text = "Detect the smell of smoke" },
    { text = "0" },
  ],
  [
    { text = "Hear the details of a conversation" },
    { text = "0" },
  ],
  [
    { text = "Notice a visible creature" },
    { text = "0" },
  ],
  [
    { text = "Determine if food is spoiled" },
    { text = "5" },
  ],
  [
    { text = "Hear the sound of a creature walking" },
    { text = "10" },
  ],
  [
    { text = "Hear the details of a whispered conversation" },
    { text = "15" },
  ],
  [
    { text = "Find the average concealed door" },
    { text = "15" },
  ],
  [
    { text = "Hear the sound of a key being turned in a lock" },
    { text = "20" },
  ],
  [
    { text = "Find the average secret door" },
    { text = "20" },
  ],
  [
    { text = "Hear a bow being drawn" },
    { text = "25" },
  ],
  [
    { text = "Sense a burrowing creature underneath you" },
    { text = "25" },
  ],
  [
    { text = "Notice a pickpocket" },
    { text = "Opposed by Sleight of Hand" },
  ],
  [
    { text = "Notice a creature using Stealth" },
    { text = "Opposed by Stealth" },
  ],
  [
    { text = "Find a hidden trap" },
    { text = "Varies by trap" },
  ],
  [
    { text = "Identify the powers of a potion through taste" },
    { text = "15 + the potion's caster level" },
  ],
  [
    { text = "Perception Modifiers", header = true },
    { text = "DC Modifier", header = true },
  ],
  [
    { text = "Distance to the source, object, or creature" },
    { text = "+1/10 feet" },
  ],
  [
    { text = "Through a closed door" },
    { text = "+5" },
  ],
  [
    { text = "Through a wall" },
    { text = "+10/foot of thickness" },
  ],
  [
    { text = "Favorable conditions^1^" },
    { text = "–2" },
  ],
  [
    { text = "Unfavorable conditions^1^" },
    { text = "+2" },
  ],
  [
    { text = "Terrible conditions^2^" },
    { text = "+5" },
  ],
  [
    { text = "Creature making the check is distracted" },
    { text = "+5" },
  ],
  [
    { text = "Creature making the check is asleep" },
    { text = "+10" },
  ],
  [
    { text = "Creature or object is invisible" },
    { text = "+20" },
  ],
]
foot = [
  [
    { text = "1 Favorable and unfavorable conditions depend upon the sense being used to make the check. For example, bright light might decrease the DC of checks involving sight, while torchlight or moonlight might increase the DC. Background noise might increase a DC involving hearing, while competing odors might increase the DC of a check involving scent.", colspan = 2 },
  ],
  [
    { text = "2 As for unfavorable conditions, but more extreme. For example, candlelight for DCs involving sight, a roaring dragon for DCs involving hearing, and an overpowering stench covering the area for DCs involving scent.", colspan = 2 },
  ],
]
:::

## Action {#action}

Most Perception checks are reactive, made in response to observable stimulus. Intentionally
searching for stimulus is a move action.

## Try Again {#try-again}

Yes. You can try to sense something you missed the first time, so long as the stimulus is still
present.

## Special {#special}

Elves, half-elves, gnomes, and halflings receive a +2 racial bonus on Perception checks. Creatures
with the scent special quality have a +8 bonus on Perception checks made to detect a scent.
Creatures with the [tremorsense](ref/umr/tremorsense) special quality have a +8 bonus on Perception
checks against creatures touching the ground and automatically make any such checks within their
range. For more on special qualities, see Special Abilities.

A spellcaster with a hawk or owl familiar gains a +3 bonus on Perception checks. If you have the
Alertness feat, you get a bonus on Perception checks (see Feats).
