from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.

def evaluate_hand(hand: list[Card]) -> str:
    if not hand:
        return "High Card"

    rank_counts = {}
    suit_counts = {}
    suits_ranks = {}

    for card in hand:
        r = card.rank.value
        s = card.suit

        rank_counts[r] = rank_counts.get(r, 0) + 1

        suit_counts[s] = suit_counts.get(s, 0) + 1

        if s not in suits_ranks:
            suits_ranks[s] = []
        if r not in suits_ranks[s]:
            suits_ranks[s].append(r)

    for suit, ranks_list in suits_ranks.items():
        if len(ranks_list) >= 5:
            sorted_ranks = sorted(ranks_list)
            if Rank.ACE.value in sorted_ranks:
                sorted_ranks.append(1)
            for i in range(len(sorted_ranks) - 4):
                if (sorted_ranks[i] + 1 == sorted_ranks[i+1] and
                    sorted_ranks[i] + 2 == sorted_ranks[i+2] and
                    sorted_ranks[i] + 3 == sorted_ranks[i+3] and
                    sorted_ranks[i] + 4 == sorted_ranks[i+4]):
                    return "Straight Flush"


    flush = any(count >= 5 for count in suit_counts.values())

    unique_ranks = list(set(rank_counts.keys()))
    unique_ranks.sort()
    if Rank.ACE.value in unique_ranks:
        unique_ranks.append(1)

    straight = False
    for i in range(len(unique_ranks) - 4):
        if (unique_ranks[i] + 1 == unique_ranks[i+1] and
            unique_ranks[i] + 2 == unique_ranks[i+2] and
            unique_ranks[i] + 3 == unique_ranks[i+3] and
            unique_ranks[i] + 4 == unique_ranks[i+4]):
            straight = True
            break

    counts_sorted = sorted(rank_counts.values(), reverse=True)


    if 4 in counts_sorted:
        return "Four of a Kind"
    if 3 in counts_sorted and 2 in counts_sorted:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if 3 in counts_sorted:
        return "Three of a Kind"
    if counts_sorted.count(2) >= 2:
        return "Two Pair"
    if 2 in counts_sorted:
        return "One Pair"

    return "High Card"
